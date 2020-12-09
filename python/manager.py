import calls, asterisk, utils, sounds, alsaaudio, lights, buttons, smoke, easter_eggs
alsaaudio.Mixer(control="Headphone").setvolume(100)
#sounds.update_database()

while True:
    current_step = asterisk.check_current_step()
    print("we're on step: " + current_step)
    calls.launch_main_call(current_step)
    sounds.launch_sounds(current_step)
    lights.launch_diegetic_lights(current_step)
    smoke.launch_smoke(current_step)
    easter_eggs.check_easter_eggs()
    #finish diegetic lights and send background
    lights.finish_diegetic_lights()
    lights.launch_background_lights(current_step)
    #wait for every process to be done
    calls.finish_main_call(current_step)
    sounds.finish_diegetic_sounds()
    #launch background lights
    #next step
    asterisk.update_step()

    


#print('END OF PROGRAM')