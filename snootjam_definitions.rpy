
init python:
    mod_menu_access += [{
        'Name': "SnootJam",
        'Label' : "snootjam_storyline_1"
    }]

init:
 $ snootjamRoot = "mods/horrorJamModFroomerFork/assets"
 
#Images
image car neutral = Image(snootjamRoot+"/images/the car.png")
image black = Image(snootjamRoot+"images/black.png")
 
#Music
define audio.maltShopTheme = snootjamRoot+"/music/scooby looped.ogg"