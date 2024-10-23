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
    "I no longer had any chance of executing my plan, now I only hoped to make it out of here safe and sound."
    "In hindsight, I probably shouldn't have goaded her on like that."
    "But if I entertain her just a little longer, then I'm sure she'll relent."

    stop music

    "I round the final turn and spot Fang standing at the bottom,"
    show fang sad at sright
    with Dissolve(2)

    "shining the weak light of her phone against a large metal door."
    "Her expression is stoic but intense, perhaps her nerves finally caught up with her."
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
    "She flinches at my touch, and she nearly swings a left hook into my cheek before realizing it's me."

    F "Oh it’s just a dweeb. A little warning would be nice."

    A "It's a one-way trip to the bottom. Who else could it be?"

    show fang considering flip with dissolve

    F "Whatever."

    show fang neutral:
     easein_cubic 1 xcenter 0.85

    "Fang starts working on the lock."
    "My phone buzzes in my pocket, and I fish it out."
    "It's a text from Reed asking if we're still alive."
    "I shoot back an equally sarcastic remark and let them know they're clear to join us"

    play sound lockSound

    "Fang grasps the handle with a hint of hesitation."

    F "You ready?"

    A "Ready to poke around more abandoned junk? Knock yourself out."

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

    "I shine the flashlight into the sea of darkness as we step out into the underground lair before us."
    "The dust is thick and visible in the air."
    "Cobwebs crowded the walls and corners so densely you'd think they'd hired a city planner."
    "Old lockers, cabinets, and doors dot the wall,"
    "crates stacked wherever free space is available."

    A "Well, there you go, same crap we've been looking at all night." 
    A "Not even any good commentary from the peanut gallery. Can we go now?"

    show fang neutral at scenter with dissolve

    F "No way, don't think you're off the hook yet."

    show fang happy with dissolve

    F "Don't worry, I’ll protect you from the “ghost” ok?"

    A "Christ, for the last time I don't believe in-"

    "Something takes my shoulder, and I nearly jump out of my skin"

    show black 
    hide fang
    pause 0.2
    hide black
#make reed close to the screen
    show reed neutral:
        xcenter 0.4 yalign 0.1 zoom 2.0
    show trish smug at tright
     
    A "Dammit Reed, don't sneak up on me like that."
#move reed back to normal distance
    show reed explanatory:
        linear 1 zoom 1

    Re "Sorry bro, but I mean, it's a staircase."
    Re "Who else would it be?"

    show reed neutral with dissolve

    "I groan as Fang erupts in laughter at my expense."
    A "Had your fill yet, Fang?"

    F "You wish. We're just getting started"

    scene black with Dissolve(2)
  
    pause 1
    scene basement  
    show black 
    show screen anon_camera 
    hide black with Dissolve(1)

    "As we plunge deeper into the storeroom, something about the place doesn't sit right with me."
    "I know it was locked but it’s far too orderly, not a single paint tag in sight."
    "The furnishings stuck out as being new, like they were a recent addition…"

    "Wait"
    "This place was locked."
    play music worried fadein 2.0

    A "Guys, I'm getting the feeling we shouldn't be down here."
    A "Let's just cut our losses and split."

    show fang neutral flip at sright
    with Dissolve(1)

    F "Not a chance. You just don't want to get busted for whatever scheme you're planning."
    "It's too late to weasel out now, so be a good dweeb and keep that camera rolling, m’kay?"

    show fang happy with dissolve

    show fang:
      easein_cubic 1  xcenter 0.5 

    "We reach the other end of the room." 
    "There's a large table draped with a tarp covering something huge"    

    F "This is it, the moment of truth. You'd better not disappoint me."

    show fang:
        easein_cubic 1 xcenter 0.85

    play sound tarpPull

    "Before I can interject, she grabs the tarp and tears it off to reveal what's beneath." 

    "It’s an enormous machine of some kind."

    show fang surprised with dissolve

    F "What the hell is this?"

    A "I don't know. I keep telling you this isn't some fucking bit Fang."
    A "I've never been to this place before in my life."

    Re "Uh guys, I think you should see this."

    show fang:
        linear 1.5 xcenter -0.5

    show trish neutral:
        xcenter 1.5 yalign 0.1

    show reed neutral:
        xcenter 1.5 yalign 0.1  

    show trish:
        linear 1.5 xcenter 0.55

    show reed:
        linear 1.5 xcenter 0.7     

    "Reed calls over from a pile of crates by the wall."
    "He's ripped open the top of one," 
    "the inside sits stacked wall to wall with cellophane bricks."

