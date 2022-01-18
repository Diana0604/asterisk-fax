import os, utils, vlc, asterisk, easter_eggs
## =========================================== NEW ========================================
SOUNDS_PATH = '/fax/sounds/speaker/'
CONNECTED_CALL_PATH = SOUNDS_PATH + 'connected_call/'
POST_CALL_PATH = SOUNDS_PATH + 'post_call/'
PRE_CALL_PATH = SOUNDS_PATH + 'pre_call/'
BACKGROUND_SOUNDS_PATH = SOUNDS_PATH + 'background/'

CONNECTED_CALL_SOUNDS = os.listdir(CONNECTED_CALL_PATH)
POST_CALL_SOUNDS = os.listdir(POST_CALL_PATH)
PRE_CALL_SOUNDS = os.listdir(PRE_CALL_PATH)
background_sounds = os.listdir(BACKGROUND_SOUNDS_PATH)


diegetic_player = vlc.MediaPlayer()
diegetic_player.audio_set_volume(100)

def get_call_sound(step, path):
    #if diegetic sound has already played do not play again
    #if previous_step == step:
    #    return None
    #look for diegetic sound in this step
    for sound in path:
        if sound.startswith(step):
            return sound
    return None

def launch_connected_call_sound(step):
    connected_call_sound = get_call_sound(step, CONNECTED_CALL_SOUNDS)
    utils.debug("checking connected call")
    if connected_call_sound != None:
        if(asterisk.wait_call_on()):
            utils.debug("detected connected call on")
            connected_call_sound = CONNECTED_CALL_PATH + connected_call_sound
            background_player.audio_set_volume(50)
            diegetic_player.audio_set_volume(100)
            play_sound(sound = connected_call_sound, diegetic = True)
        else: 
            launch_connected_call_sound(step)

def launch_post_call_sound(step):
    post_call_sound = get_call_sound(step, POST_CALL_SOUNDS)
    if post_call_sound != None:
        post_call_sound = POST_CALL_PATH + post_call_sound
        background_player.audio_set_volume(50)
        diegetic_player.audio_set_volume(100)
        play_sound(sound = post_call_sound, diegetic = True)

#TO DO - randomize not by step
def launch_pre_call_sound(step):
    pre_call_sound = get_call_sound(step, PRE_CALL_SOUNDS)
    if pre_call_sound != None:
        pre_call_sound = PRE_CALL_PATH + pre_call_sound
        background_player.audio_set_volume(50)
        diegetic_player.audio_set_volume(100)
        play_sound(sound = pre_call_sound, diegetic = True)

#FINISH
def finish_diegetic_sounds():
    while diegetic_player.is_playing():
        utils.countdown(1)
    background_player.audio_set_volume(100)

def stop_call_sounds():
    diegetic_player.stop()

#COMMON METHODS
def get_player_wrapper(diegetic, background, easteregg):
    player_wrapper = [vlc.MediaPlayer()]
    if easteregg :
        player_wrapper = [easter_egg_player]
    if diegetic :
        player_wrapper = [diegetic_player]
    if background :
        player_wrapper = [background_player]
    return player_wrapper

def play_sound(sound, diegetic = False, background = False, easteregg = False):
    
    player_wrapper = get_player_wrapper(diegetic, background, easteregg)
    #if(background):
        #if(player_wrapper[0].is_playing()):
    #        return
    media = vlc.Media(sound)
    player_wrapper[0].set_media(media)
    player_wrapper[0].play()
    if ((not background and not easteregg)):
        utils.countdown(1)
    
    duration = media.get_duration()/1000
    return duration


## ========================================= OLD ============================================

#SOUNDS_FAX_PATH_BASE = '/fax/sounds/'
DIEGETIC_SOUNDS_PATH = SOUNDS_PATH
diegetic_sounds = os.listdir(DIEGETIC_SOUNDS_PATH)

previous_step = None

background_player = vlc.MediaPlayer()
background_player.audio_set_volume(100)
easter_egg_player = vlc.MediaPlayer()
easter_egg_player.audio_set_volume(100)
fax_player = vlc.MediaPlayer()
fax_player.audio_set_volume(100)

#GET SOUNDS FROM FOLDER
def get_background_sound(step):
    global previous_step
    for sound in background_sounds:
        initial_step = sound[0] + sound[1]
        last_step = sound[3]+sound[4]
        #check if step has background sound assigned
        if initial_step <= step and last_step >= step:
            #if background sound is not on return sound
            if background_player.is_playing() == 0:
                previous_step = step
                return sound
            #if background sound is on but has to be changed return sound
            if initial_step == step and previous_step != step:
                previous_step = step
                return sound
            #correct background sound is playing -> return None
            return None
    #no background sound found -> silence
    return 'silence'

def get_diegetic_sound(step):
    #if diegetic sound has already played do not play again
    if previous_step == step:
        return None
    #look for diegetic sound in this step
    for sound in diegetic_sounds:
        if sound.startswith(step):
            if step == '15':
                if sound.endswith(asterisk.get_from_database('agent') + '.wav'):
                    return sound
            else:
                return sound
    return None

#LAUNCHERS
def launch_background_sounds(step):
    #background sounds
    background_sound = get_background_sound(step)
    utils.debug(background_sound)
    if background_sound != None:
        if background_sound == 'silence':
            background_player.stop()
            return
        background_sound = BACKGROUND_SOUNDS_PATH + background_sound
        play_sound(sound = background_sound, background=True)
    

def launch_diegetic_sounds(step):
    global previous_step
    #diegetic sounds
    diegetic_sound = get_diegetic_sound(step)
    if diegetic_sound != None:
        asterisk.wait_fax_not_ringing()
        diegetic_sound = DIEGETIC_SOUNDS_PATH + diegetic_sound
        background_player.audio_set_volume(50)
        diegetic_player.audio_set_volume(100)
        play_sound(sound = diegetic_sound, diegetic = True)
    previous_step = step

def launch_easter_eggs(fax = False):
    egg_number = int(asterisk.get_from_database("soundegg"))
    if egg_number == 0:
         return
    if not fax and easter_eggs.is_fax(egg_number):
        return
    utils.debug(egg_number)
    sound = easter_eggs.get_easter_egg_sound(egg_number)
    if sound == None:
        return
    asterisk.wait_fax_not_ringing()
    play_sound(sound = sound, easteregg=True)
    asterisk.add_to_database("soundegg", "0")
    if egg_number == 100:
        while not asterisk.fax_free():
            utils.countdown(1)
        asterisk.add_to_database("step", '05')


#FINISH
def finish_easter_eggs_sounds():
    global easter_egg_player
    if not easter_egg_player.is_playing():
        return
    asterisk.wait_for_fax_free()
    easter_egg_player.stop()
    background_player.audio_set_volume(100)



#SPECIAL SOUNDS
def play_pre_show():
    sound = '/fax/sounds/speaker/pre_show_message.wav'
    duration = play_sound(sound)
    utils.countdown(duration)

def play_rescue():
    sound = '/fax/sounds/speaker/buttonreboot.wav'
    duration = play_sound(sound)
    utils.countdown(duration)
