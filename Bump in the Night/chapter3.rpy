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
    show fang sad at sright:
    alpha 0.0
    ease 2.0 alpha 1.0

    "I round the final turn and spot Fang standing at the bottom,{fast} shining the weak light of her phone against a large metal door."
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
    "There's a large table draped with a tarp covering something huge."    

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
    "He's ripped open the top of one,{w} the inside sits stacked wall to wall with cellophane bricks." 

#reed dips down slightly then back up
    show reed:
        easein 0.5 ycenter 0.8
        pause 1.0
        easein 1.0 ycenter 0.655

    "He takes one out and opens it up to reveal a compressed cake of something white."

    show reed considering with dissolve

    "With a concerned look he gives it a lick and purses his lips."

    show reed shocked with dissolve

    Re "This is coke!"

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
        xcenter 0.6 ycenter 0.75 
        linear 0.5 rotate 180 
    pause 0.5
#rapidly flip trish left and right until reeds tackle
    show trish angry:
        xcenter 0.6 ycenter 0.75 rotate -180 yzoom 1.0
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

    jump bitn_interrogation
    
    #scene ends here thismis an extra bit for the jam version only

    FC "Unfortunately that's all the time we have for today folks!"
    FC "What?"
    FC "You want to know what happens next?"
    FC "Then you'll have to check out the full release coming out this halloween!"
    FC "Hopefully."
    "Happy holidays Snoot Club!"
    
    return

