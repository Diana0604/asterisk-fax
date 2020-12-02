import calls, asterisk, utils, sounds, alsaaudio, lights
alsaaudio.Mixer(control="Headphone").setvolume(100)
#sounds.update_database()

while True:
    current_step = asterisk.check_current_step()
    print("we're on step: " + current_step)
    calls.launch_call(current_step)
    sounds.launch_sounds(current_step)
    lights.launch_lights(current_step)
    #wait for every process to be done
    calls.finish_call(current_step)
    sounds.finish_diegetic_sounds()
    lights.finish_diegetic_lights()
    #next step
    asterisk.update_step()

    


#print('END OF PROGRAM')