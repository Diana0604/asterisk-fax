import calls, asterisk, utils, vlc, sounds

call_time = asterisk.get_timings()
call_wait = asterisk.get_waits()


while True:
    current_step = asterisk.check_current_step()
    print("we're on step: " + current_step)
    sounds.manage_sounds(current_step)
    calls.manage_calls(current_step)


#print('END OF PROGRAM')