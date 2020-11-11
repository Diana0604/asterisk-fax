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

def manage_calls(step):
    call_file = get_call_file(step)
    if call_file != None:
        print('dialing call: ' + call_file)
        dial(call_file)

def get_call_file(step):
    for call_file in call_files:
        if call_file.startswith(step):
            return call_file

def remove_files_from(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def dial(call):
    while not asterisk.fax_free():
        print('fax is not free - waiting for it to be free')
        time.sleep(1)
    
    call_file = CALLS_PATH + call
    outgoing_call = OUTGOING_PATH + call
    print('making call: ' + call)
    copyfile( call_file, outgoing_call)
    
    asterisk.error()

    error = False

    while asterisk.fax_free() and not error:
        time.sleep(1)
        error = asterisk.error()
        if error:
            utils.countdown(10)
            dial(call)
            print('resending: ' + call)
            return

    remove_files_from(OUTGOING_PATH)

    while not asterisk.fax_free() and not error:
        time.sleep(1)
        error = asterisk.error()
        if error:
            utils.countdown(10)
            dial(call)
            return
    utils.countdown(20)