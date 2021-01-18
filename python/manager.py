import calls, asterisk, utils, sounds, lights, buttons, smoke, easter_eggs
import alsaaudio, datetime, os

#alsaaudio.Mixer(control=alsaaudio.Mixer().mixer()).setvolume(100)
alsaaudio.Mixer(control="Headphone").setvolume(100)

now = datetime.datetime.now()

## yyyy/mm/dd/hh/mm
show_date = datetime.datetime(2020, 1, 7, 14, 30) 

if show_date > now:
    sounds.play_pre_show()
    os.system('poweroff')
    exit()

current_step = asterisk.check_current_step()
if current_step == "30":
    if asterisk.database_exists("finish_time"):
        finish_time = datetime.datetime.strptime(asterisk.get_from_database("finish_time").replace('SPACE', ' '), '%Y-%m-%d %H:%M:%S.%f')
        if finish_time + datetime.timedelta(minutes=30) < now:
            asterisk.update_step(current_step)

previous_step = str(int(current_step) - 1)

if len(previous_step) == 1:
    previous_step = '0' + previous_step

asterisk.resest_easter_eggs()

if utils.DEBUG < 2 and previous_step != '-1':
    sounds.play_rescue()

def diegetics_running():
    if sounds.diegetic_player.is_playing():
        return True
    if calls.DIEGETIC_CALLS_ON:
        return True
    if lights.DIEGETIC_LIGHTS_ON:
        return True
    return False

def launch_diegetics():
    sounds.launch_diegetic_sounds(current_step)
    lights.launch_diegetic_lights(current_step)
    smoke.launch_smoke(current_step)

def launch_easter_eggs():
    if calls.launch_easter_eggs():
        sounds.launch_easter_eggs(fax = True)
    else:
        sounds.launch_easter_eggs(fax = False)
    sounds.finish_easter_eggs_sounds()

while current_step != "30":
    current_step = asterisk.check_current_step()
    #INIT
    #make sure background sound is playing
    sounds.launch_background_sounds(current_step)
    #if we're on new step -> launch diegetics
    launch_diegetic = False
    calls.launch_main_call(current_step)
    if previous_step != current_step:
        launch_diegetics()

    if not diegetics_running():
        launch_easter_eggs()
    
    #FINISH
    #finish diegetic lights and send background
    lights.finish_diegetic_lights()
    lights.launch_background_lights(current_step)
    #wait for every process to be done
    calls.finish_main_call(current_step)
    sounds.finish_diegetic_sounds(current_step)
    if diegetics_running():
        asterisk.wait_for_fax_free()
    #easter_eggs.reset()
    
    #UPDATE
    if previous_step == current_step:
        asterisk.update_step(current_step)
    previous_step = current_step

    #CHECK IF CONNECTED AND RECONNECT OTHERWISE
    utils.check_for_wifi()

now = datetime.datetime.now()

#get finish time and store to database
finish_time = now + datetime.timedelta(minutes=30)
print('ADDING; ' + str(finish_time).replace(' ', 'SPACE'))
asterisk.add_to_database("finish_time" , str(finish_time).replace(' ', 'SPACE'))

lights.launch_background_lights(current_step)

while datetime.datetime.now() < finish_time:
    launch_easter_eggs()

lights.launch_diegetic_lights(current_step)
lights.finish_diegetic_lights()
asterisk.update_step(current_step)

utils.debug('END OF PROGRAM')
