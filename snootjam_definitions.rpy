
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
image black = Image(snootjamRoot+"/images/black.png")
 
#Music
define audio.maltShopTheme = snootjamRoot+"/music/scooby looped.ogg"

#Transforms
transform carBump:
  linear 0.1 ycenter 0.48
  linear 0.1 ycenter 0.50