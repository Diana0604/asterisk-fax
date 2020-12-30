import calls, asterisk, utils, sounds, alsaaudio, lights, buttons, smoke, easter_eggs, datetime, os
#alsaaudio.Mixer(control=alsaaudio.Mixer().mixer()).setvolume(100)
alsaaudio.Mixer(control="Headphone").setvolume(100)

now = datetime.datetime.now()
## yyyy/mm/dd/hh/mm
show_date = datetime.datetime(2020, 1, 7, 14, 30) 

if show_date > now:
    sounds.play_pre_show()
    os.system('poweroff')
    exit()

#sounds.update_database()
previous_step = str(int(asterisk.check_current_step()) - 1)
if len(previous_step) == 1:
    previous_step = '0' + previous_step

while True:
    current_step = asterisk.check_current_step()
    #INIT
    #make sure background sound is playing
    looped_background = sounds.launch_background_loop_sounds(current_step)
    unlooped_background = sounds.launch_background_unloop_sounds(current_step)
    if looped_background == 'silence' and not unlooped_background:
        sounds.background_player.stop()
    #if we're on new step -> launch diegetics
    launch_diegetic = False
    if previous_step != current_step:
        if calls.launch_main_call(current_step):
            launch_diegetic = True
        if sounds.launch_diegetic_sounds(current_step):
            launch_diegetic = True
        if lights.launch_diegetic_lights(current_step):
            launch_diegetic = True
        if smoke.launch_smoke(current_step):
            launch_diegetic = True
    
    if not launch_diegetic:
        sounds.launch_easter_eggs()
        if calls.launch_easter_eggs():
            #TODO: make it into a wait
            asterisk.wait_for_fax_free()
        sounds.finish_easter_eggs_sounds()
    
    #FINISH
    #finish diegetic lights and send background
    lights.finish_diegetic_lights()
    lights.launch_background_lights(current_step)
    #wait for every process to be done
    calls.finish_main_call(current_step)
    sounds.finish_diegetic_sounds()
    sounds.finish_background_sounds(current_step)

    easter_eggs.reset()
    
    #UPDATE
    #current_step = asterisk.check_current_step()
    if previous_step == current_step:
        asterisk.update_step(current_step)
    previous_step = current_step

    


#print('END OF PROGRAM')