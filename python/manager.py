import asterisk, utils, sounds
import alsaaudio
from gpiozero import MotionSensor, Button
from Call import Call
import json
import threading
import os
from merger import merge_loop

class Manager : 
    def __init__(self, DEBUG = 0, current_step = 0):
      asterisk.reset_database()
      #general properties
      self.loop = True
      self.current_step = current_step
      self.previous_step = -1
      self.DEBUG = DEBUG
      

      #audio
      try :
        alsaaudio.Mixer(control="PCM").setvolume(100) #audio jack
      except :
        alsaaudio.Mixer(control="Master").setvolume(100) #usb sound
      
      #buttons
      self.button = Button(26)
      
      #Motion Sensor
      # print('motion sensor started')
      print(self.DEBUG)
      #wait for 1st motion at startup
    
    def background_sound(self):
      global run_threads
      while(run_threads):
        play_background = asterisk.get_from_database("play_background")
        print("obtained play bg")
        print(play_background)
        if(play_background == "False") :
            print("not playing bg")
            if(sounds.background_player.is_playing()):
              sounds.background_player.pause()
            continue
        print("checking restart")
        if(not sounds.background_player.is_playing()):
          #play bg sound
          print("restarting bg")
          sounds.play_sound('/fax/sounds/background/bg_advert.wav', diegetic = False, background=True)
          sounds.background_player.audio_set_volume(45)
        utils.countdown(1)
      

    #reboot button stops loop
    def reboot(self):
      print('rebooting')
      global run_threads
      run_threads = False
      manager.background_thread.join()
      self.loop = False
      os.system('pkill python')
    
    #start show
    def startShow(self):
      # if not self.DEBUG :
      #   self.button.wait_for_press()
      
      #start bg sound
      self.background_thread = threading.Thread(target=self.background_sound)
      self.background_thread.start()
      
      
      
      while(self.loop):
        self.loop_step()
        
    def play_diegetic(self, sound_info, loop=0):
      #check if needs playing
      if "playIf" in sound_info :
        value = asterisk.get_from_database(sound_info["playIf"]["key"])
        if not (value in sound_info["playIf"]["values"]) :
          return

      #start playing sound and obtain duration in seconds
      duration = sounds.play_sound(sound_info["sound"], diegetic=True)
      if("wait" in sound_info) :
        duration = sound_info["wait"]
      
      #if there is no condition to stop sound, play until end
      if not "nextSoundIf" in sound_info :
        utils.countdown(duration)
        return
      
      #if there is condition to stop sound play until either:
      # 1. end reached
      #or
      #2. condition reached
      next_step = False
      while duration > 0 and not next_step:
        utils.countdown(1)
        #condition is checked on the asterisk databse
        value = asterisk.get_from_database(sound_info["nextSoundIf"]["key"])
        if value in sound_info["nextSoundIf"]["values"] :
          next_step = True
        duration = duration - 1
      
      if(not next_step) : 
        if("loop" in sound_info) :
          if("stopAfter" in sound_info) :
            if(loop > sound_info["stopAfter"]):
              return
          self.play_diegetic(sound_info, loop=loop+1)
    
    #loop continuously running
    def loop_step(self):      
      global step_info
      with open('/fax/performance.json') as f:
          json_data = json.load(f)
          if(self.current_step >= len(json_data)) :
            print("restarting show")
            self.current_step = 0
            return
          step_info = json_data[self.current_step]
        
      
      #check call - outgoing
      if("call" in step_info) :
        call_info = step_info["call"]
        current_call = Call(call_info["call"])
        current_call.launch_call()
        
        #wait time according to json instrucitons
        #1. manual wait -> wait for that time
        #2. no manual wait -> wait until call done
        if("wait" in call_info):
          utils.countdown(call_info["wait"])
        else :
          current_call.finish_call()
      
      #check call - incoming
      if("incomingCall" in step_info) :
        found = False
        
        while(not found) :
          utils.countdown(1)
          
          #condition is checked on the asterisk databse
          
          value = asterisk.get_from_database(step_info["incomingCall"]["key"])
          if (value == 'received') :
            found = True
      
      #check bg sound
      if("backgroundSound" in step_info) :
        sounds.play_sound(step_info["backgroundSound"])
      
      #check sound
      if("diegeticSounds" in step_info) :
        #get list of diegetic sounds from json
        all_sounds = step_info["diegeticSounds"]
        
        #loop through list of sounds
        for sound_info in all_sounds :
          self.play_diegetic(sound_info)
      
      
      if("buttonPress" in step_info) :
        print("waiting for press")
        self.button.wait_for_press()
      
      merge_loop()
      
      sounds.diegetic_player.pause()
      
      if("wait" in step_info) :
        utils.countdown(step_info["wait"])
      
      if("nextStepWhen" in step_info) :
        next_step_info = step_info["nextStepWhen"]
        change_step = False
        while(not change_step) : 
          utils.countdown(1)
          value = asterisk.get_from_database(next_step_info["key"])
          if(value in next_step_info["values"]):
            change_step = True
      
      #wait one second in between steps
      utils.countdown(1)
            
      self.current_step += 1
        

manager = Manager(DEBUG=False,current_step=5)

run_threads = True

manager.startShow()

run_threads = False

manager.background_thread.join()
