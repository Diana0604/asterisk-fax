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
CHARGING_UP = currentPath + "audios/speaker/02-charging_up.mp3"
HEARTBEAT = currentPath + "audios/speaker/03-breathing_hearbeat.mp3"
HEARTBEAT_INTENSE = currentPath + "audios/speaker/04-breathing_heartbeat_intense.mp3"
TBL_MONOLOGUE = currentPath + "audios/speaker/08-tbl_monologue1.wav"
threads = []
#lights
lightsController = lights.Lights()

debugger.log('************ MACHINE IS BREATHING ************')

healthcall = calls.Call('00-healthcall.call')
raw_input("PRESS ENTER IF YOU WANT TO TRIGGER THE HEALTH CALL")
healthcall.dial()
debugger.log('********* LAUNCHED FIRST CALL ****************')


raw_input("PRESS ENTER IF YOU WANT TO TRIGGER THE HEALTH FAX. THIS GOES AFTER THEY SEND A FAX")
#NEEDS TIME IN BETWEEN FOR THEM TO LEARN TO ANSWER
healthfax = calls.Call('00-healthfax.call')
healthfax.dial()
debugger.log('********* LAUNCHED HEALTHCHECK FAX ****************')
#KNOW WHEN THAT FAX IS DONE?
raw_input("PRESS ENTER IF YOU WANT TO TRIGGER THE HELLO WORLD. MAKE SURE HEATHLINE FAX HAS GONE THROUGH")
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

raw_input("PRESS ENTER IF YOU WANT TO TRIGGER THE ANTENNA FAX. THIS SHOULD HAPPEN AFTER WE RECEIVE XXX FAX FROM THEM.")
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

raw_input("PRESS ENTER IF YOU WANT TO TRIGGER CONSIGNIA FAX. THIS SHOULD COME AFTER ALLERGIES")
charging = music.Audio(CHARGING_UP, 1)
threads.append(charging.play())
#time.sleep(20)
lightsController.red()
consignia = calls.Call('06-consignia.call')
consignia.dial()

debugger.log('********************* LAUNCHED CONSIGNIA CALL ***************')

raw_input("PRESS WHEN LAST FAXES SHOULD COME THROUGH")
lightsController.purple()
calls.Call('07-laststeps1.call').dial()
debugger.log('********************* LAUNCHED FINAL STEPS EXPLAINED ***************')
music.Audio(HEARTBEAT,1).play()
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
for thread in threads:
    thread.join()
