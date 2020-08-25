#REMEMBER TO CHANGE TO /fax BEFORE GITTING
import sys, time

#insert path to system
sys.path.insert(1, '/fax/python')

import music, debug, calls

debugger = debug.Debug(1)
currentPath = "/fax/"
#sounds
OPENING_THEME = "audios/speaker/00-arrival.mp3"
BREATHING = currentPath + "audios/speaker/01-breathing.mp3"

threads = []

#play first song
#opening = music.Audio(OPENING_THEME)
#breathing = music.Audio(BREATHING, 1)

#opening.play()


debugger.log('************ OPENING THEME FINISHED ************')

#threads.append(breathing.play())

debugger.log('************ MACHINE IS BREATHING ************')

#healthcall = calls.Call('00-healthcall.call')
#time.sleep(30)
#healthcall.dial()

debugger.log('********* LAUNCHED FIRST CALL ****************')


debugger.checkpoint("PRESS ENTER IF YOU WANT TO TRIGGER THE HEALTH FAX. THIS GOES AFTER THEY SEND A FAX")
healthfax = calls.Call('00-healthfax.call')
healthfax.dial()

debugger.log('********* LAUNCHED HEALTHCHECK FAX ****************')

time.sleep(70)
debugger.log('********* LAUNCHED HELLOWORLD FAX ****************')
helloworld = calls.Call('01-helloworld.call')
helloworld.dial()
debugger.checkpoint("PRESS ENTER IF YOU WANT TO TRIGGER THE FIRST TRUST EXERCISE. THIS SHOULD HAPPEN AFTER CHECKLIST.")

for thread in threads:
    thread.join()
