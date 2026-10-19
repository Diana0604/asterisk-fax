import sys, version
sys.path.insert(1, '/fax/python')
import buttons, asterisk

asterisk.add_to_database('step', '25')
buttons.launch_buttons('25')

question = version.get_input("press BIG RED BUTTON. Press ENTER when you are done. ")

print(asterisk.check_current_step())

if(asterisk.check_current_step() != '26'):
    print('ERROR => BIG RED BUTTON DID NOT CHANGE STEP!')
    sys.exit()

question = version.get_input("press RESQUE button and check if machine sends resque to our email. Write OK if success. ")

if question != "OK":
    print('ERROR => RESQUE FAILED!')
    sys.exit()

version.get_input("press REBOOT button and check if machine reboots. You will have to start tests again. ")