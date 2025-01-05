label bitn_snootjam_storyline_1:

 scene black
 with None
 show car neutral with Dissolve(2)
 play music maltShopTheme fadein 2.0
 play ambient insideCarNoise fadein 2.0
 show car anon
 A "-hey, it could have been worse."
 show car trish
 T "Oh fuck off."
 show car fang at carBump
 F "I mean, he’s got a point, {w=0.40}be glad all they did was kick us out."
 show car trish
 T "Just because you’re fucking doesn’t mean you have to defend him, dude."
 show car neutral
 "Reed finishes taking a long drag on his half-finished joint."
 show car reed
 Re "What did you guys even do?"
 show car fang
 F "Anon sprayed the path to the cooler down with cooking oil."
 show car neutral
 "Reed chuckles."
 show car reed
 Re "Oh so thats why everyone–"
 show car trish
 T "Yes! {w=0.40}That’s why!"
 show car anon
 A "Well Stella thought it was pretty funny."
 show car trish at carBump
 T "{size=*0.5}Walking gym bag whore...{/size}"
 show car fang
 F "Your powerslide through the screen door was fucking cash to watch. {w=0.40}Did anyone get a video?"
 show car trish
 T "Screw you guys."
 show car anon
 A "Trish if you just kept your mouth shut-"
 show car trish
 T "Did I ask you, skinnie!?"
 show car neutral at carBump

 menu:
  "Play it off":
   jump bitn_decision_1_pio
  "Keep quiet":
   jump bitn_decision_1_kq
  "I fucked your mom":
   jump bitn_decision_1_ifym
   
label bitn_decision_1_pio:
 show car anon
 A "It’s a prank, not a dick. {w=0.40}Don't take it so hard." 
 show car trish at carBump
 T "WHAT?"
 show car anon
 A "Besides I didn’t think you’d drop so harsh. {w=0.40}How’s your head?"
 show car trish
 T "My head is the best in the state."
 show car neutral
 "Reed and I snicker as Fang rolls her eyes. Seems Trish is calming down"
 show car trish
 T "Look- the tile took more damage than I did. {w=0.40}Thank god. {w=0.40}I would have gored you right then and there if I cracked a horn because of your stupid prank."
 show car fang
 F "We could always go back and crash that shit."
 show car anon at carBump
 A "Game."
 show car trish
 T "Nah. Those guys are lame anyway. {w=0.40}Not a drop of alcohol… {w=0.25}who does that?"
 show car reed
 Re "Mormons, usually. {w=0.40}Gotta go to the catholic parties. {w=0.40}Those guys roll DEEP before it even starts. {w=0.40}Highly recommend it."
 show car neutral
 jump bitn_end_decision_1

label bitn_decision_1_kq:
 show car trish
 T "Thought as much."
 show car neutral at carBump
 "She turns to Fang."
 show car trish
 T "You two leave me out of your fucking prank war. {w=0.40}Can’t you see you’re just enabling him? {w=0.25}What’s next, {w=0.40}laxatives? {w=0.40}ARSON!?"
 show car anon
 A "It’s not off the table."
 show car neutral
 "Trish narrows her eyes at me through the mirror."
 show car trish
 T "Anon."
 show car anon
 A "Permission to speak your trigger-ness"
 show car trish
 T "Just pushing all the buttons you can find tonight?"
 show car anon
 A "Bet if I push a little harder, I can get steam to come out of your nose."
 show car trish at carBump
 T "Yeah, and a horn in the chest. {w=0.40}You have insurance?"
 show car anon
 A ".{w=0.40}.{w=0.40}.{w=0.40}Do you?"
 show car trish
 T "No. {w=0.25}So– {w=0.25}Don’t act like I can go to a hospital, and I’ll do the same for you, {w=0.25}dig?"
 show car anon
 A "Loud and clear."
 stop music fadeout 1.0
 show car neutral
 
 pause 1.0

 play music maltShopTheme fadein 1.0
 show car reed
 Re "Anyone want a hit?"
 show car fang
 F "I’ll take one. {w=0.40}You two are giving me a fucking migraine with your{nw}"
 play sound laughTrack volume 1.2
 extend "  mating calls."
 

 show car neutral at carBump
 jump bitn_end_decision_1

