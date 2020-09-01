#REMEMBER TO CHANGE TO /fax BEFORE GITTING
import sys, time

#insert path to system
sys.path.insert(1, '/fax/python')

import music, debug, calls, lights, utils
debugger = debug.Debug(1)
threads = []
#lights
lightsController = lights.Lights()

helloworld = calls.Call('01-helloworld.call')
helloworld.dial()
lightsController.purple()
debugger.log('********* LAUNCHED HELLOWORLD FAX ****************')


raw_input("PRESS ENTER IF YOU WANT TO TRIGGER THE FIRST TRUST EXERCISE. THIS SHOULD HAPPEN AFTER CHECKLIST IS SENT BACK.")
trust_exercise_1 = calls.Call('02-trust1.call')
trust_exercise_1.dial()
debugger.log('********* LAUNCHED TRUST EX 1 ****************')

raw_input("PRESS ENTER IF YOU WANT TO TRIGGER THE SECOND TRUST EXERCISE. THIS HSOULD HAPPEN AFTER WE KNOW THEY HAVE CALLED NUMBER XXXX.")
trust_exercise_2 = calls.Call('02-trust2.call')
trust_exercise_2.dial()
debugger.log('********* LAUNCHED TRUST EX 2 ****************')

raw_input("PRESS ENTER IF YOU WANT TO TRIGGER THE THIRD TRUST EXERCISE. THIS HSOULD HAPPEN AFTER WE KNOW THEY HAVE CALLED NUMBER XXXX.")
trust_exercise_3 = calls.Call('02-trust3.call')
trust_exercise_3.dial()
debugger.log('********* LAUNCHED TRUST EX 3 ****************')