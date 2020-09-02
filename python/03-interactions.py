#REMEMBER TO CHANGE TO /fax BEFORE GITTING
import sys, time

#insert path to system
sys.path.insert(1, '/fax/python')

import music, debug, calls, lights, utils

debugger = debug.Debug(1)
#lights
lightsController = lights.Lights()

antenna = calls.Call('03-antenna.call')
antenna.dial()
debugger.log('***************** LAUNCHED ANTENNA ***********')

raw_input("PRESS ENTER IF YOU WANT TO TRIGGER THE SPIES FAX. THIS SHOULD HAPPEN AFTER WE RECEIVE XXX CALL FROM THEM.")
spies = calls.Call('04-spies.call')
spies.dial()
debugger.log('***************** LAUNCHED SPIES CALL ***********')

raw_input("PRESS ENTER IF YOU WANT TO TRIGGER THE MISSION FAX. THIS SHOULD HAPPEN AFTER WE RECEIVE XXX CALL FROM THEM.")
mission = calls.Call('05-mission.call')
mission.dial()

debugger.log('***************** LAUNCHED MISSION CALL ***********')
currentPath = "/fax/"
#sounds
COUGHING = currentPath + "audios/speaker/03-coughing.mp3"
BREATHING = currentPath + "audios/speaker/01-breathing.mp3"

music.Audio(COUGHING).play()

while True:
    breathing = music.Audio(BREATHING).play()