label bitn_decision_1_ifym:
 show car anon
 A "Your mom sure didn’t ask when she tongue punched my fart-box. {w=0.40}Should have heard the sound I made."
 show car trish
 T "Still didn’t ask."
 show car neutral
 "Fang starts laughing."
 show car anon
 A "Or maybe the time she gave me an under-table foot job at the Dave-and-Busters, {w=0.25}don’t tell her that I was thinking about Fang’s mom the whole time though."
 show car reed
 Re "Alright, Anon, that’s enough."
 show car neutral
 "Fang is dying of laughter."
 show car trish at carBump
 T "Oh, you wanna fucking go?"
 show car anon
 A "Lookie here, {w=0.25}I got that exact DM from your grandmother last night."
 stop music fadeout 1.0
 show car neutral
 "Fuming, Trish whips her head around and lets loose"
 show car trish
 play sound whipCrack volume 1
 T "{sc=1}You cueball lookin’ beach ball looking ass skinnie prick.{/sc}{nw}"
 play sound whipCrack volume 1.1
 T "{sc=2}Lookin’ like Mr. Clean's downie brother.{/sc}{nw}"
 play sound whipCrack volume 1.2
 T "{sc=3}Trigga’s got that 19-head, you look like a sniper’s dream.{/sc}{nw}" 
 play sound whipCrack volume 1.3
 T "{sc=4}Big words coming from a man with a hundred trigga-bytes of memory.{/sc}{nw}" 
 play sound whipCrack volume 1.4
 T "{sc=5}Got beforehead, forehead, and afterhead.{/sc}{nw}"
 show car trish at carBump
 play sound whipCrack volume 1.5
 T "{sc=6}Trigga tryna talk hot when bro’s brain is fucking vertical.{/sc}{nw}" 
 play sound whipCrack volume 1.6
 T "{sc=7}Frontal globe lookin’ ass trigga.{/sc}{nw}"
 play sound whipCrack volume 1.7
 T "{sc=8}Don’t get me started on that toothpick you call your morning wood.{/sc}{nw}"
 play sound whipCrack volume 1.8
 T "{sc=9}It’s like God's shaft division was out of budget when they made you.{/sc}{nw}" 
 play sound cornered volume 2.0
 T "{sc=10}Trigga you were made on Friday at 4:59 PM.{/sc}{nw}"
 show car neutral at carBump
 "Trish gets lost in a trigga moment and devolves into an unintelligible rant."
 "Fang grabs trish by the thigh."
 "She stops in place, and looks at fang with rage in her eyes."
 show car fang
 F "Be nice, Trish, {w=0.40}he’s got a lot on his mind."
 show car neutral
 "Trish cracks a smile as she continues to stew in silence."
 
 pause 1.0

 show car reed at carBump
 Re "You know what could be on all our minds?"
 show car anon
 A "Whats that, bub?"
 show car neutral
 "Reed is all too eager to indulge."
 show car reed
 Re "I’ve been thinking a lot about Wienerschnitzel."
 play music maltShopTheme fadein 2.0
 show car anon
 A "Oh my god, please tell me all about Wienerschnitzel."
 show car neutral at carBump
 "Reed goes into a conspiracy theory about money laundering. {w=0.40}The rabbit hole goes deep, {w=0.25}and Reed takes us all to the bottom."
 "Despite my heavy investment, {w=0.25}The girls him off after the fifth minute."
 jump bitn_end_decision_1
 
