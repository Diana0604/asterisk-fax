from shutil import copyfile
import shutil
import os
import time
import endpoint_status

OUTGOING_PATH = '/var/spool/asterisk/outgoing/'
CALLS_PATH = '/fax/calls/'



NOT_CALLING = False

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

def dial(call, time_left_for_call):
    while not endpoint_status.fax_free():
        print('fax is not free - waiting for it to be free')
        time.sleep(1)
    
    call_file = CALLS_PATH + call
    outgoing_call = OUTGOING_PATH + call
    print('making call: ' + call)
    copyfile( call_file, outgoing_call)
    while endpoint_status.fax_free():
        print('fax is free - waiting for it to be busy')
        time.sleep(1)
    remove_files_from(OUTGOING_PATH)

    while(time_left_for_call > 0):
        time.sleep(1)
        print(time_left_for_call)
        if endpoint_status.fax_free():
            print('fax is free - need to resend')
            dial(call, time_left_for_call)
            return
        time_left_for_call = time_left_for_call - 1
   