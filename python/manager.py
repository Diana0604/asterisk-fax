import calls, endpoint_status, utils

calls.dial('00-healthcall.call')

utils.countdown(60)

calls.dial('00-healthfax1.call')
print('fax  dialed')

print('END OF PROGRAM')