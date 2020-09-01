#REMEMBER TO CHANGE TO /fax BEFORE GITTING
import sys, time

#insert path to system
sys.path.insert(1, '/fax/python')

import music, debug, calls, lights, utils

debugger = debug.Debug(1)
currentPath = "/fax/"
#sounds
OPENING_THEME = currentPath + "audios/speaker/00-arrival.mp3"
BREATHING = currentPath + "audios/speaker/01-breathing.mp3"
CHARGING_UP = currentPath + "audios/speaker/02-charging_up.mp3"
HEARTBEAT = currentPath + "audios/speaker/03-breathing_hearbeat.mp3"
HEARTBEAT_INTENSE1 = currentPath + "audios/speaker/04-breathing_heartbeat_intense.mp3"
HEARTBEAT_INTENSE2 = currentPath + "audios/speaker/05-breathing_heartbeat_intense.mp3"
HEARTBEAT_INTENSE3 = currentPath + "audios/speaker/06-breathing_heartbeat_intense.mp3"
TBL_MONOLOGUE = currentPath + "audios/speaker/08-tbl_monologue1.wav"
threads = []
#lights
lightsController = lights.Lights()


lightsController.purple()
calls.Call('07-laststeps1.call').dial()
debugger.log('********************* LAUNCHED FINAL STEPS EXPLAINED ***************')

calls.Call('07-laststeps2.call').dial()
debugger.log('********************* LAUNCHED FINAL STEP 1 ***************')
music.Audio(HEARTBEAT).play()
utils.stop_previous_scripts()

calls.Call('07-laststeps3.call').dial()
debugger.log('********************* LAUNCHED FINAL STEP 2 ***************')
music.Audio(HEARTBEAT_INTENSE1).play()

calls.Call('07-laststeps4.call').dial()
debugger.log('********************* LAUNCHED FINAL STEP 3 ***************')
music.Audio(HEARTBEAT_INTENSE2).play()

calls.Call('07-laststeps5.call').dial()
debugger.log('********************* LAUNCHED FINAL STEP 4 ***************')
music.Audio(HEARTBEAT_INTENSE3).play()