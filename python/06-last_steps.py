#REMEMBER TO CHANGE TO /fax BEFORE GITTING
import sys, time

from gpiozero import Button

#insert path to system
sys.path.insert(1, '/fax/python')

import music, debug, calls, lights, utils

debugger = debug.Debug(1)
currentPath = "/fax/"
#sounds
SOUND12 = currentPath + "audios/speaker/05-sound12.mp3"
SOUND13 = currentPath + "audios/speaker/06-sound13.mp3"
SOUND14 = currentPath + "audios/speaker/07-sound14.mp3"
SOUND15 = currentPath + "audios/speaker/08-sound15.mp3"
TBL_MONOLOGUE = currentPath + "audios/speaker/09-tbl.mp3"
FINALE = currentPath + "audios/speaker/10-final.mp3"
threads = []
#lights
lightsController = lights.Lights()
lightsController.purple()
calls.Call('07-laststeps2.call').dial()
debugger.log('********************* LAUNCHED FINAL STEP 1 ***************')
utils.stop_previous_scripts()
music.Audio(SOUND12).play()

calls.Call('07-laststeps3.call').dial()
debugger.log('********************* LAUNCHED FINAL STEP 2 ***************')
music.Audio(SOUND13).play()

calls.Call('07-laststeps4.call').dial()
debugger.log('********************* LAUNCHED FINAL STEP 3 ***************')
music.Audio(SOUND14).play()

calls.Call('07-laststeps5.call').dial()
debugger.log('********************* LAUNCHED FINAL STEP 4 ***************')
music.Audio(SOUND15).play()
debugger.log('PLAYING TBL')
music.Audio(TBL_MONOLOGUE).play()

#button = Button(26)
#def launch_finale():
#    print('finale')
#    music.Audio(FINALE).play()

#pressed = False
#while not pressed:
#    if button.is_pressed:
#        pressed = True
#        launch_finale()
