from shutil import copyfile
import shutil
import debug
import time

OUTGOING_PATH = '/var/spool/asterisk/outgoing/'
CALLS_PATH = '/fax/calls/'

debugger = debug.Debug(1)

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

def dial(call):
    call_file = CALLS_PATH + call
    outgoing_call = OUTGOING_PATH + call
    copyfile( call_file, outgoing_call)