label bitn_end_decision_1:
 "Trish slouches in her seat and sighs."
 show car trish
 T "Alright. {w=0.25}Where we heading? {w=0.40}I guess we've still got a few hours before Ripley sends the locusts."
 show car reed
 Re "Anon thought we'd go take a trip downtown and celebrate the holidays properly."
 show car fang
 F "What are you talking about?"
 show car anon
 A "Go urban exploring! {w=0.40}There’s an exquisite shithole downtown I would love to show off! {w=0.40}Absolute masterpiece of engineering. "
 show car trish
 T "You’re fucking with me, right? {w=0.40}Where’s the fun in that?"
 show car anon
 A "Dead serious, {w=0.25}people leave the strangest shit just lying around, {w=0.25}not to mention it's where all the top graffiti is, {w=0.25}and the best haunts feel like little time capsules of the past."
 A "Come on, where's your childlike urge to enter places you don’t belong?"
 show car fang
 F "Mine fell off a cliff in 12’."
 show car anon at carBump
 A "Oh right…."
 show car trish
 T "Can we not, and say we did?"
 show car anon
 A "Besides, {w=0.25}you're overlooking the best part of it all."
 show car neutral
 "Anon grins and picks up a case of Coors Banquet from the back of the van."
 show car anon
 A "Unlike when we were children, we can- {w=0.30}as Reed so eloquently puts it- {w=0.30}‘roll deep’."
 show car reed
 Re "Highly recommended."
 show car neutral
 "The looks of skepticism were quickly wiped off their faces."
 show car fang
 F "Alright, {w=0.25}Dweeb went nuclear, {w=0.25}what’s the plan?"
 show car anon
 A "You want to tell them Reed?"
 show car trish
 T "Pass me a road soda."
 show car neutral at carBump
 "Reed is quick on the draw, and hands a frosty beer to Trish. {w=0.40}Feeling a bit sober, he grabs one for himself."
 show car reed
 Re "What's the limit to drive in this county?"
 show car trish
 T "For an 18 year old male, {w=0.25}I think it's 0.00."
 show car reed
 Re "They really need to work on that."
 show car neutral
 "Reed cracks his brew and takes a swig."
 show car anon
 A "Reed, you gonna tell them the details or what."
 show car reed
 Re "Right."
 show car neutral
 "Reed drops it in his cupholder and starts gesturing in a general direction."
 show car reed at carBump
 Re "We're headed straight into the heart of VB’s old industrial district." 
 Re "We’ll be welcomed by the rotting remains of what’s left of the manufacturing plant on the corner of Spring and Thompson."
 Re "A magnificent construct of rebar, brick, and concrete. {w=0.40}The clientele that reside in this area are very nice and can be trusted."
 show car trish
 T "But why there? {w=0.40}I bet there's a hundred dumps just like it around VB."
 show car reed
 Re "Well..."
 show car neutral
 "He grins and holds his phone under his maw on high like a flashlight"
 #[dim scene a bit except for reeds face or at least reed]
 hide car
 show reedStoryBack:
  matrixcolor BrightnessMatrix(-0.25)
 show reedStory neutral
 with Dissolve(2)
 #[cut out the music]
 stop music fadeout 2.0
 show reedStory speak
 Re "Many years ago, {w=0.25}it was an empire of steel processing, {w=0.25}even got into plane building during the great war." 
 Re "The family that ran it were geniuses of their craft, {w=0.25}and had perfected the art of worker exploitation."
 show reedStory neutral
 "He sits up and leans over as he gets sucked into his role"
 show reedStory speak
 Re "Once it finally came time to retire or refit the plant, {w=0.25}they decided to keep its doors wide open until the place started really collapsing." 
 Re "The death rates of the underpaid workers broke some international records, {w=0.25}and in ‘62 the city finally shut down the operation for good."
 Re "Rumors say ever since, {w=0.25}the victims' spirits continued to wander the crumbling halls, {w=0.25}seeking vengeance on those that wronged them."
 show reedStory neutral
 pause 0
 #[return bright levels to normal]
 show reedStoryBack:
  matrixcolor BrightnessMatrix(0)
 with dissolve
 hide reedStory neutral
 hide reedStoryBack
 show car neutral
 "Reed puts away his phone and goes back to finishing his joint."
 show car trish at carBump
 T "You don't think it's actually haunted do you?"
 show car fang
 F "Nah, ghosts aren’t real, {w=0.40}Trust me I’ve tried all the rituals."
 show car anon
 A "People have said they've seen weird stuff happen out there. {w=0.40}Strange noises late at night, {w=0.40}a flicker of light in the windows, {w=0.40}shadowy figures that'll disappear when you blink."
 show car fang
 F "Captain Carfe and his gang of retard squatters pulling copper."
 show car reed
 Re "Nah, {w=0.40}the locals steer clear of Spring and Thompson."
 show car neutral
 "…"
 show car anon
 A "Sure…{w=0.40}and if it seems occupied, {w=0.25}we’ll just turn around and leave; {w=0.40}I mean it's not like those bums are gonna follow us home. So,{w=0.20}we game?"
 show car trish
 T "Do we have a gun?"
 show car reed
 Re "No, {w=0.25}but I’m a 6 foot 2 raptor, {w=0.25}and I don’t doubt Fang’s ability to kill us all."
 show car fang at carBump
 F "I mean, {w=0.25}he’s got a point."
 #[everything except anon dims out a bit]
 hide car
 show anonThinkBack:
  matrixcolor BrightnessMatrix(-0.25)
 show anonThink
 with Dissolve(2)
 #[return music but quiet]
 play music maltShopTheme fadein 2.0 volume 0.25 
 "While the rest of the gang find something else to yap about, {w=0.25}I slump back in my seat and mentally rehearse my greatest prank yet."
 "Trish may have been amused by the appetizer, {w=0.25}but the real show was just beginning."
 "I've been planning this shit for weeks. {w=0.40}And in a few short hours, {w=0.25}I'm gonna get Fang so good she'll have no choice but to surrender the crown to me permanently."
 #[thought bubble graphic appears, dot by dot, about 2 or 3 dots whatever looks good, then the bubble, the animations should fit inside the bubble.)
 show thought bubble1
 with dissolve
 show thought bubble2
 with dissolve
 show thought bubble3
 with dissolve
 show thought bubble4
 with dissolve
 #[pull up first 2 frame loop]
 show animation animation1
 "The stage was all set, {w=0.25}and Reed was easy to bribe with a few herbal remedies."
 #[pull up second 2 frame loop]
 show animation animation2
 "Step one, {w=0.40}play it off legit. {w=0.40}Slowly get them boozed up."
 #[pull up third 2 frame loop]
 show animation animation3
 "Step two, {w=0.40}once they’re cooked, {w=0.25}Reed and I slip away."
 #[pull up fourth 2 frame loop]
 show animation animation4
 "Step three, {w=0.40}slather Reed in phosphorescent paint until he glows like nuclear waste. {w=0.40}Then suit him up."
 #[pull up fifth 2 frame loop]
 show animation animation5
 "The coup de grace, {w=0.25}come back screaming and get their attention."
 #[pull up 6th 2 frame loop]
 show animation animation6
 "Reed follows close behind and nails me with the trick knife. {w=0.40}The fake blood packs pop and I play dead. {w=0.40}Pray that Fang gets scared and takes the bait."
 #[pull up 7th 2 frame loop]
 show animation animation7
 "If everything goes right, {w=0.25}the chase begins."
 #[pull up 8th 2 frame loop]
 show animation animation8
 "And I make sure to get it all on film."
 #[pull up 9th 2 frame loop]
 show animation animation9
 "Final objective: {w=0.25}Survive."
 #[Cut music for next score and cut to black]
 stop music fadeout 2.0
 hide animation animation9
 hide thought bubble4
 hide anonThink
 hide anonThinkBack
 window auto hide
 pause 1
 stop ambient fadeout 2.0
 "It's not long before we finally arrive at our destination. {w=0.40}We collect our goods and disembark from Reed's pussy wagon to take in the view."
 #[cut in outside van and ambient sounds]
 scene outsideVan with dissolve 
 play music outsideAmbience fadein 2.0
 #[the gangs sprites all enter together stage left in neutral pose]
 show reed neutral:
  xcenter -0.5 yalign 0.1
  ease 1.75 xcenter 0.85  
  xzoom -1
 show trish neutral:
  xcenter -0.5 yalign 0.1
  easein 2.0 xcenter 0.6
  xzoom -1
 show fang neutral:
  xcenter -0.5 yalign 0.1
  easeout 1.5 xcenter 0.4
 show anon neutral:
  xcenter -0.5 yalign 0.1
  ease_cubic 2.0 xcenter 0.2
 pause 1.1
 Re "Well {w=0.25}this is the place!"
 F "Oh my god."
 #[anon switches to the thumbs up one]
 show anon happy
 with dissolve
 A "Hey, {w=0.25}what it lacks in youthful good looks, {w=0.25}it makes up for in character!"
 #[switch trish to considering]
 show trish considering
 with dissolve
 T "You really didn’t grow up in the projects, did ya?"
 #[Anon switches to grin]
 show anon grin
 with dissolve
 A "I’m from Rock Bottom."
 T " …Fair. "
 #[anon & trish expression back to neutral, all sprites exit stage right (maybe trish lags behind a little?)]
 show anon neutral
 show trish neutral
 with dissolve
 show reed neutral:
  xzoom 1
  ease 1 xcenter 1.5
 show fang neutral:
  easeout 1 xcenter 1.5
 show anon neutral:
  ease_cubic 1 xcenter 1.5
 show trish neutral:
  pause 0.5
  xzoom 1
  pause 0.5
  xzoom -1
  pause 0.25
  xzoom 1
  pause 0.25
  easein 1 xcenter 1.5
 pause 1.5
 #[screen fades to black]
 scene black with dissolve
 pause 0.5
 "We approach the derelict old cinder block. {w=0.40}It's a miracle a junk-heap like this is still standing. {w=0.40}I pull out my camera and flip it on."
 #[Fade in to front entrance pic, reed fang and trish are all already standing there, the camera canvas is active now, anon is permanently off screen while camera is in play.]
 scene outsideBuilding
 show fang neutral:
  xcenter 0.25 yalign 0.1
 show trish neutral:
  xcenter 0.50 yalign 0.1
 show reed neutral:
  xcenter 0.85  yalign 0.1 xzoom-1
 play sound "audio/effects/cameraShutterClick.ogg"
 show screen anon_camera
 with dissolve
 F "What do you need that thing for?"
 "I fail to contain my smug grin."
 A "Making memories."
 #[trish switches to unimpressed]
 show trish unimpressed
 T "And record us committing a misdemeanor?"
 A "Fine, {w=0.25}I’ll keep you out of the shot. {w=0.40}But also, {w=0.25}ghosts are supposed to show up on cameras! {w=0.40}Seen it on TV."
 T "Oh, {w=0.25}on the show that plays before Ancient Aliens?"
 A "{i}Maybe.{/i}"
 #[fang exits on the closest side]
 show fang neutral:
  xzoom -1
 with dissolve 
 show fang neutral:
  easeout 1 xcenter -0.5
 with None
 show reed neutral:
  ease 0.25 xcenter 0.70
 show trish unimpressed:
  easein 0.25 xcenter 0.35
 "Fang stifles a laugh and leans in, whispering into my ear." 
 F "Level with me dweeb. {w=0.40}Do you actually believe in ghosts?"
 A "I’m just saying that I personally cannot take a mere mortal’s word on such a fantastical thing." 
 F "You’re trying to get on TV, {w=0.25}arent you?"
 A "Perchance."
 #[switch trish to considering]
 show trish considering
 with dissolve
 T "You can’t just say perchance."
 #[Switch reed to explanatory]
 show reed explanatory
 with dissolve
 Re "All set?"
 $ patience = 0
 jump bitn_decision_2
 
