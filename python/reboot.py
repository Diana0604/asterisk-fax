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

#play first song


debugger.title('STARTING OPENING THEME')
music.Audio(OPENING_THEME, True).play()
lights_controller.blink_to(IRADESCENT)

debugger.title('OPENING THEME FINISHED')
t1 = music.Audio(BREATHING, False, True).play()
debugger.title('MACHINE IS BREATHING')
t1.join()
