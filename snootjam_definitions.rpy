
init python:
    mod_menu_access += [{
        'Name': "SnootJam",
        'Label' : "snootjam_storyline_1"
    }]

init:
 $ snootjamRoot = "mods/horrorJamModFroomerFork/assets"
 
#Images
image car neutral = Image(snootjamRoot+"/images/the car.png")
image car anon = Image(snootjamRoot+"/images/anonCar.png")
image car reed = Image(snootjamRoot+"/images/reedCar.png")
image car fang = Image(snootjamRoot+"/images/fangCar.png")
image car trish = Image(snootjamRoot+"/images/trishCar.png")
image reedStory neutral = Image(snootjamRoot+"/images/reedStory.png")
image reedStory speak = Image(snootjamRoot+"/images/reedStorySpeak.png")
image anonThink = Image(snootjamRoot+"/images/anonThink.png")
image thought bubble1 = Image(snootjamRoot+"/images/Bubble1.png")
image thought bubble2 = Image(snootjamRoot+"/images/Bubble2.png")
image thought bubble3 = Image(snootjamRoot+"/images/Bubble3.png")
image thought bubble4 = Image(snootjamRoot+"/images/Bubble4.png")
image black = Image(snootjamRoot+"/images/black.png")

#Thought bubble Animations
image animation animation1:
 snootjamRoot+"/images/animation 1.1.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.2
 snootjamRoot+"/images/animation 1.2.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.2
 repeat
image animation animation2:
 snootjamRoot+"/images/animation 2.1.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.2
 snootjamRoot+"/images/animation 2.2.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.2
 repeat
image animation animation3:
 snootjamRoot+"/images/animation 3.1.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.2
 snootjamRoot+"/images/animation 3.2.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.2
 repeat
image animation animation4:
 snootjamRoot+"/images/animation 4.1.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.3
 snootjamRoot+"/images/animation 4.2.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.3
 repeat
image animation animation5:
 snootjamRoot+"/images/animation 5.1.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.3
 snootjamRoot+"/images/animation 5.2.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.3
 repeat
image animation animation6:
 snootjamRoot+"/images/animation 6.1.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.3
 snootjamRoot+"/images/animation 6.2.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.3
 repeat
image animation animation7:
 snootjamRoot+"/images/animation 7.1.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.3
 snootjamRoot+"/images/animation 7.2.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.3
 repeat
image animation animation8:
 snootjamRoot+"/images/animation 8.1.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.3
 snootjamRoot+"/images/animation 8.2.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.3
 repeat
image animation animation9:
 snootjamRoot+"/images/animation 9.1.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.3
 snootjamRoot+"/images/animation 9.2.png"
 zoom 0.30
 xcenter 0.64
 ycenter 0.15
 pause 0.3
 repeat
 
#Music
define audio.maltShopTheme = snootjamRoot+"/music/scooby looped.ogg"

#Transforms
transform carBump:
  linear 0.1 ycenter 0.48
  linear 0.1 ycenter 0.50