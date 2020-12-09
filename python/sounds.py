import os, utils, vlc, asterisk

SOUNDS_PATH = '/fax/sounds/speaker/'
DIEGETIC_SOUNDS_PATH = SOUNDS_PATH + 'diegetic/'
BACKGROUND_SOUNDS_PATH = SOUNDS_PATH + 'background/'
background_sounds = os.listdir(BACKGROUND_SOUNDS_PATH)
diegetic_sounds = os.listdir(DIEGETIC_SOUNDS_PATH)

background_player = vlc.MediaPlayer()
previous_step = None

diegetic_players = []

def get_diegetic_sound(step):
    #if diegetic sound has already played do not play again
    if previous_step == step:
        return None
    #look for diegetic sound in this step
    for sound in diegetic_sounds:
        if sound.startswith(step):
            return sound
    return None

def get_background_sound(step):
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
            
def play_diegetic_sound(sound):
    asterisk.wait_fax_not_ringing()
    diegetic_player = vlc.MediaPlayer()
    diegetic_player.set_media(media)
    background_player.audio_set_volume(50)
    diegetic_player.play()
    diegetic_players.append(diegetic_player)

def play_background_sound(sound):
    media = vlc.Media(sound)
    background_player.stop()
    background_player.set_media(media)
    background_player.play()

def launch_sounds(step):
    global previous_step
    #diegetic sounds
    diegetic_sound = get_diegetic_sound(step)
    if diegetic_sound != None:
        diegetic_sound = DIEGETIC_SOUNDS_PATH + diegetic_sound
        play_diegetic_sound(sound = diegetic_sound)
    #background sounds
    background_sound = get_background_sound(step)
    if background_sound != None:
        if background_sound == 'silence':
            background_player.stop()
        else :
            background_sound = BACKGROUND_SOUNDS_PATH + background_sound
            play_background_sound(sound = background_sound)
    #update step so we do not replay sounds
    previous_step = step

def finish_diegetic_sounds():
    global diegetic_players
    utils.countdown(1)
    for diegetic_player in diegetic_players:
        while diegetic_player.is_playing():
            utils.countdown(1)
    background_player.audio_set_volume(100)
    diegetic_players = []