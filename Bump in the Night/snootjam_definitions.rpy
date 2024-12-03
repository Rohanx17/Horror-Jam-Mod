init:
    $ bitnRoot = "mods/Bump in the Night/assets/"

    $ bitnImages = bitnRoot+"images/"
    $ bitnSprites = bitnImages+"sprites/"
    $ bitnCgs = bitnImages+"cgs/"
    $ bitnBgs = bitnImages+"bgs/"
    $ bitnScreens = bitnImages+"screens/"
    $ bitnMisc = bitnImages+"misc/"

    $ bitnSounds = bitnRoot+"sounds/"
    $ bitnMusic = bitnSounds+"music/"
    $ bitnEffects = bitnSounds+"effects/"
    $ bitnAmbience = bitnSounds+"ambience/"

#Images

#Sprites

#Fooly Cooly
image puppet fc neutral = bitnSprites+"foolyCooly/fooly neutral.webp"
image puppet fc point up = bitnSprites+"foolyCooly/fooly point up.webp"
image puppet fc point out = bitnSprites+"foolyCooly/fooly point out.webp"

#Goons
image goon1 = Image(bitnSprites+"goons/goon1.png")
image goon1 flip = im.Flip(bitnSprites+"goons/goon1.png", horizontal=True)
image goon2 = Image(bitnSprites+"goons/goon2.png")
image goon2 flip = im.Flip(bitnSprites+"goons/goon2.png", horizontal=True)
image goon3 = Image(bitnSprites+"goons/goon3.png")
image goon3 flip = im.Flip(bitnSprites+"goons/goon3.png", horizontal=True)

define base = Character (ctc="ctc_end_marker", ctc_pause="ctc_mid_marker", ctc_timedpause=Null(), ctc_position="nestled") #will not work if I don't copypaste it 
define G1 = Character(_('[G1_Name]'), base, color="#5e2f1f", who_outlines=[(gui.name_text_thickness, '#401c0a')])
define G2 = Character(_('[G2_Name]'), base, color="#75382b", who_outlines=[(gui.name_text_thickness, '#40130a')])

default G1_Name = 'Short Goon'
default G2_Name = 'Tall Goon'

image short goon neutral = Image(bitnSprites+"goons/short goon neutral.png")
image short goon neutral flip = im.Flip(bitnSprites+"goons/short goon neutral.png", horizontal=True)
image short goon neutral ec = Image(bitnSprites+"goons/short goon neutral eyes closed.png")
image short goon angry = Image(bitnSprites+"goons/short goon angry.png")
image short goon shocked = Image(bitnSprites+"goons/short goon shocked.png")
image short goon shocked flip = im.Flip(bitnSprites+"goons/short goon shocked.png", horizontal=True)
image short goon grin  = Image(bitnSprites+"goons/short goon grin.png")

image tall goon neutral = Image(bitnSprites+"goons/tall goon neutral.png")
image tall goon neutral flip = im.Flip(bitnSprites+"goons/tall goon neutral.png", horizontal=True)
image tall goon shocked = Image(bitnSprites+"goons/tall goon shocked.png")
image tall goon shocked flip = im.Flip(bitnSprites+"goons/tall goon shocked.png", horizontal=True)

#Moe
image moe shocked = Image(bitnSprites+"moe/moe shocked.png")
image moe shocked flip = im.Flip(bitnSprites+"moe/moe shocked.png", horizontal=True)
image moe shocked bloodstain = Image(bitnSprites+"moe/moe shocked bloodstain.png")
image moe shocked bloodstain flip = im.Flip(bitnSprites+"moe/moe shocked bloodstain.png", horizontal=True)
image moe neutral bloodstain = Image(bitnSprites+"moe/moe neutral bloodstain.png")
image moe neutral bloodstain flip = im.Flip(bitnSprites+"moe/moe neutral bloodstain.png", horizontal=True)

#CGs

#Opening Car
image car neutral = Image(bitnCgs+"openingCar/the car.png")
image car anon = Image(bitnCgs+"openingCar/anonCar.png")
image car reed = Image(bitnCgs+"openingCar/reedCar.png")
image car fang = Image(bitnCgs+"openingCar/fangCar.png")
image car trish = Image(bitnCgs+"openingCar/trishCar.png")
image reedStory neutral = Image(bitnCgs+"openingCar/reedStory.png")
image reedStory speak = Image(bitnCgs+"openingCar/reedStorySpeak.png")
image reedStoryBack = Image(bitnCgs+"openingCar/reedStory2.png")
image anonThink = Image(bitnCgs+"openingCar/anonThink.png")
image anonThinkBack = Image(bitnCgs+"openingCar/anonThink2.png")

