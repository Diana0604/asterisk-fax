import os, debug, calls, music, utils
import multiprocessing
from time import sleep
import lights

CURRENT_PATH = ""
if os.uname()[0] != 'Darwin':
    CURRENT_PATH = "/fax/"

COUGHING = CURRENT_PATH + "audios/speaker/02-coughing.mp3"
BREATHING = CURRENT_PATH + "audios/speaker/01-breathing.mp3"
CHARGING_UP = CURRENT_PATH + "audios/speaker/03-charging_up.mp3"
SOUND11 = CURRENT_PATH + "audios/speaker/04-sound11.mp3"
SOUND12 = CURRENT_PATH + "audios/speaker/05-sound12.mp3"
SOUND13 = CURRENT_PATH + "audios/speaker/06-sound13.mp3"
SOUND14 = CURRENT_PATH + "audios/speaker/07-sound14.mp3"
SOUND15 = CURRENT_PATH + "audios/speaker/08-sound15.mp3"
TBL_MONOLOGUE = CURRENT_PATH + "audios/speaker/09-tbl.mp3"
FINALE = CURRENT_PATH + "audios/speaker/10-final.mp3"

PURPLE = (0.7,0,0.3)
RED = (1,0,0)
IRADESCENT = (0.5,0,0.5)

debugger = debug.Debug(1)
music_processes = []

def step1_healthcall():
    debugger.title('LAUNCHING HEALTHCHECK NUMBER 1')
    calls.dial('00-healthcall.call')
    debugger.title('HEALTHCHECK NUMBER 1 HAS BEEN LAUNCHED')
def step2_healthfax1():
    debugger.title('LAUNCHING HEALTHCHECK NUMBER 2')
    calls.dial('00-healthfax1.call')
    debugger.title('HEALTHCHECK NUMBER 2 HAS BEEN LAUNCHED')
def step3_healthfax2():
    debugger.title('LAUNCHING HEALTHCHECK NUMBER 3')
    calls.dial('00-healthfax2.call')
    debugger.title('HEALTHCHECK NUMBER 3 HAS BEEN LAUNCHED')
def step4_helloworld():
    debugger.title('LAUNCHING HELLOWORLD FAX')
    calls.dial('01-helloworld.call')
    debugger.title('HELLOWORLD FAX HAS BEEN LAUNCHED')
    lights_controller.fade_in_to(PURPLE)
def step5_trust1():
    debugger.title('LAUNCHING TRUST EXERCISE NUMBER 1')
    calls.dial('02-trust1.call')
    debugger.title('TRUST EXERCISE NUMBER 1 LAUNCHED')
def step6_trust2():
    debugger.title('LAUNCHING TRUST EXERCISE NUMBER 2')
    calls.dial('02-trust2.call')
    debugger.title('TRUST EXERCISE NUMBER 2 LAUNCHED')
def step7_trust3():
    debugger.title('LAUNCHING TRUST EXERCISE NUMBER 2')
    calls.dial('02-trust3.call')
    debugger.title('TRUST EXERCISE NUMBER 2 LAUNCHED')
def step8_antenna():
    debugger.title('LAUNCHING ANTENNA FAX')
    calls.dial('03-antenna.call')
    debugger.title('ANTENNA FAX LAUNCHED')
def step9_spies():
    debugger.title('LAUNCHING SPIES FAX')
    calls.dial('04-spies.call')
    debugger.title('SPIES FAX LAUNCHED')
def step10_mission():
    debugger.title('LAUNCHING MISSION FAX')
    calls.dial('05-mission.call')
    debugger.title('MISSION FAX LAUNCHED')
    debugger.title('PLAYING COUHGING')
    p = music.Audio(COUGHING, True).play()
    new_music_process(p)
    p.join()
    debugger.title('FINISHED PLAYING COUGHING')
    debugger.title('SETTING BREATHING ON BACKGROUND')
    new_music_process(music.Audio(BREATHING, True, True).play())
    debugger.title('MACHINE IS BREATHING')
def step11_consignia():
    lights_controller.fade_in_to(RED)
    debugger.title('LAUNCHING CONSIGNIA CALL')
    calls.dial('06-consignia.call')
    debugger.title('CONSIGNIA CALL LAUNCHED')
    debugger.title('SETTING CHARGE UP ON BACKGROUND')
    new_music_process(music.Audio(CHARGING_UP, True, True).play())
    debugger.title('MACHINE IS CHARGING UP')
    sleep(60)
    lights_controller.pulse()
def step12_laststeps_explained():
    debugger.title('LAUNCHING LAST STEPS EXPLANATION')
    calls.dial('07-laststeps1.call')
    debugger.title('LAST STEPS EXPLANATION LAUNCHED')
    debugger.title('SETTING SOUND11 ON BACKGROUND')
    new_music_process(music.Audio(SOUND11, True, False).play())
    debugger.title('SOUND 11 SET')
    lights_controller.fade_in_to(PURPLE)
def step13_laststeps():
    debugger.title('LAUNCHING LAST STEP 1')
    calls.dial('07-laststeps2.call')
    debugger.title('LAUNCHED LAST STEP 1')
    debugger.title('PLAYING SOUND 12')
    kill_all_processes()
    music.Audio(SOUND12).play()

    debugger.title('LAUNCHING LAST STEP 2')
    calls.dial('07-laststeps3.call')
    debugger.title('LAUNCHED LAST STEP 2')
    debugger.title('PLAYING SOUND 13')
    music.Audio(SOUND13).play()

    debugger.title('LAUNCHING LAST STEP 3')
    calls.dial('07-laststeps4.call')
    debugger.title('LAUNCHED LAST STEP 3')
    debugger.title('PLAYING SOUND 14')
    music.Audio(SOUND14).play()

    debugger.title('LAUNCHING LAST STEP 4')
    calls.dial('07-laststeps5.call')
    debugger.title('LAUNCHED LAST STEP 4')
    debugger.title('PLAYING SOUND 15')
    music.Audio(SOUND15).play()
    import button
    debugger.title('PLAYING TBL')
    music.Audio(TBL_MONOLOGUE).play()


def new_music_process(process):
    kill_all_processes()
    music_processes.append(process)

def kill_all_processes():
    debugger.title('KILLING PROCESSES')
    while len(music_processes) != 0:
        music_processes.pop().terminate()

def exit():
    debugger.title("KILLING PROCESSES")
    kill_all_processes()
    debugger.title("PROCESSES PROCESSES")


new_music_process(music.Audio(BREATHING, True, True).play())
lights_controller = lights.Controller()
lights_controller.change_color(IRADESCENT)