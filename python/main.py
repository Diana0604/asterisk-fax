#REMEMBER TO CHANGE TO /fax BEFORE GITTING
import sys, time

#insert path to system
sys.path.insert(1, '/fax/python')

import music, debug, calls

debugger = debug.Debug(1)
currentPath = "/fax/"
#sounds
OPENING_THEME = currentPath + "audios/speaker/00-arrival.mp3"
BREATHING = currentPath + "audios/speaker/01-breathing.mp3"
CHARGING_UP = currentPath + "audios/speaker/02-charging_up.mp3"
HEARTBEAT = currentPath + "audios/speaker/03-breathing_hearbeat.mp3"
HEARTBEAT_INTENSE = currentPath + "audios/speaker/04-breathing_hearbeat_intense.mp3"
threads = []

#play first song



music.Audio(OPENING_THEME).play()

debugger.log('************ OPENING THEME FINISHED ************')
breathing = music.Audio(BREATHING, 1).play()

debugger.log('************ MACHINE IS BREATHING ************')

healthcall = calls.Call('00-healthcall.call')
time.sleep(30)
healthcall.dial()

debugger.log('********* LAUNCHED FIRST CALL ****************')


input("PRESS ENTER IF YOU WANT TO TRIGGER THE HEALTH FAX. THIS GOES AFTER THEY SEND A FAX")
healthfax = calls.Call('00-healthfax.call')
healthfax.dial()
debugger.log('********* LAUNCHED HEALTHCHECK FAX ****************')

time.sleep(100)
helloworld = calls.Call('01-helloworld.call')
helloworld.dial()
debugger.log('********* LAUNCHED HELLOWORLD FAX ****************')


input("PRESS ENTER IF YOU WANT TO TRIGGER THE FIRST TRUST EXERCISE. THIS SHOULD HAPPEN AFTER CHECKLIST IS SENT BACK.")
trust_exercise_1 = calls.Call('02-trust1.call')
trust_exercise_1.dial()
debugger.log('********* LAUNCHED TRUST EX 1 ****************')

input("PRESS ENTER IF YOU WANT TO TRIGGER THE SECOND TRUST EXERCISE. THIS HSOULD HAPPEN AFTER WE KNOW THEY HAVE CALLED NUMBER XXXX.")
trust_exercise_2 = calls.Call('02-trust2.call')
trust_exercise_2.dial()
debugger.log('********* LAUNCHED TRUST EX 2 ****************')

input("PRESS ENTER IF YOU WANT TO TRIGGER THE THIRD TRUST EXERCISE. THIS HSOULD HAPPEN AFTER WE KNOW THEY HAVE CALLED NUMBER XXXX.")
trust_exercise_3 = calls.Call('02-trust3.call')
trust_exercise_3.dial()
debugger.log('********* LAUNCHED TRUST EX 3 ****************')

input("PRESS ENTER IF YOU WANT TO TRIGGER THE ANTENNA FAX. THIS SHOULD HAPPEN AFTER WE RECEIVE XXX FAX FROM THEM.")
#antenna = calls.Call('03-antenna.call')
#antenna.dial()
debugger.log('***************** LAUNCHED ANTENNA ***********')

input("PRESS ENTER IF YOU WANT TO TRIGGER THE SPIES FAX. THIS SHOULD HAPPEN AFTER WE RECEIVE XXX CALL FROM THEM.")
#spies = calls.Call('04-spies.call')
#spies.dial()
debugger.log('***************** LAUNCHED SPIES CALL ***********')

input("PRESS ENTER IF YOU WANT TO TRIGGER THE MISSION FAX. THIS SHOULD HAPPEN AFTER WE RECEIVE XXX CALL FROM THEM.")
#spies = calls.Call('05-mission.call')
#spies.dial()
debugger.log('***************** LAUNCHED MISSION CALL ***********')

input("PRESS ENTER IF YOU WANT TO TRIGGER CONSIGNIA FAX. THIS SHOULD COME AFTER ALLERGIES")
charging = music.Audio(CHARGING_UP, 1)
threads.append(charging.play())
#consignia = calls.Call('06-consignia.call')
#consignia.dial()

debugger.log('********************* LAUNCHED CONSIGNIA CALL ***************')

input("PRESS WHEN LAST FAXES SHOULD COME THROUGH")
#calls.Call('07-laststeps1.call').dial()
music.Audio(HEARTBEAT,0).play()
debugger.log('********************* LAUNCHED FINAL STEPS EXPLAINED ***************')
heartbeat_intense = music.Audio(HEARTBEAT_INTENSE,1)
heartbeat_intense_thread = heartbeat_intense.play()
#calls.Call('07-laststeps2.call').dial()
debugger.log('********************* LAUNCHED FINAL STEP 1 ***************')
time.sleep(120)
#calls.Call('07-laststeps3.call').dial()
debugger.log('********************* LAUNCHED FINAL STEP 2 ***************')
time.sleep(300)
#calls.Call('07-laststeps4.call').dial()
debugger.log('********************* LAUNCHED FINAL STEP 3 ***************')
time.sleep(600)
heartbeat_intense_thread.join()
music.Audio(HEARTBEAT,1).play()
#calls.Call('07-laststeps5.call').dial()
debugger.log('********************* LAUNCHED FINAL STEP 4 ***************')

for thread in threads:
    thread.join()
