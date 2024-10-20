
init python:
    mod_menu_access += [{
        'Name': "SnootJam",
        'Label' : "snootjam_storyline_1"
    }]

init:
 $ snootjamRoot = "mods/horrorJamModFroomerFork/assets/"
 
#Images
image car neutral = Image(snootjamRoot+"images/the car.png")
image car anon = Image(snootjamRoot+"images/anonCar.png")
image car reed = Image(snootjamRoot+"images/reedCar.png")
image car fang = Image(snootjamRoot+"images/fangCar.png")
image car trish = Image(snootjamRoot+"images/trishCar.png")
image reedStory neutral = Image(snootjamRoot+"images/reedStory.png")
image reedStory speak = Image(snootjamRoot+"images/reedStorySpeak.png")
image anonThink = Image(snootjamRoot+"images/anonThink.png")
image thought bubble1 = Image(snootjamRoot+"images/Bubble1.png")
image thought bubble2 = Image(snootjamRoot+"images/Bubble2.png")
image thought bubble3 = Image(snootjamRoot+"images/Bubble3.png")
image thought bubble4 = Image(snootjamRoot+"images/Bubble4.png")
image black = Image(snootjamRoot+"images/black.png")
image outsideVan = Image(snootjamRoot+"images/outside van.webp")
image outsideBuilding = Image(snootjamRoot+"images/outside building.webp")
image camera = Image(snootjamRoot+"images/viewfinder.webp")
image recording:
 snootjamRoot+"images/rec.webp"
 zoom 0.75
 xcenter 0.92
 ycenter 0.093
 pause 0.50
 matrixcolor OpacityMatrix(0)
 pause 0.25
 matrixcolor OpacityMatrix(1)
 repeat

#Thought bubble Animations
image animation animation1:
 snootjamRoot+"images/animation 1.1.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.3
 snootjamRoot+"images/animation 1.2.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.3
 repeat
image animation animation2:
 snootjamRoot+"images/animation 2.1.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.3
 snootjamRoot+"images/animation 2.2.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.3
 repeat
image animation animation3:
 snootjamRoot+"images/animation 3.1.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.3
 snootjamRoot+"images/animation 3.2.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.3
 repeat
image animation animation4:
 snootjamRoot+"images/animation 4.1.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.4
 snootjamRoot+"images/animation 4.2.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.4
 repeat
image animation animation5:
 snootjamRoot+"images/animation 5.1.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.4
 snootjamRoot+"images/animation 5.2.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.4
 repeat
image animation animation6:
 snootjamRoot+"images/animation 6.1.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.4
 snootjamRoot+"images/animation 6.2.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.4
 repeat
image animation animation7:
 snootjamRoot+"images/animation 7.1.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.4
 snootjamRoot+"images/animation 7.2.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.4
 repeat
image animation animation8:
 snootjamRoot+"images/animation 8.1.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.4
 snootjamRoot+"images/animation 8.2.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.4
 repeat
image animation animation9:
 snootjamRoot+"images/animation 9.1.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.5
 snootjamRoot+"images/animation 9.2.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.5
 repeat
 
#Music
define audio.maltShopTheme = snootjamRoot+"music/scooby looped.ogg"
define audio.outsideAmbience = snootjamRoot+"music/ambient noises for outside.mp3"
define audio.doorOpening = snootjamRoot+"music/door opening.mp3"

#Transforms
transform carBump:
  linear 0.1 ycenter 0.48
  linear 0.1 ycenter 0.50
  
default abandoned_door_opened = False

define ANVL = nvl_narrator 

image abandoned_atrium = snootjamRoot+"pics/1920x1080/insidePic1.webp"
image abandoned_acoustics = snootjamRoot+"pics/1920x1080/insidePic2.webp"
image abandoned_graffiti = snootjamRoot+"pics/1920x1080/insidePic3.webp"
image abandoned_depth = snootjamRoot+"pics/1920x1080/insidePic4.webp"
image abandoned_conveyor = snootjamRoot+"pics/1920x1080/insidePic5.webp"
image abandoned_uptosomething = snootjamRoot+"pics/1920x1080/insidePic6.webp"
image abandoned_somewhere = snootjamRoot+"pics/1920x1080/insidePic7.webp"
image abandoned_door = ConditionSwitch("abandoned_door_opened == False", snootjamRoot+"pics/1920x1080/doorClosed.webp", "abandoned_door_opened == True", snootjamRoot+"pics/1920x1080/doorOpen.webp")


image abandoned_mirror_1 = snootjamRoot+"pics/1920x1080/anonMirror.webp"
image abandoned_mirror_2 = snootjamRoot+"pics/1920x1080/AnonMirrorConfused.webp"

image anim_mirror_ghost = Movie(play=snootjamRoot+"pics/1920x1080/mirror.webm", loop=False) #.gif was kind of useless, Ren'Py eats only video formats and frame-to-frame animation

image beer_anon = snootjamRoot+"pics/beer.webp"
image beer_fang = snootjamRoot+"pics/beer.webp"
image beer_trish = snootjamRoot+"pics/beer.webp"
 

image abandoned_graffiti_2 = snootjamRoot+"pics/1920x1080/insidePic3.webp" #for the easiest bluring workaround

