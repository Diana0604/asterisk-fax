#REMEMBER TO CHANGE TO /fax BEFORE GITTING
import sys, time, os

#insert path to system
sys.path.insert(1, '/fax/python')

IRADESCENT = (0.5,0,0.5)

import music, debug, calls, lights

debugger = debug.Debug(1)
CURRENT_PATH = ""
if os.uname()[0] != 'Darwin':
    CURRENT_PATH = "/fax/"
#sounds
OPENING_THEME = CURRENT_PATH + "audios/speaker/00-arrival.mp3"
BREATHING = CURRENT_PATH + "audios/speaker/01-breathing.mp3"
#lights
lights_controller = lights.Controller()
music_controller = music.Controller()
#play first song


debugger.title('STARTING OPENING THEME')
music_controller.play(OPENING_THEME, True)
lights_controller.blink_to(IRADESCENT, time=18)

debugger.title('OPENING THEME FINISHED')
music_controller.play(BREATHING, False, True)
debugger.title('MACHINE IS BREATHING')
t1.join()
