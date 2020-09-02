#REMEMBER TO CHANGE TO /fax BEFORE GITTING
import sys, time

#insert path to system
sys.path.insert(1, '/fax/python')

import music, debug, calls, lights, utils

debugger = debug.Debug(1)
currentPath = "/fax/"
#sounds
SOUND11 = currentPath + "audios/speaker/04-sound11.mp3"
threads = []
#lights
lightsController = lights.Lights()
lightsController.purple()
calls.Call('07-laststeps1.call').dial()
debugger.log('********************* LAUNCHED FINAL STEPS EXPLAINED ***************')
sound11 = music.Audio(SOUND11, 1).play()
utils.stop_previous_scripts()

sound11.join()
while True:
        music.Audio(SOUND11, 0).play()
