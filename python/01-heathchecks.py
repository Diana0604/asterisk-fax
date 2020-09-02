import sys, time

#insert path to system
sys.path.insert(1, '/fax/python')

import music, debug, calls, lights, utils

debugger = debug.Debug(1)

healthcall = calls.Call('00-healthcall.call')
healthcall.dial()
debugger.log('********* LAUNCHED FIRST CALL ****************')
time.sleep(60)
#NEEDS TIME IN BETWEEN FOR THEM TO LEARN TO ANSWER
healthfax1 = calls.Call('00-healthfax1.call')
healthfax.dial()

raw_iput("PRESS ENTER WHEN YOU WANT TO SEND LAST FAX. THIS COMES AFTER BOTH THEY CALL AND FAX US")
healthfax2 = calls.Call('00-healthfax2.call')
healthfax.dial()
debugger.log('********* LAUNCHED HEALTHCHECK FAX ****************')