label bitn_decision_2:
 show reed neutral
 show trish neutral
 if patience >= 5:
  jump bitn_decision_2_p
 menu:
  "Yes":
   jump bitn_decision_2_yes
  "No":
   jump bitn_decision_2_no
 
label bitn_decision_2_yes: 
 A "Lubed and loaded."
 F "Cocked and Locked."
 T "Unfortunately."
 #[switch reed to happy]
 show reed happy
 with dissolve
 Re "Right on."
 show reed neutral:
  ease 1.0 xcenter 0.20
 show trish neutral:
  xzoom -1
  easein 1.0 xcenter 0.70
 "Reed approaches the large iron door and gives the handle a shake,{nw}"
 play sound fang_attempt_door_sfx 
 extend " {w=0.25}but predictably it's locked tight."
 show trish unimpressed
 with dissolve
 T "I thought you said this place was abandoned?"
 A "It's still someone's property, {w=0.30}you think they're just gonna roll out the red carpet for us?"
 show trish considering
 with dissolve
 T "Well then how do you plan on getting in if there's no entrance?"
 "I sprout a mischievous grin."
 A "Then we'll just have to make our own. {w=0.60}Reed, {w=0.25}would you do the honors?"
 show reed happy
 with dissolve
 Re "Way ahead of ya."
 show reed happy:
  ease 1 xcenter -1.5
 "Reed inspects the nearby windows for a moment before picking one out {w=0.40}, putting a little pressure on the decaying frame, {nw}"
 play sound glassBreaking
 extend "{w=0.30}the whole thing goes crashing in."
 show trish surprised
 with dissolve
 "Fang runs over to give him a boost into the now glass-free hole, {w=0.30}and he disappears headfirst into the darkness within."
 show trish unimpressed
 with dissolve
 T "If tonight ends at the detention center, {w=0.30}I'm going to personally kick your ass."
 A "Don't be silly, {w=0.25}no one's going to find us out here."
 T "That's what you said about our trip to Angel's crest."
 A "Oh come on, {w=0.25}how was I supposed to know the park ranger would be out so late?"
 T "That's the point stupid, {w=0.25}and next time we might not be so lucky."
 A "Look, {w=0.25}no one comes into this part of town if they don't have to, {w=0.30}so try not to set the place on fire and we'll be just fine ok?"
 play sound lockSound
 "Before she retort, {w=0.25}there's a sound at the door as reed forces the rusty slabs wide open,{nw}"
 play sound doorOpening
 extend " {w=0.40}waving us in with a dorky bow."
 A "Ladies first."
 show black with dissolve
 hide outsideBuilding
 hide fang
 hide trish
 hide reed
 with dissolve
 "Trish gives me the evil eye as they passes by."
 "I quickly follow suit and we stop for a moment to take in our new surroundings."
 jump bitn_goofy_investigation

 #[cut to black except the camera]
 #show black with dissolve
 #hide outsideBuilding
