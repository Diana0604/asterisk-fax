import sys
sys.path.insert(1, '/fax/python')
import calls

print("==================== Test 1 ===============================")
print("Test one is to receive a phone call. When the phone rings, pick up the handle. You should hear Eva saying: 'please dial your access code to begin'.")
print("Once you have heard the message, you can hang up (no need to enter access code).")
print("WARNING: If you pick up very quickly you may have to wait a few seconds before hearing it.")
raw_input("press enter when ready to test")

calls.launch_main_call('02')
calls.finish_main_call('02')

question = raw_input("Write OK if you have received 'Please dial your access code to begin'. Write anything else otherwise. ")


print("==================== Test 2 ===============================")
print("Test two is to receive a fax. When the phone rings, do not pick up. You should receive HEALTHCHECK 2")
raw_input("press enter when ready to test")

if question != "OK":
    print('ERROR => CALL FAILED!')
    sys.exit()

calls.launch_main_call('03')
calls.finish_main_call('03')

question = raw_input("Write OK if you have received HEALTHCHECK 2. Write anything else otherwise. ")

if question != "OK":
    print('ERROR => FAX FAILED!')
    sys.exit()

print("==================== Test 3 ===============================")
print("Test three is to make a call.")
print("You need to test that: ")
print("     1. You hear Eva asking you to describe the internet world")
print("     2. antsonstilts gmail receives your recorded message")

import asterisk
asterisk.add_to_database('step', '09')
question = raw_input("When ready, dial 2019. Write OK if test passed")

if question != "OK":
    print('ERROR => OUTGOING CALL FAILED!')
    sys.exit()


print("==================== Test 4 ===============================")
print("Test four is to send a fax. You can send anything")
print("You need to test that: ")
print("     1. The fax goes through")
print("     2. antsonstilts gmail receives your fax")

asterisk.add_to_database('step', '05')

question = raw_input("When ready, fax something to 456. Write OK if test passed")

if question != "OK":
    print('ERROR => OUTGOING FAX FAILED!')
    sys.exit()


print('======================================= CALLS - SUCCESS! ============================')