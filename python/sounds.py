import os, utils, vlc, asterisk, easter_eggs

SOUNDS_PATH = '/fax/sounds/speaker/'
DIEGETIC_SOUNDS_PATH = SOUNDS_PATH + 'diegetic/'
BACKGROUND_SOUNDS_PATH = SOUNDS_PATH + 'background/'
BACKGROUND_LOOP_SOUNDS_PATH = BACKGROUND_SOUNDS_PATH + "loop/"
BACKGROUND_UNLOOP_SOUNDS_PATH = BACKGROUND_SOUNDS_PATH + "unloop/"
background_loop_sounds = os.listdir(BACKGROUND_LOOP_SOUNDS_PATH)
background_unloop_sounds = os.listdir(BACKGROUND_UNLOOP_SOUNDS_PATH)
diegetic_sounds = os.listdir(DIEGETIC_SOUNDS_PATH)

background_player = vlc.MediaPlayer()
previous_step = None
background_player.audio_set_volume(100)
diegetic_players = []
easter_egg_players = []

def get_diegetic_sound(step):
    #if diegetic sound has already played do not play again
    if previous_step == step:
        return None
    #look for diegetic sound in this step
    for sound in diegetic_sounds:
        if sound.startswith(step):
            if step == '15':
                print('GETTING STEP 15 SOUND')
                print('checking sound: ' + sound)
                print(asterisk.get_from_database('agent'))
                if sound.endswith(asterisk.get_from_database('agent') + '.wav'):
                    return sound
            else :
                return sound
    return None

def get_background_sound_loop(step):
    global previous_step
    for sound in background_loop_sounds:
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

def get_background_sound_unloop(step):
    global previous_step
    for sound in background_unloop_sounds:
        initial_step = sound[0] + sound[1]
        last_step = sound[3]+sound[4]
        #check if step has background sound assigned
        if initial_step == step and previous_step != step:
            return sound
        if initial_step <= step and last_step >= step:
            return 'playing'
    return None

def play_diegetic_sound(sound):
    asterisk.wait_fax_not_ringing()
    media = vlc.Media(sound)
    diegetic_player = vlc.MediaPlayer()
    diegetic_player.set_media(media)
    background_player.audio_set_volume(50)
    diegetic_player.audio_set_volume(100)
    diegetic_player.play()
    diegetic_players.append(diegetic_player)

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

def launch_background_loop_sounds(step):
    #background sounds
    background_sound = get_background_sound_loop(step)
    if background_sound != None:
        if background_sound == 'silence':
            return 'silence'
        background_sound = BACKGROUND_LOOP_SOUNDS_PATH + background_sound
        play_background_sound(sound = background_sound)

def launch_background_unloop_sounds(step):
    background_sound = get_background_sound_unloop(step)
    if background_sound == 'playing':
        return True
    if background_sound != None :
        play_background_sound(BACKGROUND_UNLOOP_SOUNDS_PATH + background_sound)
        return True
    return False

def finish_background_sounds(step):
    global previous_step
    for sound in background_unloop_sounds:
        initial_step = sound[0] + sound[1]
        last_step = sound[3]+sound[4]
        #check if step has background sound assigned
        if last_step == step:
            while background_player.is_playing():
                utils.countdown(1)


def launch_diegetic_sounds(step):
    global previous_step
    #diegetic sounds
    diegetic_sound = get_diegetic_sound(step)
    if diegetic_sound != None:
        diegetic_sound = DIEGETIC_SOUNDS_PATH + diegetic_sound
        play_diegetic_sound(sound = diegetic_sound)
        utils.countdown(1)
        previous_step = step
        return True
    previous_step = step
    return False

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

def finish_diegetic_sounds():
    global diegetic_players
    for diegetic_player in diegetic_players:
        while diegetic_player.is_playing():
            utils.countdown(1)
    background_player.audio_set_volume(100)
    diegetic_players = []

def play_pre_show():
    player = vlc.MediaPlayer()
    media = vlc.Media('/fax/sounds/speaker/pre_show_message.wav')
    player.set_media(media)
    player.play()
    utils.countdown(1)
    duration = media.get_duration()/1000
    utils.countdown(duration)