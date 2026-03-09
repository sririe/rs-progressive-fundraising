---
title: "Client Meeting Transcript — Progressive + Red Stamp: Ecommerce Evolution"
type: discovery
category: meeting-transcript
date: 2025-01-29
status: complete
format: transcript
source_url: https://supernorm.al/tentative-progressive-redstamp-ecommerce-evolution-b92c52608aa841f09dce54e1ac863956
participants:
  progressive:
    - Doug B. (Owner)
    - Gord S. (Advisor)
    - Lloyd S. (Technical Contractor)
  redstamp:
    - Spencer R.
    - Tim L.
    - Brontë B.
    - Stephanie L.
tags: [client-meeting, digital-fulfillment, card-generation-workflow, vendor-integration, white-label, automation-roadmap, security, two-factor-auth, loblaws, walmart, amazon, cash-star]
key_insights:
  - Doug's three priorities in order — (1) customer portal for digital card retrieval, (2) white-label portals, (3) automation/AI discussion
  - Lloyd detailed card generation process — four vendors require manual generation (Walmart, Amazon, Chapters, Loblaws/Shoppers)
  - Loblaws ~20 sec/card generation; others ~1 sec/card
  - Doug agreed to standardize on URLs over PDFs to simplify automation
  - Progressive already integrated with Walmart backend; starting Amazon and Tim Hortons (via Cash Star)
  - Lloyd flagged need for 2FA or device-level auth on any portal storing card numbers
  - Doug explicitly asked Red Stamp to come back with recommendations, not just respond to requests
  - 3-5 year automation roadmap — sticker machine (imminent) → barcode/magstripe capture → merchant backend integration
related:
  - docs/discovery/2025-01-29-client-discovery-call.md
  - docs/discovery/2025-01-27-internal-pre-meeting.md
---

[Tentative] Progressive + Redstamp: Ecommerce Evolution transcript
Thursday, January 29th @ 10:40 AM | View at https://supernorm.al/tentative-progressive-redstamp-ecommerce-evolution-b92c52608aa841f09dce54e1ac863956


