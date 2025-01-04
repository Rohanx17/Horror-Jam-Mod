label bitn_Chapter3:
   
    stop music fadeout(3)
    scene black with Dissolve(2)
    camera:
        ycenter 0.5 xcenter 0.5
        zoom 1
  
    pause 1
    scene stairs
    play music footsteps 
    show black 
    hide black with Dissolve(1)
   

    "I descend with one hand glued to the guardrail."
    "The light does little to guide my way beyond the steps in front of me."
    "I had long given up hope of executing my plan." 
    "I'll sure the'll be plenty of opportunities to try again later. {w=0.40}But for now, {w=0.20}I just want to get out of here."
    "In hindsight, {w=0.25}I probably shouldn't have goaded her on like that."
    "But if I entertain her just a little longer, {w=0.25}then I'm sure she'll relent."

    stop music

    "I round the final turn and spot Fang standing at the bottom,"
    show fang sad at sright:
        alpha 0
        ease 2.0 alpha 1.0

    "I round the final turn and spot Fang standing at the bottom,{fast} shining the weak light of her phone against a large metal door."
    "Her expression is stoic but intense, {w=0.25}perhaps her nerves finally caught up with her."
#zoom in effect
    camera:
        xcenter 0.5 ycenter 0.5 
        linear 0.5 zoom 1.75 
    "I reach out and put my hand on her shoulder."

#fang moves slightly up and down
    show fang surprised: 
        easein 0.25 ycenter .5
        easein 0.25 ycenter .655
    pause 0.5 
    show fang angry flip with dissolve
#zoom back out to normal
    camera:
        linear 0.5 xcenter 0.5 zoom 1
    "She flinches at my touch, {w=0.25}and she nearly swings a left hook into my cheek before realizing it's me."

    F "Oh it’s just a dweeb. {w=0.40}A little warning would be nice."

    A "It's a one-way trip to the bottom. {w=0.40}Who else would it be?"

    show fang considering flip with dissolve

    F "Whatever."

    show fang neutral:
     easein_cubic 1 xcenter 0.85

    "Fang starts working on the lock."
    play sound phoneBuzz
    "My phone buzzes in my bag, {w=0.25}and I fish it out."
    "It's a text from Reed asking if we're still alive."
    "I shoot back an equally sarcastic remark, {w=0.25} and let them know they're clear to join us"

    play sound lockSound

    "Fang grasps the handle with a hint of hesitation."

    F "You ready?"

    A "Ready to poke around more abandoned junk? {w=0.40}Knock yourself out."

    show fang happy with dissolve

    F "Ready to call your bluff more like it."

    "I shrug."

    A "Whatever blows your dress up."

    show fang considering:
        linear 2 xcenter 1.5

    scene black with Dissolve(2)
  
    pause 1
    scene basement  
    show black 
    show screen anon_camera
    hide black with Dissolve(1)

    "I shine the flashlight into the sea of darkness {w=0.25}as we step out into the underground lair before us."
    "The dust is thick and visible in the air."
    "Cobwebs crowded the walls and corners so densely,{w=0.25} you'd think they'd hired a city planner."
    "Old lockers, {w=0.20}cabinets, {w=0.20}and doors dot the wall."
    "Crates stacked wherever free space is available."

    A "Well, there you go, {w=0.25}same crap we've been looking at all night." 
    A "Not even any good commentary from the peanut gallery down here. {w=0.40}Can we please go now?"

    show fang neutral at scenter with dissolve

    F "Don't think you're off the hook yet."

    show fang happy with dissolve

    F "Don't worry, {w=0.25}I’ll protect you from the “ghost” ok?"

    A "Christ, {w=0.20}for the last time I don't believe in-"

    "Something takes my shoulder, and I nearly jump out of my skin."

    show black 
    hide fang
    pause 0.2
    hide black
#make reed close to the screen
    show reed neutral:
        xcenter 0.4 yalign 0.1 zoom 2.0
    show trish smug at tright
    with vpunch 
    A "Dammit Reed, {w=0.25}don't sneak up on me like that."
