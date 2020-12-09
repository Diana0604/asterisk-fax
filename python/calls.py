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

def get_call_file(step):
    for call_file in call_files:
        if call_file.startswith(step):
            return call_file

def launch_main_call(step):
    #get call file
    call = get_call_file(step)
    if call == None:
        return
    #launch call
    launch_call(call)

def finish_main_call(step):
    #get call file
    call = get_call_file(step)
    if call == None:
        return
    #finish call
    finish_call(call)

def launch_call(call):
    #wait for fax to be ready to receive
    print('waiting for fax to be free')
    asterisk.wait_for_fax_free()
    print('getting paths')
    #get call paths
    call_file = CALLS_PATH + call
    outgoing_call = OUTGOING_PATH + call
    #get rid of residual error
    asterisk.error()

    #make call
    copyfile( call_file, outgoing_call)
    #wait for call to begin
    print('waiting for fax to be busy')
    success = asterisk.wait_for_fax_busy()

    #check if error
    if not success:
        utils.countdown(3)
        launch_call(call)
        return

    #remove file from outgoing folder
    utils.remove_files_from(OUTGOING_PATH)

def finish_call(call):
    #wait for call to complete
    success = asterisk.wait_for_fax_free()
    #check if error
    if not success:
        print('found error')
        print('success: ' + str(success))
        utils.countdown(3)
        launch_call(call)
        return