# hide fang
# hide trish
 #hide reed
 #with dissolve
 #[play door opening sounds]
# play sound doorOpening
 #"Reed strains against the rusty iron slabs until they finally shriek in protest as they give against his incredible strength, he waves us in with a dorky bow and we take a moment to absorb our new surroundings."
 #[End branch, Begin section 2]
# jump bitn_goofy_investigation

label bitn_decision_2_no:
 A "…"
 Re "You need more time?"
 
 menu:
  "Yeah, one moment":
   jump bitn_decision_2_yeah
  "This reeks, let's leave":
   jump bitn_decision_2_tr
   
label bitn_decision_2_yeah:
 $ patience += 1
 "You take a moment to prepare yourself."
 Re "Ready now?"
 #[return to Yes/No]
 jump bitn_decision_2

label bitn_decision_2_tr:
 A "You know what, {w=0.25}Trish is right, {w=0.25}this is stupid. {w=0.40}Let’s go somewhere else."
 show trish smug with dissolve
 T "Finally, {w=0.25}some sense."
 F "Alright, {w=0.25}I know the perfect beach to go drink on!"
 show reed angry with dissolve
 Re "I hate sand."
 show trish unimpressed with dissolve
 T "It’s coarse and gets everywhere."
 scene black with dissolve
 "Reed and Trish skipped the beach, {w=0.40}but Fang and I didnt."
 "I got drunk and said something I shouldn't have, {w=0.40}and Fang broke up with me."
 "After a very long story, {w=0.40}involving me joining the Navy and Fang becoming addicted to Carfetanyl. {w=0.40}We made up, {w=0.25}fixed our problems, {w=0.20}and lived happily ever after as successful musicians."
 "The End?"
 "Ending 2 of 4: “The Infinite Cope.”"
 return

