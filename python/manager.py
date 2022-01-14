import buttons
import calls, asterisk, utils, sounds, lights, smoke, easter_eggs
import alsaaudio, datetime, os, time

utils.send_email('machine is on, show has begun')

#alsaaudio.Mixer(control=alsaaudio.Mixer().mixer()).setvolume(100)
alsaaudio.Mixer(control="Headphone").setvolume(100)

now = datetime.datetime.now()

current_step = asterisk.check_current_step()
if current_step == "31":
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
    buttons.launch_buttons(current_step)
    sounds.launch_diegetic_sounds(current_step)
    lights.launch_diegetic_lights(current_step)
    smoke.launch_smoke(current_step)

def launch_easter_eggs():
    if calls.launch_easter_eggs():
        sounds.launch_easter_eggs(fax = True)
    else:
        sounds.launch_easter_eggs(fax = False)
    sounds.finish_easter_eggs_sounds()

while current_step != "31":
    #get current step
    current_step = asterisk.check_current_step()

    #make sure background sound is playing
    sounds.launch_background_sounds(current_step)

    #launch main call
    calls.launch_main_call(current_step)

    #if we're on new step -> launch diegetics
    if previous_step != current_step:
        launch_diegetics()

    if not diegetics_running():
        launch_easter_eggs()
    
    #FINISH
    #finish diegetic lights and send background
    lights.finish_diegetic_lights()
    lights.launch_background_lights(current_step)
    #finish diegetic sounds
    sounds.finish_diegetic_sounds(current_step)
    
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
