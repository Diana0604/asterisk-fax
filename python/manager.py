import calls, asterisk, utils, sounds, alsaaudio
alsaaudio.Mixer(control="Headphone").setvolume(100)
sounds.update_database()


while True:
    current_step = asterisk.check_current_step()
    print("we're on step: " + current_step)
    #sounds.manage_sounds(current_step)
    calls.manage_calls(current_step)


#print('END OF PROGRAM')