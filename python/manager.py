import calls, asterisk, utils

call_time = asterisk.get_timings()
call_wait = asterisk.get_waits()

while True:
    current_step = asterisk.check_current_step()
    print("we're on step: " + current_step)
    call_file = calls.get_call_file(current_step)
    print(call_file)
    if call_file != None:
        print('dialing call: ' + call_file)
        calls.dial(call_file, call_time[current_step])
        if call_wait[current_step] != None:
            utils.countdown(call_wait[current_step])
    

#print('END OF PROGRAM')