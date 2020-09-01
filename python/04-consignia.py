#REMEMBER TO CHANGE TO /fax BEFORE GITTING
import sys, time

#insert path to system
sys.path.insert(1, '/fax/python')

import music, debug, calls, lights, utils

debugger = debug.Debug(1)
currentPath = "/fax/"
#sounds
CHARGING_UP = currentPath + "audios/speaker/02-charging_up.mp3"
threads = []
#lights
lightsController = lights.Lights()

raw_input("PRESS ENTER IF YOU WANT TO TRIGGER CONSIGNIA FAX. THIS SHOULD COME AFTER ALLERGIES")
charging = music.Audio(CHARGING_UP, 1)
lightsController.red()
utils.stop_previous_scripts()
threads.append(charging.play())

consignia = calls.Call('06-consignia.call')
consignia.dial()

debugger.log('********************* LAUNCHED CONSIGNIA CALL ***************')