#move reed back to normal distance
    show reed explanatory:
        linear 1 zoom 1

    Re "Sorry bro, {w=0.40}but I mean, {w=0.20}it's a staircase."
    Re "Who else would it be?"

    show reed neutral with dissolve

    "I groan as Fang erupts in laughter at my expense."
    A "Had your fill yet Fang?"

    F "You wish. {w=0.40}We're just getting started."

    scene black with Dissolve(2)
  
    pause 1
    scene basement  
    show black 
    show screen anon_camera 
    hide black with Dissolve(1)

    "As we plunge deeper into the storeroom, {w=0.25}something about the place doesn't sit right with me."
    "I know it was locked, {w=0.25}but it’s far too orderly. {w=0.40}Not a single paint tag in sight."
    "The furnishings stuck out as rather modern by comparison, {w=0.25}like they were a recent addition…"

    "Wait."
    "This place was locked."
    play music worried fadein 2.0

    A "Guys, {w=0.25}I'm getting the feeling we shouldn't be down here."
    A "Let's just cut our losses and split."

    show fang neutral flip at sright
    with Dissolve(1)

    F "Not a chance. {w=0.25}You just don't want to get busted for whatever scheme you're planning."
    F "It's too late to weasel out now, {w=0.25}so be a good dweeb and keep that camera rolling, m’kay?"

    show fang happy with dissolve

    show fang:
      easein_cubic 1  xcenter 0.5 

    "We reach the other end of the room. {w=0.40}There's a large table draped with a tarp covering something huge."    

    F "This is it, {w=0.20}the moment of truth. {w=0.40}You'd better not disappoint me."

    show fang:
        easein_cubic 1 xcenter 0.85

    F "Before I can interject,{w=0.25}{nw}"
    play sound tarpPull
    extend " she grabs the tarp and tears it off to reveal what's beneath." 

    "It’s an enormous machine of some kind."

    show fang surprised with dissolve

    F "What the hell is this?"

    A "I don't know. {w=0.40}I keep telling you this isn't some fucking bit Fang. {w=0.40}I've never been to this place before in my life."

    Re "Uh guys, {w=0.25}I think you should see this."

    show fang:
        easein_cubic 2.0 xcenter -0.2

    show trish neutral:
        xcenter 1.5 yalign 0.1
        0.5
        easein_cubic 1.0 xcenter 0.55
        
    show reed neutral:
        xcenter 1.5 yalign 0.1  
        0.5
        easein_cubic 1.0 xcenter 0.7     

    "Reed calls over from a pile of crates by the wall."
    "He's ripped open the top of one,{w} the inside sits stacked wall to wall with cellophane bricks." 

#reed dips down slightly then back up
    show reed:
        easein 0.5 ycenter 0.8
        pause 1.0
        easein 1.0 ycenter 0.655

    "He takes one out, {w=0.25}and opens it up to reveal a compressed cake of something white."

    show reed considering with dissolve

    "With a concerned look he gives it a lick, {w=0.25}and purses his lips as his eyes light up."

    show reed shocked with dissolve

    pause 0.5

    Re "This is coke."

    show trish surprised with dissolve

    "My heart sinks like a stone, {w=0.25}Trish covers the lower half of her face and furrows her brow."

    T "Oh shit..."

    show fang shocked:
        easein_cubic 1 xcenter 0.3

    F "Wait, {w=0.20}for real?"

    A "Yes for real, {w=0.25}we need to get the fuck out of here now."

    stop music
    play sound lockSound

    pause 1

    "Reed drops the cover on the crate, {nw}"
     
    show fang:
        easein 1.0 xcenter -0.5

    show reed:
        ease 1.0 xcenter 1.5

    show trish:
        easeout 1.0 xcenter 1.5
     
    extend "and instinctively we all scatter to the nearest hiding places we can find."        

    show black with Dissolve(1)

    hide trish
    hide reed
    hide fang

    "Reed stuffs himself into a closet while Trish dives under the table." 
    "Fang and I cower behind some crates. {w=0.40}She gives me a worried look."

    F "Anon I-"

    A "Shhh not now."

    play sound doorCreaking
    pause 2.0
    play sound lightSwitch
    play music footsteps 

    pause 2

    "Moments later, {w=0.20}I hear a door open,"
    "and suddenly a meager string of lights along the ceiling spring to life." 

    goon "-ld you I heard something. {w=0.40}The next shipment isn't due till tomorrow. {w=0.40}Keep ya pants on, {w=0.20}it'll only take a minute."

    goon "It's probably just some rats like always. {w=0.25}You're so paranoid. {w=0.40}We haven't had to worry about snoops since-"

    "The voices go silent."
    "I can practically hear my heartbeat thump through my chest."

    goon "Hey, {w=0.25}one of you remember to cover the packer up before we left?"

    goon "I think so?"

    goon "Well then, {w=0.25}I think we might just have a “rat” problem after all."

    goon "Or you're just a fuckin dolt is what it is."

    stop music
    play sound tarpPull

    pause 0.5

    goon "Come on, {w=0.20}it's late and I want to get out of here. {w=0.30}{nw}"
    play sound sneeze
    extend "Any longer and the boys are gonna start without-."

    pause 1.5

    show goon1:
     xcenter 0.4 yalign 0.1 

    show goon2:
     xcenter 0.25 yalign 0.1 

    show goon3:
     xcenter 0.1 yalign 0.1  

