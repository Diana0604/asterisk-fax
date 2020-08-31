from shutil import copyfile

OUTGOING_PATH = '/var/spool/asterisk/outgoing/'
CALLS_PATH = '/fax/calls/'

class Call(object):
    def __init__(self, call):
        self.call = call
    
    def dial(self):
        #FIRST CHECK IF PJSIP/2000 IS FREE
        copyfile( CALLS_PATH + self.call, OUTGOING_PATH + self.call)
        #CHECK ASTERISK -R FOR ERRORS