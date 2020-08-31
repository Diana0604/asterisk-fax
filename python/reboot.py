#REMEMBER TO CHANGE TO /fax BEFORE GITTING
import sys, time

#insert path to system
sys.path.insert(1, '/fax/python')

import music, debug, calls, lights

debugger = debug.Debug(1)
currentPath = "/fax/"
#sounds
OPENING_THEME = currentPath + "audios/speaker/00-arrival.mp3"
BREATHING = currentPath + "audios/speaker/01-breathing.mp3"
#lights
lightsController = lights.Lights()

#play first song

debugger.log('************ TURNING LIGHTS ************')
lightsController.iradescent()
debugger.log('************ LIGHTS ON ************')
debugger.log('************ STARTING OPENING THEME ************')
music.Audio(OPENING_THEME).play()