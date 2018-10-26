"""
Peruse the latest xkcd strips
"""
___name___         = "xkcdview"
___license___      = "MIT"
___dependencies___ = ["app", "sleep", "wifi", "http", "ugfx_helper"]
___categories___   = ["Other"]

import wifi, ugfx, http, ujson, app, sleep
from tilda import Buttons, LED

def get_strip():
    global strip

    LED(LED.RED).on()
    try:
        strip_json = http.get("https://xkcd.com/info.0.json").raise_for_status().content
        strip = ujson.loads(strip_json)
    except: 
        print('couldn't fetch strip json')
    LED(LED.RED).off()
	
	LED(LED.GREEN).on()
    try:
        strip_img = http.get(strip['img']).raise_for_status().content
		ugfx.display_image(0,0,bytearray(strip_img))
    except: 
        print('couldn't fetch strip image')
    LED(LED.GREEN).off()

while (not Buttons.is_pressed(Buttons.BTN_A)) and (not Buttons.is_pressed(Buttons.BTN_B)) and (not Buttons.is_pressed(Buttons.BTN_Menu)):
    sleep.wfi()
	
ugfx.clear()
app.restart_to_default()