label bitn_interrogation:
    play ambient lamp_buzz fadein 3.0 volume 1.0
    scene torture_room
    show tunnel_vision onlayer screens:
        blend "multiply" alpha 1.0 blur 50.0
        5.0
        linear 5.0 alpha 0.0 
        
        
    show short goon neutral:
        zoom 0.5 xcenter 0.65 ycenter 0.6 xzoom -1.0 
        matrixcolor TintMatrix ('#364259')* ContrastMatrix(0.0)  
        
    show tall goon neutral:
        zoom 0.5 xcenter 0.325 ycenter 0.5
        matrixcolor TintMatrix ('#364259')* ContrastMatrix(0.0)  
    
    camera:
        blur 10.0
        linear 10.0 blur 0.0
    
    with Dissolve(3)
    
    pause 2.0
    play ambient1 playing_cards fadein 10.0
    "Slowly I regain consciousness, {w=0.10}my body sore and immobile as my eyes adjust."
    
    "I'm tied to a chair in a modest concrete room."
    
    "At the other end is a small table, {w=0.10}where two bored-looking goons sit playing cards under the dingy light of a flickering bulb."      
    
    A "Fang?"
   
    F "A-Anon?"    
    
    F "Thank God you're ok."
    
    "I see Fang on my left and we exchange worried looks. {w}The others are here too, looks like Reed’s been roughed up pretty bad."
    
    A "Where are we?"
    
    T "We don't know."
    
    "The pair take notice of our conversation."
    
    show short goon neutral:
        matrixcolor TintMatrix ('#364259')* ContrastMatrix(0.0)  
        easeout_quint 2.0 matrixcolor TintMatrix ('#f7f7f7')* ContrastMatrix(1.0)  
        
    G1 "Hey, looks like our guests are finally awake. {w}Let's get this show started."
    
    show tall goon neutral:
        matrixcolor TintMatrix ('#364259')* ContrastMatrix(0.0)
        easein_quint 2.0 matrixcolor TintMatrix ('#f7f7f7')* ContrastMatrix(1.0)  
    
    G2 "Just when you're about to lose, how convenient."
    
    stop ambient1
    "He waves his hand dismissively and sighs."
    
    G1 "Keep the pot for all I care, just go get my tools." 
    
    G1 "We have a job to do."
    
    play sound card_gather
    
    "The taller one rolls his eyes before scooping the change off the table and into his coat pocket,{nw}" 
    
    show tall goon neutral:
        xcenter 0.325 
        easein_quint 3.0 xcenter 1.2
    
    "The taller one rolls his eyes before scooping the change off the table and into his coat pocket,{fast} then shuffles off through one of the doors." 
    
    hide tall goon
    
    show short goon neutral:
        zoom 0.5 xcenter 0.65 ycenter 0.6 matrixcolor TintMatrix ('#f7f7f7')* ContrastMatrix(1.0)  
        easeout_quint 1.5 xcenter 0.5 ycenter 0.655 zoom 1.0 
    
    "The short one gets up to face us,"
    
    show short goon grin:
        xzoom -1.0 xcenter 0.5 ycenter 0.655 zoom 1.0
    
    "The short one gets up to face us,{fast} his tired expression shifts into a beaming grin as he locks eyes with ours."
    
    G1 "Welcome to our humble little abode."
    
    G1 "My name is Paulie and that was my associate Bruce, {w=0.10}and we'll be your hosts for tonight's entertainment."
    
    $ G1_Name = 'Paulie'
    $ G2_Name = 'Bruce'
    
    F "Where the hell are we?"
    
    G1 "Sorry but we'll be asking the questions here. Starting with who you all are, and who sent you."
    
    Re "Nobody man, we don't know anything about this."
    
    show short goon neutral
    
    G1 "Well that's very unfortunate to hear..."
    
    "He picks up our video camera off the table."
    
    G1 "Because {i}someone{/i} thought it was a real good idea to break into our hidden depot and get every last detail on tape."
    
    G1 "Y'all were real desperate to make sure it got out too. Now the boss wants to know who out there is stupid enough to fuck with him."
    
    show short goon grin
    
    G1 "And we intend to find out by any means necessary."
    
    pause .5
    
    hide tunnel_vision onlayer screens
    camera:
      blur 0        
    
    
    show short goon neutral with dissolve
    
    A "We're telling the truth! {w=0.10}We're just some teens who wandered in here for fun, we don't work for anybody."
    
    show short goon grin
    
    G1 "Come on kid you can do better than that. {w}The place is locked and built like a bomb shelter, {w=0.10}no one just stumbles in there by accident."
    
    show tall goon neutral behind short:
        xzoom -1.0 ycenter 0.655 xcenter 1.2 zoom 0.5 
        easein_quint 2.0 xcenter 0.65
    
    show short goon grin:
        xcenter 0.5
        pause 1.0
        easeout_quint 1.0 xcenter 0.3 ycenter 0.655 
    
    pause 1.0
    play sound tableDrop
    
    "The taller goon comes back and drops a large leather wrapping on the table."
    
    "It looks kinda like that thing they hold surgical equipment in."

    G1 "Since none of you feel like doing this the easy way, we'll just have to do it our way."

    "He unrolls it and we all quietly gasp. {w}Knives, {w=0.10}scissors, {w=0.10}a ballpoint hammer, {w=0.10}and a collection of other tools are laid out in horrific fashion."     
    
    G1 "Alright Pink, how about we start with you?"
    
    show tall goon neutral:
        xcenter 0.65
        easein_quint 3.0 xcenter -0.2
    
    camera:
       zoom 1.0 ycenter 0.5
       2.0
       linear 0.5 zoom 1.5    

    
    show short goon grin:
        xzoom -1.0 xcenter 0.3 ycenter 0.655 zoom 1.0
        2.0
        easeout_quint 1.0 xcenter 0.7 zoom 0.7  
    
    pause 2.0
    
    play sound chair_pull
    
    show tall goon neutral:
        xcenter -0.5 ycenter 0.655 zoom 0.65 xzoom 1.0
        1.5
        easein_quint 1.0 xcenter 0.3
     
    show reed neutral:
        ycenter 0.655 xcenter -0.2 zoom 0.7
        1.0
        ease 1.0 xcenter 0.4
    
    "The taller one grabs Reed's chair and pulls him over to the table."
        
    play sound reed_lighter_sfx
    
    show reed neutral:
        xcenter 0.4 ycenter 0.655 zoom 0.7
    
    show tall goon neutral:
        xcenter 0.3 ycenter 0.655 zoom 0.65 xzoom 1.0
        
        
    show short goon grin:
        xzoom -1.0 xcenter 0.7 zoom 0.7 ycenter 0.655      
    
    "The short one pulls out a pack of cigs from his coat and lights one up, {nw}"
    
    show tall goon neutral:
        xzoom -1.0 xcenter 0.3 xoffset -100
        .5
        easein_quint 1.5 xcenter 0.2
        easein_quint 0.5 xcenter 0.3
        xzoom 1.0 xoffset 0
        
    show short goon grin:
        xcenter 0.7 zoom 0.7 xzoom 1.0
        easeout_quint 0.5 xcenter 0.8
        1.0
        easeout_quint 0.5 xcenter 0.7
        xzoom -1.0
    
    play sound [ "<silence 1.25>", reed_lighter_sfx ] 
    
    "The short one pulls out a pack of cigs from his coat and lights one up, {fast}then hands it out to his partner who does the same."
    
    G1 "So me and you are going to play a little game see? {w}I'm gonna ask you a question, {w=0.10}if you tell me something useful, maybe you and your friends will get to wake up tomorrow."
    
    "He picks up a knife, artfully spinning it through his fingers."
    
    G1 "Try to bullshit me..."
    
    play sound tableKnife
    
    "He catches the knife and slams the blade into the table."
    
    G1 "Let's just say you ain't gonna like the prize we have in store."
    
    show reed sad with dissolve
    stop ambient fadeout 0.5
    play music torture_p1 fadein 0.5
    
    "We all gulp, a look of dread creeps across Reed's face."
    
    G1 "Now let's begin."
    
    "He looks over at us."
    
    G1 "And of course, {w=0.10}if you don't like what you see, the audience is always free to answer for him."
    
    show short goon neutral with dissolve
    
    "His smile evaporates as he turns back to Reed and stares him down."
    
    G1 "Now question number one: {w=0.25} Who exactly do you work for?"
    
    
    menu:
        
        "Plead ignorance":
         Re "Please we don't know anything, let us{nw} g-AHHHH!" 
         
         show reed shocked:
            ycenter 0.655
            ease 0.25 ycenter 0.68
            ease 0.5  ycenter 0.63 
            ease 0.5  ycenter 0.68 
            ease 0.25 ycenter 0.63   
            ease 0.25 ycenter 0.655
        
         play sound "audio/effects/sizzle.ogg"
         queue sound ouch         
         
         Re "Please we don't know anything, let us{fast} g-AHHHH!" 
         
         show reed sad
         
         pass
         
        "Prove innocence":
         "Reed looks ready to puke as his nerves run overtime, {w=0.10}thinking of what he could possibly say to placate the villain."
         
         Re "We're telling you the truth I swear! We don't work for anybody!" 
         
         show reed neutral
         
         "His face lights up."
         
         Re "Check the cam footage you'll see!"
         
         show short goon grin
         
         G1 "Oh don't you worry we've given your little home movie a good look over."
         
         G1 "Y'all seem to be searching real hard for something {w=0.10}until suddenly, you're showing off our product like you're the home shopping network." 
         
         G1 "Care to explain?"
         
         show reed unimpressed
         
         Re "...uh, well, I think she was looking for a ghost or someth-{nw}"
         
         
         show reed shocked:
            ycenter 0.655
            ease 0.25 ycenter 0.68
            ease 0.5  ycenter 0.63 
            ease 0.5  ycenter 0.68 
            ease 0.25 ycenter 0.63   
            ease 0.25 ycenter 0.655
         
         play sound "audio/effects/sizzle.ogg"
         queue sound ouch
         
         Re "...uh, well, I think she was looking for a ghost or someth-{fast}AHHHH!"
         
         show reed sad
         
         show short goon neutral
         
         pass 
            
        "Antagonize":
            
         show reed angry with dissolve

         Re "Are you deaf? We don't work for anyone! How many times do-{nw}" 
         
         
         show reed shocked:
            ycenter 0.655
            ease 0.25 ycenter 0.68
            ease 0.5  ycenter 0.63 
            ease 0.5  ycenter 0.68 
            ease 0.25 ycenter 0.63   
            ease 0.25 ycenter 0.655
         
         
         play sound "audio/effects/sizzle.ogg"
         queue sound ouch
        
        
         Re "Are you deaf? We don't work for anyone! How many times do-{fast}AHHHH!"         
            
         show reed sad
         
         
         pass            
    
    play music torture_p2 fadein 0.5
    
    "Reed yelps as the goon standing over him, {w=0.10}putting out his cig on the top of his maw."
    
    G1 "Strike one."
    
    play sound goon_smoke volume 0.5
    
    "The short one says, leaning back in his chair and releasing a cloud of smoke."

    G1 "I take it that cleared your mind a little?" 
    
    G1 "We're not screwing around kid, {w=0.10}you're going to give us what we want, one way or the other."
    
    G1 "So I suggest you cooperate before I have to take more{cps=10}... drastic measures."

    show tall goon neutral:
        xcenter 0.3
        easein_quint 1.0 xcenter 0.35

    "He looks over to his companion who nods." 
    
    "Without a moment's hesitation, he grabs the tuft at the end of Reed's tail."
    
    T "Get your hands off him!"
    
    T "Fangs dad is a cop {w=0.10}and you lay a finger on us he'll make you wish you were never born!"
        
    F "Trish, shut up!"
    
    show short goon grin
    
    G1 "Oh he is? {w}Well now we're getting somewhere." 
    
    G1 "Had a feeling you might be with the cops; {w}no way the other families would muscle in on our turf so openly."
    
    
    show short goon neutral:
        xcenter 0.7
        easeout_quint 1.0 xcenter 0.6
    
    "He leans back into Reed's face."
    
    G1 "Question two: {w}So are you kids a bunch of fresh recruits?" 
    
    G1 "If so, {w=0.10}were you out here looking for evidence?" 
    
    G1 "What do your superiors already know about our operations?"
    
    
    menu:
        
        "Deny everything":
            Re "We don't work for the cops or anyone man I swear!" 
            
            Re "Were just a bunch of dumb teens in way over our heads! {w=0.10}You have to believe me!"
            
            "The goon sighs and shakes his head."
            
            G1 "Strike two."
            
            pass
            
        "Beg for life":
            "Reed's face is completely enveloped in fear, I doubt ours are any better."
            
            Re "Please, I promise we'll do anything you want! {w}You can destroy the tape and we won't tell anybody what we saw tonight I swear!" 
            
            Re "Whatever you want man just let us go..."
            
            "The goon sighs and shakes his head." 
            
            G1 "Strike two."

            pass
            
        "Strike a deal":

            show reed neutral

            "Suddenly Reed's face relaxes a little, {w=0.10}like he's found a way to bail us out of this."

            Re "I got nothing man we've told you all everything." 
            
            Re "Since we know too much already, {w=0.10}why don't we join up? {w=0.10}We're not cops and we'd be happy to prove it."            
            
            $ renpy.music.set_volume(0.2,delay=0.5,channel='music')
            
            pause .5
            
            play sound af_wtf
            
            AnonAndFang "{size=50}{b}WHAT!?"
            
            T "..."
            
            $ trish_extended_dialogue = True
            
            show short goon grin with dissolve
            
            "The goon slaps the table and laughs, {w=0.10}then looks at his friend while pointing at Reed."
            
            G1 "You know I'm starting to like this one."
            
            "He turns back to Reed."
            
            G1 "Ya got balls kid I'll give you that."
            
            G1 "Truth be told we're always shorthanded around here." 
            
            G1 "Unfortunately for you, orders are orders."
            
            $ renpy.music.set_volume(1.0,delay=0.5,channel='music')
            
            show short goon neutral with dissolve
            
            G1 "More importantly, that's NOT what I asked you, {w=0.25}strike two."
            
            
            
            pass            
    
        "Antagonize":
            
            play sound reed_spit
            
            show reed angry:
                xcenter 0.4
                ease 0.25 xcenter 0.35
                ease 0.5 xcenter 0.4
                
            
            show short goon neutral:
                xcenter 0.6
                pause .5
                easeout_quint 0.25 xcenter 0.65
            
            "Without hesitation Reed hawks a loogie into the goon's face."
                
            
            G1 "AAUGH YOU LITTLE SHIT!"
            
            show short goon angry:
                xcenter 0.65
                easeout_quint 0.5 xcenter 0.7
            
            "He reels back to wipe it off,"
            
            play sound "audio/effects/slapstickPunch.ogg"
            
            show short goon angry:
               xcenter 0.7
               easeout_quint 0.25 xcenter 0.5
               easeout_quint 0.25 xcenter 0.6
            
            show reed shocked:
               xcenter 0.4
               .25
               ease 0.25 xcenter 0.4 rotate -25
               ease 1.0 xcenter 0.4 rotate 0              
            
            
            
            "He reels back to wipe it off,{fast} and then slaps reeds maw so hard it almost knocks him over."
            
             
            G1 "You think this is funny!? I'll show you something real funny!" 
             
             
    
    show short goon neutral with dissolve
    
    play sound goon_fingersnap 
    
    play music torture_p3 fadein 1.0
    
    "He snaps his fingers."
    
    pause .25
    
    
    "The taller one takes a handful of the feathers, {w=0.10}and with a quick jerk, {w=0.25}{nw}"
    
    play sound goon_ripout    
    queue sound short_scream
    
    
    show reed shocked:
        ycenter 0.655
        1.0
        parallel:
         .5
         ease 0.2 ycenter 0.68
         ease 0.4 ycenter 0.63
         ease 0.4 ycenter 0.68
         ease 0.4 ycenter 0.63
         ease 0.2 ycenter 0.655
         
        
        
        parallel:
         matrixcolor TintMatrix('#f7f7f7')
         1.0
         matrixcolor TintMatrix('#e0b6b6')
         1.0
         repeat       
    
    "The taller one takes a handful of the feathers, {w=0.10}and with a quick jerk, {fast}rips them out at the root."
    
    "Reed screams in agony, {w=0.10}staring at the ceiling as he squirms against his restraints." 
    
    "Blood started to drip from the missing section of the pattern." 
    
    "Fang stares agape in abject horror, Trish starts to cry."
    
    show reed sad
    
    G1 "Ready to talk yet?"

    "Reed is breathing heavily as he wrestles with the pain." 

    G1 "Let me tell you what I think."
    
    show short goon neutral:
        easeout_quint 1.5 xcenter 0.7
        
        
    play sound chair_creak
    
    "The goon lays back in his chair again."     

    G1 "My guess is you're a bunch of rookies who got tipped off and are operating off the books."
    
    show short goon grin 
    
    G1 "Hell, there might not even be another living soul who knows where you went tonight."
    
    G1 "There's no one coming for ya, and you'll be dog food by the time people start asking questions." 
    
    show short goon neutral
    
    G1 "We've made plenty of young fools disappear, {w=0.10}don't think we can't do the same with you."
    
    show short goon neutral:
        xcenter 0.7
        easeout_quint 1.0 xcenter 0.6
        
    "The goon sits back up and picks out a long, thick butcher knife from his cavalcade of carnage and eyes it longingly. "
    
    G1 "So taking that into account, {w=0.10}I hope you have the prudence to choose your next words very carefully {w=0.10}because, as I'm sure you are now aware, I don't give second chances."
    
    "The taller one grabs Reed's arm and holds it out in place." 
    
    show short goon neutral with dissolve
    
    play ambient knife_sharpening
    
    "The other takes the knife and dances it across Reed’s fingers. "
    
    G1 "A single slip, and five becomes four."
    
    G1 "So I'll ask you one more time: {w}Who are you kids?"
    
    menu: 
      "Please...":
        "Thick streams of tears streak across a face full of despair. "
        
        Re "{cps=10}Please...{w=0.25}{cps=50}we don't know anything, you have to believe me..."
        
        "The goon stares into him unflinchingly."
        
        G1 "Is that your final answer?"
        
        show reed considering
        
        Re "{cps=10}{b}...Please..."
        
        
        pass
          
      "Try to save friends":
        pause 1.0
        show reed neutral: 
          parallel: 
           xcenter 0.4
           xzoom 1.0
           pause .5
           xzoom -1.0 xoffset 200
           pause .5
           xzoom 1.0 xoffset 0
          
          parallel:
           matrixcolor TintMatrix('#f7f7f7')
           1.0
           matrixcolor TintMatrix('#e0b6b6')
           1.0
           repeat  
                          
        
        "Reed looks over to us for a moment before facing the man again."

        "Thick streams of tears streak across a face full of despair."

        Re "“{cps=10}...{w=0.25}{cps=50}Do whatever you want with me, {w=0.10}but please don't hurt my friends."
        
        Re "This is all my fault."
        
        Re "I'll do or say whatever you want, but {cps=10}please...{w=0.25}{cps=50} just let my friends go..."        
            
        "The goon stares into him unflinchingly."
        
        G1 "Is that your {w=0.10}final answer?"
        
        Re "{cps=10}{b}...Please..."
        
        
        pass
      
      
      "Antagonize":
        
        show reed unimpressed
        
        "Reed laughs quietly to himself."
        
        Re "Why answer if you're not gonna listen?"
        
        Re "You get off on this don't you?" 
        
        Re "You sick fuck..."
        
        "The goon stares into him unflinchingly."

        G1 "Is that your {w=0.10}final answer?"
        
        Re "{cps=10}{b}...Bite me..."
        
        pass  
    
    stop music fadeout 2.0
    
    show black:
        alpha 0.0
        linear 2.0 alpha 1.0
    
    
    "The goon closes his eyes and takes a deep breath."
    
    stop ambient fadeout 0.5
    
    pause 2.0
    
    G1 "Strike three."
    
    play sound goon_fingerchop_delay
    queue sound long_scream
    
    pause 2.0
    
    play music torture_p4 fadein 1.0
    
    
    show reed shocked:
        ycenter 0.655
        parallel:
         alpha 0.9
         ycenter 0.655
         ease 0.15 ycenter 0.63
         ease 0.3 ycenter 0.68
         ease 0.3 ycenter 0.63
         ease 0.3 ycenter 0.68
         ease 0.3 ycenter 0.63
         ease 0.3 ycenter 0.68
         ease 0.5 ycenter 0.63
         ease 0.5 ycenter 0.68
         ease 0.5 ycenter 0.63
         ease 0.5 ycenter 0.68
         ease 0.8 ycenter 0.63
         ease 0.8 ycenter 0.68
         ease 0.8 ycenter 0.63
         ease 0.8 ycenter 0.68
         ease 0.4 ycenter 0.655
       
        parallel:
         matrixcolor TintMatrix('#e0b6b6')
         .5
         matrixcolor TintMatrix('#f7f7f7')
         .5
         repeat         
    
    show black:
        alpha 1.0
        linear 2.0 alpha 0.0
    
    "I heard Reed utter a blood curdling scream loud enough to wake the dead."
    
    "As soon as the finger hits the table, {w=0.10}the taller goon pulls out a roll of gauze and wraps up the stub to stem the bleeding."
    
    "The girls let out an involuntary shriek."
    
    T "What the fuck is wrong with you!?"
    
    show short goon angry
    
    G1 "Pipe down, or I'll stuff it down your throat!"
    
    "That quickly shut them up, {w=0.10}and soon only their muffled sniffling could be heard."
    
    show short goon neutral
    
    G1 "One down nine to go, {w}ya ready to talk now?"
    
    menu:
      "...":
         pass 
      "...":
         pass
      "...":
         pass
    
    
    show reed sad
    
    pause 1.0
    
    "Reed holds his head held low, as he tries to cope with the pain as best he can."     
         
    Re "...don't know anything...I swear..."      
    
    show short goon angry with dissolve
    
    "The goon merely rolls his eyes with a growing look of frustration." 
    
    G1 "Loyal to the end, eh?"
    
    G1 "Fine then, we can do this all night."
    
    show short goon angry:
        xcenter 0.6
        easeout_quint 0.5 xcenter 0.5
        easeout_quint 0.5 xcenter 0.6
    
    pause .5
    
    play sound goon_fingerchop
    
    show black:
        linear .5 alpha 1.0
        linear 1.5 alpha 0.0
    
    "{b}THWACK{nw}"
   
    
    show reed shocked:
        ycenter 0.655 alpha 0.85
        parallel:
         ease 0.25 ycenter 0.68
         ease 0.5 ycenter 0.63
         ease 0.5 ycenter 0.68
         ease 0.8 ycenter 0.63
         ease 0.8 ycenter 0.68
         ease 0.8 ycenter 0.63
         ease 0.8 ycenter 0.68
         ease 0.4 ycenter 0.655
        
        parallel:
         matrixcolor TintMatrix('#e0b6b6')
         0.25
         matrixcolor TintMatrix('#f7f7f7')
         0.25
         repeat 
    
    "Another finger drops to the table, {w=0.10}Reed's body spasms like a beheaded chicken, but there's no verbal response. "
    
    "The girls have completely broken down, {w=0.10}pleading on deaf ears for the safety of their friend." 
    
    "I sit there paralyzed in shock, {w=0.10}barely able to process what's going on around me, it feels like I'm in a dream."
    
    show reed sad
    
    "Trapped in a nightmare I know I'll never wake up from."
    
    G1 "We can stop this at any time you know, {w}all you have to do is say the word."
    
    Re "..."
    
    show short goon neutral
    
    G1 "{cps=10}...{cps=50}Hey pal, you still in there?"
    
    "Reed just sits there with a vacant expression, {w=0.10}the light extinguished from his eyes." 
    
    play sound end_groan
    
    "His feeble breath the only sign he was still living."
    
    show tall goon neutral:
        xcenter 0.35
        easein_quint 3.0 xcenter 0.4
    
    G2 "If this ain't exciting enough for you anymore, I can go get the drill-"
    
    "The shorter one waves his hand dismissively."
    
    G1 "Eh, don't bother, {w=0.10}I've been in the business long enough to know this one’s a lost cause."
    
    show tall goon neutral:
        xcenter 0.4
        easein_quint 1.0 xcenter 0.45       
    
    show reed sad:
        alpha 0.85
        ease 2.0 alpha 0.0
    
    show short goon grin with dissolve
    
    G1 "I think it's time we picked a new contestant."
    
    show short goon grin:
        zoom 0.7
        easeout_quint 1.0 zoom 1.0
    
    "He saunters over, leaning in to inspect us like cattle."
    
    "As he turns to Fang she quickly leans her head in {nw}" 
    
    play sound fang_bite volume 2.0
    
    show short goon neutral:
        zoom 1.0
        easeout_quint 0.25 zoom 0.9
        easeout_quint 0.25 zoom 1.0
    
    
    "As he turns to Fang she quickly leans her head in {fast}and snaps at him like a shark, {w=0.10}her face coated in pure hatred."
    
    "He pulls away just in time to avoid needing a skingraft."
    
    G1 "Whoa there, looks like there's still some fight left in this one!"
    
    show short goon grin 
    
    G1 "I think, you'll do nicely."
    
    pause .5
    
    A "Please god no! Take me, not her!"
    
    G1 "If you don't want her to get hurt, you're free to cooperate anytime!"
    
    show short goon neutral:
        zoom 1.0
        easeout_quint 1.0 zoom 0.7
    
    play sound fang_resist volume 1.5
    
    "He grabs her by the hair and starts pulling her over." 
    
    "I wrack my brain feverishly for something, {w=0.10}anything, I could possibly say or do that could prevent the scene happening before me."

    play sound "audio/effects/cellphone.ogg"    
   
    stop music fadeout 10.0
    play ambient lamp_buzz fadein 10.0 volume 1.0
    
    pause .25
    
    show short goon shocked
    show tall goon shocked
    
    pause .25
    
    show short goon neutral
    show tall goon neutral
   
    "The shorter goon whips out a flip phone from his pocket and holds it to his ear."
    
    "His eyes go wide."
    
    G1 "Boss!? {w=0.10}Uh, yeah we’re in the middle of it now."
    
    show short goon neutral
    
    G1 "Well, {w=0.10}not great."
    
    G1 "I think they might be with the force, but the first one was a dead end so we're not-, {w=0.10}I'm sorry it's just-,{nw}"
    
    show short goon shocked
    
    G1 "I think they might be with the force, but the first one was a dead end so we're not-, I'm sorry it's just-,{fast}wait what?!"
    
    G1 "That's not necessary I've-,{nw}" 
    
    show short goon neutral
    
    G1 "That's not necessary I've-,{fast} yes, alright, I understand." 
    
    G1 "Will do."
    
    play sound goon_phone
    
    pause 2.0
    
    G1 "Good news! {w=0.10}The Boss happened to be in the neighborhood, and has decided to handle the matter personally."
    
    G1 "You should feel honored! {w=0.10}Not everyone has the opportunity to get worked over by a man of his caliber."
    
    G1 "They'll be scrubbing you off the walls by the time he's done with ya!"
    
    show short goon neutral:
        xcenter 0.6 xzoom -1.0
        0.5
        xzoom 1.0
        easeout_quint 2.0 xcenter 0.8
        xzoom -1.0
        
    show tall goon neutral:
        xcenter 0.45
        easein_quint 8.0 xcenter 1.2
    
    "He and his companion laugh and head for the exit, before passing through he turns his head back around and points with an evil grin." 
    
    show short goon grin
    
    G1 "Now don't you kids go anywhere! {w}The main event will begin shortly!"
    
    show short goon grin:
        xzoom 1.0 xcenter 0.8
        easeout_quint 2.0 xcenter 1.2
        
    
    pause .25
    
    play sound lightSwitch
    stop ambient
    
    scene black with fade
    
    "He shuts off the light and leaves the room."
    
    play sound "audio/effects/doorSlam.ogg"
    
    "The door closes behind them with a slam, {w=0.10}leaving only the darkness and the sounds of Trish's crying."
    
    window hide
    
    play sound trish_cry
    
    pause 8.0
    
    
    return
