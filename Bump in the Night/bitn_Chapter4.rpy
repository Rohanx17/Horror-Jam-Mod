label bitn_Chapter4:

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
    "Slowly I regain consciousness, {w=0.25}my body sore and immobile as my eyes adjust."
    
    "I'm tied to a chair in a modest concrete room."
    
    "At the other end is a small table, {w=0.25}where two bored-looking goons sit playing cards under the dingy light of a flickering bulb."        

    A "Fang?" 

    A "Is that you?" 
    
    F "yes, {w=0.25}thank God you're ok."
    
    "I see Fang on my left and we exchange worried looks. {w}The others are here too, {w=0.25}looks like Reed’s been roughed up pretty bad."
    
    A "Where are we?"
    
    T "We don't know."
    
    "The pair take notice of our conversation."
    
    show short goon neutral:
        matrixcolor TintMatrix ('#364259')* ContrastMatrix(0.0)  
        easeout_quint 2.0 matrixcolor TintMatrix ('#f7f7f7')* ContrastMatrix(1.0)  
        
    G1 "Hey, {w=0.25}looks like our guests are finally awake. {w}Let's get this show started."
    
    show tall goon neutral:
        matrixcolor TintMatrix ('#364259')* ContrastMatrix(0.0)
        easein_quint 2.0 matrixcolor TintMatrix ('#f7f7f7')* ContrastMatrix(1.0)  
    
    G2 "Just when you're about to lose, {w=0.40}how convenient."
    
    stop ambient1
    "He waves his hand dismissively and sighs."
    
    G1 "Keep the pot for all I care, {w=0.25}just go get my tools." 
    
    G1 "We have a job to do."
    
    play sound card_gather
    
    "The taller one rolls his eyes before scooping the change off the table and into his coat pocket,{nw}" 
    
    show tall goon neutral:
        xcenter 0.325 
        easein_quint 3.0 xcenter 1.2
    
    "The taller one rolls his eyes before scooping the change off the table and into his coat pocket,{fast} {w=0.25}then shuffles {nw}"
    play sound doorOpenClose
    extend "off through one of the doors." 
    
    hide tall goon
    
    show short goon neutral:
        zoom 0.5 xcenter 0.65 ycenter 0.6 matrixcolor TintMatrix ('#f7f7f7')* ContrastMatrix(1.0)  
        easeout_quint 1.5 xcenter 0.5 ycenter 0.655 zoom 1.0 
    
    "The short one gets up to face us,"
    
    show short goon grin:
        xzoom -1.0 xcenter 0.5 ycenter 0.655 zoom 1.0
    
    "The short one gets up to face us,{fast} his tired expression shifts into a beaming grin as he locks eyes with ours."
    
    G1 "Welcome to our humble little abode!"
    
    G1 "My name is Paulie{w=0.25} and that was my associate Bruce, {w=0.25}and we'll be your hosts for tonight's entertainment."
    
   # $ G1_Name = 'Paulie'
   # $ G2_Name = 'Bruce'
    
    F "Where the hell are we?"
    
    G1 "Sorry kid but we'll be asking the questions here. {w=0.30}Starting with who you all are, {w=0.20}and who sent you."
    
    Re "Nobody man, {w=0.20}we don't know anything about this."
    
    pause 1.0
    show short goon neutral
    
    G1 "Well that's very unfortunate to hear..."

    show short goon neutral:
      easeout 1.5  zoom 0.5 xcenter 0.65 ycenter 0.6 xzoom -1.0

    pause 1  

    show short goon grin:
         easeout_quint 1.5 xcenter 0.5 ycenter 0.655 zoom 1.0 
    
    "He picks up my video camera off the table."
    
    G1 "Because {i}SOMEONE{/i} {w=0.20}thought it was a real good idea to break into our hidden depot, {w=0.20}and get every last detail on tape."
    
    G1 "Y'all were real desperate to make sure it got out too. {w=0.40}Now the boss wants to know who out there is stupid enough to fuck with him."
    
    show short goon grin
    
    G1 "And we intend to find out by {i}any means necessary{/i}."
    
    pause .5
    
    hide tunnel_vision onlayer screens
    camera:
      blur 0        
    
    
    show short goon neutral with dissolve
    
    A "We're telling the truth! {w=0.20}We're just some teens who wandered in here for fun, {w=0.25}we don't work for anybody."
    
    show short goon grin
    
    G1 "Come on kid, {w=0.25}you can do better than that. {w}The place is locked down like a bomb shelter, {w=0.30}no one just stumbles in there by accident."
    
    show tall goon neutral behind short:
        xzoom -1.0 ycenter 0.655 xcenter 1.2 zoom 0.5 
        easein_quint 2.0 xcenter 0.65
    
    show short goon grin:
        xcenter 0.5
        pause 1.0
        easeout_quint 1.0 xcenter 0.3 ycenter 0.655 
    
    pause 1.0
        
    "The taller goon comes back{nw}"
    play sound tableDrop
    extend " and drops a large leather wrapping on the table."
    
    "It looks kinda like that thing they hold surgical equipment in."

    G1 "Since none of you feel like doing this the easy way, {w=0.25}we'll just have to do it our way."

    "He unrolls it and we all quietly gasp. {w}Knives, {w=0.30}scissors, {w=0.30}a ballpoint hammer, {w=0.30}and a collection of other tools are laid out in horrific fashion."     
    
    G1 "Alright Pink, {w=0.25}how about we start with you?"
    
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
    
    G1 "So me and you are going to play a little game see? {w}I'm gonna ask you a question, {w=0.25}if you tell me something useful, {w=0.25}maybe you and your friends will get to wake up tomorrow."
    
    "He picks up a knife, {w=0.25}artfully spinning it through his fingers."
    
    G1 "Try to bullshit me..."
    
    play sound tableKnife
    
    "He catches the knife and slams the blade into the table."
    
    G1 "Let's just say you ain't gonna like the prize we have in store."
    
    show reed sad with dissolve
    stop ambient fadeout 0.5
    play music torture_p1 fadein 0.5
    
    "We all gulp, {w=0.25}a look of dread creeps across Reed's face."
    
    G1 "Now let's begin."
    
    "He looks over at us."
    
    G1 "And of course, {w=0.20}if you don't like what you see, {w=0.25}the audience is always free to answer for him."
    
    show short goon neutral with dissolve
    
    "His smile evaporates as he turns back to Reed and stares him down."
    
    G1 "Now question number one: {w=0.40} Who exactly do you work for?"
    
    
    menu:
        
        "Plead ignorance":
         Re "Please {w=0.30}we don't know anything, {w=0.25}let us{nw} g-AHHHH!" 
         
         show tall goon neutral:
          linear 0.5 xcenter 0.4

         pause 0.2

         show tall goon neutral:
          linear 0.5 xcenter 0.3

         show reed shocked:
            ycenter 0.655
            ease 0.25 ycenter 0.68
            #ease 0.5  ycenter 0.63 
            #ease 0.5  ycenter 0.68 
            ease 0.25 ycenter 0.63   
            ease 0.25 ycenter 0.655
        
         play sound "audio/effects/sizzle.ogg"
         #queue sound ouch         
         
         Re "Please we don't know anything, let us{fast} g-AHHHH!" 
         
         show reed sad
         
         pass
         
        "Prove innocence":
         "Reed looks ready to puke as his nerves run overtime, {w=0.30}thinking of what he could possibly say to placate the villain."
         
         Re "We're telling you the truth I swear! {w=0.40}We don't work for anybody!" 
         
         show reed shocked
         
         "His face lights up."
         
         Re "Check the cam footage you'll see!"
         
         show short goon grin
         
         G1 "Oh don't you worry, {w=0.30}we've given your little home movie a good look over."
         
         G1 "Y'all seem to be searching real hard for something, {w=0.20}until suddenly, {w=0.20}you're showing off our product like you're the home shopping network." 
         
         G1 "Care to explain?"
         
         show reed unimpressed
         
         Re "...uh, {w=0.30}well, {w=0.50}I think she was looking for a ghost or someth-{nw}"
         

         show tall goon neutral:
          linear 0.5 xcenter 0.4

         pause 0.2

         show tall goon neutral:
          linear 0.5 xcenter 0.3
         
         show reed shocked:
            ycenter 0.655
            ease 0.25 ycenter 0.68
            #ease 0.5  ycenter 0.63 
            #ease 0.5  ycenter 0.68 
            ease 0.25 ycenter 0.63   
            ease 0.25 ycenter 0.655
         
         play sound "audio/effects/sizzle.ogg"
         #queue sound ouch
         
         Re "...uh, well, I think she was looking for a ghost or someth-{fast}AHHHH!"
         
         show reed sad
         
         show short goon neutral
         
         pass 
            
        "Antagonize":
            
         show reed angry with dissolve

         Re "Are you deaf? {w=0.20}We don't work for anyone! {w=0.30}How many times do-{nw}" 
         

         show tall goon neutral:
          linear 0.5 xcenter 0.4

         pause 0.2

         show tall goon neutral:
          linear 0.5 xcenter 0.3
         
         show reed shocked:
            ycenter 0.655
            ease 0.25 ycenter 0.68
            #ease 0.5  ycenter 0.63 
            #ease 0.5  ycenter 0.68 
            ease 0.25 ycenter 0.63   
            ease 0.25 ycenter 0.655
         
         
         play sound "audio/effects/sizzle.ogg"
         #queue sound ouch
        
        
         Re "Are you deaf? We don't work for anyone! How many times do-{fast}AHHHH!"         
            
         show reed sad
         
         
         pass            
    
    play music torture_p2 fadein 0.5
    
    "Reed yelps as the goon standing over him puts out his cig on the top of his maw."
    
    G1 "Strike one.{w} he leans back in his chair {nw}"

    play sound goon_smoke volume 0.5

    extend "releasing a cloud of smoke."

    G1 "I take it that cleared your mind a little?" 
    
    G1 "We're not screwing around kid, {w=0.40}you're going to give us what we want, {w=0.25}one way or the other."
    
    G1 "So I suggest you cooperate before I have to take more.{w=0.20}.{w=0.20}.{w=0.20} drastic measures."

    show tall goon neutral:
        xcenter 0.3
        easein_quint 1.0 xcenter 0.35

    "He looks over to his companion, {w=0.20}who nods back. {w=0.30}And without a moment's hesitation, {w=0.20}grabs the tuft at the end of Reed's tail."
    
    T "Get your hands off him! {w=0.50}Fangs dad is a cop{w=0.30} a-{w=0.20}and you lay a finger on us he'll make you wish you were never born!"
        
    F "Trish, shut up!"
    
    show short goon grin
    
    G1 "Oh is he now? {w}Well now we're getting somewhere." 
    
    G1 "Had a feeling you might be with the cops; {w}no way the other families would muscle in on our turf so openly."
    
    
    show short goon neutral:
        xcenter 0.7
        easeout_quint 1.0 xcenter 0.6
    
    "He leans back into Reed's face."
    
    G1 "Question two: {w}So are you kids a bunch of fresh recruits?" 
    
    G1 "If so, {w=0.30}were you out here looking for evidence? {w=0.30}Or something more?" 
    
    G1 "How much do your superiors already know about our operation?"
    
    
    menu:
        
        "Deny everything":
            Re "We don't work for the cops or anyone man I swear! {w=0.40}We're just a bunch of dumb teens in way over our heads! {w=0.30}You have to believe me!"
            
            "The goon sighs and shakes his head."
            
            G1 "Strike two."
            
            pass
            
        "Beg for life":
            "Reed's face is completely enveloped in fear, {w=0.30}I doubt ours are any better."
            
            Re "Please, {w=0.20}I promise we'll do anything you want! {w}You can destroy the tape a{w=0.15}-a{w=0.15}-and we won't tell anybody what we saw tonight. {w=0.30}I swear!" 
            
            Re "We'll do whatever you want man just let us go..."
            
            "The goon sighs and shakes his head." 
            
            G1 "Strike two."

            pass
            
        "Strike a deal":

            show reed neutral with dissolve

            "Suddenly Reed's face relaxes a little, {w=0.20}like he's found a way to bail us out of this."

            Re "I got nothing man, {w=0.20} we've told you all everything." 
            
            Re "Since we know too much already, {w=0.20}why don't we join up?{w= 0.4} We're not cops and we'd be happy to prove it."            
            
            $ renpy.music.set_volume(0.2,delay=0.5,channel='music')
            
            pause .5
            
            play sound af_wtf
            
            AnonAndFang "{size=50}{b}WHAT!?"
            
            T "..."
            
            $ trish_extended_dialogue = True
            
            show short goon grin with dissolve
            
            "The goon slaps the table and laughs, {w=0.25}then looks at his friend while pointing at Reed."
            
            G1 "You know, {w=0.25}I'm starting to like this one."
            
            "He turns back to Reed."
            
            G1 "Ya got balls kid, {w=0.25}I'll give you that."
            
            G1 "Truth be told, {w=0.25}we're always short-handed around here." 
            
            G1 "But unfortunately for you, {w=0.25}orders are orders."
            
            $ renpy.music.set_volume(1.0,delay=0.5,channel='music')
            
            show short goon neutral with dissolve
            
            G1 "More importantly, {w=0.25}that's NOT what I asked you"
            G1 "strike two."
            
            
            
            pass            
    
        "Antagonize":
            
            "Without hesistation,{nw}"
            play sound reed_spit
            
            show reed angry:
                xcenter 0.4
                ease 0.25 xcenter 0.35
                ease 0.5 xcenter 0.4
                
            
            show short goon neutral:
                xcenter 0.6
                pause .5
                easeout_quint 0.25 xcenter 0.65
            
            "Without hesitation,{fast} {w=0.25}Reed hawks a loogie into the goon's face."
                
            
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
    
    
    "The taller one takes a handful of the feathers, {w=0.20}and with a quick jerk, {w=0.25}{nw}"
    
    play sound goon_ripout    
    #queue sound short_scream
    
    
    show reed shocked:
        ycenter 0.655
        0.5
        parallel:
         .5
         ease 0.02 ycenter 0.68
         ease 0.04 ycenter 0.63
         ease 0.04 ycenter 0.68
         ease 0.04 ycenter 0.63
         ease 0.04 ycenter 0.68
         ease 0.04 ycenter 0.63
         ease 0.04 ycenter 0.68
         ease 0.04 ycenter 0.63
         ease 0.02 ycenter 0.655
         
        
        
        parallel:
         matrixcolor TintMatrix('#f7f7f7')
         1.0
         matrixcolor TintMatrix('#e0b6b6')
         1.0
         repeat       
    
    "The taller one takes a handful of the feathers, {w=0.10}and with a quick jerk, {fast}rips them out at the root."
    
    "Reed screams in agony, {w=0.30}staring at the ceiling as he squirms against his restraints." 
    
    "Blood started to drip from the missing section of the pattern." 
    
    "Fang stares agape in abject horror, {w=0.25}Trish starts to cry."
    
    show reed sad
    
    G1 "Ready to talk yet?"

    "Reed is breathing heavily as he wrestles with the pain." 

    G1 "Let me tell you what I think."
    
    show short goon neutral:
        easeout_quint 1.5 xcenter 0.7
        
        
    play sound chair_creak
    
    "The goon lays back in his chair again."     

    G1 "My guess is you're a bunch of rookies who got a hot tip and are operating off the books."
    
    show short goon grin 
    
    G1 "Hell, {w=0.4}there might not even be another living soul who knows where you went tonight."
    
    G1 "There's no one coming for ya, {w=0.25}and you'll be dog food by the time people start asking questions." 
    
    show short goon neutral
    
    G1 "We've made plenty of young fools disappear, {w=0.20}don't think we can't do the same with you."
    
    show short goon neutral:
        xcenter 0.7
        easeout_quint 1.0 xcenter 0.6
        
    "The goon sits back up and picks out a long, thick butcher knife from his cavalcade of carnage and eyes it longingly. "
    
    G1 "So taking that into account, {w=0.25}I hope you have the prudence to choose your next words very carefully {w=0.25}because, as I'm sure you are now aware,"
    G1 "I don't give second chances."
    
    "The taller one grabs Reed's arm and holds it out in place." 
    
    show short goon neutral with dissolve
    
    play ambient knife_sharpening
    
    "The other takes the knife and dances it across Reed’s fingers. "
    
    G1 "So I'll ask you one more time: {w}Who are you kids?"
    
    menu: 
      "Please...":
        "Thick streams of tears streak across a face full of despair. "
        
        Re "{cps=10}Please.{w=0.25}.{w=0.25}.{w=0.25}{cps=50}we don't know anything, {w=0.25}you have to believe me..."
        
        "The goon stares into him unflinchingly."
        
        G1 "Is that your final answer?"
        
        show reed considering
        
        Re "{cps=10}{b}.{w=0.25}.{w=0.25}.{w=0.25}Please..."
        
        
        pass
          
      "Try to save friends":
        pause 1.0
        show reed sad: 
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

        Re "“{cps=10}.{w=0.25}.{w=0.25}.{w=0.25}{cps=50}Do whatever you want with me, {w=0.30}but please don't hurt my friends."
        
        Re "This is all my fault."
        
        Re "I'll do or say whatever you want, {w=0.25}but {cps=10}please.{w=0.25}.{w=0.25}.{w=0.25}{cps=50} just let my friends go..."        
            
        "The goon stares into him unflinchingly."
        
        G1 "Is that your {w=0.10}final answer?"
        
        Re "{cps=10}.{w=0.25}.{w=0.25}.{w=0.25}Please..."
        
        
        pass
      
      
      "Antagonize":
        
        show reed unimpressed
        
        "Reed laughs quietly to himself."
        
        Re "Why answer if you're not gonna listen?"
        
        Re "You get off on this don't you? {w=0.3}You sick fuck..."
        
        "The goon stares into him unflinchingly."

        G1 "Is that your {w=0.10}final answer?"
        
        Re "{cps=10}{b}.{w=0.25}.{w=0.25}.{w=0.25}Bite me..."
        
        pass  
    
    stop music fadeout 2.0

    show short goon neutral ec
       
    "The goon closes his eyes and takes a deep breath."
    
    show black:
        alpha 0.0
        linear 2.0 alpha 1.0

    stop ambient fadeout 0.5
    
    pause 3.0
    
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
         ease 0.015 ycenter 0.63
         ease 0.03 ycenter 0.68
         ease 0.03 ycenter 0.63
         ease 0.03 ycenter 0.68
         ease 0.03 ycenter 0.63
         ease 0.03 ycenter 0.68
         ease 0.05 ycenter 0.63
         ease 0.05 ycenter 0.68
         ease 0.05 ycenter 0.63
         ease 0.05 ycenter 0.68
         ease 0.08 ycenter 0.63
         ease 0.08 ycenter 0.68
         ease 0.08 ycenter 0.63
         ease 0.08 ycenter 0.68
         ease 0.04 ycenter 0.655
       
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
    
    "As soon as the finger hits the table, {w=0.30}the taller goon pulls out a roll of gauze and wraps up the stub to stem the bleeding."
    
    "The girls let out an involuntary shriek."
    
    F "What the fuck is wrong with you!?"
    
    show short goon angry
    
    G1 "Pipe down, {w=0.30}or I'll stuff it down your throat!"
    
    "That quickly shut them up, {w=0.20}and soon only muffled sniffling could be heard."
    
    show short goon neutral
    
    G1 "One down nine to go, {w=0.50}ya ready to talk now?"
    
    menu:
      "...":
         pass 
      "...":
         pass
      "...":
         pass
    
    "..."
    show reed sad
    
    pause 1.0
    
    "Reed head is held low, as he tries to cope with the pain as best he can."     
         
    Re ".{w=0.20}.{w=0.20}.{w=0.20}don't know anything.{w=0.20}.{w=0.20}.{w=0.20}I swear..."      
    
    show short goon angry with dissolve
    
    "The goon merely rolls his eyes with a growing look of frustration." 
    
    G1 "Loyal to the end, eh?"
    
    G1 "Fine then, {w=0.30}we can do this {i}all{/i} night."
    
    show short goon angry:
        xcenter 0.6
        easeout_quint 0.5 xcenter 0.5
        easeout_quint 0.5 xcenter 0.6
    
    show black:
      linear .5 alpha 1.0

    pause .5
    
    play sound goon_fingerchop
    
    

    pause 1

    show black:    
        linear 1.5 alpha 0.0
    
    "{b}THWACK{nw}"
   
    
    show reed shocked:
        ycenter 0.655 alpha 0.85
        parallel:
         ease 0.025 ycenter 0.68
         ease 0.05 ycenter 0.63
         ease 0.05 ycenter 0.68
         ease 0.08 ycenter 0.63
         ease 0.08 ycenter 0.68
         ease 0.08 ycenter 0.63
         ease 0.08 ycenter 0.68
         ease 0.05 ycenter 0.63
         ease 0.05 ycenter 0.68
         ease 0.05 ycenter 0.63
         ease 0.05 ycenter 0.68
         ease 0.05 ycenter 0.63
         ease 0.05 ycenter 0.68
         ease 0.04 ycenter 0.655
        
        parallel:
         matrixcolor TintMatrix('#e0b6b6')
         0.25
         matrixcolor TintMatrix('#f7f7f7')
         0.25
         repeat 
    
    "Another finger drops to the table, {w=0.30}Reed's body spasms like a beheaded chicken, {w=0.30}but there's no verbal response. "
    
    "The girls have completely broken down, {w=0.20}pleading on deaf ears for the safety of their friend." 
    
    "I sit there paralyzed in shock, {w=0.20}barely able to process what's going on around me, {w=0.30}it feels like I'm in a dream."
    
    show reed sad
    
    "Trapped in a nightmare I know I'll never wake up from."
    
    G1 "We can stop this at any time you know, {w}all you have to do is say the word."
    
    Re "..."
    
    show short goon neutral
    
    G1 "{cps=10}...{cps=50}Hey pal, you still in there?"
    
    "Reed just sits there with a vacant expression, {w=0.30}the light extinguished from his eyes." 
    
    #play sound end_groan
    
    "His feeble breath the only sign he was still living."
    
    show tall goon neutral:
        xcenter 0.35
        easein_quint 3.0 xcenter 0.4
    
    G2 "If this ain't exciting enough for you anymore, {w=0.30}I can go get the drill-{nw}"
    
    "The shorter one waves his hand dismissively."
    
    G1 "Eh, {w=0.20}don't bother. {w=0.40}I've been in the business long enough to know this one’s a lost cause."
    
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
    
    "He saunters over, {w=0.30}leaning in to inspect us like cattle."
    
    "As he turns to Fang, {w=0.20} she quickly leans her head in {nw}" 
    
    play sound fang_bite volume 2.0
    
    show short goon neutral:
        zoom 1.0
        easeout_quint 0.25 zoom 0.9
        easeout_quint 0.25 zoom 1.0
    
    
    "As he turns to Fang she quickly leans her head in {fast}and snaps at him like a shark, {w=0.30}her face coated in pure hatred."
    
    "He pulls away just in time to avoid needing a skingraft."
    
    G1 "Whoa there, {w=0.20}looks like there's still some fight left in this one!"
    
    show short goon grin 
    
    G1 "I think, you'll do nicely."
    
    pause .5
    
    A "Please god no! {w=0.40}Take me!"
    
    G1 "If you don't want her to get hurt, {w=0.30}you're free to cooperate anytime!"
    
    show short goon neutral:
        zoom 1.0
        easeout_quint 1.0 zoom 0.7
    
    play sound fang_resist volume 1.5
    
    "He grabs her by the hair and starts pulling her over." 
    
    "I wrack my brain feverishly for something, {w=0.40}anything, {w=0.40}I could possibly say or do that could stop this."

    play sound "audio/effects/cellphone.ogg"    
   
    stop music fadeout 5.0
    play ambient lamp_buzz fadein 10.0 volume 1.0
    
    pause .25
    
    show short goon shocked
    show tall goon shocked
    
    pause .25
    
    show short goon neutral
    show tall goon neutral
   
    "The shorter goon whips out a flip phone from his pocket {w=0.30}and holds it to his ear."
    
    show short goon neutral:
      easeout 1.5  zoom 0.4

    show short goon shocked
    
    G1 "{size=*0.7}Boss!? {w=0.40}Uh, {w=0.20}yeah we’re in the middle of it now.{/size}"
    
    show short goon neutral
    
    G1 "{size=*0.7}Well, {w=0.20}not great.{/size}"
    
    G1 "{size=*0.7}I think they might be with the force, {w=0.20}but the first one was a dead end so we're not-, {w=0.60}I'm sorry it's just-,{/size}{w=0.60}{nw}"
    
    show short goon shocked
    
    G1 "{size=*0.7}I think they might be with the force, but the first one was a dead end so we're not-, I'm sorry it's just-,{fast} wait what?!{/size}"
    
    G1 "{size=*0.7}That's not necessary I've-,{/size}{w=0.60}{nw}" 
    
    show short goon neutral
    
    G1 "{size=*0.7}That's not necessary I've-,{fast} yes, {w=0.40}alright, {w=0.40}I understand.{/size}" 
    
    G1 "{size=*0.7}Will do.{/size}"
    
    play sound goon_phone
    
    pause 2.0

    show short goon neutral:
        easeout_quint 1.0 zoom 0.7

    pause 1  
    
    G1 "Good news! {w=0.30}The Boss happened to be in the neighborhood, {w=0.20}and has decided to handle the matter personally!"
    
    G1 "You should feel honored! {w=0.40}Not everyone has the opportunity to get worked over by a man of his caliber."

    show short goon grin
    
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
    
    "He and his companion laugh and head for the exit, {w=0.30}before passing through {w=0.20}he turns his head back around and points with an evil grin." 
    
    show short goon grin
    
    G1 "Now don't you kids go anywhere! {w=0.40}The main event will begin shortly!"
    
    show short goon grin:
        xzoom 1.0 xcenter 0.8
        easeout_quint 2.0 xcenter 1.2
        
    
    pause .25
    
    play sound lightSwitch
    stop ambient
    
    scene black with fade
    
    "He shuts off the light and leaves the room."
    
    "The door closes behind them with a slam,{nw}"

    play sound "audio/effects/doorSlam.ogg"

    extend" {w=0.20}leaving only the darkness and the sounds of Trish's crying."
    
    window hide
    camera:
       zoom 1.0 ycenter 0.5
    
    #play sound trish_cry
    
    pause 4.0

    F "So this is it then? {w=0.4}We're all going to die because you just couldn't keep it in your fucking pants. {w=0.4}Way to go dweeb."
    A "For christsakes are you still on about that!? {w=0.4}You were the one that wanted to push our luck tonight and get us in trouble, {w=0.25}not me."
    F "Only because of your prank, {w=0.3}which I was right about by the way!{nw}" #[have line be interrupted at end]
    play sound cornered
    T "WILL YOU TWO SHUT THE FUCK UP!"
    play music Sad fadein 2.0
    "We’re stunned into silence, {w=0.25}Trish continues barely holding it together."
    T "This is both your faults!"
    T "Anon you're always getting into trouble with your stupid antics, {w=0.25}because you never think about any of the consequences of your bullshit!"
    T "It's like you don't care what happens or who you hurt so long as you think it's fucking funny!"
    T "And Fang! {w=0.4} you're always enabling him! {w=0.4}Whenever he pushes the line on anything you're right there to cheer him on!"
    T "You're probably the most stubborn person I've ever met! {w=0.4}If you had taken even a moment to consider the thoughts of anyone besides yourself, {w=0.25}we wouldn't be here right now!"
    
    "She starts to sob again."
    
    T "What's my family going to do without me? {w=0.4}Riley sure as hell can't manage them all. "
    T "I'm never going to see any of them again and it's all YOUR FAULT! {w=0.50}The least you two could do is not spend our final moments arguing!"
   
    "We sit there quietly for awhile, {w=0.30}taking in her words. {w=0.50}As much as I hate to admit it, she's right."
   
    A ".{w=0.25}.{w=0.25}.{w=0.25}I'm sorry guys, {w=0.30}I didn't check out the place before we came, just googled haunted places in VB and took down the address. "
    A "It just seemed so perfect{w=0.25} all I could think about was the look on your faces once it was over. {w=0.40}It never crossed my mind anything like this could happen."
    F "No, {w=0.25}she's right, {w=0.40}you all were. I knew I had fucked up as soon as we found their stash I just couldn't bear to admit it."
    F "If we had just left when you asked we would have been fine, {w=0.55}god why would there even be a locked door in a place that old?"
    A "Yeah {w=0.25}but I shouldn't have been egging you on to think the place was haunted. {w=0.40}You wouldn't have felt the need to prove me wrong if I never gave you a reason too."
    F "Dammit dweeb, {w=0.25}that's bullshit and you know it. {w=0.4}I would have found some other excuse to drag us down there I'm sure."
    A "Not if I had just came clean from the start."

    "Suddenly Reed interjects, {w=0.4}his voice sullen and defeated."

    Re "No, {w=0.30}this is my fault."
    Re "I'm the one that made Anon’s plan possible and drove us there without knowing what we were getting into. "
    Re "I let Fang drag us around instead of putting my foot down and getting out of there."
    Re "I knew it wasn't a good idea, {w=0.25}but instead of doing anything about it I just stood around and watched it all happen, {w=0.25}like I always fucking do."
    pause 2.0
    Re "Christ, why am I like this?"

    A "Come on man, {w=0.25}you know that's not true. {w=0.4}We have a little time before they get back. {w=0.40}Maybe we can cook up a story they'll buy?"

    "Reed laughs cynically."
   
    Re "You really think they're going to let us go at this point? {w=0.4}We were fucked the second they caught us. {w=0.4}Sorry dude but..."
    Re "...this is it."
    
    "It takes a moment to process. Try as I might, {w=0.25}I really can't refute it. {w=0.4}I turn to Fang and whisper in her direction."
    A "I love you Fang, {w=0.2}I'm.{w=0.2}.{w=0.2}.{w=0.2} so sorry it had to end this way."
    F ".{w=0.2}.{w=0.2}.{w=0.2}Well, {w=0.3}if I have to go, {w=0.3}I'm glad I don't have to face it alone at least. {w=0.4}There's no one else I'd rather spend my last moments with than my dweeb."
    "Her confession warms my heart, {w=0.3}and I reach out my hand to find hers."
    "We connect, {w=0.30}the warmth of her scales now the only light I have in this desolate place."
    A "Me neither. {w=0.4}One last kiss for the road?"
    F "Sure."
    "I crane out my neck until I bump into her snoot. {w=0.4}We're only just barely able to close the distance, {w=0.2}but I’d say it was the best one I'd ever had."
    "As I pull my head away I can hear footsteps off in the distance, {w=0.2}squeezing her hand tighter as I do. {w=0.4}If it has to end here then so be it."
    "Honestly, {w=0.2}until I met Fang I wasn't expecting I'd make it that far anyway."
    "At least now I can die knowing what it meant to live." 
    stop music fadeout 2.0
    #[play a door opening sound]
    play sound doorOpening

    "We hear the door swing open and a horrible booming voice echoes across the room."
    goon "Alright ya maggots! {w=0.4}My men tell me you thought you could interfere with one of my operations {w=0.2}and live to tell about it!" 
    goon "Now spill or I'm going to beat your faces in so badly your own motha won't recognize ya!"
    "We're all speechless as the figure takes command of the room, {w=0.25}we brace ourselves for what's to come."
    goon "Hey one of youse get the lights {w=0.1}I'm not a bat!"
    "The lights flicker back on {w=0.1}and I can hardly believe my eyes."

    #[fade into the interrogation room, moe is in to the middle and the two goons are behind him, all neutral, fade in the moe theme]
    scene tortureRoom
    show short goon neutral flip:
        xcenter 0.75
    show tall goon neutral flip:
        xcenter 0.25
    show moe neutral flip:
        xcenter 0.6
    with Dissolve(2)
    play music venetianValues fadein 1

    "It's Moe, {w=0.2}Uncle Moe, {w=0.3}so long as my eyes aren't playing tricks on me. {w=0.4}The second he notices it's us he freezes."

    #[switch moe to Shocked]
    show moe shocked flip with dissolve

    "His face goes pale{nw}"
    play sound pipeDrop
    extend " and he drops the iron rod he was beating across his palm."
   
    "The metal clang against the floor quickly swallowed by our incredulous silence."
    Moe "Lucy, {w=0.4}is that you?"
    F "...Uncle Moe!?"
    "He grabs his head and I can see the years of his life peel off though his worried expression, {w=0.2}quietly cursing to himself."

    #[turn moe right and have him exit stage right, when he passes short goon he moves with moe off screen still facing left and changed to shocked]
    show moe
    with dissolve
    show moe:
        easein 2.0 xcenter 0.85
    pause 2
    show short goon shocked flip
    with dissolve
    pause 0.5
    show moe:
        ease_cubic 4.0 xcenter 1.55
    show short goon shocked flip:
        ease_cubic 4.0 xcenter 1.5
    with None
    show tall goon neutral
    with dissolve
    show tall goon neutral:
        easein 3.5 xcenter 0.75
    pause 4

    "He turns around and grabs the shorter goon by his collar, {w=0.2} and promptly drags him into a nearby room."

    #[switch moe to neutral and move him just enough on screen right side to see most of his head]
    show moe neutral flip:
        easein 1 xcenter 0.95 rotate -15
    pause 1

    Moe "One moment please."

    #[move moe back offscreen, play door slam sound loud]
    show moe neutral flip:
        easein 1 xcenter 1.5 rotate 15
    pause 1
    play sound doorSlam
    $ renpy.music.set_volume(0.10,delay=0.5,channel='music')
    hide moe neutral flip
    hide short goon shocked flip

    #[lower the moe theme volume, and run the shouting loop, play some of the banging sounds as they feel fitting with what’s playing, then once it feels right cut the shouting loop and play gunshot sound at least once, or a grouping whatever sounds good, switch tall goon to shocked]
    play ambient arguing loop volume 4
    pause 9
    play sound bangCrash volume 0.5
    pause 5
    play sound crash1 volume 0.5
    pause 4
    play audio crash2 volume 0.5
    play audio woodCrash volume 0.5
    pause 5
    play audio woodCrash volume 0.5
    pause 0.2
    play audio pipeDrop volume 0.5
    play audio doorSlam volume 0.5
    pause 0.6
    play audio stairCrash volume 0.5
    stop audio
    stop sound 
    
    stop ambient
    stop voice
    play sound pistolFire
    pause 1
    show tall goon shocked
    with dissolve
    play audio pistolFire
    pause 0.6
    play audio pistolFire
    pause 0.6
    play audio pistolFire
    pause 0.6
    stop music fadeout 1
    "Suddenly the room goes quiet.{w} We're all stunned in silence."

    #[bring moe theme to full volume, have stained neutral moe enter stage right facing left to the middle in front of tall goon]
    play music venetianValues fadein 1
    $ renpy.music.set_volume(1,delay=0.5,channel='music')
    show moe neutral bloodstain flip:
        xcenter 1.5
        easein 2.0 xcenter 0.5
    pause 2
    show tall goon shocked flip
    with dissolve

    "The door swings open, {w=0.2}and Moe strolls out towards Fang, {w=0.2}his apron covered in fresh marinara."

    #[switch moe to stained/shocked and move him closer to the camera]
    show moe shocked bloodstain flip:
        linear 1 zoom 1.5 ycenter 0.95

    Moe "Oh my little Lucy, {w=0.3}are you alright? {w=0.4}What did they do to you?"
    F "Uh.{w=0.3}.{w=0.3}.{w=0.3}I{w=0.1}-I'm alright, I think.{w=0.2}.{w=0.2}.{w=0.2}but Reed is-{nw}"

    #[move moe very close to the camera, shift sprite to stained/neutral]
    show moe neutral bloodstain flip:
        linear 1 zoom 2 ycenter 1.25

    "He picks her up {w=0.2}chair and all, {w=0.3}and squeezes for dear life. {w=0.4}The relief nearly reshapes his face."
    Moe "Oh thank God! {w=0.4}In that case, {w=0.25}I think we're all gonna make it out just fine."
    F ".{w=0.2}.{w=0.2}.{w=0.2}That's great Moe but uh.{w=0.2}.{w=0.2}.{w=0.2} Reeds hand-"

    #[moe steps back to normal distance]
    show moe neutral bloodstain flip:
        linear 1 zoom 1 ycenter 0.655

    "He puts her down, {w=0.25}and looks over at reed to assess the damage."
    Moe "Ah yes."

    #[moe faces right to tall goon]
    show moe neutral bloodstain
    with dissolve

    "He turns around and gestures at the remaining goon."
    Moe "What's your name Picciotto?"
    G2 "B-{w=0.1}B-{w=0.1}B-{w=0.1}Bruce sir."
    Moe "Alright Deuce, {w=0.25}go put the limbs on ice and take the boy downtown. {w=0.4}Ring Dr. Quale before you get there and he'll take care of the rest."
    G2 "Actually, {w=0.25}my name is-{nw}" #[do the forced text cutoff thing]
    Moe "{sc=5}DID I STUTTER?" #(use the shaky text)

    #[goon sprite moves down a little then turns right and quickly exits stage right]
    show tall goon shocked flip:
        ease_cubic 0.1 ycenter 0.6
        ease_cubic 0.1 ycenter 0.55
        ease_cubic 0.1 ycenter 0.6
        ease_cubic 0.1 ycenter 0.55
    pause 0.4
    show tall goon shocked
    with dissolve
    show tall goon shocked:
        ease_cubic 1 xcenter 1.5

    G2 "N-{w=0.1}N-{w=0.1}No sir, {w=0.25}right away, sir!"
    "With a panicked expression, {w=0.25}he leaps into action. {w=0.4}Scooping up the goods and leading a disoriented Reed away like a porcelain doll."

    #[the screen slowly fades to black, music fades out too]
    scene black with Dissolve(2)
    stop music fadeout 2
 

    "Moe wastes no time taking a knife off the table and severing our bonds, {w=0.25}once we get our bearings he leads us back into the world above."
    pause 6
    #[cut to moe car cg 1, play driving sounds loud and moe theme quiet]
    show moeCar1 with Dissolve(2)
    play music venetianValues fadein 2 volume 0.20
    play sound insideCarNoise fadein 2 volume 0.8 loop

    A "...Uh, {w=0.25}thanks again for the save Moe."
    Moe "Don't worry about it. {w=0.4}Now one more time, {w=0.25}if anyone asks what happened tonight, {w=0.25}what's the story you're going to tell them?"
    A "We were out joyriding after leaving Stella's Halloween party."
    A "Reed totaled his van and since you were nearby, {w=0.25}we called you for help." 
    A "We had a nice evening together and lost track of time before you drove us home."
    Moe "Correct."

    #////////////////////////////////////////////////////////////If the flag is triggered include this
    if trish_extended_dialogue == True:
        jump bitn_chapter4_trish_dialogue
    else:
        jump bitn_chapter4_continue

