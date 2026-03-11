---
title: "Internal Pre-Meeting Discussion — Progressive Gift Cards"
type: discovery
category: internal-discussion
date: 2026-01-27
status: complete
format: transcript
source_url: https://supernorm.al/bronte-spencer-progressive-8773c7cef897453abdc9c9f16067727f
participants:
  redstamp:
    - Spencer R.
    - Tim L.
    - Brontë B.
tags: [internal, white-label, wordpress, custom-post-type, woocommerce, formidable-forms, payment-processing, scope-assessment, cash-star, feasibility]
key_insights:
  - White-label = essentially building a product, not just a website
  - WordPress custom post type per vendor is the most pragmatic MVP for white-label
  - Formidable Forms can likely be retained if no account creation is needed
  - Account creation + order history pushes scope toward full rebuild
  - Payment processing must stay external (BenjaPay) — no credit card storage
  - Team consensus to temper expectations and pitch incremental approach
  - Digital card creation/redemption mechanics are still unclear and need Lloyd walkthrough
  - Traditional e-commerce platforms (WooCommerce, Square) don't fit because Progressive's model is "faux commerce" — order capture without on-site payment
related:
  - docs/discovery/2026-01-29-client-discovery-call.md
  - docs/discovery/2026-01-29-client-meeting-transcript.md
---

Brontë / Spencer: Progressive transcript
Tuesday, January 27th @ 11:49 AM | View at https://supernorm.al/bronte-spencer-progressive-8773c7cef897453abdc9c9f16067727f