[0:00] Brontë B.: Yeah.
[0:01] Doug B.: Very good.
[0:04] Stephanie L.: Great. How do you Spencer? How's it going?
[0:07] Brontë B.: I think you're a mute Spencer.
[0:10] Spencer R.: Oh, sorry about that. I had joined a Google meet for my next meeting, and I'm
[0:11] Stephanie L.: it's
[0:13] Spencer R.: sitting there. I'm like, man, there is no way that I am. The only one that showed up for this call yet. I must be on the wrong link. Oh well, great to to see everyone and Enjoying the miserable rainy, cold weather out here on the West Coast I know folks back East have had it worse. So no complaining loud probably for me. But yeah. Doug, we've been, you know, obviously chatting about a couple different.
[0:51] Spencer R.: scenarios but would love to sort of maybe get an update from from you folks on What's what's front of mind and how we best use? Use the time today.
[1:03] Doug B.: Sure. Okay, so I I got it down to sort of three categories and I think the first two are related. So first one is A website. We want we'd like to have a portion of the website where you need a username and password to get into, where we can do some, do some things. The first thing is we're thinking that We want to automate our whole digital gift card scenario quite a bit more. So like Lloyd mentioned to me last week is we kind of really want our clients to be able to go in to that part of the website and retrieve gift cards. That they've paid for take that off our hands in a sense, right? So some of the, some of the orders we get are like, two of this, three of those, five of that, it takes forever, to kind of pull it all together, right? And and, and get it,
[2:07] Doug B.: get it out to our clients. So I think that's, that's one thing. The second thing is Right now, we're in a situation where we we email out with a password protected attachment to deliver the the digital gift cards, but we want to be able to deliver to the end user as well, right? So right now we just have a contact, we get it to the contact and that's their job to hand it out to people. So I'm thinking that There should be a way on this website that we can do that as well. How Lloyd's researched it a little bit where like blah blah is how they do it with a sort of Excel spreadsheet and stuff, like How can we set it up? So, so on this, this part of this site where they've logged in and stuff, that they can set it up. So
[3:02] Doug B.: if they wanted to go out to a hundred or five hundred people in their company, what's the mechanism to set that up and then once they've paid for it to go back on that site and retrieve it and have it delivered out to all the people. So that's kind of one thing I showed you a little bit of information. How Loblaz does it Cash Star? Does a really good job of it, too. Like we're when we buy Tim Hortons or Subway, Boston piece before, like a whole list of them once we've paid and they've approved that payment we just log in and we go grab we go grab those cards Lloyd can get into more of the Effects, but I would say, that's kind of a general, general overview. So, that's number. One, number two is about what we've already talked about where we're Gordon and I are going out to suppliers, we've gone out, and we've talked with Save on Foods. We've talked to the Sequoia group which is, you know, seasons and and the Tea House out in Stanley, Park like high-end restaurants and white spot. We I've talked to White Spot yesterday, so in all those cases we've told them that we'd like to look after their bulk fulfillment of gift cards. And I see
[4:16] Doug B.: that there's three possibilities there if they agree to it. And they want to have people go on to their website and link to ours. There's there's three scenarios one. They can just like Walmart they can just come to our existing site Level number two is they come to a site? Operated administered by us where they could only buy white spot cards or they can only buy sequoia cars. They want it. They what they don't want to send people to our link and have them the ability to buy keg and anything else that we have on our site. So that's number two and then level number three, which is
[4:51] Doug B.: the most involved is, which we've talked about and you've sent us those mock-ups and stuff was where they go into a site, and it's branded right in their branding, we're in ministering it, but looks like they're still connected to to White Spot of Sequoia or the Keg or whoever, right? So those are the three different levels. that we've sort of talked about and then the third thing, if we have time, last time we mentioned Sort of you talked about the AI that you've figured out with with Danny about automation and stuff. I kind of just want to give you our sort of general vision of where we're going from and sort of automation point of view and see if it fits in with what you guys have done. But that would be sort of a third Discussion point that maybe we do in another time or maybe maybe gets fit in today. So that's that's kind of a third thing on my plate but I think in my mind my limited mind on this whole knowledge of technology, number one and two seem to be the same thing. They're gonna go to us, go to a site where they have to have a username and login. Step one is, we want to work on this whole digital card world. But then number two is, I'm sort of thinking that basis would also
[6:06] Doug B.: could could be where they also could go on username login, where they go on to a white spot branded sort of progressive and ministers, but think they're still talking to White Spot. So I kind of, I kind of see those two related. How are they related? You know, kind of get into the details of whether they're two separate things, or they could be part of the same package. So,
[6:30] Spencer R.: Yeah.
[6:32] Doug B.: So maybe Lloyd, could you maybe expand on the digital stuff of what what you think we need from? What, you know about, you know, dealing with the merchant cards and things, what's your vision of what you think we need on this? This sort of digital portion of this website.
[6:55] Lloyd S.: Well, I don't really have a vision. I just I think That people should be able to just go get cards, right? If I want to get a gift card, they come to you. And so you need to provide the facility as if someone's just going to the log laws or something, to get the card and and I know humans aren't involved in that at. All right? Like what we do now? So, so there has, I
[7:15] Doug B.: Yeah.
[7:16] Lloyd S.: just believe there has to be some existing interest or technology there, which there is to, basically, that you have the same thing. So you don't have to have a human doing. And so don't have a vision. I just think that that's what you
[7:28] Tim L.: Yeah.
[7:30] Lloyd S.: should do to, to stop, you know, paying me to do something that could be
[7:32] Doug B.: Yeah.
[7:35] Lloyd S.: automated, right? I, I
[7:37] Doug B.: Plus the other.
[7:39] Tim L.: The.
[7:39] Doug B.: Plus the other thing we find is we get a lot of people. That don't know how to do it properly at the other end and they get Lloyd gets these emails. Like my thing won't open or their company. Protections won't allow them to open things and it's just it's constant, right? And it's just a pain in the ass dealing with all those those sort of situations. So we want to eliminate that pain as well. So um, yeah.
[8:06] Tim L.: One thing I was gonna just flag right from the beginning. Is all of these companies loblaws, you've mentioned, they're all kind of dealing with their own, like internal gift cards and stuff like for their businesses. I would not be surprised at all, if none of them allow Kind of access of gift cards outside of their own portals and stuff. I mean exactly an example is cash star. So they are able to work with these other companies. But they might have kind of like a specific agreement so I don't, I don't think you'd be something that could be accessed without a prior agreement. With the companies is what I'm saying.
[8:49] Doug B.: So in response to that. So the way that I look at that is Is we've already bought the cards from log laws, so we own those cards, you know, they're they're right now, they're sitting in our inventory on Google Docs or whatever. Is there not a way that someone could go under our website and, and grab those cards that we've already bought from Lavas? And now we have them as a reseller.
[9:16] Tim L.: There could be if that's how you want to do it, like kind of manage an inventory of say La Blas cards. But then at that point, you're still gonna have to do
[9:25] Lloyd S.: Right.
[9:25] Tim L.: that. There's going to be some manual step along the way, where either there's inventory, updated or some sink that's run for sure. Yeah no that would be certainly easier than Saying, Hey Lovelace. I'd like to buy 10 cards. Let me behind the curtain, please. So I can buy those 10 cards. But yeah, if you're kind of from the reseller perspective that's definitely easier for sure.
[9:46] Doug B.: Yeah. Yeah, because
[9:47] Spencer R.: Yeah.
[9:48] Doug B.: We've been talking to sort of Amazon Walmart and Loblas this week about a few different things and Loblaz is, is very protective. They're not open to anybody integrating with them. Walmart is like we're already integrated with their backend and Amazon. We're starting down that path of getting integrated with them at whatever level, we will be able to get to with that. We're not sure. But a lot of laws is quote, is quite protective of that and they haven't really advanced at a technical level that that some of these other companies have obviously Amazon number one, but Walmart too. And then I would say Love was
[10:25] Tim L.: Yeah.
[10:26] Doug B.: those are the only three we really care about. Like, we want to be able to have the others to be retrieved on the site. But those are the big three sellers. So, those are the ones that I'm most concerned about and want to make sure we have solutions more.
[10:39] Tim L.: For sure.
[10:41] Lloyd S.: And, and just regarding what Tim said. The only thing that we know of are informed us from funds. Amazon cards on a site, then you can't have the Some piece of information up there for more than you know, like an hour or something like that, right? That when we talked to those guys from Front Street so, so there may be things like that, that we need to investigate but otherwise, Yeah, there's no no restrictions. Once we have the cards, right? And I in fact they don't care like they once they once they get sell the cars, they're they're not really interested in providing support or anything at the cards, get stolen or whatever. So they've already got their money. They don't.
[11:22] Lloyd S.: Okay.
[11:23] Doug B.: Yeah.
[11:25] Spencer R.: Yeah. So I mean, obviously there's some some technical complexity that sort of underlies the solution but, you know, at a broad level sort of what I'm hearing is. you know, if we're, if we kind of make a change to move towards orders being captured within it confined like organizational account with, you know, blog, used user name, login, etc, Once someone completes an order. Payment is captured outside of the the website. Once payment is confirmed. It sounds like we would need to look at building a mechanism that allows your team to say. Okay. We've captured payment. now, we're going to put This portion of our inventory to this client where they can now access it in their account. So I imagine we would need a
[12:31] Spencer R.: We would need some form of a method of assigning, the gift card, you know, the gift card number range or whatnot. And being able to push that into the actual order. And once that's done, obviously, and email can go out saying, you know, you can now access your cards within your account, Is that sort of what you're seeing Doug.
[12:55] Doug B.: No, some what? I I see that the ordering will continue exactly how it is. Right now they don't have to log in or anything to order. That's just it'll stay
[13:04] Spencer R.: Hey.
[13:06] Doug B.: exactly how it is. There'll be able to be a new banner at the. This is just my
[13:07] Spencer R.: Okay.
[13:11] Doug B.: little vision of it. It'll be the banner at the top of the website which is the
[13:12] Spencer R.: Okay. Yeah.
[13:16] Doug B.: login portion of the website.
[13:18] Spencer R.: Okay.
[13:19] Doug B.: And and the first step of the login portion of the website is there'll be able to go in and retrieve their digital gift cards. That's kind of what I see is like Step, Ace step number one, right? So they're still going to go on. They're gonna order their digital card just like they do without having to log in or anything. We're going to invoice them just like we do now. They're gonna pay us just like they do now. There's no payment website.
[13:41] Spencer R.: Yeah.
[13:43] Doug B.: And then now, when they paid us instead of Lloyd having to go out and email
[13:43] Spencer R.: Yeah.
[13:48] Doug B.: them, their digital cards and then deal with all the followed, all the questions and stuff that we're going to deal with, we're going to throw that on that logged in website portion and they're gonna go in and retrieve it. That's, that's what I see is. Kind of step one.
[14:02] Spencer R.: Okay.
[14:04] Doug B.: But not not not we're not getting into login. Place, an order. Pay with your credit card on the website. Like we're not going there yet.
[14:13] Spencer R.: yeah, just so I guess the, the one
[14:14] Lloyd S.: See.
[14:16] Spencer R.: thing I would say is, Yeah. The the login piece, the reason why that's it, like, important is, it it creates a fractured user experience where Someone comes to place an order and the old, you know? If let's say they place a digital card order, we would need to be able to associate that order with someone and so they would need to have created an account before. Placing the order in order for that association to be automatic
[14:51] Doug B.: Hmm.
[14:53] Spencer R.: because otherwise it's still going to require. Some manual effort for someone on your end. To say, Okay, this digital order came in. We now, in order for them to retrieve it, we need them to go and create an account. And so if the orders already happened and then they go and create an
[15:13] Doug B.: so,
[15:14] Spencer R.: account, they would need to have done that before. That's only way we can associate the order with the person.
[15:20] Doug B.: Okay, so maybe we could have the digital orders. They need to log.
[15:26] Spencer R.: Yeah.
[15:29] Doug B.: we're getting groups. You guys have done a fantastic job with the website. We've
[15:33] Spencer R.: Yeah.
[15:33] Doug B.: got lots of coming on in place in first orders with us, right? And as long as as long as they're not saying they're choosing to pay with a credit card, that's his gravy for us, right. They say there isn't to pay with a credit card, then we have to do our due diligence, and make sure they're legit and all that sort of stuff. But we're in the bulk business too. Right. So when we, if we've got someone, that's gonna order a bulk, what digital cards, we already have a relationship with them. So we could easily, we could easily do that. We're the
[15:59] Spencer R.: Right.
[16:02] Doug B.: ordering of the digital cards. They need to create an account law, login, password, and off, we go. So, it's something like that.
[16:09] Spencer R.: Yeah. yeah, that that could You know, Option.
[16:18] Lloyd S.: That, that would be greater when you create like yeah when the digital or you would create the account that they wouldn't create it, would they like that would be something that you would have to provide on those systems like
[16:29] Spencer R.: We want them to do it because they would need to set their credentials.
[16:33] Stephanie L.: Password. Yeah.
[16:37] Doug B.: so,
[16:38] Tim L.: you could I mean, Yeah. So you could do it a few different ways as far as I see it, if that was kind of the way to go is so after like while while you said in the invoice I could see. Potentially You also include a link to create your account there and
[16:57] Spencer R.: That's the point.
[16:57] Tim L.: that you say like Your your digital cards will be delivered securely via our, you know, our account or whatever, our portal, Digital gift card portal. Please sign up for an account. And then once they've signed up for an account then you know, whatever transfer of digital cards numbers could happen. Then the reason I say maybe it'd be better to happen as kind of an after step is then, because right now, the, the order form, Has nothing to do with any kind of user a creation or account creation. So if it were to have that step we'd have to kind of probably modify it So if it's working as it is, now I would say, if it's not broken, don't fix it. So we could add that step as a
[17:49] Spencer R.: Yeah, that's a good point.
[17:50] Tim L.: as like,
[17:51] Gord S.: I think, I think Spencer, you know, you're correct and say you don't want to create any stickiness, on the order Doug, I mean, I think in terms of, you know, if we can continue to have some manual input in terms of the actual initial order and then from from there, like Tim says, I mean make it. It's almost an opt-in if they want to monitor it. I mean if they're able to disperse it as is and there's no friction.
[18:16] Spencer R.: Oh yeah. Fred you froze, their Gordon?
[18:17] Gord S.: Sorry. No, I just, I just think in terms of making it seamless in terms of the
[18:18] Stephanie L.: That was my connection. They're not.
[18:21] Spencer R.: Catch that last bit.
[18:22] Doug B.: yeah, just
[18:26] Gord S.: flow through of start to finish. If you will, I think we want to have the order of the collective amounts, as a third party. We sell our, the digital format stay the same. It's on that order. Give them the ability to opt in. At that point because I don't think you want to do that from the start because some people they'll be calling us and say How do we do this and there have us walk through the whole process. And it's sort of a dashboard that they can sort of the way I see it is. They could have this on the digital side, a dashboard, as to how their flow through is going on there. And there may not be any stickiness at all, they may be able to just disperse the the E cards, you know, as they normally had in the past, but it's only if, you know, from lost sort of cards or whatever that they'd have to refer to something, and find it, and not avoids them, calling Lloyd or us or whatever, as to, you know, where's this individual?
[19:19] Gord S.: Hard gone. It would be there for them, but I think on the, at the outset, I think, I don't think we want to have a login initially because that will dissuade people from from coming and ordering. I think
[19:32] Tim L.: Yeah, you wouldn't. Yeah you need a login after the fact if you're gonna deliver anything digitally like via the portal or else, there'd be no way of
[19:37] Gord S.: Right.
[19:40] Tim L.: differentiating. Between this user that user. One question as we kind of think through this potential approach. So the gift card numbers. So a client would order the gift cards. You know, they'd have gone through the account creation step are you envisioning that then someone on your team would then input the numbers into their account or would that happen? You know, automatically if possible?
[20:11] Doug B.: Lloyd's.
[20:12] Lloyd S.: Oh well, give gift cards. And so Doug, this is something you have to think about whether you want to continue to offer PDF or just URLs or both.
[20:18] Doug B.: Chair. Okay.
[20:24] Lloyd S.: The offer both. So some people for those that have those office right, which basically is only blah blahs and well, anything that we generate right, anything like good
[20:33] Doug B.: Right.
[20:36] Lloyd S.: So so they're they're basically just PDF files with car with gift cards or their URLs. So they can be packaged in. So currently the process is that you get an order if we get like somethings we generate. So basically we get we've received from the vendor a id and a pin, and then we run through some stuff and create a card for them or we just go the best buy, and they just give us earls. And we just take the best bios, they give us and we just send them to them, right? So these are just things that are existing either in our inventory or origin them to their existing sitting on a disk and should just be able to be digitally collected as opposed to Some digitally picked somehow, right? So if there's I don't know of applications that do that now but I'm sure they're they exist. So that's that's the thing. So
[21:33] Lloyd S.: right now, We would. Put the cards together. Put them in if they want PDFs We put them in a zip file and then encrypt that if they want earls, we put them in a Excel file and we encrypt that and then we emailed into them.
[21:51] Tim L.: Yeah, so yeah.
[21:53] Lloyd S.: And it's done on a on a per and they received their cards Perpended. They're not all cards sent to one, so if they order five different vendors to get five different zip files or or Excel files and then they're just sent. Yeah, this one
[22:08] Tim L.: For sure.
[22:10] Lloyd S.: winning. Yeah.
[22:10] Tim L.: Yeah, yeah. And that, that makes sense. And the reason I I see that little still likely be some manual effort there because the one thing I think kind of a security risk that we'd want to avoid is having a lot of like, unsort or having any really unsold inventory like numbers or files or anything sitting on the site or being pulled in automatically because you know, someone were to kind of, Get in there where they're not supposed to. They could, in, in theory, kind of like redeem, you know, the numbers. And then Just like like cash. So yeah, there will still likely have to be just some manual effort. Just kind of calling that out because otherwise It's kind of like a bank site then you got to have, you know, such intense security so that these numbers aren't getting hacked or you know somebody sneaks in and takes a bunch of them. So
[23:13] Tim L.: Yeah, that's just one thing I popped into my brain.
[23:18] Spencer R.: Yeah, so we just did.
[23:18] Doug B.: So Lloyd, sorry. Can I just
[23:19] Lloyd S.: I don't know, like if it's
[23:20] Spencer R.: Fine. Just yeah.
[23:22] Doug B.: Sorry, I'm Lloyd when we go in and grab like the cards from like Tim Hortons, or whatever, do you think someone is manually put those on the Tim Horton site, and then we, then they say they're approved and we go, we go get them. Or do you think that's happened automatically?
[23:42] Tim L.: Well.
[23:43] Lloyd S.: For instance, if it's Suncor, like the Petro Canada, guys. They seem that a lot of manual stuff's happened in the background, it takes forever to get the card. So it seems like they're probably doing what we do but I don't know about those other ones
[23:58] Doug B.: Yeah.
[23:59] Lloyd S.: because you go through a site. Seems like you're waiting for. They wait you you pay? And then all of a sudden magically this Indian notification saying Your cards are ready. I have no idea
[24:08] Doug B.: Yes.
[24:10] Lloyd S.: what they're doing in the background. I guess you could phone them and ask them like How do they How do they pick their? How do they create the because some of them provide multiple formats too, right like blah blahs, hit they they gave you the option to get different types of Besides earls, wasn't it or no, it wasn't loved one, somebody gave you like to give you numbers or what or to get.
[24:30] Doug B.: Yeah, yeah. That's fine.
[24:33] Lloyd S.: Yeah. So
[24:33] Tim L.: Yeah, the
[24:33] Doug B.: It's it seems on the Cash Star site. You can order links or codes like almost all of them have links or codes. I don't even know exactly what all that means. But what what I would suggest we do is Tim, we automate as much as we can and Lloyd if we need to streamline it we only do a URLs. We don't do PDFs. I'm all
[24:55] Tim L.: You. Yeah, but but the thing is, you, you can't
[24:56] Doug B.: that too. Okay, okay, well that's good.
[25:00] Tim L.: Can't. Because it's just, I mean, the one thing I will say is, like, you think of Walmart is a massive, massive corporation, right? With a huge, IT department,
[25:09] Doug B.: Yeah.
[25:10] Tim L.: huge security. So, the reason they're able to kind of Generate these numbers and have them activated. Then have them kind of referenced with all their point of sale systems and their online stores because they are so massive and they have this infrastructure The challenging thing with your approach is, there's so many different or there's Even if there isn't so many different vendors, there's a number of different vendors. And so like, even if you were to build, say some kind of automatic connection to one, It wouldn't be the same as to another, or to another to another. So
[25:44] Spencer R.: Well. I think the difference is that. you know, Progressive has all of the inventory in theory already, so we don't need to worry about connecting with The other platforms since they already have these, so we So, I think we could look at it and, and we pray to do a little thinking, on our end Doug of
[26:16] Doug B.: Yeah.
[26:19] Spencer R.: And I again I always view this in stages. Just like the first website is saying in a perfect world. Someone could come to the site without creating an account. they can order digital cards maybe at, you know, right before they submit we, we have like an option that says, if you would like to handle your own distribution of these cards, Click this box. And that would then push them into either an account creation flow. Or if they already have an account after they submit their order, they wouldn't need to do that. and then, once once the order has been captured, And they have an account. We could look at. Okay? Knowing the different types of vendors and the types of cards that you'll have an inventory.
[27:13] Spencer R.: Is there? What is the tiered approach as far as if, if there's a manual aspect, what does that look like? and then, What is a more? And maybe it's semi-automated in that someone on your team, looks at the order and vets it, and before approving, that cards are dispersed to like that online account for distribution. Because, you know, the end of the day. I know where Tim is coming from, which I agree with is that obviously in a fraud written industry, we just want to make, sure, whatever approach we we use limits, what I would call attack vectors. If you will is any bad actors, we need to limit. as much as possible, the potential for someone to You know, be able to interfere at any any stage of this and that's where I think the biggest risks are. But we can certainly look at, is it possible once in order has been captured and someone has an account? Is there a way for us to reduce the level of human? You know, input to push.
[28:24] Spencer R.: You know, whether it's these and obviously, it's better if the files are encrypted. Because then they could receive a separate email or something. Potentially that has what they need to gain access to that. yeah, we'd have to take a look at what the best way and, you know, come back because again, it also could be a scenario where Maybe it takes three times much development, effort to to have an automation component versus something that still has. Something slightly manual, you know? Obviously our goal is always thinking with whatever solution. You know we map out we're we're thinking how do we build this in such a way to like, Maybe Lloyd is spending X amount of hours a week, dealing with this. What if we can With the least amount of effort, cut that in half. and then determine If we want to like cut that by 90%, this is what would what that might look like and how much more effort it might be. Because I think that also might come into play is
[29:39] Spencer R.: There's always. kind of diminishing returns sometimes like on on engineering work where The fully automated thing could be. Maybe it's, you know, maybe it's three months of work to make that happen. and then we have to look at sort of the, the cost benefit of like, is it worth it to to build that extra, you know, functionality For the for the cost. So those are all things you know that are coming to my mind. I certainly think there's something there. That's feasible. It's I think it's just a matter of One understanding. On the digital side, what? You know, what would be the full breath of
[30:24] Spencer R.: You know, card vendors that would be provided. What are the current? What are the current formats of those look like for distribution? just because even adding an interface that allows someone to then, Distribute cards from their account. You know, out to different email, addresses. Those are all things that we would want to look at and factor in just because that certainly does add complexity. Not saying it's impossible but it just A lot there's quite a few things to consider for sure.
[30:59] Lloyd S.: so, so that I think well hearing is So, someone would still need to generate the cards, right? So, there's two different like, I explained earlier, like, there's either the cards that you receive and just forward in a different.
[31:17] Doug B.: Yes.
[31:17] Lloyd S.: Format right to get from best.
[31:24] Doug B.: Yeah.
[31:27] Lloyd S.: file generate the cards, right? So it seems like the packaging will still remain so you'll you'll if you decide to still deliver cards and CRYPTED Excel files and encrypted ZIP files. Then that process won't be automated. Someone has to do that. Right. And then and then there's going to be. Now they're going to be put
[31:45] Doug B.: Yeah. Okay. Yeah.
[31:49] Lloyd S.: somewhere and then The, the distribution, there's you have to decide how that's going to happen through. Various interviews like either this automated interface and that so that, okay, so to distribute like the way we do now, so eliminate the standing of email with their cards. It's gonna be somewhere where you plunk them in a folder and then some automated thing gets those files and sends them to the particular address and sends the password. Then there's and the other step where? Okay, so these things have been put into Zip file or Excel file, and you want to do the sending to the end. The actual person is going to receive the gift card on behalf of the customer, or let the customer do they, then there's another process there to I guess, unzipped or
[32:36] Doug B.: Yeah.
[32:38] Lloyd S.: Uncrypt those files. Take the the things and somehow map those to emails, and
[32:41] Stephanie L.: Up.
[32:44] Lloyd S.: send them for a customer, right? So, which is another process. But, but the generation will still have to have to be there.
[32:53] Spencer R.: You know, I don't know enough about the generation process. I mean they're there is a possibility that some automation could could happen there but I it just Because I'm assuming now, like, when you need to generate cards are, are you
[33:08] Lloyd S.: Yeah.
[33:14] Spencer R.: logging into a third party platform to do that, or
[33:18] Lloyd S.: No, no. So we have, we, we get the, the cards and whatever format we receive them. So, say, Earls typically earls. We can we can just pass on before we used to have to because of a thing with Loblaws, they would have progressive name in the card. So we used to do generation to remove. They would provide us earls. We would do
[33:38] Spencer R.: Right.
[33:43] Lloyd S.: generation to remove the stuff they put on there. That would say that cards are coming from progressive, and then just generate an empty card. And then we add the ability to add to, and from, and that sort of stuff as part of the cold, Okay? So if you limit it, all that stuff done, like, you know, do that anymore, you just get people cards and that, that sells one thing. So, then
[34:00] Doug B.: Yeah.
[34:02] Lloyd S.: there's the Walmart where we, they give us numbers. And we have to generate a car that someone could and could, you could use, right? So, so basically we'll
[34:11] Doug B.: Yeah.
[34:14] Lloyd S.: get a bunch of numbers from Walmart. In an account number. We'll put that into an Excel file. Then we'll run it will run a program on that Excel file which then generates PDFs. And those pdfs are the cards and then if the customer wants and PDF files. Then we'll just Zip those, those PDF files up and then send it to them. If they want a URL then we have to upload. Those zip files to another site which then converts the model to you URLs and then you put those into and then generate the next fall with all yours so that's kind of the process. So so basically
[34:55] Doug B.: Right.
[35:01] Lloyd S.: Early. It's Amazon and Walmart and shoppers drug marts. That little shopper drug. Mart is basically log ones, right?
[35:12] Doug B.: Yes, same company but their gift card.
[35:13] Lloyd S.: So they, they're not sending us. They're sending us earls now. Oh, they have, they always sent this earls. I can't remember. anyway, so if it's not shoppers, then
[35:22] Doug B.: I didn't.
[35:28] Lloyd S.: feels like four, four things now where we have to to Walmart Amazon
[35:32] Doug B.: Sure.
[35:34] Lloyd S.: Oh, chapters. And no more uber, right?
[35:41] Doug B.: Yeah.
[35:43] Lloyd S.: So anyway so four things where we have to actually do generation. Otherwise we're just getting URLs and just passing those URLs on to whoever. So
[35:53] Doug B.: Yeah. so here's Spencer, here's what I'm sort of seeing is that From listening to everything I've heard is clients still come on to the the regular website in order without logging in just like they've always done if
[36:10] Spencer R.: Yeah.
[36:12] Doug B.: it's if it's a digital order and it's the first time then we send them their invoice and then as Tim suggests that there's a link for them to register so that they can go and retrieve their cards, right? So once they once they've paid
[36:28] Spencer R.: Yeah.
[36:30] Doug B.: us, we'll still do what we what we need to do Lloyd, is right now, training Mario, who's in our office to, to do this stuff. So then one of the step that I'm hoping, Be done, is we will do all that manual work here in the office and then can we can Mario go and just plunk those those cards onto the website. So that the client can then go in and go log in and go grab those cards. So Mario's done all the the the manual stuff that Lloyd, you know, created code and all the thing to Mario's, and it just do that. Do that manual? Work and boom, throw it onto the website and then the client comes logs, in and goes, grabs goes, and grab those those cards. That's the way I see it. Sort of in stage one.
[37:21] Spencer R.: Yeah. That that seems viable to me.
[37:24] Doug B.: The only thing that I want to be able to do is I want that off that website. website. The, the clients that want it to go out to individual cardholders, I want to have that ability as well, if possible. And if that's not possible, then Lloyd, maybe the ones that want to individually delivered, maybe we have to deliver it through the through, the email process or whatever, I don't know, but that that's kind of, that's kind.
[37:49] Lloyd S.: Well, that's gonna be that's gonna be a big manual. Like to say they have like,
[37:52] Doug B.: Is okay.
[37:53] Lloyd S.: you you get 670 into his emails then. They're gonna make mistakes and email addresses. Anyway. Yeah. So there's
[38:01] Doug B.: Okay.
[38:02] Lloyd S.: there's stuff that has to be. I mean it's doable but stuff that has to be considered right to like if you have a big order to distribute but yeah it's
[38:06] Spencer R.: Yeah.
[38:06] Doug B.: Spencer.
[38:10] Lloyd S.: possible for sure.
[38:11] Doug B.: So that's where Spencer. I think that's kind of where I'm at is.
[38:14] Spencer R.: Okay.
[38:18] Doug B.: The like, Tim suggests that link. If but we got regular clients, that order digital cards from us every every month like The lady Lloyd that we're just dealing with on the Esso card. Heather Harvey or whatever. She she's gonna come in order. She'll she'll have her account. She'll come in, she'll come on our website, she'll place an hour, she'll get her invoice. She pays for it will, let her know your cards are ready. She'll log in, she'll go grab her cards and coffee. Go done, right? That's that's sort of easy
[38:45] Spencer R.: Yeah.
[38:47] Doug B.: in my mind. The issues seems the delivery to the end card holder sort of thing,
[38:49] Spencer R.: Yeah.
[38:55] Doug B.: right? So, I know,
[38:56] Spencer R.: that's that's part is definitely where where there's a lot more complexity and again, I'm not saying it's impossible
[39:04] Doug B.: Sure.
[39:08] Spencer R.: but probably a lot of
[39:11] Doug B.: Yeah. Yeah.
[39:11] Spencer R.: A lot of time and energy to figure out how something like that might work again.
[39:14] Doug B.: Sure. So how do? How does, How does Loblaz work then. So they they have a like a Excel form that they make you fill out. So Lloyd like said they they obviously make
[39:24] Spencer R.: Yeah.
[39:27] Doug B.: the client put in the email addresses if one of them don't work. Well, that's
[39:39] Spencer R.: Yeah, possibly.
[39:42] Tim L.: Yeah. Well the Excel like the entry of the emails isn't the tricky part. It's the delivery of the emails and doing that in a kind of a secure way and
[39:51] Doug B.: Okay.
[39:55] Tim L.: The secure and scalable way. So like you said, if there were 600 emails and then how would you parse out the different numbers and assign them to each individual email? Or so? Yeah, it's it's like like Spencer said it's definitely possible.
[40:06] Doug B.: Yeah.
[40:10] Tim L.: And I would just caution against again, comparing to one of the big companies because They have the resources and the structure. So I mean like I said it is like
[40:17] Doug B.: Yeah. Okay.
[40:21] Tim L.: sending emails through a WordPress site is totally possible but you'd want to be able to do it in a way that could scale with you and also be secure so that you're not worried about You know, 600 card numbers going somewhere wrong or something.
[40:36] Spencer R.: yeah, yeah, so we can Certainly, look at that. I view the, you know, the individual. Distribution of a bulk. Order would be like, You know. The. That would be the cherry on top if, if that's feasible, you know. So we can
[40:56] Doug B.: Yeah.
[40:57] Spencer R.: certainly look at like What is this? Look like across these couple of different options? And then that, that certainly could be considered. But but yeah, just especially when Tim Brontë and I met earlier this week and we're looking at it, it's Definitely is some some added complexity and you know, obviously that is It creates a better consumer experience for whoever's ordering the cards because it helps sort of eliminate, you know, someone having to download a file and then it's on them to figure out how to distribute. There is.
[41:37] Lloyd S.: You know.
[41:38] Spencer R.: You know, a possible scenario in maybe this is a separate. Future consideration is. You know understanding what Lloyd is going to be training? Your your team member on like there maybe there is a way for us to to maybe help there as far as Maybe. and figuring out a way to streamline that That sort of generation process to being sort of a local. in office tool that can be used, but you know, that I would say, From a customer standpoint. If if you can automate as much of the you know, sort of checkout ordering process as possible. You know. Obviously, eliminating sort of the manual pain of having to generate these different file types. And things probably is something that takes up a lot of time. So certainly that might be something that we could look at, but
[42:50] Spencer R.: you know, to keep the the shift on the website side of things, You know, obviously, we're always trying to think of how do we, how do we do something that is effective and it moves you forward. But, you know, is also we're factoring in like engineering overhead and like, As soon as you have a system that is transmitting, you know, the actual gift card numbers. That's gonna be something that has to be like maintained. In kept secure sort of at all times. Just because this technology continues to evolve, you know, we would just want to make sure that we had something built in such a way that was was secure and, and That, that certainly would add some risk now. I guess. And and what we'll do after this call is, is trying to best summarize, everything that we've heard and sort of a couple of the different past four. Just so when we parent that back to you that it tracks with With what you had in mind.
[43:53] Spencer R.: when it comes to the white labeling, I guess one caveat is The. The White label Portal Side of Things. Is is a different solution than then the other two. because, it would essentially require like, what we're what we built today is likely not gonna It may not work in in that sort of white label scenario. and so, like, as as I'm thinking about this as a project, I'm mindful of if we jump in, we add the additional options for the digital with the account side. And then down the road. We decided to do the the, you know, the white label sort of ability. That likely means, we're coming back to have to reduce some, some work elsewhere. So, I'm, I'm always just mindful of which path we take, because it does have downstream sort of implications on how we would approach solving first project, if that makes sense.
[45:09] Lloyd S.: Thank you.
[45:11] Doug B.: It. Yeah okay so just kind of coming back to the digital card sort of thing. So the only difference Lloyd were really talking about is delivering it by email or clients coming on to a website and retrieving the cards, right? That's the only the only difference. So there's no real advantage really doing
[45:28] Lloyd S.: It correct? No. Yeah.
[45:33] Doug B.: this. Right.
[45:36] Lloyd S.: Well, I think the advantage if If you can control the distribution this and that's your furthest one, right? Like actually doing the emails. Then then We'll cut down all your it will cut down like calls or you get where I think. I mean people just make mistakes they they send out cards twice, they do right? Potentially all those things, right? And then those all come back to you and your control. So the more control you have in that then that that's a good thing
[46:04] Doug B.: Yeah.
[46:04] Lloyd S.: but and the The manual part is so in the generation process, like so if you have 600 cards and you want to generate that it takes some time, right? So loblaws was the longest, it was about 20 seconds per car. The other ones are about a second per thing, right? So it's not, it's maybe five minutes you're sitting there, right? So and then there's just the, you know, so you get inventory, we put it into our
[46:25] Doug B.: Yeah.
[46:32] Lloyd S.: local storage, then an order comes in for x number of cards. So, then, for the ones that have to be generated, we have to go go into a file mark that we're using. This inventory. It's going This customer, take those things. Copy it into an Excel. From one Excel file into another Excel file. Save that run the generation program. It generates it just verify that things got generated, do some checks there and then zip them up or upload them to the site that creates the if they want to earls. Right? So that's that's the basic
[47:06] Lloyd S.: process. So the more Running around like so two cards here, you do that. You have 15 different words. So that's just, you know, so that could be automated if you eliminate, I guess you just have a big every time you set up your inventory so that you can run another thing that basically, Goes and grabs the cards automatically from that file. Populates the file you want to use for your generation and all that's automate. Then you just you hit a button, one button and you just sit there and wait for it to finish, and then you zip them up, right? So that'll cut down on errors and that kind of stuff, right? So there's some, there's some possibility there, but you have to serve, come up with a system for what, for how you do that, right. But otherwise, it's, it's you have to go through and, and manually do those things, right? And you go
[47:58] Lloyd S.: into our cards on there, then you have to go and order them. And, and that's it, and you and now it's pretty streamlined where, you know, you know, these orders are coming in. So, By the time they've paid. waiting around or going to with with more inventory, something so But yes, the what's gonna change now like that, won't that can't change. It could probably could be automated more but it it is what it is and it's just going to be the delivery. And the delivery of the cards. So some of what we're seeing they're doing in email, grabbing the cards attaching all those attachments writing whatever and then saying the cards, it will be put on the site somewhere and then someone else will come in and grab them. And if you're going to do that way too, I would say. but I don't know that just having a username password is good enough because then I think you need to have something that will. You know, like two step off it authentication or verifying that this is a computer that belongs the organization that like they have a certain computer that has to be used. At least there's no
[49:20] Lloyd S.: Somehow someone who the people who put their password on a sticky and leave it up on the wall that someone can go and read it and then log in and go get the go get the gift cards, right? So
[49:36] Doug B.: So Spencer when it. Why don't you guys? I'm also open to suggestions too. Right, so what guys you know you've heard kind of what we're thinking kind of with the
[49:42] Spencer R.: Yeah.
[49:47] Doug B.: processes in the back. Why don't you guys come back with some suggestions and ideas and thoughts. And my initial thought is, I don't know if if we can't really automate too much whether the investment would be worth, shooting it out by email versus someone logging in and coming in and grabbing them and all the risk involved with all that. Is that worth it, right? So, I'm, I'm open to
[50:11] Spencer R.: Yeah.
[50:16] Doug B.: Gordon. I have talked about this a lot. We really trust your company and trust you guys. And we we see this as a long-term partnership where we're going to
[50:20] Spencer R.: Yeah.
[50:25] Doug B.: need you for a lot of different things. We're we're gonna be automating more and
[50:27] Spencer R.: Absolutely.
[50:30] Doug B.: more so we trust you a lot and yeah Lisa talk to Tim the other day.
[50:32] Spencer R.: Yeah.
[50:36] Doug B.: She works in Mark Tim's a great guy, so helpful. No, seriously like we. Yes,
[50:39] Spencer R.: Yeah, for sure that
[50:41] Doug B.: there's a long. We see this as a long-term partnership so we want you to say Doug. You're thinking on the wrong way, this is what you should be thinking about. Like, I'm open to that.
[50:51] Spencer R.: Yeah, absolutely.
[50:51] Stephanie L.: Okay.
[50:52] Doug B.: Some more discussions with Tim and Danny with what Lloyd's actually built on the automation side. Maybe there's some some ideas that we can automate and what's involved at the cost to do that and whatever this is you know kind of know. I don't know. Lloyd's told me many times it's not his exact exact expertise but he's he's smart enough to figure it out and do it for us and helping us out. So
[51:12] Spencer R.: Yeah.
[51:17] Doug B.: maybe there's some new things that we could do to automate that whole process. So maybe some more discussions, but I see this is a deep partnership that help us. Like What do you think we should do? I have, I have no clue. Like, honestly,
[51:29] Spencer R.: Yeah. Yeah.
[51:33] Doug B.: I I don't admit I like I'm running the successful business and I'm gonna stage where I need to automate. I I don't know what the f*** to do. Seriously, like
[51:41] Spencer R.: Yeah.
[51:41] Doug B.: he's telling me, what's your vision? Well, I don't know. My vision is because I don't know enough about this stuff and Gord helps me and what helps me a lot and stuff. So that's why that's where I'm at. I'm talking to family.
[51:49] Spencer R.: Absolutely.
[51:52] Doug B.: Members. I'm bringing in people that know, machinery stuff because I don't, I don't have clue and I know we got to go. We got to go there so that's where
[51:59] Spencer R.: Yeah, absolutely.
[52:00] Doug B.: that's where I'm at. So go go, you guys go back, you guys discuss it, come back to us. And you don't have to just, you know, kind of see what their problem is, they're paying is and create the benefit they need. I want you to come back and tell me. What we should be doing. From you, from your, your basis of your expertise. Because I'm happy to invest
[52:21] Spencer R.: Yeah, absolutely.
[52:24] Doug B.: in you guys to help us make this better. And what do we need to do? And maybe maybe like Tim says, maybe it's It's too much of an expense to get into that game. All I want. I want to know that too.
[52:38] Spencer R.: Yeah, absolutely.
[52:38] Stephanie L.: Yeah.
[52:38] Lloyd S.: Yeah, the only thing I would add Doug is, is you know, and again, I don't I'm on in your office. So I don't know what when you're doing physical cards, but but
[52:49] Doug B.: Yeah.
[52:50] Lloyd S.: I think probably with the physical card you probably get most people to be able to go and you say, Okay, I need to get these cards. They could go and pick the cards as they go. Grab these, put them into a into a folder even if they didn't
[53:03] Doug B.: Yeah.
[53:03] Lloyd S.: know anything about and and get FedEx and send them to these people wherever like in general, that's what right? But but so now if If I'm not here, Mario is on vacationer decides to play it or whatever. Like it's not easy to now, get people to do your, your digital card fulfillment. You can't just you can't you can't go to Elena and say, Okay can you take this?
[53:25] Doug B.: No, for sure.
[53:30] Lloyd S.: I know you're busy but can you say, she won't, right? So so you either have to
[53:33] Doug B.: No, she
[53:34] Lloyd S.: get and I know you have a, You don't have many people in office. So so see. You have to have multiple backups.
[53:42] Doug B.: Yeah.
[53:42] Lloyd S.: in case something goes wrong, and I don't know that and it's not something that everybody's just going to be able to To just pick up and do, right? So that that's that's what I see is the as the, the main thing, it's just a different process and it's not, it's not, you know,
[53:57] Doug B.: Yeah.
[53:59] Lloyd S.: I would say it's hard but it's I don't think you can just find anybody just
[54:03] Doug B.: Another reason why it should be automated more streamlined more, so it can, it
[54:04] Lloyd S.: there to do it for you. In the case of the sudden it comes.
[54:11] Doug B.: can work, you know what I mean? So, and so just this go ahead.
[54:19] Lloyd S.: No. Yeah and and I think it can it can be fully audited me that I think. But
[54:24] Doug B.: Yeah.
[54:24] Lloyd S.: again it's how much are you willing to?
[54:26] Doug B.: Sure.
[54:27] Lloyd S.: To pay I guess in.
[54:29] Doug B.: So the last piece I'll just I'll just do a quick summary of. Here's here's where we are with the automation of the company inside. We've got sort of three stages now. So number one is, we're gonna get in a little machine into our office that will be able to stick our gift cards. Just put 25 dollars on 50, whatever that is step one. And soon as my guy, he's a family friend that used to own a own machine companies. He's also related to People, Jim Cody's brother-in-law for for the two people that I know well here and soon as Gavin figures out, what machine, we're going to buy, we're going to buy that, that's going to happen. ASAP Step Two is, we're we're gonna get some machinery. That's going to be able to capture barcode magstripe and QR code
[55:18] Doug B.: information off the various merchants We're going to be able to do that. And then we're going to put
[55:26] Spencer R.: Okay.
[55:26] Doug B.: And then from that we're going to then use that use that database to control our inventory. And also, to have to control and help us with our order fulfillment, rather than pen and paper and all that kind of stuff, right? So that that's going to be step two in the process and I'm not fully explaining it, but that's kind of where we're at with that, and that's a much bigger investment. And that's the point
[55:48] Spencer R.: Yeah, that makes sense.
[55:53] Doug B.: where I think that the, the ai stuff that you are talking about automation is, Gavin tells me, that we be able to tie this in, with invoice in and the whole, the whole operation. So that's step two. And that's a, that's a big not. And that's gonna be a big investment which I know. And then the third step will be taking that stage two stuff and integrating with the merchants. So that'll be a point where then we can go and we don't have to go to Walmart and say, which of these cards where were they use? We, we don't have to go to law blogs, we don't have to go to all these guys, we'll have that because we'll be integrated with their back and Is starting that process already where we're starting with. So we're starting with Tim Hortons through Cash Star and we're starting with with Amazon. Those are our first three. So my theory is, will start to build that through. That
[56:38] Doug B.: silo loader, Lloyd will start to integrate, and then in three to five years, whatever it will have all this integration done with these guys, we'll have our stage two kind of capturing of the barcode magstriping to our code, in our own database. Then we'll be able to connect the two. I kind of see this without Knowing what the investment dollars are yet. But I see this is kind of the vision over the next three to five years. And and so that's kind of the Lloyd
[57:03] Spencer R.: Yeah.
[57:06] Doug B.: kept saying Doug, what's the vision where do you want to go? So now I met my my people and that's kind of where we're at. So I think and then this website thing
[57:13] Spencer R.: Yeah.
[57:18] Doug B.: is a whole different thing, like the digital gift cards is a whole different thing. Besides this, this automation inside our office here for the kind of the physical card world and we got to figure out this digital car thing too to to
[57:28] Spencer R.: Yeah.
[57:33] Doug B.: get into competing with, you know, the the fun stream guys. They have a system where they can just in, what do they say Lloyd? Like in two seconds, they can have any good gift card. Do they end user and have it on their phone and off they go. So I don't know what they've done. They've invested a lot for like, 10. 15 years, we can't catch up right away, but we got to do something. Or we're not even in the game sort of
[57:56] Spencer R.: Yeah.
[57:57] Doug B.: so, you know,
[57:57] Spencer R.: Okay.
[57:59] Doug B.: so,
[58:00] Stephanie L.: It I gotta run to another call. Thank you. Bye.
[58:02] Doug B.: Yeah, that took long but that is a really important for us. So,
[58:04] Spencer R.: No. Yeah, no, absolutely yeah. So we can That context is is super helpful. And it, it sounds like to me. Obviously. website front end customers being able to do things as valuable, but it sounds like a really major Pain Point slash point of failure in the business right now is is the actual generation of of the cards. You know? Lloyd not around forever, new staff, if you I forget I try not to say hit by the bus at someone who wins the lottery and retires. That's better enough than she and they're no longer there. You want to make sure that you've got the ability to transition that work to someone very easily. And that, it's something that
[58:56] Spencer R.: Someone could read a set of simple instructions and be able to do without having to have a bunch of training. So to me it sounds like You know, we started talking about White label and you know, adding a few features but underlying it's like Hey this is actually probably something that could keep you up at night. If if all the sudden, you know, the the people that have the the knowledge to do, those things are gone. So
[59:22] Doug B.: Yeah.
[59:23] Spencer R.: I definitely will will tap Danny just to to put this on his radar and and we'll
[59:26] Doug B.: Yes.
[59:28] Spencer R.: work to sort of summarize what we heard. And then, yeah, then as a team, we can look at like, You know, I'm I'm always the the optimist when it comes to solutions and I always appreciate Tim and Brontë. are really good at saying, Yeah, anything is possible. But, you know, here here's like, really boots on the
[59:51] Doug B.: Yeah.
[59:52] Spencer R.: ground. This is what building something like that, looks like. And, of course, we're always trying to think creatively about how we can tackle things, but, yeah, we'll we'll chat and see what we can come up with.
[1:00:07] Doug B.: You also said, you guys are moving into this sort of automation world as well too. These sizes the website world, right? So
[1:00:13] Spencer R.: Yeah, absolutely. It's it touches almost every facet of our business right now.
[1:00:20] Doug B.: Yeah.
[1:00:20] Spencer R.: So it's And it's moving quickly, too. So it's there's always new tools, new things coming out. But again, I think the the big caveat with any AI work is is just it presents a sort of new security risk to businesses just because just because you can use AI to do a thing, doesn't mean you should right now. I see people, you know the new thing came out this past weekend. Everyone was doing it and bad actors already started targeting those folks and Caused people to delete their entire databases delete their entire email history. Just because someone saw something on Twitter and decided, Hey, I'm gonna go run this thing on my machine and see what happens, you know. So Yeah you have to just, you know, the future is looking pretty incredible but you know, we have to remember that. Takes time for, you know security researchers to vet a lot of this. We always want to be make sure that we're you know not getting too excited about humans not having to do work anymore. It's still I think we're still at a juncture where having someone actually checking and verifying things still is pretty critical. But yeah, we're we're always what monitoring
[1:01:38] Spencer R.: And watching what's coming out.
[1:01:39] Doug B.: Yeah, and if if Danny or Tim or whatever need to talk to Lloyd, he would be happy to you know share what he's done and where we're at and all that sort of stuff too. So we kind of
[1:01:50] Spencer R.: yeah, I might loop Danny in on that, just because it might be helpful to even You know. For him or me to jump on with Lloyd and even just have him walk us through like Hey this is, This is how I've this is how I'm generating stuff now you know for these different vendors. Here's the part that takes the longest Here's here's why bring someone else in to do this, if I'm not here as hard. because maybe we have some ideas to, you know, To package something up. That could help make that, you know, build on what Lloyd has if you will, and make it a little bit easier for the team, that that's certainly might be possible.
[1:02:34] Doug B.: And and most of the stuff we're just resellers of gift cards like Lloyd, those are the few exceptions that he had to do his work on. don't really have a voice in that, right? So we're just doing whatever. They,
[1:02:47] Spencer R.: Yeah. Yeah.
[1:02:51] Doug B.: you know, Starbucks sends us an email with like an hour. Here's your car, it's
[1:02:51] Spencer R.: Yeah.
[1:02:56] Doug B.: and somebody Elena shoots it off the Lloyd goes. Here's our cards, right? So it's like, they're all different, right?
[1:03:04] Spencer R.: and that always, Makes It Tricky When you know an industry doesn't have a standardized sort of practice or approach and because it's a bulk commercial. Business. You know, you don't have the end consumer, bitching about this being painful.
[1:03:22] Doug B.: Yeah. Yeah.
[1:03:24] Spencer R.: You just not when you're dealing with volume like. Yeah, at the end of the day it's like Okay this is how you get it. You know as I tell my three year old you get what you get, you don't get upset, kind of thing, you know.
[1:03:34] Doug B.: Yeah, but I think that's another thing Lloyd too. I think you know, if we have to streamline what we offer them to make it. Work better. Maybe we do that. Right. Maybe don't give them the choice of the PDF in the URL and whatever. We just say your bulk, this is what you get or I don't know.
[1:03:52] Lloyd S.: Yeah. I mean you don't have that many just some of the original people. They want the pdfs. But most people everyone that we you get now they're just, we just default to earlier which
[1:04:06] Doug B.: So I just, I would think in that way area. Spencer, and Tim let's just you. Thank you, think in the world of URLs, don't worry about the yes. Well, we'll
[1:04:13] Spencer R.: Yeah.
[1:04:15] Doug B.: move those people off if we have to and we need to
[1:04:18] Spencer R.: Yeah, URLs would would be a lot easier to manage that's for sure.
[1:04:24] Doug B.: Though, I think we need to in order for us to automate more. I think we have to streamline it more too like this, this is what you get. Yeah.
[1:04:29] Spencer R.: yeah, yeah, sometimes you have to You know, it's just like any business that is moving forward. There's always going to be some customers that fall off the back of the wagon but you've got more coming on. And you know so at the end of the day it's it's part of business, right? As any business evolves, there's always going to be a few folks that maybe don't love the change in to say, Hey, this isn't for me but usually that you can grow faster when you're able to deliver more because the last thing you want in a business is to get You know, I always do this with our team. It's like, Hey, if we had five new clients all come next week, And say they wanted X thing. You know what would be our response to that and if the responses I don't know how we can possibly do it. Like that means there's an opportunity to improve delivery somewhere and so when you tell Lloyd hey we just had 10,000 gift card order come in. And Lloyd, you know, like you want that to be a celebration conversation. Not a, How in the heck, are we gonna? I don't know how we're gonna do that. You know?
[1:05:35] Spencer R.: And so that's where I'm always thinking from a technology standpoint, how do you make new business wins? Be not restrained by human capacity, like Like not, who are we gonna bring in to help make this happen, right? Like, so if you can automate some of that and make obviously Any business there. There's effort that goes in but if we can somehow make it easier, big orders come in and they're easier to deliver without as much, you know, manual touching then obviously that that's a win.
[1:06:04] Doug B.: plus more, and more of our existing business is Switching from physical to digital too. So digital is becoming even more important in those areas. It's, and it's going to be more and more and more, we
[1:06:13] Spencer R.: Yeah.
[1:06:16] Doug B.: all know that. So,
[1:06:18] Spencer R.: Yeah, absolutely.
[1:06:18] Lloyd S.: Yeah. I think if you're, if you had the same number of digital card orders, as you had physical, then you wouldn't be able to keep up.
[1:06:29] Doug B.: Not a chance. No.
[1:06:31] Spencer R.: Yeah so that yeah that right there certainly means tick ticking time bomb, so
[1:06:31] Doug B.: Not.
[1:06:31] Lloyd S.: Okay.
[1:06:36] Spencer R.: it's good that you're thinking about it. Now before you get to that point where it's like we can't we can't keep up. Yeah.
[1:06:40] Doug B.: Okay, so if you know where no where we're at and like I said before we we trust
[1:06:42] Spencer R.: so, Well.
[1:06:51] Doug B.: you guys immensely and we see this as a long term partnership and what's the next? What's the next step in it?
[1:06:59] Spencer R.: Absolutely, yeah. We'll we'll chat on our end and um, I know it's Thursday, probably gonna take us a couple days to to work work through this, but we'll probably reach out sometime next week and Give you an update on where we're at? And then we can go from there.
[1:07:22] Doug B.: Of yeah. Okay. Thank you.
[1:07:24] Spencer R.: All right, appreciate your time. Thanks Lloyd. Thanks Court.
[1:07:26] Lloyd S.: Okay. Thanks. Good. My
[1:07:28] Spencer R.: Have cheers.
