import calls, endpoint_status, utils

calls.dial('00-healthcall.call', 163)
utils.countdown(5) # IMPORTANT: this time is taking into account we will add extra beeping. Remember to update if we don't do that in the end
calls.dial('00-healthfax1.call', 82)
print('fax  dialed')

print('END OF PROGRAM')