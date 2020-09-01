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
spies = calls.Call('05-mission.call')
spies.dial()
debugger.log('***************** LAUNCHED MISSION CALL ***********')