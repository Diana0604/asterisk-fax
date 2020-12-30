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
easter_egg_players = []

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

def play_diegetic_sound(sound):
    asterisk.wait_fax_not_ringing()
    media = vlc.Media(sound)
    diegetic_player.set_media(media)
    background_player.audio_set_volume(50)
    diegetic_player.audio_set_volume(100)
    diegetic_player.play()

def play_background_sound(sound):
    media = vlc.Media(sound)
    background_player.stop()
    background_player.set_media(media)
    background_player.play()
    utils.countdown(1)

def launch_easter_eggs():
    egg_number = int(asterisk.get_from_database("soundegg"))
    print('found egg number')
    print(egg_number)
    if egg_number == 0:
        return
    sound = easter_eggs.get_easter_egg_sound(egg_number)
    if sound == None:
        return
    play_easter_egg(sound)
    print ('is playing')
    asterisk.add_to_database("soundegg", "0")

def play_easter_egg(sound):
    asterisk.wait_fax_not_ringing()
    media = vlc.Media(sound)
    easter_egg_player = vlc.MediaPlayer()
    easter_egg_player.set_media(media)
    background_player.audio_set_volume(50)
    easter_egg_player.audio_set_volume(100)
    easter_egg_player.play()
    easter_egg_players.append(easter_egg_player)

def launch_background_sounds(step):
    #background sounds
    background_sound = get_background_sound(step)
    if background_sound != None:
        if background_sound == 'silence':
            background_player.stop()
            return
        background_sound = BACKGROUND_SOUNDS_PATH + background_sound
        play_background_sound(sound = background_sound)

def launch_diegetic_sounds(step):
    global previous_step
    #diegetic sounds
    diegetic_sound = get_diegetic_sound(step)
    if diegetic_sound != None:
        diegetic_sound = DIEGETIC_SOUNDS_PATH + diegetic_sound
        play_diegetic_sound(sound = diegetic_sound)
        utils.countdown(1)
    previous_step = step

def finish_easter_eggs_sounds():
    global easter_egg_players
    found = False
    for easter_egg_player in easter_egg_players:
        if easter_egg_player.is_playing():
            found = True
    if not found : 
        easter_egg_players = []
        return
    asterisk.wait_for_fax_free()
    for easter_egg_player in easter_egg_players:
        while easter_egg_player.is_playing():
            easter_egg_player.stop()
    background_player.audio_set_volume(100)
    easter_egg_players = []

def finish_diegetic_sounds(step):
    global diegetic_players
    for sound in diegetic_sounds:
        last_step = sound[3]+sound[4]
        if last_step == step:
            while diegetic_player.is_playing():
                utils.countdown(1)
            return

def play_pre_show():
    player = vlc.MediaPlayer()
    media = vlc.Media('/fax/sounds/speaker/pre_show_message.wav')
    player.set_media(media)
    player.play()
    utils.countdown(1)
    duration = media.get_duration()/1000
    utils.countdown(duration)