label bitn_chapter4_trish_dialogue:
    F "Man It's a good thing they didn't take up Reed's offer, I don't know we would have done."
    Moe "Well, {w=0.25}the boys were telling you the truth, {w=0.25}good help is hard to find these days."
    T  "You have an opening?"
    "Fang and I look over eyes agape."
    F "What the fuck Trish?"
    "Moe finds her outburst amusing."
    Moe "I think you're a little young to be considering this life."
    T "I'm serious."
    pause 1
    "Moe stops to think for a moment."
    pause 2
    Moe "Alright then."
    "He reaches back and hands her a small card."
    Moe "Stop by the old place when you have a chance. {w=0.4}I'm sure I can find something for you to do." #[this’ll trigger a cg in the credits where she’s washing dishes in moe’s kitchen lol]
    "The air is stained in silence until Fang breaks the ice."
    jump bitn_chapter4_continue
    #///////////////////////////////////////////////////////////////

label bitn_chapter4_continue:
    F "So.{w=0.2}.{w=0.2}.{w=0.2} you're really not going to tell mom and dad?"
    Moe "Of course not, {w=0.25}just stay out of trouble and this'll be our little secret ok?"
    T "I don't get it, {w=0.25}you're really gonna let us go, {w=0.25}just like that?"
    "He chuckles."
    Moe "Who said anything about letting you go?"
    
    #[cut the music]
    stop music fadeout 0

    Moe "In our way of life, {w=0.40}the most important thing in this world is trust."
    Moe "For the sake of my little Lucy, {w=0.25}I've chosen to trust that you kids have enough sense to not do anything foolish."
    Moe "It would be a great shame to find out that trust was.{w=0.2}.{w=0.2}.{w=0.2}misplaced."
    Moe "We know where you live after all..."
    T "But how would you know it was one of us?"
    Moe "Oh..."
    
    #[switch to moe cg 2]
    show moeCar2

    Moe "...We'll know."
    "We all gulp in unison."
    A "Not a word I promise."

    #[switch to moe cg 3]
    show moeCar3

    Moe "Good, {w=0.15}that's what I like to hear. {w=0.4}Because if this happens again, {w=0.25}then next time you won't be so lucky. {w=0.5}Do I make myself clear?"
    A "Crystal sir."

    #[switch to moe cg 1]
    show moeCar1

    Moe "Good, {w=0.25}I believe this is your stop lovebirds. {w=0.4}Have a good night and tell Ol' Rip I said hello!"
    F ".{w=0.2}.{w=0.2}.{w=0.2}Will do."
    
    #[fade to black, the fade in to fangs house front at night, anon and fang enter from stage left in neutral, anon on the left facing right, fang stops at the right and turns right.]
    scene black with Dissolve(2)
    scene home fang outside night with Dissolve(2)
    show fang neutral:
        xcenter -0.5
        easein 2 xcenter 0.66
    show anon neutral:
        xcenter -0.5
        easein 3 xcenter 0.33
    pause 3 
    stop sound fadeout 1.0
    play music outsideAmbience fadein 2.0

    "We disembark and say our goodbyes, {w=0.25}as Moe takes off into the distance with a very distressed Triceratops in tow. {w=0.4} I check the time on my phone."
    A "Well I doubt the bus runs this late, {w=0.25}so I'll go phone a ride."
    
    #[switch fang to happy]
    show fang happy flip
    with dissolve

    F "If you weren't planning to stay, {w=0.25}why'd you get out?"
    
    #[switch anon to concerned]
    show anon concerned
    with dissolve

    A "I.{w=0.2}.{w=0.2}.{w=0.2}think I'll be keeping my distance from Moe for a while."
    
    #[switch fang to considering]
    show fang considering flip
    with dissolve 

    F "Fair enough."
    
    #[switch anon to sad, ]
    show anon sad
    with dissolve

    A "So, {w=0.25}sorry about tonight and all."
    
    #[switch fang to happy]
    show fang happy flip
    with dissolve

    F "You're fine, {w=0.25}wasn't the worst place we've snuck off to go drink."
    
    #[switch anon to unimpressed]
    show anon unimpressed
    with dissolve

    A "Really?"

    #[switch fang to considering]
    show fang considering flip
    with dissolve

    F "Well, {w=0.25}maybe not, {w=0.25}but.{w=0.15}.{w=0.15}.{w=0.15} all's well that ends well?"
    
    #[Switch anon to shrug]
    show anon shrug
    with dissolve

    A "...I guess."

    #[switch anon and fang to neutral]
    show anon neutral
    show fang neutral flip
    with dissolve

    "We stand awkwardly in silence for a moment."
    A "Anyway, {w=0.25}I think it's about time we call a truce before someone ends up getting killed for real."
    F "Agreed, {w=0.25}I was getting kinda bored of it anyway."
    A "Awesome, {w=0.25}...so what do you want to do next week?"
    
    #[switch fang to considering]
    show fang considering flip
    with dissolve

    F "mmm, {w=0.15}we could go see a movie?"
    
    #[switch anon to happy]
    show anon happy
    with dissolve

    A "Sounds good, {w=0.25}see you later."
    F "Later."

    #[switch anon to neutral and fang to happy, fang moves up next to anon and the turns right and exits]
    show fang happy flip
    with dissolve
    show fang happy flip:
        easein 1 xcenter 0.425
    pause 2
    show fang neutral
    with dissolve
    show fang neutral:
        easein 2 xcenter 1.5
    show anon neutral
    with dissolve

    "We kiss and she heads inside while I sit on the curb and wait for a ride."
    #[slow fade to black]
    scene black
    with Dissolve(4)
    "I whip out my phone and look for a thread to derail to pass the time. {w=0.4}I stare at it for a moment before deciding to close the tab out entirely."
    "Instead I check the local AMC showtimes to see if there's anything worth seeing. {w=0.4}There's a neat little documentary about famous roadside attractions."
    "I'll see if Fang is game for that tomorrow."
    play music credits_theme fadein 4.0
    "A few minutes later a certain taxi who I swear follows me around pulls up. {w=0.4}I get in and have him take me straight home. {w=0.4}I think that's enough excitement for one lifetime."
    "..."
    "THE END..."

    if trish_extended_dialogue == True:
      jump bitn_chapter4_trish_end
    else: 
      jump bitn_chapter4_end


label bitn_chapter4_trish_end:
    
    show trishEnd


    pause 5

    return

label bitn_chapter4_end:

    return