#Mirror Anon
image abandoned_mirror_1 = bitnCgs+"mirrorAnon/anonMirror.webp"
image abandoned_mirror_2 = bitnCgs+"mirrorAnon/AnonMirrorConfused.webp"
image anim_mirror_ghost = Movie(play=bitnCgs+"mirrorAnon/mirror.webm", loop=False) #.gif was kind of useless, Ren'Py eats only video formats and frame-to-frame animation

image car complete = Image(bitnCgs+"car complete.webp")

#Moe Car
image moeCar1 = bitnCgs+"moeCar/moe car 1.png"
image moeCar2 = bitnCgs+"moeCar/moe car 2.png"
image moeCar3 = bitnCgs+"moeCar/moe car 3.png"

#BGs

#Fooly Cooly Opening
image background_lightning_fc = bitnBgs+"foolyCoolyOpening/background.webp"
image wall_fc = bitnBgs+"foolyCoolyOpening/wall.webp"
image table_fc = bitnBgs+"foolyCoolyOpening/table.webp"

image outsideVan = Image(bitnBgs+"outside van.webp")
image outsideBuilding = Image(bitnBgs+"outside building.webp")
image abandoned_atrium = bitnBgs+"insidePic1.webp"
image abandoned_acoustics = bitnBgs+"insidePic2.webp"
image abandoned_graffiti = bitnBgs+"insidePic3.webp"
image abandoned_depth = bitnBgs+"insidePic4.webp"
image abandoned_conveyor = bitnBgs+"insidePic5.webp"
image abandoned_uptosomething = bitnBgs+"insidePic6.webp"
image abandoned_somewhere = bitnBgs+"insidePic7.webp"
image abandoned_door = ConditionSwitch("abandoned_door_opened == False", bitnBgs+"doorClosed.webp", "abandoned_door_opened == True", bitnBgs+"doorOpen.webp")
image abandoned_graffiti_2 = bitnBgs+"insidePic3.webp" #for the easiest bluring workaround
image basement = Image(bitnBgs+"basement.webp")
image stairs = Image(bitnBgs+"stairs.webp")
image torture_room = bitnBgs+"torture room.png"
image tortureRoom = Image(bitnBgs+"torture room.png")

#Screens

#Main Menu with all the stuff of this
screen bitn_menu:
    
    modal True

    layer "master"
    
    tag menu
    
    style_prefix "main_menu"

    add gui.main_menu_background
    
    $ main_menu_button_img = bitn_menu_button
    
    add bitn_menu_bg xysize (0.7, 1.0) xcenter 0.4
     
    frame:
         background bitn_menu_overlay 
    
    
    text _('Bump In The Night') size 70 xcenter 0.83 ycenter 0.3 
    
    vbox:
        spacing 10
        xpos 1865
        ypos 800
        use main_menu_buttons(main_menu_button_img,
            [
                [ _("Bump In"), Hide(screen=None,transition=Dissolve(2))],
                [ _("Bump Out"), Return()]
            ] )
    
    on "hide" action Jump("bitn_fooly_cooly_preintro")
 
define bitn_menu_bg = bitnScreens+"senza_titolo.png" #not 16:9, if it was the whole deal
define audio.bitn_menu_theme = bitnMusic+"silent_bluffs_menu.ogg"
define bitn_menu_overlay = im.MatrixColor("gui/overlay/main_menu.png", im.matrix.saturation(0)) 
define bitn_menu_button = im.MatrixColor("gui/button/menubuttons/template_full_idle.png", im.matrix.saturation(0)) 
image grey = Solid("#747574") 

#Anon's Camera (do we have it in the original game?)
image anon_camera_rec_dot:
    bitnScreens+"/anonsCamera/rec.webp"
    alpha 0.0
    1.0
    alpha 1.0
    1.0
    repeat
screen anon_camera:
    add "anim_static_fc" blend "multiply" alpha 0.2
    add bitnScreens+"/anonsCamera/viewfinder.webp"
    add "anon_camera_rec_dot" xalign 0.935 yalign 0.0725
