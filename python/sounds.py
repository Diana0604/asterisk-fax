import os, utils, vlc, asterisk, easter_eggs

SOUNDS_PATH = '/fax/sounds/speaker/'
DIEGETIC_SOUNDS_PATH = SOUNDS_PATH + 'diegetic/'
BACKGROUND_SOUNDS_PATH = SOUNDS_PATH + 'background/'
background_sounds = os.listdir(BACKGROUND_SOUNDS_PATH)
diegetic_sounds = os.listdir(DIEGETIC_SOUNDS_PATH)

previous_step = None

background_player = vlc.MediaPlayer()
background_player.audio_set_volume(100)
diegetic_player = vlc.MediaPlayer()
diegetic_player.audio_set_volume(100)
easter_egg_player = vlc.MediaPlayer()
easter_egg_player.audio_set_volume(100)

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
                return sound
            #if background sound is on but has to be changed return sound
            if initial_step == step and previous_step != step:
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
        utils.countdown(1)
    previous_step = step

def launch_easter_eggs():
    egg_number = int(asterisk.get_from_database("soundegg"))
    print('found egg number')
    print(egg_number)
    if egg_number == 0:
        return
    sound = easter_eggs.get_easter_egg_sound(egg_number)
    if sound == None:
        return
    asterisk.wait_fax_not_ringing()
    play_sound(sound = sound, easteregg=True)
    print ('is playing')
    asterisk.add_to_database("soundegg", "0")

#FINISH
def finish_diegetic_sounds(step):
    for sound in diegetic_sounds:
        last_step = sound[3]+sound[4]
        if last_step == step:
            while diegetic_player.is_playing():
                utils.countdown(1)
            break
    background_player.audio_set_volume(100)

def finish_easter_eggs_sounds():
    global easter_egg_player
    if not easter_egg_player.is_playing():
        return
    asterisk.wait_for_fax_free()
    easter_egg_player.stop()
    background_player.audio_set_volume(100)

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
    media = vlc.Media(sound)
    player_wrapper[0].set_media(media)
    player_wrapper[0].play()
    utils.countdown(1)
    duration = media.get_duration()/1000
    return duration

#SPECIAL SOUNDS
def play_pre_show():
    sound = '/fax/sounds/speaker/pre_show_message.wav'
    duration = play_sound(sound)
    utils.countdown(duration)

def play_rescue():
    sound = '/fax/sounds/speaker/buttonreboot.wav'
    duration = play_sound(sound)
    utils.countdown(duration)