#reed dips down slightly then back up
    show reed:
        easein 0.5 ycenter 0.8
        pause 1.0
        easein 1.0 ycenter 0.655

    "He takes one out and opens it up to reveal a compressed cake of something white."

    show reed considering with dissolve

    "With a concerned look he gives it a lick and purses his lips."

    show reed shocked with dissolve

    Re "This is coke"

    show trish surprised with dissolve

    "My heart sinks like a stone, Trish covers the lower half of her face and furrows her brow."

    T "Oh shit..."

    show fang shocked:
        easein_cubic 1 xcenter 0.3

    F "Wait, for real?"

    A "Yes for real, we need to get the fuck out of here now."

    stop music
    play sound lockSound

    pause 1

    show fang:
        linear 0.5 xcenter -0.5

    show reed:
        linear 0.5 xcenter 1.5

    show trish:
        linear 0.5 xcenter 1.5

    "Reed drops the cover on the crate, and instinctively we all scatter to the nearest hiding places we can find."    

    show black with Dissolve(1)

    hide trish
    hide reed
    hide fang

    "Reed stuffs himself into a closet while Trish jumps under the table." 
    "Fang and I cower behind some crates. She gives me a worried look."

    F "Anon I-"

    A "Shhh not now."

    play sound doorCreaking
    pause 2.0
    play sound lightSwitch
    play music footsteps 

    pause 2

    "Moments later, I hear a door open,"
    "and suddenly a meager string of lights along the ceiling spring to life." 

    goon "-told you I heard something. The next shipment isn't due till tomorrow. Keep ya pants on, it'll only take a minute."

    goon "It's probably just some rats like always. Ya so paranoid Paulie. We haven't had to worry about snoops since the Boss-"

    "The voices go silent."
    "I can practically hear my heartbeat thump through my chest."

    goon "Hey Vito, you remember to cover the packer back up before we left?"

    goon "I think so?"

    goon "Well then, I think we might just have a “rat” problem after all."

    goon "Or your just a fuckin dolt is what it is."

    stop music
    play sound tarpPull

    goon "Come on, it's late and I want to get out of here. Any longer and the boys are gonna start without-"

    play sound sneeze

    pause 2

    show goon1:
     xcenter 0.4 yalign 0.1 

    show goon2:
     xcenter 0.25 yalign 0.1 

    show goon3:
     xcenter 0.1 yalign 0.1  

#set trish at lower yaxis
    show trish surprised flip:
        xcenter 0.85 ycenter 0.75  

    hide black with dissolve

    "Silence again fills the air." 
    "I peek out and see Trish covering her mouth with a face as grim as death." 
    "There are three figures standing by the table next to her just as shocked as the rest of us."
    play music escape fadein 1.0
    show goon1:
      easein 1 xcenter 0.85

    show trish: 
      easein 0.5 xcenter 0.90
    "After a moment, one ducks down and spots her." 
 
    show goon1:
      easein_cubic 1 xcenter 0.5

    show trish:
      easein_cubic 1 xcenter 0.6
    "She yelps as he pulls her out by the leg,"
#raise goon back to normal height, flip trish upside down and make her feet even with his head
    show trish: 
        linear 0.5 rotate 180 
    pause 0.5
#rapidly flip trish left and right until reeds tackle
    show trish angry:
        linear 0.25 xzoom -1 
        linear 0.25 xzoom 1 
        repeat
    "holding her like a plucked chicken while she swats at them out of reach."

    "The man wears a horrible, toothy grin."
    goon "Well, what do we have here? I think someone owes me an apology."

    goon "Yeah sure. I'll go call the 'exterminator', and we can get this little infestation cleaned up."

