import sys
sys.path.insert(1, '/fax/python')
import calls

#calls.launch_main_call('02')
#calls.finish_main_call('02')

question = raw_input("Write OK if you have received 'Please dial your access code to begin'. Write anything else otherwise. ")

if question != "OK":
    print('ERROR => CALL FAILED!')
    sys.exit()

#calls.launch_main_call('03')
#calls.finish_main_call('03')

question = raw_input("Write OK if you have received HEALTHCHECK 2. Write anything else otherwise. ")

if question != "OK":
    print('ERROR => FAX FAILED!')
    sys.exit()

import asterisk
asterisk.add_to_database('step', '09')
question = raw_input("dial 2019. Write OK if you hear Eva saying you can hear internet world. Check it gets recorded and sent! ")

if question != "OK":
    print('ERROR => OUTGOING CALL FAILED!')
    sys.exit()

asterisk.add_to_database('step', '05')

question = raw_input("Send fax to 456. Write OK if it goes through (check email as well!) ")

if question != "OK":
    print('ERROR => OUTGOING FAX FAILED!')
    sys.exit()


print('======================================= CALLS - SUCCESS! ============================')