import os, utils, vlc, asterisk

SOUNDS_PATH = '/fax/sounds/speaker/'
DIEGETIC_SOUNDS_PATH = SOUNDS_PATH + 'diegetic/'
BACKGROUND_SOUNDS_PATH = SOUNDS_PATH + 'background/'
BUTTON_SOUNDS_PATH = SOUNDS_PATH + 'button/'
background_sounds = os.listdir(BACKGROUND_SOUNDS_PATH)
diegetic_sounds = os.listdir(DIEGETIC_SOUNDS_PATH)
button_sounds = os.listdir(BUTTON_SOUNDS_PATH)

background_player = vlc.MediaPlayer()
previous_step = None

diegetic_players = []

def get_diegetic_sound(step):
    if previous_step == step:
        return None
    for sound in diegetic_sounds:
        if sound.startswith(step):
            return sound
    return None

def get_background_sound(step):
    found = False
    for sound in background_sounds:
        initial_step = sound[0] + sound[1]
        last_step = sound[3]+sound[4]
        if initial_step <= step and last_step >= step:
            found = True
            if background_player.is_playing() == 0:
                return sound
            if initial_step == step and previous_step != step:
                return sound
    if not found:
        return 'silence'
    return None
            
def get_button_sound(step):
    for sound in button_sounds:
        if sound.startswith(step):
            return sound

def play_sound(sound, background):
    media = vlc.Media(sound)
    if background: 
        background_player.stop()
        background_player.set_media(media)
        background_player.play()
        return
    diegetic_player = vlc.MediaPlayer()
    diegetic_player.set_media(media)
    background_player.audio_set_volume(50)
    diegetic_player.play()
    diegetic_players.append(diegetic_player)

def finish_diegetic_sounds():
    global diegetic_players
    utils.countdown(1)
    for diegetic_player in diegetic_players:
        while diegetic_player.is_playing():
            utils.countdown(1)
    background_player.audio_set_volume(100)
    diegetic_players = []

def stop_background():
    background_player.stop()

def launch_sounds(step):
    print('managing sound')
    global previous_step
    print('last step was: ' + str(previous_step))
    diegetic_sound = get_diegetic_sound(step)
    print('we found this diegetic sound: ' + str(diegetic_sound))
    if diegetic_sound != None:
        print(diegetic_sound)
        diegetic_sound = DIEGETIC_SOUNDS_PATH + diegetic_sound
        play_sound(sound = diegetic_sound, background = False)
    background_sound = get_background_sound(step)
    print('we found this background sound' + str(background_sound))
    if background_sound != None:
        if background_sound == 'silence':
            stop_background()
        else :
            print(background_sound)
            background_sound = BACKGROUND_SOUNDS_PATH + background_sound
            play_sound(sound = background_sound, background = True)
    print('updateing last step to: ' + str(step))
    previous_step = step