#set trish at lower yaxis
    show trish surprised flip:
        xcenter 0.75 ycenter 0.95  

    hide black with dissolve

    "Silence again fills the air." 
    "I peek out and see Trish covering her mouth with a face as grim as death." 
    "There are three figures standing by the table next to her, {w=0.25} just as shocked as the rest of us."
    play music escape fadein 1.0
    show goon1:
      easein 1 ycenter 1.2
    "After a moment, {w=0.25}one ducks down and spots her."
    show goon1:
      easein 1 xcenter 0.85

    show trish:
      easein 0.5 xcenter 0.95 xzoom -1

    show goon1:
      easein 1 xcenter 0.90
    
    "She yelps as he pulls her out by the leg,"
 
    show goon1:
      easein_cubic 1 xcenter 0.45 

    show trish:
      easein_cubic 1 xcenter 0.55 

    pause 0.5

    show goon1:
      easein_cubic 1 xcenter 0.45 yalign 0.1

    show trish: 
        xcenter 0.55 ycenter 0.65 
        linear 0.5 rotate 180 

    pause 0.5

   #rapidly flip trish left and right until reeds tackle
    show trish angry:
        xcenter 0.55 ycenter 0.65 rotate -180 yzoom 1.0
        linear 0.25 xzoom 1 
        linear 0.25 xzoom -1 
        repeat

   # show trish:
    #  easein_cubic 1 xcenter 0.55 ycenter 0.65 yzoom 1.0
      #linear 0.5 rotate 180

    #pause 0.5

    #show trish angry:
    #  xcenter 0.55 ycenter 0.65 rotate -180 yzoom 1.0
    #  linear 0.25 xzoom -1 
    #  linear 0.25 xzoom 1 
    #  repeat

   # show trish angry:        
   # pause 0.1
   # show trish angry flip:
  #  pause 0.1
  #    repeat

    #show trish angry:        
    #  linear 0.25 xzoom 1 
    #  pause 0.1
    #  linear 0.25 xzoom -1 
    #  repeat
    
    "dangling her in the air like a plucked chicken while she swats at them out of reach."

    "The man wears a horrible, toothy grin."
    goon "Well what do we have here? {w=0.40}I think someone owes me an apology."

    goon "Yeah whatever. {w=0.40}I'll go call the {i}exterminator{/i}, {w=0.25}and we can get this little infestation cleaned up."

#reed(angry) moves in front stage left at high speed, upon touching the goon holding trish all three fall to ground(reed fell kinda like this before anon/fang study date)
    show reed angry:
        xzoom -1

    show reed angry:
        xcenter 1.5
        linear 0.5  xcenter 0.5
    pause 0.5 
    show reed:
        linear 0.1 xcenter 0.45
        linear 0.25 xcenter 0.4 ycenter 1.99
    show goon1:
        linear 0.1  xcenter 0.45
        linear 0.25 xcenter 0.40   ycenter 1.99
    show goon2:
        linear 0.1 xcenter 0.20
        linear 0.25 xcenter 0.15 ycenter 1.99
    show goon3:
        linear 0.1 xcenter 0.05
        linear 0.25 xcenter 0.0 ycenter 1.99
    show trish:
        linear 0.1 xcenter 0.55
        linear 0.25 xcenter 0.50 ycenter 1.99

    Re "TRISH!"
#reed pops back up at center stage, key graphic appears at center and flies at screen/grows until deleted
    hide reed
    show reed angry:
        ycenter 1.99 xcenter 0.45 
        linear 0.5 ycenter 0.655
    pause 0.5

    Re "ANON RUN!"
    
    show keys:
        ycenter 0.5 xcenter 0.5
        linear 0.5 zoom 4
    pause 0.5
    hide keys

    play sound keyGet

    "Reed throws me his keys and I pop up to catch them"
    "Then grabbing Fang's wrist, {w=0.30}I book it for the entrance we came in from."

    hide screen anon_camera
    scene black with dissolve 

    goon "“Hey! {w=0.3}Don't let those kids get away!"
    "Says the one grappling with Reed, {w=0.30}as another picks himself back up and pulls out a knife."

    scene abandoned_atrium with Dissolve(2)

    pause 1.5

    show anon ohshit flip:
        xcenter 1.5 yalign 0.1

    show fang sad flip:
        xcenter 1.5 yalign 0.0

    show anon:
        easein_cubic 1 xcenter 0.2  

    show fang:
        easein_cubic 1 xcenter 0.6

    pause 1.5    

    show fang very sad with dissolve  

    pause 1

    F "We have to go back.{w=0.3}.{w=0.3}.{w=0.3}we can't just leave them here."

    show anon pissed:
        easein_cubic 1 xcenter 0.55

    pause 1

    show anon pissed flip:
        easein_cubic 1 xcenter -0.5

    show fang:
        easein_cubic 1 xcenter -0.5

    A "There's no time! {w=0.30}If we stop now then we're all done for!"
    
    scene black with dissolve

    scene outsideVan with dissolve
 
