from shutil import copyfile
import os
import time
import utils, asterisk, easter_eggs

#OUTGOING_PATH = 
OUTGOING_PATH = '/var/spool/asterisk/outgoing/'
CALLS_PATH = '/fax/calls/'
call_files = os.listdir(CALLS_PATH)

DIEGETIC_CALLS_ON = False

def get_call_file(step):
    for call_file in call_files:
        if call_file.startswith(step):
            return call_file

def launch_main_call(step):
    global DIEGETIC_CALLS_ON
    #get call file
    call = get_call_file(step)
    if call == None:
        return False
    #launch call
    #DIEGETIC_CALLS_ON = True
    launch_call(call)
    return True

def call_is_ongoing():
    global DIEGETIC_CALLS_ON
    if(asterisk.fax_free()):
        return False
        #DIEGETIC_CALLS_ON = False
    return True

def finish_main_call(step):
    global DIEGETIC_CALLS_ON
    #get call file
    call = get_call_file(step)
    if call == None:
        return
    #finish call
    finish_call(call)
    DIEGETIC_CALLS_ON = False

def launch_call(call):
    if not asterisk.fax_available():
        asterisk.wait_fax_available()
    #wait for fax to be ready to receive
    if(not asterisk.fax_free()):
        return
    #get call paths
    call_file = CALLS_PATH + call
    outgoing_call = OUTGOING_PATH + call
    #get rid of residual error
    asterisk.error()

    #make call
    copyfile( call_file, outgoing_call)
    #wait for call to begin
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
        utils.debug('found error')
        utils.debug('success: ' + str(success))
        utils.countdown(3)
        launch_call(call)
        return

def launch_easter_eggs():
    egg_number = int(asterisk.get_from_database("faxegg"))
    utils.debug('found egg number')
    utils.debug(egg_number)
    if egg_number == 0:
        return False
    call = easter_eggs.get_easter_egg_call(egg_number)
    if call == None:
        return False
    call_file = '/fax/calls/eastereggs/' + call
    #wait for fax to be ready to receive
    asterisk.wait_for_fax_free()
    #get call paths
    outgoing_call = OUTGOING_PATH + call
    #get rid of residual error
    asterisk.error()
    #make call
    copyfile( call_file, outgoing_call)
    #wait for call to begin
    utils.debug('waiting for fax to be busy')
    success = asterisk.wait_for_fax_busy()

    #check if error
    if not success:
        utils.countdown(3)
        return launch_easter_eggs()
        
    #remove file from outgoing folder
    utils.remove_files_from(OUTGOING_PATH)
    
    easter_eggs.call_made(egg_number)
    asterisk.add_to_database('faxegg', '0')
    asterisk.add_to_database('faxegg' + str(egg_number), '1')
    return True
