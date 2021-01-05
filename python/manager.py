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
current_step = asterisk.check_current_step()
if len(previous_step) == 1:
    previous_step = '0' + previous_step

#if previous_step != '-1':
    #sounds.play_rescue()

def diegetics_running():
    if sounds.diegetic_player.is_playing():
        return True
    if calls.DIEGETIC_CALLS_ON:
        return True
    if lights.DIEGETIC_LIGHTS_ON:
        return True
    return False

while current_step != "30":
    current_step = asterisk.check_current_step()
    #INIT
    #make sure background sound is playing
    sounds.launch_background_sounds(current_step)
    #if we're on new step -> launch diegetics
    launch_diegetic = False
    if previous_step != current_step:
        calls.launch_main_call(current_step)
        sounds.launch_diegetic_sounds(current_step)
        lights.launch_diegetic_lights(current_step)
        smoke.launch_smoke(current_step)
    
    if not diegetics_running():
        calls.launch_easter_eggs()
        sounds.launch_easter_eggs()
        sounds.finish_easter_eggs_sounds()
    
    #FINISH
    #finish diegetic lights and send background
    lights.finish_diegetic_lights()
    lights.launch_background_lights(current_step)
    #wait for every process to be done
    calls.finish_main_call(current_step)
    sounds.finish_diegetic_sounds(current_step)

    asterisk.wait_for_fax_free()
    easter_eggs.reset()
    
    #UPDATE
    if previous_step == current_step:
        asterisk.update_step(current_step)
    previous_step = current_step

    #CHECK IF CONNECTED AND RECONNECT OTHERWISE
    utils.check_for_wifi()

now = datetime.datetime.now()
finish_time = now + datetime.timedelta(minutes=30)

lights.launch_background_lights(current_step)

while datetime.datetime.now() < finish_time:
        calls.launch_easter_eggs()
        sounds.launch_easter_eggs()
        sounds.finish_easter_eggs_sounds()

lights.launch_diegetic_lights(current_step)
lights.finish_diegetic_lights()
asterisk.update_step(current_step)

print('END OF PROGRAM')