#[If it’s not too much trouble, If you loop No/yeah more than 5 times than fork to this dialogue instead of going back to Yes/No]
label bitn_decision_2_p:
 F "Are you just going to stand there and stare at the wall all night? {w=0.40}Come on!"
 "Fang grabs my wrist and drags me towards the entrance"
 show reed neutral:
  linear 0.5 xcenter 0.20
 show trish neutral:
  linear 0.5 xcenter 0.70 xzoom -1
 "Reed approaches the large iron door and gives the handle a shake,{nw}"
 play sound fang_attempt_door_sfx 
 extend " {w=0.25}but predictably it's locked tight."
 show trish unimpressed
 with dissolve
 T "I thought you said this place was abandoned?"
 A "It's still someone's property, {w=0.30}you think they're just gonna roll out the red carpet for us?"
 show trish considering
 with dissolve
 T "Well then how do you plan on getting in if there's no entrance?"
 "I sprout a mischievous grin."
 A "Then we'll just have to make our own. {w=0.60}Reed, {w=0.25}would you do the honors?"
 show reed happy
 with dissolve
 Re "Way ahead of ya."
 show reed happy:
  ease 1 xcenter -1.5
 "Reed inspects the nearby windows for a moments before picking one out {w=0.40}, putting a little pressure on the decaying frame, {nw}"
 play sound glassBreaking
 extend "{w=0.30}the whole thing goes crashing in."
 show trish surprised
 with dissolve
 "Fang runs over to give him a boost into the now glass-free hole, {w=0.30}and he disappears headfirst into the darkness within"
 show trish unimpressed
 with dissolve
 T "If tonight ends at the detention center, {w=0.30}I'm going to personally kick your ass."
 A "Don't be silly, {w=0.25}no one's going to find us out here."
 T "That's what you said about our trip to Angel's crest."
 A "Oh come on, {w=0.25}how was I supposed to know the park ranger would be out so late?"
 T "That's the point stupid, and next time we might not be so lucky."
 A "Look, {w=0.25}no one comes into this part of town if they don't have to, {w=0.30}so try not to set the place on fire and we'll be just fine ok?"
 play sound lockSound
 "Before she retort, {w=0.25}there's a sound at the door as reed forces the rusty slabs wide open,{nw}"
 play sound doorOpening
 extend " {w=0.40}waving us in with a dorky bow."
 A "Ladies first."
 show black with dissolve
 hide outsideBuilding
 hide fang
 hide trish
 hide reed
 with dissolve
 "Trish gives me the evil eye as they passes by."
 "I quickly follow suit and we stop for a moment to take in our new surroundings."
 jump bitn_goofy_investigation
