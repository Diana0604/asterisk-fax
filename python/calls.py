from shutil import copyfile
import os
import debug

OUTGOING_PATH = '/var/spool/asterisk/outgoing/'
CALLS_PATH = '/fax/calls/'

debugger = debug.Debug(1)

def dial(call):
    call_file = CALLS_PATH + call
    outgoing_call = OUTGOING_PATH + call
    if os.uname()[0] == 'Darwin':
        debugger.title('I AM NOT DIALING RIGHT NOW!')
        debugger.log('THIS WOULD COPY: '  + call_file + ' to ' + outgoing_call)
    else :
        copyfile( call_file, outgoing_call)