screen forwarding:
    add "anim_static_fc" blend "multiply" alpha 0.2
    add "images/vfx/fastforward.webp" xalign 0.5 yalign 0.5

#Misc

#Anon Thoughts
image thought bubble1 = Image(bitnMisc+"anonThoughts/Bubble1.png")
image thought bubble2 = Image(bitnMisc+"anonThoughts/Bubble2.png")
image thought bubble3 = Image(bitnMisc+"anonThoughts/Bubble3.png")
image thought bubble4 = Image(bitnMisc+"anonThoughts/Bubble4.png")
image animation animation1:
    bitnMisc+"anonThoughts/animation 1.1.png"
    zoom 0.30
    xcenter 0.64
    ycenter 0.15
    pause 0.3
    bitnMisc+"anonThoughts/animation 1.2.png"
    zoom 0.30
    xcenter 0.64
    ycenter 0.15
    pause 0.3
    repeat
image animation animation2:
    bitnMisc+"anonThoughts/animation 2.1.png"
    zoom 0.30
    xcenter 0.64
    ycenter 0.15
    pause 0.3
    bitnMisc+"anonThoughts/animation 2.2.png"
    zoom 0.30
    xcenter 0.64
    ycenter 0.15
    pause 0.3
    repeat
image animation animation3:
    bitnMisc+"anonThoughts/animation 3.1.png"
    zoom 0.30
    xcenter 0.64
    ycenter 0.15
    pause 0.3
    bitnMisc+"anonThoughts/animation 3.2.png"
    zoom 0.30
    xcenter 0.64
    ycenter 0.15
    pause 0.3
    repeat
image animation animation4:
    bitnMisc+"anonThoughts/animation 4.1.png"
    zoom 0.30
    xcenter 0.64
    ycenter 0.15
    pause 0.4
    bitnMisc+"anonThoughts/animation 4.2.png"
    zoom 0.30
    xcenter 0.64
    ycenter 0.15
    pause 0.4
    repeat
image animation animation5:
    bitnMisc+"anonThoughts/animation 5.1.png"
    zoom 0.30
    xcenter 0.64
    ycenter 0.15
    pause 0.4
    bitnMisc+"anonThoughts/animation 5.2.png"
    zoom 0.30
    xcenter 0.64
    ycenter 0.15
    pause 0.4
    repeat
image animation animation6:
    bitnMisc+"anonThoughts/animation 6.1.png"
    zoom 0.30
    xcenter 0.64
    ycenter 0.15
    pause 0.4
    bitnMisc+"anonThoughts/animation 6.2.png"
    zoom 0.30
    xcenter 0.64
    ycenter 0.15
    pause 0.4
    repeat
image animation animation7:
    bitnMisc+"anonThoughts/animation 7.1.png"
    zoom 0.30
    xcenter 0.64
    ycenter 0.15
    pause 0.4
    bitnMisc+"anonThoughts/animation 7.2.png"
    zoom 0.30
    xcenter 0.64
    ycenter 0.15
    pause 0.4
    repeat
image animation animation8:
    bitnMisc+"anonThoughts/animation 8.1.png"
    zoom 0.30
    xcenter 0.64
    ycenter 0.15
    pause 0.4
    bitnMisc+"anonThoughts/animation 8.2.png"
    zoom 0.30
    xcenter 0.64
    ycenter 0.15
    pause 0.4
    repeat
image animation animation9:
    bitnMisc+"anonThoughts/animation 9.1.png"
    zoom 0.30
    xcenter 0.64
    ycenter 0.15
    pause 0.5
    bitnMisc+"anonThoughts/animation 9.2.png"
    zoom 0.30
    xcenter 0.64
    ycenter 0.15
    pause 0.5
    repeat

image black = Image(bitnMisc+"black.png")
image anim_static_fc:
    bitnMisc+"static1.webp"
    pause .05
    bitnMisc+"static2.webp"
    pause .05
    bitnMisc+"static3.webp"
    pause .05
    bitnMisc+"static4.webp"   
    repeat
image beer_anon = bitnMisc+"beer.webp"
image beer_fang = bitnMisc+"beer.webp"
image beer_trish = bitnMisc+"beer.webp"
image keys = Image(bitnMisc+"keys.png")

#Sounds

