import calls, asterisk, utils, sounds, alsaaudio, lights, buttons, smoke, easter_eggs
alsaaudio.Mixer(control="Headphone").setvolume(100)
#sounds.update_database()
easter_eggs.start_easter_eggs()
previous_step = 0
while True:
    current_step = asterisk.check_current_step()
    #INIT
    calls.launch_main_call(current_step)
    calls.launch_easter_eggs()
    sounds.launch_sounds(current_step)
    lights.launch_diegetic_lights(current_step)
    smoke.launch_smoke(current_step)
    
    #FINISH
    #finish diegetic lights and send background
    lights.finish_diegetic_lights()
    lights.launch_background_lights(current_step)
    #wait for every process to be done
    calls.finish_main_call(current_step)
    sounds.finish_easter_eggs_sounds()
    sounds.finish_diegetic_sounds()
    
    #UPDATE
    if previous_step == current_step:
        asterisk.update_step()
    previous_step = current_step

    


#print('END OF PROGRAM')