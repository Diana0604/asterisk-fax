from shutil import copyfile
import utils, asterisk


OUTGOING_PATH = '/var/spool/asterisk/outgoing/'
CALLS_PATH = '/fax/calls/'

class Call:
    def __init__(self, file):
        global OUTGOING_PATH
        global CALLS_PATH
        self.call_file = CALLS_PATH + file
        self.outgoing_call = OUTGOING_PATH + file
    
    def launch_call(self):
        global OUTGOING_PATH
        global CALLS_PATH
        if not asterisk.fax_available():
            asterisk.wait_fax_available()
        #wait for fax to be free
        asterisk.wait_for_fax_free()
        
        #get rid of residual errors
        asterisk.error()
        
        #make call
        copyfile(self.call_file, self.outgoing_call)
        
        #wait for call to begin
        success = asterisk.wait_for_fax_busy()
        
        #check if error
        if not success:
            utils.countdown(3)
            return self.launch_call()
        
        asterisk.wait_fax_not_ringing()

        #remove file from outgoing folder
        utils.remove_files_from(OUTGOING_PATH)
        
        return True
        
    def finish_call(self):
        #wait for call to complete
        success = asterisk.wait_for_fax_free()
        #check if error
        if not success:
            utils.debug('found error')
            utils.debug('success: ' + str(success))
            utils.countdown(3)
            return self.launch_call()
        return True