#Music
define audio.maltShopTheme = bitnMusic+"scooby looped.ogg"
define audio.exploration_bgm = bitnMusic+"exploration_theme.ogg"
define audio.party_bgm = bitnMusic+"nothing_ever_happens.ogg"
define audio.mystery_bgm = bitnMusic+"something_happened.ogg" #this track has some artifacts (idk, seems not intended for my ear)
define audio.fc_bgm = bitnMusic+"fooly_cooly_creature_feature.ogg"
define escape = bitnMusic+"escape.ogg"
define worried = bitnMusic+"worried.ogg"
define torture_p1 = bitnMusic+"PHASE 1.ogg"
define torture_p2 = bitnMusic+"PHASE 2.ogg"
define torture_p3 = bitnMusic+"PHASE 3.ogg"
define torture_p4 = bitnMusic+"PHASE 4.ogg"
define venetianValues = bitnMusic+"Venetian Values.ogg"

#Effects
define audio.doorOpening = bitnEffects+"door opening.mp3"
define audio.fang_pickup_sfx = bitnEffects+"fang_pick_up_hl.ogg"
define audio.trish_pickup_sfx = bitnEffects+"trish_pick_up.ogg"
define audio.reed_closing_door_sfx = bitnEffects+"closing_door.ogg" #also changed it a bit
define audio.van_horn_sfx = bitnEffects+"dixie_car_horn.ogg"
define audio.static_noise_sfx = bitnEffects+"static_noise.ogg"
define audio.anon_bottle_throw_sfx = bitnEffects+"tada_throw.ogg"
define audio.fang_attempt_door_sfx = bitnEffects+"locked_door.ogg"
define audio.anon_bathroom_sfx = bitnEffects+"peeing.mp3"
define audio.anon_spray_sfx = bitnEffects+"spray.mp3"
define audio.ghost_bathroom_sfx = bitnEffects+"whoosh.mp3"
define audio.reed_lighter_sfx = bitnEffects+"lighter.ogg" # made it louder manually + convert to ogg in process
define audio.fang_scream_sfx = bitnEffects+"dolphine_call.ogg"
define audio.gang_beer_sfx = bitnEffects+"beer_open_cap.ogg"
define audio.fang_lockpick_sfx = bitnEffects+"lock_sound.mp3"
define audio.fang_door_opened_sfx = bitnEffects+"creaking_door.mp3"
define audio.fc_cackle_sfx = bitnEffects+"witch_laugh.mp3"
define carCrash = bitnEffects+"car crash.ogg"
define carDoor = bitnEffects+"car door.mp3"
define doorCreaking = bitnEffects+"door creaking.mp3"
define footsteps = bitnEffects+"footsteps.mp3"
define insideCarNoise = bitnEffects+"inside car noise.mp3"
define keyGet = bitnEffects+"key get.mp3"
define lightSwitch = bitnEffects+"light switch.mp3"
define lockSound = bitnEffects+"lock sound.mp3"
define sneeze = bitnEffects+"sneeze.mp3"
define tackle = bitnEffects+"tackle.mp3"
define tarpPull = bitnEffects+"tarp pull.mp3"
define tableDrop = bitnEffects+"table drop.mp3"
define tableKnife = bitnEffects+"knife table stab.ogg"
define af_wtf = bitnEffects+"surprise.wav" 
define reed_spit = bitnEffects+"spit.mp3" 
define goon_fingersnap = bitnEffects+"finger snap.mp3"
define goon_ripout = bitnEffects+"rip out.mp3"
define goon_fingerchop = bitnEffects+"finger chop instant.ogg"
define goon_fingerchop_delay = bitnEffects+"finger chop delayed.ogg"
define goon_phone = bitnEffects+"phone hang up.ogg"
define ouch = bitnEffects+"reed_scream_shortest.ogg"
define short_scream = bitnEffects+"reed_scream_short.ogg"
define long_scream = bitnEffects+"reed_scream_long.ogg"
define end_groan = bitnEffects+"reed_dead_inside.ogg"
define fang_bite = bitnEffects+"fang_bite.ogg"
define chair_pull = bitnEffects+"chair_pulling.ogg"
define chair_creak = bitnEffects+"chair_creaking.ogg"
define card_gather = bitnEffects+"cards_collecting.ogg"
define goon_smoke = bitnEffects+"exhale.ogg"
define pipeDrop = bitnEffects+"pipe drop.mp3"
define doorSlam = bitnEffects+"basement door slam.mp3"
define arguing = bitnEffects+"Italian Men arguing.ogg"
define bangCrash = bitnEffects+"bang-crash-103775.mp3"
define boxCrash = bitnEffects+"box-crash-106687.mp3"
define crash1 = bitnEffects+"crash-6711.mp3"
define crash2 = bitnEffects+"crash-85728.mp3"
define stairCrash = bitnEffects+"crash-down-some-stairs-106946.mp3"
define woodCrash = bitnEffects+"wood-crash-103157.mp3"
define pistolFire = bitnEffects+"pistol fire.ogg"

