label bitn_goofy_investigation:
    stop music fadeout 3.0
    
    # I know, there would be a scene with a camera before this label, so make sure you're using the right one/deleting show screen statement in here
    scene black 
    with Dissolve(3)
    
    pause 2.0
    
    play music exploration_bgm fadein 3.0
    scene abandoned_atrium with Dissolve (3)
    
    "The atrium holds the desecrated remains of a reception hall, {w=0.25}our footsteps echo across the room." 
    
    "I pull out my flashlight to dispel the darkness, {w=0.25}the dust kicked up by our entrance catches the light and floats across." 

    "We traverse through the crumbled concrete and rebar to find a good place to set up shop." 
    
    show reed flip neutral at chill_move_right(0.3)
    with dissolve 
    
    Re "Looks like the front desk."
    
    show trish flip neutral at rushed_move_right(0.5)
    with dissolve     
        
    T "Holy shit, the lightbulbs are still in the lamps."
    
    show fang flip neutral at insecure_move_right(0.7)
    with dissolve 
    
    F "Dude, you think the showroom’s still intact?" 
    
    "She points to the left at a set of double doors." 
    
    "From the moonlight I can faintly make out a sign hanging above the doorway."
    
    A "You mean the cars? {w=0.25}Probably a few decades too late on that one."
    
    show reed flip happy with dissolve
    
    Re "Hey you don't know till you try! {w=0.25}New van here I come!"
    
    show reed:
        ease 1.0 xcenter -0.2
    
    pause 1.0
    
    hide reed
   
    play sound reed_closing_door_sfx volume 0.8
    pause 1.0
    
    show fang flip:
        easeout 0.5 xcenter 0.6
    show trish flip:
        easein 0.5 xcenter 0.4
    
    
    "He shuffles over to the doorway with a goofy grin plastered across his face and heads in."
    
    show trish flip considering with dissolve
    
    T "We're already trespassing, {w=0.25}you sure it's a good idea to be taking shit too?"
    
    A "Why not? If it's still here after all this time, {w=0.25}clearly no one else wants it." 
    
    show fang flip unimpressed with dissolve

    "Fang rolls her bright adjusted amber eyes."
    
    F "Trish don't be a square and come on." 
    
  
    
    
    show black:
        alpha 0.0
        linear 3.0 alpha 1.0
    
    show fang flip unimpressed:
        easeout 1.0 xcenter -0.2
    
    pause 1.0
    
    hide fang
    
    show trish flip considering:
        easein 1.0 xcenter -0.2
    
    pause 1.0
    
    hide trish
    
    
    pause 1.0
    
    scene abandoned_acoustics with Dissolve(3)
    
    show fang neutral at insecure_move_left(0.6)
        
    show trish neutral at rushed_move_left(0.4)
    
    with dissolve
    
    "She groans but reluctantly follows us inside."
    
    "Burnt trash and debris litter the cracked, {w=0.10}splintered floorboards."
    
    pause .5
    
    show fang very happy:
     xcenter 0.6
     easeout 0.5 ycenter 0.6
     0.25
     easeout 0.5 ycenter 0.655
          
    $ renpy.music.set_volume (0.1)
    play sound fang_scream_sfx volume 0.7
    show trish shock:
        easeout 0.25 xcenter 0.3
    pause .25
    show trish neutral    
    F "{cps=0}{b}{size=60}HOW YOU DOING VOLCALDERA!{/b}"
    
    pause 1.0
    
    "Her shout echoes across the large empty space."

    show fang happy with dissolve
    $ renpy.music.set_volume(1.0, delay=3.0)
    F "Man, the acoustics in this place are great! {w=0.40}We totally could have held a show here!"

    A "Sure if you wanted to bring down the roof, {w=0.25}guess that'd be cheaper than a demo team."  

    show fang flip off happy with dissolve
    
    pause 0.5
    
    show fang happy with dissolve
    
    pause 1.0
    
    
    play sound trish_pickup_sfx
    show trish:
        easein 0.5 ycenter 0.7
        pause 1.0
        easein 1.0 ycenter 0.655
    
    pause 1.5
    
    "Trish picks up some of the crap off the floor."
    
    show trish unimpressed
    
    T "So much for no squatters."
    
    A "Nah, {w=0.25}this place hasn't been a hobo den for a long time. {w=0.40}There'd be old food cans and the like if it was, {w=0.25}those types don't clean up."
    
    pause .5
    
    Re "Hey guys check this out!"
    
    show trish neutral with dissolve 
    
    pause .5
    
    show trish neutral:
        easein 1.0 xcenter 1.2
    
    pause 1.0
    
    hide trish
    
    show black:
        alpha 0.0
        linear 2.0 alpha 1.0
    
    show fang happy:
        easeout 1.0 xcenter 1.2
    
    pause 1.0
    
    hide fang
    
    hide black 
    show reed neutral:
        ycenter .655 xcenter 0.8
    with Dissolve(1.5)
    
    show fang happy at insecure_move_left(0.3)
    
    show trish neutral at rushed_move_left(0.5)
    
    with dissolve
    
    "We look over to the back corner, {w=0.20}and see him hunched over the decrepit remains of some old classic van that's more rust than vehicle."
    
    show reed flip explanatory with dissolve
    
    Re "I bet if I get a new battery, {w=0.20}and do some touch up work here and there, {w=0.20}I could get this baby running again!"
    
    show reed flip neutral
    
    F "Reed, I don't think even Raptor Jesus could bring this thing back from the dead."
    
    show reed flip happy with dissolve
    
    "Reed waves his hand dismissively."

    Re "Oh ye of little faith."
    
    show reed happy with dissolve:
        pause .5
        ease 0.5 xcenter 1.2
    
    pause 1.0

    hide reed with None       

    show fang happy:
        easeout 0.5 xcenter 0.4
    show trish neutral:
        easein 0.5 xcenter 0.6     
    
    pause .5
    
    show trish considering with dissolve
      
    T "Why is this thing even still here?"  
    
    A "Hey, {w=0.25}even ghosts need hobbies." 
    
    A "Eternity's a long time you know."
    
    show trish unimpressed with dissolve
    
    "Fang snickers as Trish makes a face."

    T "{cps=20}That's not funny Anon I'm being ser-{nw}"    

    $ renpy.music.set_volume(0.1)
    play sound van_horn_sfx volume 0.9
    
    show trish shock:
      easein 0.25 ycenter 0.2
      easein 0.25 ycenter 0.655
            
    pause .5
    
    Re "Yep, {w=0.5}horn still works."
    $ renpy.music.set_volume(1.0, delay=3.0)
    show trish angry
    pause .75
    show trish annoyed
    
    show fang very happy:
       easeout .25 ycenter 0.6
       .25
       easeout .25 ycenter 0.655       
       repeat
    
    "Fang and I burst into laughter as Trish sulks."

    show fang happy with dissolve:
        ycenter 0.655 
    
    pause .5
    
    F "So you ready to crash and crack open that case?"
    
    "I grin."
    
    A "Not quite, {w=0.25}we've still got a lot of building to explore, {w=0.25}come on!"
    
    show trish considering with dissolve
    
    T "Well I'm dry. {w=0.25}Pass me one for the road."
    
    show fang flip happy with dissolve:
      pause .5
      easeout 1.0 xcenter -0.2
    
    pause 1.0 
    
    hide fang
    
    show trish flip considering with dissolve:
      pause .5
      easein 1.0 xcenter -0.2
      
    pause 1.0  
    
    hide trish
    
    show black:
        alpha 0.0
        linear 4.0 alpha 1.0 
    
    show reed flip happy behind black at chill_move_right(0.5) with dissolve
    
    pause 2.0
    
    show reed flip happy:
     
      ease 2.0 xcenter -0.2
    
    pause 2.0
    
    hide reed    
    
    "Reed hands Trish a bottle as he rejoins us." 
    
    "We leave the showroom and head into the factory proper."
    
    scene abandoned_graffiti with fade
    
    
    "The place has been shredded, {w=0.25}the only signs of life being the graffiti lining the walls."
    
    "I stop to look at one of the cave paintings."
    
    A "Hey Trish, {w=0.25}this one looks kinda like you!"
    
    show trish flip neutral with Dissolve(2):
       ycenter .655 xcenter 0.5
    
    pause .5
    
    show trish flip unimpressed 
    
    T "That doesn't look anything like me."
    
    A "Sure it does!" 
    
    A "How many Trikes do you know at your height and cup size?"
    
    show trish flip annoyed with dissolve
    
    T "Those aren’t tits, those are floatation devices."
    
    $ renpy.suspend_rollback(True)
    
    show fang flip happy with dissolve:
        ycenter .655 xcenter 0.7
        pause .5
        easeout .25 xcenter 0.55
        pause .25
        easeout .5 xcenter 0.7        
    
    pause 0.25
    
    show trish flip surprised
    
    pause 0.25
    
    show trish flip annoyed:
      easein 0.5 xcenter 0.4         

    show trish flip annoyed:
        xcenter 0.4 ycenter 0.655
        
    show fang flip happy:
        xcenter 0.7 ycenter 0.655
    
    $ renpy.suspend_rollback(False)

    "Fang feels up Trish’s breasts."

    F "You’re more buoyant than you’d give yourself credit for."

    show trish flip unimpressed
    
    T "If these are floatation devices, yours are the titan submersible."
    
    pause .5
    
    A "That is the most oddly specific shit I’ve ever heard you spout."
    
    show trish flip smug with dissolve
    
    T "Am I wrong?"
   
    show fang flip unimpressed
    
    F "Choose your words carefully, dweeb."
    
    menu:
        
        "They’re small, but that’s fine.":
            
            A "They’re small, {w=0.25}but it just gets me closer to the heart." 
    
            A "See, {w=0.25}people love Fang for a reason, {w=0.25}and they don't love you trike."
            
            show fang flip happy with dissolve
            
            
            show trish flip unimpressed
            T "Oh fuck off, {w=0.25}I’ve had more boyfriends than men in your family."
            
            "I grin."
            
            A "Trish, I know for a fact you’re still a virgin."
            
            show trish flip surprised
            
            pause .1
            
            show trish flip unimpressed
            T "Based on what?"
            
            show fang flip very sad with dissolve
            
            pause .5
            
            show trish flip shock
            
            pause .25 
            
            show trish shock with dissolve
            
            pause .25
            
            show trish indignant 
            T "Fang how could you!"
            
            show fang flip embarass with dissolve
            F "Sorry Trish…"
             
            show trish flip annoyed with dissolve
            
            pause .5
            
            T "Whatever, {w=0.25}I just haven’t found the right guy ok?"
            
            "My grin spreads ear to ear."

            A "Whatever helps you sleep at night."             
            
            show reed neutral:
             xcenter 0.15
             ycenter 2.0
             ease 2.0 ycenter 0.6555 
            
            show fang flip neutral
            
            with dissolve

        "They’re small, but they could be bigger.":
            F "Then impregnate me."
            
            show reed shocked at chill_move_left(0.15)
            show trish shock:
                easeout 1.5 xcenter 0.4
            with dissolve
            
            
            show fang flip unimpressed:
                easeout 0.5 xcenter 0.8
 
            "Reed chokes on his smoke."
            
            Re "What the fuck, Fang!"
            
            A "The only thing stopping me right now is consent."
            
            show abandoned_graffiti_2 behind reed,trish:
               blur 5.0
            show reed shocked behind fang:
               blur 5.0
            show trish shock:
               blur 5.0    
            show fang flip off happy:
               xzoom -1.0 zoom 4.0 xcenter 0.45 ypos 2400

            with Dissolve(2)
            
            "I consent."
            
            $ renpy.suspend_rollback(True)
            
            show trish flip unimpressed:
                easeout 2.0 xcenter 0.8 zoom 3.0 blur 0
                easeout 1.0 zoom 1.0
                
            show reed unimpressed:
                ease 2.0 zoom 3.0 blur 0
                ease 1.0 zoom 1.0
            
            pause 2.0
            hide abandoned_graffiti_2
            show fang sad flip:
                  xzoom 1.0 zoom 1.0 ycenter .655 xcenter 0.5                
            with Dissolve(1)
            
            show reed unimpressed:
                zoom 1.0 xcenter 0.15 blur 0  
                
            show trish flip unimpressed:
                zoom 1.0 xcenter 0.8 blur 0  
            
            $ renpy.suspend_rollback(False)

            "Reed and Trish peel us apart before anything paranormal happens. "
            show reed neutral

            
        "Wouldn’t you rather have Trish’s tits?":
          
          show fang flip considering with dissolve
          
          F "I’m not sure I’d be able to play guitar if I had those coconuts strapped to my chest."
          
          show trish flip considering
          
          T "I literally play bass."
          
          F "Fair."
          
          show fang flip happy 
          
          F "Then yeah, I agree. I’d rather have her tits."
            
          show reed neutral:
            xcenter 0.15
            ycenter 2.0
            ease 2.0 ycenter 0.655
          
          
    show fang flip neutral    
    show trish flip neutral    
    T "Anyway, Pterosaurs don’t get above C cups, do they?"
        
    F "Eh, they’re supposed to get pretty big once you have children."
    $ renpy.suspend_rollback (True) 

    show black:
        alpha 0.0
        linear 4.5 alpha 1.0
    
    
    show trish flip neutral with dissolve:
        .5
        easein 2.0 xcenter -0.2

    show fang flip neutral:
        easeout 2.0 xcenter -0.2

    pause 2.5
    hide fang         
    hide trish

    show reed flip neutral with dissolve:
         pause .5
         ease 2.0 xcenter -0.2        
    
    pause 2.0
    hide reed

    show black:
        alpha 1.0
    
    $ renpy.suspend_rollback (False)
    
    "The pair continue their girl talk and we head deeper into the factory."
    
    scene abandoned_depth
    show reed flip neutral:
        ycenter 0.750 xcenter 0.2 zoom 2.0
    show trish neutral:
        ycenter 0.655 xcenter 0.8
    show fang flip neutral behind reed:
        ycenter 0.655 xcenter 0.4 zoom 0.5      
    with Dissolve(3)
    
    
    A "Y’all find anything cool?"
    
    show trish flip unimpressed with dissolve
    
    T "No, this place is a dump."
    
    show reed neutral with dissolve:
        pause .5
        ease 1.0 zoom 1.0 ycenter 0.655
        
    pause 1.5
    
    show reed happy:
        zoom 1.0 ycenter 0.655 xcenter 0.2
    
    Re "I found this neat raccoon skull for Fang’s collection."
    
    show trish flip neutral
    show fang flip very happy:
        easein 1.0 zoom 1.0 xcenter 0.5
    
    
    "This elicits some excitable noises from the Ptero."
    
    A "Fang how about you?"
    
    show fang neutral with dissolve
    
    show reed neutral behind fang
    
    F "Nothing really just-{nw}"
    
    show fang surprised
    F "Nothing really just-{fast} hey look at this!"
    
    play sound fang_pickup_sfx
    show fang surprised:
        easein 0.5 ycenter 0.725
        easein 1.0 ycenter 0.655
            
    pause 1.5
    
    show fang happy
    
    "She scoops up an ancient colt revolver. {w=0.40}It’s full of empty shells and badly corroded." 
    
    F  "I’ve always wanted one of these!" 
    
    "She pockets the revolver."
    
    A "Guess I’m not going to school tomorrow."

    show fang happy:
        easein 0.5 zoom 2.0 ycenter 0.75
        easein 0.5 zoom 1.0 ycenter 0.655
    
    pause 1.0 
    
    "Fang elbows me in the side." 
    
    F "God, you're such a dweeb."
    
    A "Am I wrong?"

    $ renpy.suspend_rollback(True)

    show black:
        alpha 0.0
        linear 3.0 alpha 1.0
    
    show fang: 
       easein 3.0 zoom 0.2 xcenter 0.5 ycenter 0.5
    
    pause 1.0
    
    show trish:
        easeout 2.0 zoom 0.2 xcenter 0.5 ycenter 0.5
    
    pause 1.0
    
    show reed:
        ease 1.0 zoom 0.2 xcenter 0.5 ycenter 0.5

    pause 1.0
        
    show black:
        alpha 1.0
    
    $ renpy.suspend_rollback(False)

    "She doesn't answer that and keeps plowing ahead as I try to keep up."
    
    "I think she's finally catching the bug so to speak."
     
    hide screen anon_camera
    play sound "audio/effects/cameraShutterClick.ogg"
    stop music fadeout 2.0
    
    
    scene abandoned_conveyor with Dissolve (3)
    
    "When we pass into the next room, {w=0.20}I see a long conveyor belt still intact, {w=0.20}facing a window that peeked out into the night of the city." 
    
    "The beat up equipment created a sort of old school mystique that gave the air a sense of relaxation."
    
    
    play sound "audio/effects/carKick1.ogg"
    show anon neutral with dissolve:
        ycenter 1.0 xcenter 0.1
        ease_cubic 1.0 ycenter 0.655 
    
    pause 1.0
    
    show anon neutral:
        ycenter 0.655
        ease_cubic 3.0 xcenter 0.8
    
    pause 2.5
    
    "I climb my way up and dangle my legs off the side like a bench."

    show anon flip happy with dissolve
    
    A "Hey gang, {w=0.20}I think I found our drinking spot!"
    
    F "About time."
    
    show anon neutral
    
    play sound "audio/effects/carKick2.ogg"
    show fang neutral with dissolve:
        ycenter 1.0 xcenter 0.1
        easein 1.0 ycenter 0.655 
    
    pause 1.0
    
    show fang neutral:
        easein 3.0 xcenter 0.8
    
    play sound "audio/effects/carKick3.ogg"
    show reed neutral with dissolve:
        ycenter 1.0 xcenter 0.1
        ease 1.0 ycenter 0.655
    
    pause 1.0

    show anon flip neutral:
       ycenter 0.655
       ease_cubic 1.0 xcenter 0.6

    show reed neutral:
       ycenter 0.655
       ease 1.5 xcenter 0.3       
    
    pause 1.0

    show fang flip neutral with dissolve:
       ycenter 0.655 xcenter 0.8       
    
    "Eager, they all make their way over to join me."
    
    show trish unimpressed with dissolve:
        ycenter 1.0 xcenter 0.1
        easeout 1.0 ycenter 0.8
    
    pause 1.0      
      
    show reed flip neutral with dissolve:
       ease 0.5 xcenter 0.2
       
    show anon flip neutral:
       ease_cubic 1.0 xcenter 0.4
 
    pause 1.0
    
    play sound "audio/effects/lockerSmash.ogg"
    show trish:
       easeout 0.5 ycenter 0.655 xcenter 0.2        
    
    pause .5
    show trish neutral
    
    show anon flip neutral:
        ease_cubic 0.5 xcenter 0.6
    
    show reed neutral with dissolve:
        ease 0.5 xcenter 0.3
    
    play music party_bgm volume 0.8 fadein 0.5
    
    "Reed and I reach down to Trish to help pull her up. {w=0.10}We whip out the case and dig in."
    
    play sound gang_beer_sfx
    
    show reed explanatory
    
    show trish smile:
         easeout 0.5 ycenter 0.725
         easeout 0.5 ycenter 0.655
    show fang flip happy:
         easein 0.5 ycenter 0.725
         easein 0.5 ycenter 0.655
    show anon flip grin:
         ease_cubic 0.5 ycenter 0.725
         ease_cubic 0.5 ycenter 0.655
    
    pause 0.5
    
    show beer_trish:
        xcenter 0.2 ycenter 0.75 zoom 0.4
        easeout 0.5 ycenter 0.68
    show beer_anon:
        xcenter 0.648 ycenter 0.76 zoom 0.4 
        ease_cubic 0.5 ycenter 0.7
    show beer_fang:
        xcenter 0.81 ycenter 0.68 zoom 0.4
        easein 0.5 ycenter 0.60
    pause 1.0
    
    "Reed abstained and pulled out his pipe."
    
    play sound reed_lighter_sfx volume 1.5
    
    "Smoking an entire bowl in one glorious hit, {w=0.20}much to the beckons and cheers from Fang and Trish."
    
    "He looks more and more feral with every hit he takes, {w=0.20}as if regressing him back to the creature that climbed from the primordial soup and declared \'behold\’."
    
    "He'll be fine."
    
    show fang flip very happy
    
    show beer_fang:
        ycenter 0.27 xcenter 0.84
        
    
    with dissolve
    
    "Fang was having the time of her life." 
    
    "Stealing chaste hits from Reed’s peace pipe and drinking beer after beer, {w=0.20}as if she paid for the case."
    
    show trish happy
    
    with dissolve
    
    
    "Even Trish eventually came around and slammed more than a few of her own."
    
    
    #Gave a thought to how represent this segment better and came up with the NVL + fastforward intermissions  
    
    
    nvl show Dissolve(1)
    
    ANVL "{nw}"
    ANVL "We had a blast,"
    
    
    show screen forwarding
    pause 0.5
    
    hide beer_trish
    hide beer_anon
    hide beer_fang
    
    hide screen forwarding
    
    show reed explanatory:
        ycenter 0.655 xcenter 0.1
        
    show fang flip sad:
        ycenter 0.655 xcenter 0.6
    show anon flip neutral:
        ycenter 0.655 xcenter 0.4
    show trish flip surprised: 
        ycenter 0.655 xcenter 0.8        
    
    
    ANVL "took turns trading drunk ghost stories,"
    
    show screen forwarding
    pause 0.5   
    hide screen forwarding
   
    show anon neutral:
        ycenter 0.655 xcenter 0.7
        pause 1.0
        ease_cubic 0.25 xcenter 0.55
        ease_cubic 0.25 xcenter 0.75
        
    show beer_anon behind fang:
        xcenter 0.64 ycenter 0.69 zoom 0.4          
        pause 1.0
        ease_cubic 0.25 xcenter 0.49
        ease_cubic 0.25 xcenter 0.69
        ease_cubic 1.0 xcenter 1.2 ycenter 0.5 rotate 180
        
        
    show fang neutral:
        ycenter 0.655 xcenter 0.5
    show reed neutral:
        ycenter 0.655 xcenter 0.25
    show trish neutral: 
        ycenter 0.655 xcenter 0.1       
    
    
    
    pause 2.0
    
    play sound anon_bottle_throw_sfx volume 1.0
    
    pause 2.0
    
    play ambient "audio/effects/crowdCheerLoop.ogg"
    
    show reed happy:
      .5
      block:
        ease 1.0 ycenter 0.56
        ease 1.0 ycenter 0.655      
        repeat 
    show fang very happy: 
      .5
      block:
        easein 0.75 ycenter 0.58
        easein 0.75 ycenter 0.655      
        repeat 
    show trish shock:
      .5
      block:
       easeout 0.25 ycenter 0.62
       easeout 0.25 ycenter 0.655      
       repeat 
    show anon grin: 
      .5
      block:
        ease_cubic 0.5 ycenter 0.6
        ease_cubic 0.5 ycenter 0.655      
        repeat
    
    
    ANVL "played a rousing game of \"try to chuck your bottle through that open window\","
    
        
    stop ambient fadeout 0.5
    
    show screen forwarding
    pause 0.5   
    hide screen forwarding

    hide beer_anon
      
    
    show trish flip surprised behind reed:
         ycenter 0.655  xcenter 0.65
    show reed shocked:
         ycenter 0.655  xcenter 0.4
    show fang flip very happy:
         ycenter 0.655  xcenter 0.9
    show anon neutral:
         ycenter 0.655 xcenter 0.1
    
    
    ANVL "and in the commotion of Fang hyping up Reed to kiss Trish,"
    
    nvl hide
    
    show black:
        alpha 0.0
        linear 3.0 alpha 1.0
        
    show anon neutral:
        ycenter 0.655 xcenter 0.1
        ease_cubic 2.0 xcenter -0.2
    
    $ renpy.music.set_volume (0.1)
    
    "{w=0.20}I slip away."
    
    scene abandoned_uptosomething with Dissolve(3)
    
    show anon flip neutral at casual_move_right(0.5) with dissolve
    
    "It was time to put my plan into action."
    
    "While Reed keeps them distracted, {w=0.20}I get to work making a breadcrumb trail for him to follow."
    
    play sound anon_spray_sfx
    
    "It’s a simple plan comprising small bursts of phosphorescent spray paint to light a way out to where I’m hiding."
    
    "They’re faint but easy to follow if you know what you’re looking for."
    
    "Eventually Reed will coax the girls to go out and look for their missing friend, {w=0.20}then once he spots a tag he'll give them the slip and meet up with me."
    
    show anon flip grin with dissolve
    
    pause .5
    
    "Then the real fun begins."
    
    show black:
        alpha 0.0
        linear 2.5 alpha 1.0
    
    show anon flip grin:
        ease_cubic 2.0 xcenter -0.2

    stop music fadeout 2.0        
       
    "As I finish my task, {w=0.20}I take a moment to relieve myself in the bathroom I passed on the way over."

    play sound anon_bathroom_sfx
    
    
    "Nothing in here actually works, {w=0.20}but I like to think we're better than the animals."
    
    scene abandoned_mirror_1 with Dissolve(1)
    
    "I stop in front of the entrance mirror to check myself, {w=0.20}just to make sure there's nothing on my pants."
    pause 1.0
    window hide 
    show anim_mirror_ghost
    play sound ghost_bathroom_sfx volume 0.5
    
    pause 2.0
    
    scene abandoned_mirror_2
    
    pause 2.0
    
    play ambient1 "audio/effects/deepLoop.ogg" volume 1.0
    
    "{cps=1}…{cps=25}What the fuck was that?"
    
    "I rub my face and gaze back into the mirror, {w=0.20}sullied and cracked as it was."    
    
    "Maybe my eyes were just playing tricks on me?"
    
    
    scene abandoned_uptosomething 
    show anon neutral:
        xcenter 0.5 ycenter 0.655
    with fade
    
    "I pop my head back out of the bathroom and look around." 
    
    "There's no one here."
    
    "If that was Reed, {w=0.20}then his sense of direction is terrible."
    
    show black:
        alpha 0.0
        linear 2.0 alpha 1.0
    
    
    show anon neutral:
        ease_cubic 2.0 xcenter 1.2
        
        
    "Just to make sure, {w=0.20}I track my way back towards the group, with the paint as my guide." 
    
    "Their voices, {w=0.10}at first just hollow echoes on the brick, become brighter and more stable as I get closer."    
    
    stop ambient1 fadeout 0.5
    play ambient industrial_machine_ambient volume 0.8 fadein 1.0
    
    "I also start to hear a low humming noise, like some kind of machine."
    
    scene abandoned_conveyor
    
    show fang neutral:
        ycenter 0.655 xcenter 0.4
    
    show trish flip neutral:
        ycenter 0.655 xcenter 0.6
        
    show reed flip neutral:
        ycenter 0.655 xcenter 0.9  
        
    with Dissolve(3)
    
    "When I arrive, {w=0.10}Trish and Fang are sipping on their drinks and conversing about astrology."
    
    "Reed is at their side. {w}Guess he made it back before I did."

    show trish flip considering with dissolve
    
    T "Well, {w=0.25}I think my horoscopes have been pretty accurate."
    
    F "No that's the whole point, {w=0.25}they make them so vague that they'll always apply." 
    
    F "About as relevant as fortune cookies."
    
    
    show anon neutral at casual_move_left(0.2) with dissolve
    
    A "Worse, {w}at least you can eat those."
    
    show fang flip unimpressed with dissolve
    
    
    F "And where have you been?"
    
    show anon happy with dissolve
    
    A "Taking a piss."
    
    F "You must have touched something, {w}the whole place has been humming ever since you left."
    
    show anon neutral with dissolve
    
    A "Wasn’t me, {w}literally just went to piss."
    
    show fang flip happy with dissolve
    
    F "Eh, you must have bumped something and didn’t notice."
    
    A "I bumped into nothing." 
    
    show anon grin
    
    A "Maybe it was a ghost."
    
    
    show trish flip unimpressed
    
    T "Hilarious, {w=0.20}this better not be another of your dumb jokes."
    
    show anon shrug
    
    "I see my opportunity and strike."
    
    A "Alright fine, {w=0.20}how about we find out what it is then?"
    
    A "If it's not a ghost, then there shouldn't be a problem."
    
    show fang flip considering with dissolve
    
    F "Ok, {w=0.20}now I know you're bullshitting me."
    
    F "Fine then, {w=0.20}we're out of beer anyway. {w=0.40}Let's go find this \"ghost\" of yours."
    
    show fang flip considering:
        ycenter 0.655 xcenter 0.4
        easeout 0.5 xcenter 0.1
        easeout 0.5 ycenter 1.0
    
    
    pause 0.5
    play sound "audio/effects/carKick2.ogg"
    hide fang with dissolve
    
    pause 1.0 
    
    show anon flip happy with dissolve

    A "That's the spirit!"  

    scene black with Dissolve(2)
    $ renpy.music.set_volume(1.0)
    play music mystery_bgm fadein 1.0 
    
    "The rest of us join her {w=0.10}and we begin our search throughout the building." 
    
    
    scene abandoned_somewhere
    with Dissolve(3)
    
    play sound "audio/effects/cameraShutterClick.ogg"
    show screen anon_camera 
    
    "The noise seems to get louder and quieter as we walk around, {w=0.25}seemingly at random."
    
    "I fall back a bit and whisper to Reed."
    
    show reed flip neutral at chill_move_right(0.5) with dissolve
    
    A "I appreciate the initiative dude, {w=0.20}but we're going a bit off script now."
    
    Re "What are you talking about?"
    
    A "The noises. {w=0.40}I don't know if you planted a speaker somewhere or actually found something operational, {w=0.10}but we're going to have to improvise."
    
    A "So how about this, {w=0.40}when we reach the line I'll-{nw}"
    
    Re "I thought that was you, dawg."
    
    "I stop in my tracks."
    
    A "What?"
    
    show reed flip unimpressed with dissolve
    stop music fadeout 5.0
    
    Re "I said that wasn't me. I was about to ask you the same question; {w}I didn't remember that part of the plan."
    
    A "Then what the hell were you doing while I was away?"
    
    Re "I was with the girls, man. {w}I don't know what to tell you."
    
    Re "Was that really not you {w=0.10}or is this some extra layer you're adding?"
    
    "I felt a chill run up my spine."
    
    "If it wasn't Reed, then..."
    stop ambient fadeout 1.0
    
    pause 1.0
    
    show reed flip shocked
    
    pause 2.0
    
    
    "Reed and I exchange nervous looks."
    
    A "Hey guys, {w=0.25}maybe we should call it a night."
    
    "The girls turn back around to face me."
    
    play music mystery_bgm fadein 0.5
    show trish flip neutral at rushed_move_right(0.6)
    show fang flip unimpressed at insecure_move_right(0.8)
    with dissolve
        
    show reed flip neutral:
        ease 1.0 xcenter 0.4 

    "I put a hand on my neck."
    
    A "This place might not be as empty as we thought." 
    
    "She scoffs at me."
    
    F "Anon you can't seriously believe there's a ghost here."
        
    show fang flip surprised behind trish:
        xzoom 1.0
        pause .5
        xzoom -1.0 
        pause .5
        xzoom 1.0
        
    pause 1.5
    
    show fang flip surprised:
        xzoom -1.0

    F "Hey, that noise just stopped."  

    A "See! {w=0.20}I told you that wasn't me!"
    
    A "Now let's split before we get busted or worse."
    
    show fang flip happy with dissolve
    
    F "Alright! {w=0.20}This is more like it!"
    
    F "You plant something with a remote control?" 
    
    "She grins."
    
    F "Or maybe your plan just went up in smoke and you're trying to save face."
    
    F "Either way, {w=0.20}I'm not about to let you get off that easy."
    
    F "Let's go find this \"ghost\" of yours."
    
    
    show trish indignant with dissolve
    
    T "I don't know Fang, {w=0.25}I think he's serious."
    
    show fang happy 
    with dissolve 
    
    F "Are you in on it too? {w=0.40}What skeleton did he dig up to make that miracle happen?"
    
    show trish considering
    show fang happy:
        easein 2.0 xcenter -0.2
        
    "She turns and marches through the halls with renewed vigor."
    
    F "Now I've got to see it."

    scene black with Dissolve(2)    

    "We follow her around the building for what feels like hours."
    
    "Checking room after room with nothing to show for it."
    
    "Any attempt to persuade her just bolsters her confidence in my involvement."
    
    "Eventually, {w=0.25}we're back to searching on the main floor."    
    
    show abandoned_atrium
    show fang flip unimpressed:
        ycenter 0.655 xcenter 0.5
    with Dissolve(3)
    
    A "I think that's everything Fang, {w=0.20}nothing left to see."
    
    A "Can we go now?"
    
    F "No way, {w=0.20}there must be something I missed."
    
    show fang flip unimpressed:
        easein 2.0 xcenter -0.2
        
    scene black with Dissolve(2)

    pause 1.0
    
    scene abandoned_door with fade
    
    "Suddenly, {w=0.20}she stops in front of a small door on the side of the hall." 
    
    "It's so inconspicuous we must have passed it a half dozen times already."
    
    show fang flip neutral at insecure_move_right(0.6)
    
    F "We didn't check in here did we?" 
    
    
    play sound fang_attempt_door_sfx
    show fang flip neutral:
        easein 0.25 xcenter 0.55
        pause .25
        easein 0.25 xcenter 0.6
        
        
    "Before anyone can answer she grabs the handle only to find it locked." 
    
    F "Bingo, {w}you're so busted now."
    
    A "If it's locked, {w=0.25}there's probably a good reason."
    
    show trish flip neutral at rushed_move_right(0.8)
    show reed flip sad at chill_move_right(0.95) behind trish
    with dissolve
    
    show trish flip indignant    
    
    T "For once I agree with the skinnie, {w=0.20}I'm tired." 
    
    T "Come on Fang, {w=0.20}let's go home."
    
    F "I can't believe you guys."
    
    F "If you're going to pull a prank, {w=0.20}you could at least have the decency to see it out to the end."
    
    show fang flip neutral:
        easein 0.25 xcenter 0.55
    
    "She takes out her wallet and employs the same trick she used to use on the school roof door."
    
    play sound fang_lockpick_sfx
    
    "Our pleas do nothing to dissuade Fang from clicking the door handle and pushing it open."
    
    play sound fang_door_opened_sfx
    $ abandoned_door_opened = True
    
    "The hinges make a horrible creaking sound {w=0.20}and stagnant, {w=0.20}metallic air flows from the basement."
    
    "A dilapidated staircase plunges into an inky abyss below, {w=0.20}leaving everything to the imagination."
    
    show trish flip annoyed
    show fang flip neutral:
        easein 0.25 xcenter 0.5
    
    hide fang with dissolve
    
    "Without hesitation, {w=0.20}she steps inside its gaping maw and within moments, {w=0.20}the darkness envelops her completely, {w=0.20}leaving only the shrinking echoes of her boots against the steps as proof that she was there at all."

    "I throw a quick glance towards Reed and Trish, {w=0.25}they appeared to share my sentiments, {w=0.25}but were unsure how to proceed."
    #[start a camera zoom into the door]
    camera:
        ycenter 0.5 xcenter 0.5
        linear 15 zoom 2
    "I switch on my flashlight, {w=0.25}and without a moment to lose, {w=0.25}I swallow my fear and follow her into the depths below."
    jump bitn_Chapter3
    
