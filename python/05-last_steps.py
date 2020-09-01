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
HEARTBEAT_INTENSE = currentPath + "audios/speaker/04-breathing_heartbeat_intense.mp3"
TBL_MONOLOGUE = currentPath + "audios/speaker/08-tbl_monologue1.wav"
threads = []
#lights
lightsController = lights.Lights()


lightsController.purple()
calls.Call('07-laststeps1.call').dial()
debugger.log('********************* LAUNCHED FINAL STEPS EXPLAINED ***************')
music.Audio(HEARTBEAT,1).play()
utils.stop_previous_scripts()
heartbeat_intense = music.Audio(HEARTBEAT_INTENSE,1)
heartbeat_intense_thread = heartbeat_intense.play()
raw_input("PRESS WHEN LAST FAXES SHOULD COME THROUGH")
calls.Call('07-laststeps2.call').dial()
debugger.log('********************* LAUNCHED FINAL STEP 1 ***************')
#time.sleep(420)
raw_input("PRESS WHEN LAST FAXES SHOULD COME THROUGH")
calls.Call('07-laststeps3.call').dial()
debugger.log('********************* LAUNCHED FINAL STEP 2 ***************')
#time.sleep(240)
raw_input("PRESS WHEN LAST FAXES SHOULD COME THROUGH")
calls.Call('07-laststeps4.call').dial()
debugger.log('********************* LAUNCHED FINAL STEP 3 ***************')
#time.sleep(600)
raw_input("PRESS WHEN LAST FAXES SHOULD COME THROUGH")
heartbeat_intense_thread.join()
music.Audio(HEARTBEAT,1).play()
calls.Call('07-laststeps5.call').dial()
debugger.log('********************* LAUNCHED FINAL STEP 4 ***************')
raw_input("PRESS WHEN LAST FAXES SHOULD COME THROUGH")