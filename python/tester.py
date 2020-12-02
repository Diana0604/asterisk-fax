from shutil import copyfile
import shutil
import os
import time
import asterisk
import utils

#OUTGOING_PATH = 
OUTGOING_PATH = '/var/spool/asterisk/outgoing/'
CALLS_PATH = '/fax/calls/'
call_files = os.listdir(CALLS_PATH)

NOT_CALLING = False
call = raw_input("what call do you want to dial?")

call_file = CALLS_PATH + call
outgoing_call = OUTGOING_PATH + call
print('making call: ' + call)
asterisk.error()
copyfile( call_file, outgoing_call)

error = False

while asterisk.fax_free() and not error:
    time.sleep(1)
    error = asterisk.error()
    if error:
        utils.countdown(10)
        print('resending: ' + call)
        launch_call(step)
        break