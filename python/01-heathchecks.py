import sys, time

#insert path to system
sys.path.insert(1, '/fax/python')

import music, debug, calls, lights, utils

debugger = debug.Debug(1)

healthcall = calls.Call('00-healthcall.call')
healthcall.dial()
debugger.log('********* LAUNCHED FIRST CALL ****************')


raw_input("PRESS ENTER IF YOU WANT TO TRIGGER THE HEALTH FAX. THIS GOES AFTER THEY SEND A FAX")
#NEEDS TIME IN BETWEEN FOR THEM TO LEARN TO ANSWER
healthfax = calls.Call('00-healthfax.call')
healthfax.dial()
debugger.log('********* LAUNCHED HEALTHCHECK FAX ****************')