#reed(angry) moves in front stage left at high speed, upon touching the goon holding trish all three fall to ground(reed fell kinda like this before anon/fang study date)
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
    show reed neutral:
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
    "Then grabbing Fang's wrist, I book it for the entrance we came in from."

    hide screen anon_camera
    scene black with dissolve 

    goon "“Hey don't let those kids get away!"
    "Says the goon grappling with Reed," 
    "as the one he attacked picks himself back up and pulls out a knife."

    scene abandoned_atrium

    pause 2

    show anon ohshit flip:
        xcenter 1.5 yalign 0.1

    show fang sad flip:
        xcenter 1.5 yalign 0.0

    show anon:
        easein_cubic 1 xcenter 0.2  

    show fang:
        easein_cubic 1 xcenter 0.6

    pause 1    

    show fang very sad with dissolve  

    pause 1.5

    F "We have to go back...we can't just leave them here."

    show anon pissed:
        easein_cubic 1 xcenter 0.55

    pause 1

    show anon pissed flip:
        easein_cubic 1 xcenter -0.5

    show fang:
        easein_cubic 1 xcenter -0.5

    A "There's no time! If we stop now then we're all done for!"
    
    scene black with dissolve

    scene outsideVan with dissolve
 
#need to get the volume to lower without restarting it 
    #play music escape volume 0.25
    $ renpy.music.set_volume(0.25, 0.5, 'music')

    pause 2

    show anon ohshit:
        xcenter -0.5 yalign 0.1

    show fang sad:
        xcenter -0.5 yalign 0.0

    show anon:
        easein_cubic 2 xcenter 0.9  

    show fang:
        easein_cubic 2 xcenter 0.7

    "Before long we make it out of the building and back over to Reed's van."
    "Hands shaking, I fumble with the keys to unlock the door,"
    play sound carDoor

    show anon:
        easein_cubic 1 xcenter 1.5

    show fang:
        easein_cubic 1 xcenter 1.5

    "after which I throw myself inside and start the car up as fast as I can."
    "Fang hops in on the opposite side."

    F "Do you even know how to drive?"

    A "I've played a lot of GTA, that'll have to be good enough."

    stop music fadeout 1.0

    scene black with dissolve

    play ambient insideCarNoise fadein 1.0

    "The engine roars to life."
    "I thank the gods that Reed doesn't drive a stick as I floor the gas to pull us out of there, leaving a fat rubber track in our wake."

    show car complete with dissolve
#do car bump

    "I start to fly down the winding roads and back alleys that make up this seedy part of town,"
    "doing my best to keep from smashing us into a wall. Fang looks over, her nerves completely shot."

    F "Where are we going?"
    show car complete at carBump

    A "The police station? Your Dad's house?"
    A "I don't know just somewhere we can get away from the three stooges and let someone important know what happened."
    
    "She curls up and puts her hands on her head." 

    F "Oh god, dad's going to kill me when he finds out what we did tonight."

    A "Not as bad as those guys will, now let me drive."

    F "Christ, why did I ever agree to come out here?"
    show car complete at carBump
    F "We should have just gone drinking at the beach like we always do."

    A "Hey, I just wanted to have a fun night out with my friends."
    A "How the hell was I supposed to know we'd stumble into some drug den!?"

    F "Well, your ‘fun night’ might have just gotten our friends killed! Fuck!"

    A "And if you don't want to join them, then start charting me some directions so we can get out of here!"
   
    F "Is that all you have to say for yourself!?"

    A "Well, maybe if SOMEONE would have fucking left the hornets' nest alone when I asked them to split, they'd still be here!"
  
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

    pause 9

#scene ends here thismis an extra bit for the jam version only

    FC "Unfortunately that's all the time we have for today folks!"
    FC "What?"
    FC "You want to know what happens next?"
    FC "Then you'll have to check out the full release coming out this halloween!"
    FC "Hopefully."
    "Happy holidays Snoot Club!"
    
    return