[0:00] Tim L.: Totally.
[0:01] Spencer R.: 18.
[0:02] Brontë B.: How's it going?
[0:03] Spencer R.: Oh, pretty good. How about yourself?
[0:06] Brontë B.: Pretty good. It's pretty chilly. Hey, we're just talking about how cold it is
[0:07] Tim L.: Not too bad.
[0:11] Brontë B.: here.
[0:12] Spencer R.: oh,
[0:14] Tim L.: Yeah, it's really gross.
[0:14] Spencer R.: I, What looking out being in the more temperate to Western coastal climate.
[0:24] Brontë B.: Yeah.
[0:25] Spencer R.: Not been as nasty.
[0:27] Brontë B.: Yeah, it's been a rough winter in Ontario. Like usually it's not, I mean, we're used to snow in cold weather but this year it seems like it's like every week there's oh this or this and I mean we've already had two snow days this month, which is A lot for them a month, like, within weeks of each other. So,
[0:48] Spencer R.: Yeah. Okay. Well, hopefully You're Tim, you were out for a bit and then brontë, you're How long you're in Mexico next week?
[1:03] Brontë B.: Mm-hmm. Yeah.
[1:05] Spencer R.: I mean, if you can pick a time to go,
[1:08] Brontë B.: I know.
[1:10] Spencer R.: Now is now is the time.
[1:10] Brontë B.: I, Yeah, I'm definitely looking forward to some warmth.
[1:20] Spencer R.: Well, appreciate you both jumping on the progressive saga continues. All, let's see here. I'm trying to think of the best way to do this. Just gonna I did a couple of Simple mock-ups. For them. Sort of been. Early last week, I think. Just trying to pull these up.
[2:03] Spencer R.: Yeah. Was hesitant to sort of over invest in anything. Mainly just because I, I think Some of the stuff is still somewhat up in the air. And I I don't know what they will sort of successfully pull off. From pitching a client. Okay, here we go.
[2:34] Tim L.: This is this is all wildly different.
[2:49] Spencer R.: So there's a couple different potential roots. I think that They are looking at slash considering. One is. kind of a white label setup that Mirrors. What a company. I think they're called Cash Star does their A fairly big company. and and sort of what they've done is built a sort of E-commerce Portal If you will that's white labeled based on the vendor. So Doug has provided a handful of logins to Examples of how this has been spun up for like Tim Hortons as an example. So what it allows someone to do is on the Tim Horton's website, if you click like order, you know, corporate gift cards. You're taken to a
[3:50] Spencer R.: You know, a New page that sort of has branding customized. So and by customized, it's basically swapping out the the color bars on the background. You know, there's like a text treatment in the footer, obviously it has a Tim Hortons logo and then some sort of custom imagery. That then allows, you know, a business to basically hit sort of get access, which is kind of like a Create account flow. Obviously. You know, a login or create an account sort of screen. And then, once you're in, and I think, this will hinge on sort of what potential direction they would would want to go, but In the example here. Someone comes in, they can sort of pick from, you know, physical or digital. They can pick custom art that matches the
[5:05] Spencer R.: The Gift Card Brand. And then, they can pick. You know a delivery method, so either sending to the recipient or sending links to the person placing the order, and then they have sort of a multiple recipient versus single recipient workflow and then you can upload a spreadsheet. That would essentially populate, you know, the order form. And so nothing. I think wildly different from sort of what we've built. Yeah. Sorry sorry. I should say the
[5:44] Spencer R.: The functionality here is is not necessarily different but if if we were to go and in this direction, we You know, formidable forms, I think would likely no longer be the right solution obviously just because we would need sort of account creation. And we'd have we have to look at the viability of of some of these.
[6:02] Tim L.: Yeah.
[6:08] Spencer R.: Methods.
[6:09] Tim L.: yeah, so I just want to make it clear that none of this functionality exists like
[6:13] Spencer R.: Yeah. Yeah, correct.
[6:14] Tim L.: Okay good. Just just so we know.
[6:16] Spencer R.: Yeah, no, it's more from just a Like, I guess a UX standpoint.
[6:22] Tim L.: Sure. Yeah, for sure.
[6:24] Spencer R.: Not, it's mainly just the, the recipients piece that is different.
[6:31] Tim L.: But you're right. Yeah. Similar kind of UI flow for sure.
[6:34] Spencer R.: Yeah, so let me stop and then I'll cut over. To his email. So they've met with a couple of vendors and, and I, I didn't confirm that one of these options. Is viable. I don't think it really is, but You know, a few things that would be under consideration is that they have a link on a vendor site that just posts to the progressive site. And obviously, with this option, we would be likely looking at a full rebuild anyways. So it wouldn't have sort of any of the custom branding etc. Would be more akin to what Walmart does now. So when you go to Walmart, you go
[7:31] Spencer R.: Corporate Gift Cards, There's a link for progressive, and they basically go there. I think, obviously, that is the easiest solution. I think Doug or Gord came up with this, but essentially they put a link on their site to float through to our site where they can only order cards for this specific merchant or restaurant. now, from a technical standpoint there, There may be a way to I guess have some logic. where if someone comes from a certain link, That that maybe there is a way to filter what cards? Eventually show up in it in a dashboard. I'm not sure though this this one just seems a bit messy and has more risk because if someone has You know, if they come back they they click the site, they look. And then they come back later and they don't have like a cookie or something. That has that filter in place, then they're then they're gonna see other options. So I I think
[8:53] Spencer R.: this is one, I would Try not to steer towards. and then option three is kind of what I showed with my mock-ups is that, you know, we would essentially have individual instances of e-commerce experience that have been sort of custom branded for a vendor that we like physically, you know, that we actually manage and spin up as their own sort of some It would likely be on a subdomain of Progressives main site.
[9:31] Tim L.: Yeah.
[9:33] Spencer R.: The other points being. So another topic, we'd like to discuss are around digital card orders. We have a handle on both digital card orders or resend all the cards to one organization representative. As we have discussed, we want to be able to send to all the end users. For these book orders. When requested, the new topic you want to discuss is our clients being able to go on our website. After we have created a username and password protected area, to retrieve their digital cards. Maybe this area could also initiate their digital cards being sent out to their individual card. Recipients
[10:12] Spencer R.: Here's the Loblaws website where progressive can download their digital cards once they log in. The two green icons are where we can download our digital card order either as an Excel fire file or a CSV. The other icons are an Order Summary button that reorder button and activate Physical Cards button. So this wouldn't be necessary. And I actually have logins for this where we can like log in and look. Specifically, at this. so, I think this piece here would be sort of a component of Essentially. I think where we we likely would be going either way. Which would be looking at building out.
[11:08] Spencer R.: Has sort of an account creation process. and then obviously showing You know, the orders and whatnot order history. Now, I guess I'm curious. you know, I know that Woocommerce was something that we had considered And I'm just wondering. How much flexibility? Something like Woocommerce would allow for. you know, like, A custom status component or something like that.
[11:55] Tim L.: So, a couple things. So this would be an absolutely massive thing to build out. Are they aware aware?
[12:02] Spencer R.: Yeah.
[12:04] Tim L.: That, that is possibility.
[12:06] Spencer R.: I communicated that it would be a, it would be a basically a completely new build. Yeah.
[12:13] Tim L.: Yeah. Okay, that's good. Because like when they reference things like You know Loblaws or something, blah blahs has like dozens and dozens of developers will that like they're
[12:24] Spencer R.: So Loblaz is all. They're all built on the Cash star setup. Yeah.
[12:29] Tim L.: Okay but even probably cash stars. Probably like a large company just doing that. So I just want to make sure we're kind of tempering expectations in terms
[12:34] Spencer R.: Yeah.
[12:39] Tim L.: of like Yeah, it'll be a big build to build something like this.
[12:45] Spencer R.: Yeah.
[12:49] Tim L.: I think the thing and maybe brontë, you have a better handle on it. I'm still a little confused about when they say like vendors. So like So, a user wants to order cards. For their. Like their employees, right? Is that correct?
[13:07] Spencer R.: Yeah.
[13:07] Tim L.: And then they go to the site. And by vendors, do they mean like Walmart or like
[13:13] Spencer R.: so yeah, it so imagine, you know, a small chain of, of grocery stores in Toronto called Fresh Street Market,
[13:23] Tim L.: Sure.
[13:23] Spencer R.: And right now, Fresh Street. Doesn't have a good way of administering bulk gift card orders to businesses. So
[13:30] Tim L.: Sure.
[13:32] Spencer R.: it would, you know, rather than someone coming to progressive and having the ALA carte like option to buy both gift cards from a bunch of different stores. It would be just fresh street market cards available. And progressive, essentially, it would be. Coming in as the fulfillment partner to help capture the orders and handle the, the distribution and and they're the value prop is taking that off off the plate
[13:59] Tim L.: Yeah.
[14:02] Spencer R.: of of the vendor.
[14:03] Tim L.: Yeah, so progressive wants to move, not just beyond selling gift cards from merchants, but facilitating the sale of merchants gift cards for the merchants themselves.
[14:13] Spencer R.: Yeah, yeah, and so if they If they do it for one. Then it, you know, become something a little bit more repeatable.
[14:28] Tim L.: Sure is, is the idea that like Are they wanting to assume any of the like payment processing or things like that? Or like, like liability of storing people's credit because like like,
[14:43] Spencer R.: So yeah, I've pushed back on the payment piece again saying that. I still think the payment. Processing and captured needs to happen via Benji pays. just because they, they aren't going to be able to Get like the rates. That they would need for the margin here, to make sense.
[15:10] Tim L.: Yeah. And I mean, like, I, I would stay away from any kind of thing where they want us to like build out something that stores credit cards.
[15:21] Spencer R.: Yeah.
[15:22] Tim L.: And like you said, I mean, then then you're looking at payment processors like, PayPal or stripe or different stuff, which is possible but yeah, like you said, might eat into their margins
[15:33] Spencer R.: yeah, so the I still think
[15:34] Tim L.: Okay, so yeah.
[15:37] Spencer R.: Which which again makes it still kind of a system that is, you know, faux commerce to degree. And that it's capturing in order.
[15:47] Tim L.: Yeah.
[15:48] Spencer R.: It allows someone to see. What order has been placed. But, you know, ultimately the the actual payment
[15:53] Tim L.: Yep.
[15:58] Spencer R.: capture needs to happen outside of Of.
[16:03] Tim L.: Yeah. Yeah. It's like it's like a first step. Like a carrier pigeon saying I
[16:03] Spencer R.: You know, the system.
[16:08] Tim L.: want if cards. Okay. Okay. So I think I'm wrapping my head around it. More and
[16:08] Spencer R.: Yeah. Yeah.
[16:13] Tim L.: Brontë feel free to jump in. I'm just Thinking out loud.
[16:17] Brontë B.: No, no. I I don't really have much more to say than you already.
[16:20] Tim L.: I just know that because I I've done a little more with the format so okay, so
[16:23] Brontë B.: Yeah.
[16:25] Tim L.: that's making more sense. So in that kind of side of things I can see something where it's like, If we took payment processing totally out of the equation like it's gone like still functions the same way. As the site does now then you could probably not too hard. I mean, still a good amount of work but you could create like, a repeatable kind of post type for a merchant, like I'm saying like a WordPress post type or this is how I might see it working where it's like, Fresh street market. And then when you create that post type and you fill out the fields, it gives on the site a page with a dedicated form, right? So it's like you have Progressive. Gift. Pro Gift Cards whatever.ca/freshstreetmarket.
[17:17] Tim L.: So that, that would be kind of like the easiest entry point is basically, like, You're allowing a merchant like that has an agreement with Progressive to say, Okay, we'll spin up this page for you, your clients can go here. They submit the form and then we help fulfill things the way we've been fulfilling things.
[17:34] Spencer R.: Yeah.
[17:35] Tim L.: And then that and the benefit of maybe doing it that way, is that there's still no account creation. It's likely we could still leverage, formidable forms. So it's not like a Necessarily a rebuild at this point, it'd be more like a graft on.
[17:49] Spencer R.: Yeah.
[17:54] Tim L.: Yeah, it's where it gets kind of tricky is when they want to start thinking about like a counts and logins. And then like also things like sending out digital gift cards and like because the thing is, like, if we use this fresh street market, example, Who's creating these digital gift? Cards is progressive. Creating them and then how are they stored and redeemed, You know what I mean? Like, so even if
[18:18] Spencer R.: Yeah.
[18:19] Tim L.: Progressive sends a card that has the numbers, You have gift card number one, two, three, four. Where's that stored and how does Fresh Street Market know that? One, two, three, four has $30 on it and then when it comes time to redeem it so it's like yeah, it's like
[18:38] Spencer R.: Yeah. So that and I it from the sound of it, it seemed like Lloyd was involved to a degree on an aspect of this.
[18:49] Tim L.: True.
[18:51] Spencer R.: So, I think that's something that we would want to uncover on Thursday. Yes.
[18:55] Tim L.: Sure. Yep. Yep.
[18:59] Spencer R.: because yeah, I think That functionality is. Is certainly something that becomes more complex. Just because then you, you have.
[19:11] Tim L.: Yeah. Yeah.
[19:14] Spencer R.: You have two layers for that you have sort of a internal administration. Layer where it's like, Okay how do we? How do we assign a range of gift card numbers to an account?
[19:30] Tim L.: Yeah, and how do you keep track of their decreasing value? Or like Yeah, it's like The the distribution of the gift cards is one thing. And then the actual like, creation and management of it is another
[19:45] Spencer R.: Yeah.
[19:48] Tim L.: Yeah, and I don't mean to like harp on Progressive, but I think they also maybe need to be a little bit. Self-aware. When it comes to their their technical abilities.
[19:59] Spencer R.: Yeah, absolutely.
[20:00] Tim L.: because it's like, I think they've done a great job adapting to their website and kind of learning that some of those technical but they were still having troubles with the blogs kind of getting those up and running. So I just want to make sure. Yeah, whatever solution we're suggesting is also
[20:12] Spencer R.: Yeah.
[20:16] Tim L.: one that, you know, either, they can maintain or we can maintain
[20:22] Spencer R.: yeah, which which certainly could be a viable path forward just because it
[20:22] Tim L.: To, to maintain. Yeah.
[20:30] Spencer R.: You know.
[20:32] Tim L.: Yeah, and that might be.
[20:33] Spencer R.: None of it is rocket science from a management standpoint as long as they can
[20:37] Tim L.: No.
[20:38] Spencer R.: follow the system. But it does certainly pose some some risks. I almost feel like we will be back where we were when we first pitch this project, because we did originally pitch, you know, a more robust to count creation account management, and they weren't ready for it. I think what you you've kind of flagged their Tim is likely a pretty good like in like pretty good MVP and like, You know we create a custom post type for a vendor that restricts, what someone is able to, you know, to see. Obviously if there did need to be an account management account setup piece, that would be net new And would likely change the sort of technical constraints to a degree. but, You know, being able to Simply give someone a custom portal. if if you will or a URL at progressive for, you know that because in that custom post type, you could have some likely have some You know, custom style, attributes like colors and in a logo, right?
[22:01] Tim L.: Oh yeah. Those are the easy things, kind of the stylistic things. And because
[22:06] Spencer R.: Yeah.
[22:06] Tim L.: what it would essentially, what like I was suggesting, there would be like It's a custom order form page, basically, right? And we can figure it. I mean
[22:13] Spencer R.: Yeah.
[22:16] Tim L.: styles. Yeah. Images. Content. You know, we could add a map to where the actual You know, like a map field that's filled out to show that this is where this market is. Still, doesn't that kind of approach? Wouldn't cover the actual cards themselves? It's one thing. Like like I don't know how Progressive creates all their digital gift cards now but it's one thing to go to Walmart and say,
[22:44] Tim L.: You know, these are digital like Walmart create these digital cards.
[22:48] Spencer R.: Yeah.
[22:49] Tim L.: that still doesn't help Fresh Street Market, where it's like, You know, these are the cards. You know where the actual cards coming from and how does fresh street market? No, you know. What's on them? Like I'm just kind of half Googling while we're talking and there's like There's different. There's different like gift card plugins. I don't know why I said that was such weird emphasis on
[23:22] Spencer R.: Hmm.
[23:22] Tim L.: but but I don't really know how they work, and I don't know if it's like This plugin creates a gift card for like, for instance, like Pro Gift cards. I don't know if you can use them to create plugins for
[23:35] Spencer R.: Yeah.
[23:36] Tim L.: Different brands. but then at the still at the same point, I'm still like, Then it's all living. On progressive site and a vendor. Doesn't yet know how to like check these or redeem these or do anything.
[23:52] Spencer R.: Yeah.
[23:52] Tim L.: With them. So, Short of like progressive. Emailing Fresh Street market and saying, You've got an order for a $50 gift card, and then the manager signs it and was like $50 and then sends it back. I don't know.
[24:09] Spencer R.: Yeah.
[24:10] Tim L.: I don't my brain doesn't have a. solution for that yet, I would we'd have to do more research I guess to
[24:18] Spencer R.: Let me. would it be helpful if I put a couple of these logins into one password
[24:33] Tim L.: Possibly. I mean what the logins for were for like, Were they for?
[24:39] Spencer R.: Yeah. Like let me Let me just log into this one. It's like here.
[24:46] Tim L.: or maybe like a competitor if they have an
[24:49] Spencer R.: There. Yeah, so these are actually Love how you just sent these via email. oh man, so this this is an example like so to show you how um, sophisticated some of their Sourcing is. They often buy their gift cards in bulk. from some of these vendors for their stock,
[25:22] Tim L.: Yeah.
[25:25] Spencer R.: And that's, that's why the margins are so slim.
[25:29] Tim L.: yeah, so like Is this what progressive wants like you log into their site? You're like,
[25:36] Spencer R.: Essentially something like this. Yes. So you can see that this is a
[25:38] Tim L.: Yeah.
[25:44] Spencer R.: Essentially. A portal for Starbucks cards, you can go to the cards. you know, you can pick physical digital So, let's say I want this. You pick your quantity.
[26:13] Tim L.: Yeah.
[26:15] Spencer R.: Hard value.
[26:18] Tim L.: and then you're like,
[26:19] Spencer R.: And then you, and then you add it to your your shopping. Car, if you will.
[26:24] Tim L.: Yeah.
[26:27] Spencer R.: and then,
[26:28] Tim L.: And they want to be able to do that for anyone that comes to them, basically.
[26:32] Spencer R.: Yeah. So basically a white label system that you would essentially then deploy
[26:33] Tim L.: Yeah.
[26:38] Spencer R.: like, For them. And you can see how many orders progressive as put put through for this.
[26:46] Brontë B.: She?
[26:48] Spencer R.: so, You know, here's an order December 8th. You can.
[26:54] Tim L.: Yeah. and then, and then progressive also wants the ability to like Yeah, like a client then looks back and says Oh I ordered from Fresh Street Market, four months ago, these cards.
[27:09] Spencer R.: yeah, and then they could reorder
[27:10] Tim L.: Reorder.
[27:13] Spencer R.: Etc.
[27:17] Tim L.: yeah, I mean, this is
[27:18] Spencer R.: So it's it's not a small undertaking.
[27:22] Tim L.: Yeah, I just Yeah, yeah. No, it's it. I mean in one respect to be good because if they're into some version of this and we can figure a version of this that works and is attainable, it could be a good chunk of work if they're
[27:40] Spencer R.: Yeah, that's what I'm thinking.
[27:41] Tim L.: Yeah, I just I want to make sure we're not promising. Starbucks. IF
[27:49] Spencer R.: Yeah.
[27:49] Tim L.: you know, if that's what they're kind of envisioning and we can only do If you go back to your email for a second, did they have at the very bottom? I
[27:56] Spencer R.: Yeah.
[27:57] Tim L.: thought I kind of saw the corner. My eye like a competition.
[28:02] Spencer R.: Fun stream.
[28:03] Tim L.: Yeah, let's let's do you mind if we just look at their competition real quick
[28:05] Spencer R.: No.
[28:07] Tim L.: because That might be more helpful than This. Then.
[28:18] Spencer R.: And I think the fun stream is likely going to be, like, more kin to what? If, if we were not thinking about white labeling, what what would it look like to? Have like more of the account creation, sort of aspect.
[28:36] Tim L.: Yeah. because the thing with white labeling, it's like Yeah, we'd like be creating a product for them, right? So it's like,
[28:45] Spencer R.: Yeah.
[28:48] Tim L.: Yeah. That's that's Big stuff. Okay. So what is this? So you want
[28:55] Spencer R.: so, you can, so the individual order would be cards will be packaged in individual envelopes, for each recipient I assume Like the
[29:07] Tim L.: and these are, is this digital cards to, or just
[29:08] Spencer R.: Tim Hortons one. They had a little template like an Excel CSV template you would download to populate and then when you would upload it, um, Well, let's see. Additional.
[29:28] Tim L.: because like,
[29:28] Spencer R.: so,
[29:30] Tim L.: Like, this looks like kind of like what Progressive has on their side already.
[29:33] Spencer R.: Yeah.
[29:34] Tim L.: just maybe with like
[29:36] Spencer R.: so, I think this here looks to be physical cards
[29:40] Tim L.: Yeah, so then that takes that whole kind of Side of it out of it. It's like, you know, Because a gift card, if you sell a gift card to an established vendor, they have the The mechanism for process and stuff. So that's like, this is like
[29:53] Spencer R.: Yeah.
[29:57] Tim L.: Removing all that.
[29:59] Spencer R.: Yeah.
[30:03] Tim L.: Yeah.
[30:03] Spencer R.: And that has the order history.
[30:06] Tim L.: Just one other thing to wrap my head around, if you don't mind, so going back to the vendor example. So that the idea is that they're going to be like Marketing. This like exclusively to vendors that don't have anything like Like, they're not.
[30:23] Spencer R.: yeah, it would it would likely be
[30:24] Tim L.: They're not expecting this like importance or something.
[30:27] Spencer R.: No, no.
[30:31] Tim L.: Well, not, yeah, not necessarily even selling to Tim Hortons, but like they're
[30:32] Spencer R.: I,
[30:36] Tim L.: not anticipating providing a Tim Hortons platform page to a client or something.
[30:44] Spencer R.: No, like the the white labeled pages would be. A specifically for the the store chain group for their own gift, card product not for third-party gift cards.
[30:58] Tim L.: Sure.
[31:00] Spencer R.: and I anticipate they would likely be targeting smaller, you know, chains that Haven't been sort of engaged by. you know fun stream or if cash star or whatever, the other option is
[31:21] Tim L.: Yeah. Yeah. Yeah, it's a cool cool. Like my brain gets going thinking about it.
[31:33] Spencer R.: Yeah.
[31:34] Tim L.: but then, my brain also is like starts like Both get excited. But then also be like, Whoa. There's there's a lot a lot of meat here that would like and potential like
[31:45] Spencer R.: Yeah.
[31:48] Tim L.: holes to fall into, so
[31:50] Spencer R.: Exactly. So I think what we can really use the The call to like zero in on is one, I think. Transparency around effort. So as soon as we move from the setup, they have now into a account order history piece one. There's gonna need to be some form of, you know, API connector type. Tech that. Like, just tracking the ship, like the order shipping process and like tracking information. Like unless
[32:31] Spencer R.: Unless the first pass on some of that is they do that manually. But again I think that's also worth. They're going to struggle You know, as soon as
[32:43] Tim L.: Yeah.
[32:45] Spencer R.: As soon as they. Want to build something that allows a third party system to talk to their system. That's going to add a lot of engineering like overhead and investment. You know. I think it would be Great from a long-term like incoming, workstream but like are they? is this going to bring enough revenue to them to justify like the cost, you know,
[33:13] Tim L.: Yeah. Or is there like a modified version of that? you know, that they can implement That isn't going to require tearing down because yeah, like a lot of what they're suggesting would mean. Like totally redoing their site like
[33:31] Spencer R.: Yeah.
[33:31] Tim L.: Like, six months.
[33:33] Spencer R.: Yeah. At least the form, right? Like I don't think we'd need to change.
[33:34] Tim L.: Lot.
[33:39] Spencer R.: The Marketing aspect.
[33:41] Tim L.: Yeah. Like so the the visuals and the kind of yeah the marketing pages for sure.
[33:42] Spencer R.: but,
[33:45] Tim L.: Wouldn't need to change but like the the real guts of the site would have to change.
[33:51] Spencer R.: Yeah.
[33:53] Tim L.: and yeah, maybe maybe not a total rebuild but like the inner workings would certainly need
[33:58] Spencer R.: yeah, the definitely the the form piece, I think, You know, at least from a development standpoint is basically scrap at that point.
[34:13] Tim L.: Yeah, because it
[34:13] Spencer R.: Just because Any sort of new solution is going to require.
[34:15] Tim L.: it's
[34:19] Spencer R.: you know, account management component, you know, other things and you're better off just Finding a prebuilt sort of solution that is still somewhat flexible that allows you to. Sort of handle that.
[34:33] Tim L.: Yeah. Potentially like I'm looking just now like at square, for instance and square. Lets you create gift cards.
[34:42] Spencer R.: Yeah.
[34:43] Tim L.: but then like a client needs to have you squares, their pay like
[34:49] Spencer R.: Yeah. And that's why like we have to sort of stay away like
[34:51] Tim L.: Pos.
[34:54] Spencer R.: The problem, I think also with a lot of your sort of traditional e-commerce solutions as they're all sort of built around. Pushing someone to the actual payment processing step, right? And that's really not what we're looking for. And so that's kind of unique aspect of this
[35:22] Tim L.: yeah, it's almost like if we could there existed out there and maybe something that kind of is Worth researching is it's like, if there is an easy way, easy, I say easy quotes to create your own. Somehow be able to create and redeem your own digital gift cards. Like four client per se, then that might be something to look at because then you could retain kind of the basic form. and then use the custom post type, and then just have this Step that Progressive would need to do in the background. I don't know.
[35:58] Spencer R.: yeah, what I could see happening there is Having sort of a database of gift card numbers. But again, this this then introduces. You know, complexity, but essentially when they You know, the progressive side, to administer login, they could then. Select from a, you know, a database fed inventory. This, you know, I need to do 50 gift cards. I'm going to start with gift card that starts in these four numbers and ends in these four numbers. And then I'm going to pull from inventory this amount. But then again, that that requires some two-way sink
[36:46] Spencer R.: between a database Layer and like a front end, right?
[36:50] Tim L.: Well, yeah, and I'm also thinking like so then the person who has gift Card 101 goes to Fresh Street Market and hands it or gives it the whatever to the cashier in the cashier's. Like What do I do with this? I guess it's for a hundred bucks and they take it and then how does that hundred bucks? Then go from Progressive took the payment with Benji pays. Do you know what I mean? Like,
[37:14] Spencer R.: So so yeah. So and and that's something they can chat with us about, but they actually, they activate cards with the vendors themselves right now. For digital cards. And there was some talk about, like working with some of the, you know, vendor which Lloyd would be doing of like to make it easier for them to activate them, but right now, I think oftentimes they wait until the customer has the cards in hand before Progressive activates them. So you know, like
[37:56] Tim L.: Sure.
[37:56] Spencer R.: You know, or or it is something where the client logs into the dashboard, once they have all the gift card numbers and then they are able to activate them.
[38:08] Tim L.: The client being the vendors.
[38:10] Spencer R.: Yeah.
[38:12] Tim L.: Okay, so then yeah.
[38:14] Spencer R.: Or whoever, I guess, whoever bought the gift cards from the vendor. We can, we can get a little bit more clarity on there because I think it's it sounds like it differs from from store to store. As far as what possible. but,
[38:30] Tim L.: Yeah, no, for sure. There's lots of things to chat through. Yeah. Cool.
[38:39] Spencer R.: and you know, at the end of the day, it may End up being a scenario. Where the more we look at it we maybe we determine That, you know, hey Doug and Gord like just for my technical complexity standpoint. we may not be the best fit for the actual execution of this because like yeah, anything is possible but I'm also just thinking about like You know, our ability to sort of maintain and support and like, I don't I don't want to overextend our, you know, either of you and in such a way that
[39:23] Tim L.: I think. Yeah. I think like, for me, I'm not super concerned with about our, our
[39:23] Spencer R.: The.
[39:28] Tim L.: capability to do something for them, or to really build anything, I think.
[39:31] Spencer R.: Yeah. Yeah.
[39:34] Tim L.: I think Brontë and I are both. Like, Yeah, I think we could build anything because we're awesome. No.
[39:41] Spencer R.: Yeah, you are.
[39:42] Tim L.: No. But I mean, but I what I I think the thing that I think is like Is what Doug, what are is, what they're expecting, realistic because I could see
[39:53] Spencer R.: Yeah.
[39:53] Tim L.: them going to any number of kind of agencies or companies and they'd be like, Oh yes, we could build you that.
[39:59] Spencer R.: Yeah.
[40:00] Tim L.: Saying like yeah, what Starbucks has easy, we could do that. and then it's like and then it, they get halfway through the project and there's all kinds of problems and like, dug and Gord aren't happy or
[40:11] Spencer R.: Yeah, no. Totally
[40:12] Tim L.: It. It's like it's about kind of like thinking I think just kind of initially about the solution and expectations and like, what is actually? Attainable, What is meaningful and what it's going to benefit their business rather than kind of get to a point and realize you can't do something or like I've spent all kinds of time and money.
[40:32] Spencer R.: Yeah, exactly.
[40:33] Tim L.: And it's not actually what they want. So I think that's my more of my concern right now. Is that it's like, okay. What is the expectation? Can we deliver on that expectation? And is that expectation actually like One that's going to benefit their business.
[40:48] Spencer R.: Yeah. Yeah, agree.
[40:51] Tim L.: Kind of relative to the cash outflow that will likely of some sort will have to happen. So,
[40:57] Spencer R.: Yeah.
[40:57] Brontë B.: I'm just like the cost of what this is going to cost is going to make sense for Even being worth it for their business. Like, you know, like like Tim said like
[41:08] Spencer R.: Yeah.
[41:09] Brontë B.: this is not a small undertaking and I don't know, do they have enough interest from clients already? That want to sign up to something like this.
[41:18] Spencer R.: and that's that's where I almost think that You know, maybe the initial best pitch would be kind of the custom post type where to me, that makes the most sense because
[41:28] Tim L.: Yeah. Yeah.
[41:36] Spencer R.: It means that they're they're getting more exposure in traffic. They're able to prove, Hey this is this is working. They, you know, I think to start like we avoid The like activation management side. Because again, as soon as there's activation of cards, that's going to require an account portal and Behind the password.
[42:03] Tim L.: It's almost like you kind of pitch it like we'll be your gift card. fulfillment partners, and it's like this, this portal allows your clients an
[42:11] Spencer R.: Yeah.
[42:14] Tim L.: entry point to us, so that we can kind of Help facilitate the delivery of your gift cards, right? And then it's like,
[42:23] Spencer R.: Yeah.
[42:24] Tim L.: And then, you know, progressive, if they want to, if it's, you know, financially viable for their business, take on the nitty-gritty of helping deliver, that that's cool. But at least that way, you're not kind of sinking. A lot of technical debt into building something before. It's like,
[42:40] Brontë B.: Agree. It seems a little crazy to build something like this large for something that hasn't really been. Utilized by them yet. Like I know they have all these, like, partners and stuff,
[42:51] Spencer R.: Yeah.
[42:52] Brontë B.: but like it's a pretty deep dive to go from.
[42:56] Spencer R.: Yeah.
[42:57] Brontë B.: Nothing to that. And and I agree. I think what this is pitching kind of gives
[42:59] Tim L.: Yeah.
[43:02] Brontë B.: them a taste and You know maybe on a handful of clients to this and then they are like Wow this
[43:04] Tim L.: Yeah.
[43:09] Brontë B.: is really going well and then we can kind of open that conversation back up for something more robust. I think that's the best bet even just from like a cost
[43:16] Spencer R.: Yeah.
[43:18] Brontë B.: perspective too of You know, my eyes when I saw those examples, I was like this is a lot of work and especially for like a two team. Developer. I mean I understand we could amp up our team if you know contractors and such if if the price warranted that but still it's it's just a lot of undertaking.
[43:38] Tim L.: Yeah and they might not even know that it's a lot of undertaking, they might just see website being I'll just website stuff.
[43:44] Spencer R.: Yeah.
[43:44] Tim L.: so, there might be a little bit of understanding there to be gleamed, but it's like, Yeah, we can always scale up. We can always build more. We can always build, additionally, right? Like, you could always have the marketing site and then if they didn't want to, We could build a separate site that is kind of handling all that. So it's like there's so many different ways you could kind of scale things but
[44:05] Spencer R.: Yeah.
[44:09] Tim L.: Yeah, it's like they might because they might try it with two clients too, and be like, this is not worth our time. Like,
[44:15] Spencer R.: And that that's for the. The just the there isn't a You know as soon as you go into the more structured management of a thing, it becomes a It becomes a more custom software piece of a build, which
[44:33] Tim L.: Yeah, and I can.
[44:34] Spencer R.: Just gonna have cost.
[44:36] Tim L.: and with the custom post type because like I mentioned the styling of it all is Is very is that's the easy part. So you could really you could really create
[44:44] Spencer R.: Yeah.
[44:46] Tim L.: something that feels poor less. Like in customized to a client but in the end is just more or less a contact
[44:49] Spencer R.: Yeah.
[44:54] Tim L.: form to progressive saying. I want 10 gift cards from Fresh Street Market, Digital Gift cards. And then progressive can make that however happen, however, they need to. So,
[45:06] Spencer R.: Yeah.
[45:07] Tim L.: I mean, yeah. I think that's
[45:10] Spencer R.: Okay.
[45:12] Tim L.: I think that's what I'm thinking. Sorry, I feel like I was talking a lot.
[45:20] Spencer R.: No oh good. I just checking Miller, her message me. Yeah well why don't we you know I feel like you've at least got the contacts so that when we do jump on a
[45:30] Tim L.: Sure.
[45:33] Spencer R.: call, we can sort of hear what Lloyd is having to say. Then we can You know, from there, decide. Okay. What What's gonna make sense?
[45:41] Tim L.: Yeah. And I've had good discussions with them in the past and they're not at least in
[45:45] Spencer R.: Yeah.
[45:47] Tim L.: my experience, they haven't been unreasonable. So I think they've been open to kind of discussing things and Learning more about what's possible and stuff. So, maybe as they hear from us to Kind of a clear vision of what is actually kind of a workable solution. Might
[46:06] Spencer R.: Yeah, absolutely.
[46:07] Tim L.: Jenna, so that'll be good.
[46:10] Spencer R.: Excellent. Well, thank you both and I guess we will reconvene later this week.
[46:14] Tim L.: Yeah, sure. Yep, sounds good.
[46:21] Spencer R.: Okay, hope it warms up for you both.
[46:24] Tim L.: Yeah.
[46:27] Spencer R.: Hey, take care.
[46:29] Brontë B.: I,
[46:29] Spencer R.: Bye.