label bitn_fooly_cooly_preintro:
    stop music fadeout 2.0
    $ quick_menu = False
    play ambient2 static_noise_sfx fadein 2.0
    scene anim_static_fc
    with Dissolve(2)
    pause 3.0
    
    stop ambient2 fadeout 3.0
    play ambient fc_electricity_ambient fadein 3.0 volume 0.6
    play ambient1 fc_thunder_ambient fadein 3.0
    play music fc_bgm  fadein 3.0 volume 1.2   
    
    
    
    show background_lightning_fc behind anim_static_fc:
        matrixcolor BrightnessMatrix(0.0)
        pause 2.0
        matrixcolor BrightnessMatrix(0.4) 
        pause .25
        matrixcolor BrightnessMatrix(0.0)
        pause 1.5
        matrixcolor BrightnessMatrix(0.4) 
        pause .30
        matrixcolor BrightnessMatrix(0.0)
        pause 2.5
        matrixcolor BrightnessMatrix(0.4) 
        pause .25
        matrixcolor BrightnessMatrix(0.0)
        pause 2.0
        matrixcolor BrightnessMatrix(0.4) 
        pause .20
        matrixcolor BrightnessMatrix(0.0)
        pause 0.1
        matrixcolor BrightnessMatrix(0.4) 
        pause .25
        repeat
    
    show wall_fc behind anim_static_fc
    show table_fc behind anim_static_fc

    show puppet fc neutral behind table_fc:
        ycenter 0.55 xcenter 0.48
        
         
    hide anim_static_fc with Dissolve (3)
    
    pause 1
    
    camera:
        ycenter 0.5 xcenter 0.5
        linear 35 zoom 2.0
    $ quick_menu = True
    "Ghouls… {w=0.40}goblins… {w=0.40}monsters, {w=0.60}oh my!"
    
    "Welcome to Fooly Cooly’s{w=0.60}  {b}CREATURE{w=0.60} FEATURE{w=0.60} SHOW{/b}!"
    
    show puppet fc point up with dissolve
    
    "Don’t move,{w=0.20} don’t scream! {w}You’re watching channel 69’s Halloween eve movie marathon!"
    
    "I'm your host, {w=0.40}your ghost host, {w=0.40}with the most, {w=0.60}Dr. Fooly Cooly!"
    
    "I will be with you…{w=0.60 }until{w=0.30} the end!{w=0.50} MUAHAHAHAHA!"
    
    show puppet fc point out with dissolve
    
    "Don’t touch that dial!"
    
    stop ambient1
    show background_lightning_fc:
        matrixcolor BrightnessMatrix(0.0)
    
    stop ambient fadeout 3.0
    stop music fadeout 3.0 
    play sound fc_cackle_sfx volume 1.2
    scene black with Dissolve(2)
    pause 2
    camera:
        ycenter 0.5 xcenter 0.5
        zoom 1
    jump bitn_snootjam_storyline_1
            
label bitn_menu_label:
   show grey onlayer overlay: #tried to be fancier here with no reason, lol
       blend "add" alpha 0.0
       easein 1.0 alpha 0.90
       ease 3.0 alpha 0.0
   
   $ quick_menu = False    
   play music bitn_menu_theme fadein 0.5
   call screen bitn_menu with Dissolve(4.0, time_warp=_warper.easein)