#DBD sounds :)
define trish_cry = bitnEffects+"trish_crying.ogg"
define ouch = bitnEffects+"reed_scream_shortest.ogg"
define short_scream = bitnEffects+"reed_scream_short.ogg"
define long_scream = bitnEffects+"reed_scream_long.ogg"
define end_groan = bitnEffects+"reed_dead_inside.ogg"
define fang_resist = bitnEffects+"fang_resist.ogg"

#Ambience
define audio.outsideAmbience = bitnAmbience+"ambient noises for outside.mp3"
define audio.industrial_random_ambient = bitnAmbience+"industrial_machine_cycle_random.ogg"
define audio.fc_electricity_ambient = bitnAmbience+"electricity.ogg"
define audio.fc_thunder_ambient = bitnAmbience+"thunder.mp3"
define audio.industrial_machine_ambient = bitnAmbience+"industrial_machine_cycle.ogg"
define knife_sharpening = bitnAmbience+"knife sharpening.mp3"
define playing_cards = bitnAmbience+"playing_cards.ogg"
define lamp_buzz = bitnAmbience+"fluorescent light buzz.mp3"

#Transforms

#Reed enters the scene
transform chill_move_right(decimal):
    xcenter 1.0
    ycenter .655
    ease 2.0 xcenter decimal 
transform chill_move_left(decimal):
    xcenter 0.0
    ycenter .655
    ease 2.0 xcenter decimal 

#Trish enters the scene    
transform rushed_move_right(decimal):
    xcenter 1.0
    ycenter .655
    easein 2.0 xcenter decimal 
transform rushed_move_left(decimal):
    xcenter 0.0
    ycenter .655
    easein 2.0 xcenter decimal 

#Fang enters the scene    
transform insecure_move_right(decimal):
    xcenter 1.0
    ycenter .655
    easeout 2.0 xcenter decimal        
transform insecure_move_left(decimal):
    xcenter 0.0
    ycenter .655
    easeout 2.0 xcenter decimal          

#Anon enters the scene   
transform casual_move_right(decimal):
    xcenter 1.0
    ycenter .655
    ease_cubic 2.0 xcenter decimal    
transform casual_move_left(decimal):
    xcenter 0.0
    ycenter .655
    ease_cubic 2.0 xcenter decimal   

#Misc
transform carBump:
    linear 0.1 ycenter 0.48
    linear 0.1 ycenter 0.50
    pause 2
    linear 0.1 ycenter 0.48
    linear 0.1 ycenter 0.50
    pause 4
    linear 0.1 ycenter 0.48
    linear 0.1 ycenter 0.50
    pause 3.5
    linear 0.1 ycenter 0.48
    linear 0.1 ycenter 0.50
    pause 3
    repeat

#Characters
define goon = Character("???", color="FFFFFF")
define FC = Character("Fooly Cooly", color="72D0EA")

#Misc
default abandoned_door_opened = False
define ANVL = nvl_narrator
default trish_extended_dialogue = False

image eye:
    fps 120.0
    bitnScreens+"/anonsCamera/rec.webp"
    xcenter 0.5
    ycenter 0.5
    additive 0.5
    matrixcolor SaturationMatrix(0.0) 
    matrixcolor BrightnessMatrix(5.0)
    zoom 20.0
    yzoom 0.0
    .5
    bitnScreens+"/anonsCamera/rec.webp"
    yzoom 0.25
    .25
    bitnScreens+"/anonsCamera/rec.webp"
    yzoom 0.50
    .25
    bitnScreens+"/anonsCamera/rec.webp"
    yzoom 0.75
    .25
    bitnScreens+"/anonsCamera/rec.webp"
    yzoom 1.0
    .25
    bitnScreens+"/anonsCamera/rec.webp"


layeredimage tunnel_vision:
    always:
        "black"
    
    attribute base default:
        "eye"