#need to get the volume to lower without restarting it 
    #play music escape volume 0.25
    $ renpy.music.set_volume(0.25, 0.5, 'music')

    pause 1.5

    show anon ohshit:
        xcenter -0.5 yalign 0.1

    show fang sad:
        xcenter -0.5 yalign 0.0

    show anon:
        easein_cubic 2 xcenter 0.9  

    show fang:
        easein_cubic 2 xcenter 0.7

    "Before long we make it out of the building and back over to Reed's van."
    "Hands shaking, {w=0.25}I fumble with the keys to unlock the door."
    play sound carDoor

    show anon:
        easein_cubic 1 xcenter 1.5

    show fang:
        easein_cubic 1 xcenter 1.5

    "After which I throw myself inside and start it up as fast as I can."
    "Fang hops in the shotgun seat."

    F "Do you even know how to drive?"

    A "I've played a lot of GTA, {w=0.25}that'll have to be good enough."

    stop music fadeout 1.0

    scene black with dissolve

    play ambient insideCarNoise fadein 1.0

    "The engine roars to life."
    "I thank the gods Reed doesn't drive a stick as I floor the gas to pull us out of there, {w=0.25}leaving a fat rubber track in our wake."

    show car complete with dissolve
#do car bump

    "I start to fly down the winding roads and back alleys that make up this seedy part of town, {w=0.25}doing my best to keep us from smashing into a wall. "
    "Fang looks over, {w=0.25}her nerves completely shot."

    F "Where are we going?"
    show car complete at carBump

    A "The police station? {w=0.25}Your Dad's house?"
    A "I don't know just somewhere we can get away from the three stooges and let someone important know what happened."
    
    "She curls up and puts her hands on her head." 

    F "Oh god, {w=0.30}dad's going to kill me when he finds out what we did tonight."

    A "Not as bad as those guys will, {w=0.30}now let me drive."

    F "Christ, {w=0.30}why did I ever agree to come out here?"
    show car complete at carBump
    F "We should have just gone drinking at the beach like we always do."

    A "It's too late to worry about that now, {w=0.25}why don't you chart me some directions so we can get out of here?"

    F "Can't, {w=0.25}spent all my battery life on flashlight mode."

    A "Well then use mine, {w=0.25}should be in my backpack somewhere."

    "Fang picks it off the seat between us and starts digging through it."
    "Suddenly, {w=0.25}she stops, {w=0.25}a look of confusion spreads across her face."

    F "What the fuck is all this?"

    #show anonBackpack with dissolve

    "I look over and to my dismay she's pulled out the costume, {w=0.25}the paint, {w=0.25}all the evidence of tonights plan exposed."
    
    "In the chaos of our escape it had completely slipped my mind."
    "I grab my head with my free hand."

    A "Ah shit"

    # show carArgue with dissolve

    F "Oh my god, {w=0.25}I was right! {w=0.4}You led us there for some fucking bit didn't you?"

    "I turn away in embarrassment "

    A "Uh, yeah, {w=0.25}I brought you out tonight to give you a scare. {w=0.25}Thought if I caught you pissing yourself on camera there's no way you could ever top it."
   
    F "I can't fucking believe this..."

    A "Look I'm sorry, {w=0.25}It's not like I meant for any of this to happen. {w=0.25}How the hell was I supposed to know we'd run into some drug den?"

    F "Is that all you have to say for yourself!? {w=0.40}Our friends might be dead because of you!"

    A "Hey, {w=0.20}I wanted to split as soon as things looked shady, {w=0.30}maybe if SOMEONE would have fucking left the hornets' nest alone, {w=0.20}they'd still be here!"
  
    F "ARE YOU SAYING THIS IS MY FAULT!?"
    show car complete at carBump

    A "WELL IT SURE AS HELL ISN'T MINE!"

    F "FUCK YOU!"

    A "FUCK YOU!"

    F "ANON!"

    A "WHAT!?"

    F "THE ROAD!"
    show car complete at carBump

    A "OH SHI-"

    play sound carCrash

    scene black with dissolve

    stop ambient fadeout(2)

    pause 4

    F "Anon?"

    pause 2

    F "Anon wake up!"

    pause 2

    jump bitn_Chapter4
    