# Reed enters the scene
transform chill_move_right(decimal):
    xcenter 1.0
    ycenter .655
    ease 2.0 xcenter decimal 

transform chill_move_left(decimal):
    xcenter 0.0
    ycenter .655
    ease 2.0 xcenter decimal 
    

# Trish enters the scene    
transform rushed_move_right(decimal):
    xcenter 1.0
    ycenter .655
    easein 2.0 xcenter decimal 

transform rushed_move_left(decimal):
    xcenter 0.0
    ycenter .655
    easein 2.0 xcenter decimal 


# Fang enters the scene    
transform insecure_move_right(decimal):
    xcenter 1.0
    ycenter .655
    easeout 2.0 xcenter decimal     
    
transform insecure_move_left(decimal):
    xcenter 0.0
    ycenter .655
    easeout 2.0 xcenter decimal         
    

# Anon enters the scene   
transform casual_move_right(decimal):
    xcenter 1.0
    ycenter .655
    ease_cubic 2.0 xcenter decimal  

    
transform casual_move_left(decimal):
    xcenter 0.0
    ycenter .655
    ease_cubic 2.0 xcenter decimal   

# Anon's Camera (do we have it in the original game?)
 
image anon_camera_rec_dot:
    "images/vfx/rec.webp"
    alpha 0.0
    1.0
    alpha 1.0
    1.0
    repeat
 
screen anon_camera:
    
    add "anim_static_fc" blend "multiply" alpha 0.2
    add "images/vfx/viewfinder.webp"
    add "anon_camera_rec_dot" xalign 0.935 yalign 0.0725


screen forwarding:
    
    add "anim_static_fc" blend "multiply" alpha 0.2
    add "images/vfx/fastforward.webp" xalign 0.5 yalign 0.5
 
#Fooly Cooly Stuff
    
image anim_static_fc:
   snootjamRoot+"opener assets/static/webp/static1.webp"
   pause .05
   snootjamRoot+"opener assets/static/webp/static2.webp"
   pause .05
   snootjamRoot+"opener assets/static/webp/static3.webp"
   pause .05
   snootjamRoot+"opener assets/static/webp/static4.webp"   
   repeat


image background_lightning_fc = snootjamRoot+"opener assets/black and white/background.webp" 
image wall_fc = snootjamRoot+"opener assets/black and white/wall.webp"
image table_fc = snootjamRoot+"opener assets/black and white/table.webp"       

image puppet fc neutral = snootjamRoot+"opener assets/black and white/fooly neutral.webp"
image puppet fc point up = snootjamRoot+"opener assets/black and white/fooly point up.webp"
image puppet fc point out = snootjamRoot+"opener assets/black and white/fooly point out.webp"


#Audio (have all the sounds here as variables are more convenient if you possibly be changing their storage locations too)

define audio.fang_pickup_sfx = snootjamRoot+"sounds/fang_pick_up_hl.ogg"
define audio.trish_pickup_sfx = snootjamRoot+"sounds/trish_pick_up.ogg"
define audio.reed_closing_door_sfx = snootjamRoot+"sounds/closing_door.ogg" #also changed it a bit
define audio.van_horn_sfx = snootjamRoot+"sounds/dixie_car_horn.ogg"
define audio.static_noise_sfx = snootjamRoot+"sounds/static_noise.ogg"
define audio.anon_bottle_throw_sfx = snootjamRoot+"sounds/tada_throw.ogg"
define audio.fang_attempt_door_sfx = snootjamRoot+"sounds/locked_door.ogg"
define audio.anon_bathroom_sfx = snootjamRoot+"sounds/peeing.mp3"
define audio.anon_spray_sfx = snootjamRoot+"sounds/spray.mp3"
define audio.ghost_bathroom_sfx = snootjamRoot+"sounds/whoosh.mp3"
define audio.reed_lighter_sfx = snootjamRoot+"sounds/lighter.ogg" # made it louder manually + convert to ogg in process
define audio.fang_scream_sfx = snootjamRoot+"sounds/dolphine_call.ogg"
define audio.gang_beer_sfx = snootjamRoot+"sounds/beer_open_cap.ogg"
define audio.industrial_random_ambient = snootjamRoot+"sounds/industrial_machine_cycle_random.ogg"
define audio.fc_electricity_ambient = snootjamRoot+"opener assets/electricity.ogg"
define audio.fc_thunder_ambient = snootjamRoot+"opener assets/thunder.mp3"



#renamed original files because Python would not access it elsewise in the audio namespace
define audio.fang_lockpick_sfx = snootjamRoot+"sounds/lock_sound.mp3"
define audio.fang_door_opened_sfx = snootjamRoot+"sounds/creaking_door.mp3"
define audio.exploration_bgm = snootjamRoot+"sounds/exploration_theme.ogg"
define audio.party_bgm = snootjamRoot+"sounds/nothing_ever_happens.ogg"
define audio.mystery_bgm = snootjamRoot+"sounds/something_happened.ogg" #this track has some artifacts (idk, seems not intended for my ear)
define audio.industrial_machine_ambient = snootjamRoot+"sounds/industrial_machine_cycle.ogg"
define audio.fc_bgm = snootjamRoot+"opener assets/fooly_cooly_creature_feature.ogg"
define audio.fc_cackle_sfx = snootjamRoot+"opener assets/witch_laugh.mp3"