import os, utils, vlc

SOUNDS_PATH = '/fax/sounds/speaker/'
DIEGETIC_SOUNDS_PATH = SOUNDS_PATH + 'diegetic/'
BACKGROUND_SOUNDS_PATH = SOUNDS_PATH + 'background/'
BUTTON_SOUNDS_PATH = SOUNDS_PATH + 'button/'
diegetic_sounds = os.listdir(DIEGETIC_SOUNDS_PATH)
background_sounds = os.listdir(BACKGROUND_SOUNDS_PATH)
button_sounds = os.listdir(BUTTON_SOUNDS_PATH)

def get_diegetic_sound(step):
    for sound in diegetic_sounds:
        if sound.startswith(step):
            return sound

def get_background_sound(step):
    for sound in background_sounds:
        initial_step = sound[0] + sound[1]
        last_step = sound[3]+sound[4]
        if initial_step <= step and last_step >= step:
            if initial_step == step:
                return sound
            else:
                return None
            
def get_button_sound(step):
    for sound in button_sounds:
        if sound.startswith(step):
            return sound

def manage_sounds(step):
    diegetic_sound = DIEGETIC_SOUNDS_PATH + get_diegetic_sound(step)
    print(diegetic_sound)
    if diegetic_sound != None:
        player = vlc.MediaPlayer(diegetic_sound)
        player.play()
        utils.countdown(1)
        duration = player.get_length() / 1000
        utils.countdown(duration)
        player.stop()
    background_sound = BACKGROUND_SOUNDS_PATH + get_background_sound(step)
    print(background_sound)
    if background_sound != None:
        player = vlc.MediaPlayer(background_sound)
        player.play()



    # get diegetic sounds
    # play if needed
    # get background sounds
    # play if needed
    return

#current_step = asterisk.check_current_step()
#if current_step == '00':
#    player = vlc.MediaPlayer("/fax/audios/speaker/00-arrival.mp3")
#    player.play()
#    utils.countdown(1)
#    duration = player.get_length() / 1000
#    utils.countdown(duration)