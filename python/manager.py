import asterisk, utils, sounds
import alsaaudio
from gpiozero import MotionSensor, Button
from Call import Call
import json
import threading

class Manager : 
    def __init__(self, DEBUG = 0, current_step = 0):
      asterisk.reset_database()
      #general properties
      self.loop = True
      self.current_step = current_step
      self.previous_step = -1
      self.DEBUG = DEBUG
      

      #audio
      alsaaudio.Mixer(control="PCM").setvolume(100)
      
      #buttons
      self.reboot_button = Button(24)
      self.reboot_button.when_pressed = self.reboot
      
      #Motion Sensor
      self.pir = MotionSensor(26)
      print('motion sensor started')
      print(self.DEBUG)
      #wait for 1st motion at startup
      if not self.DEBUG :
        self.pir.wait_for_motion()
        self.pir.wait_for_no_motion()
    
    def background_sound(self):
      global run_threads
      while(run_threads):
        if(not sounds.background_player.is_playing()):
          #play bg sound
          sounds.play_sound('/fax/sounds/background/breathing.wav', background=True)
        utils.countdown(1)
      

    #reboot button stops loop
    def reboot(self):
       self.loop = False
    
    #start show
    def startShow(self):
      if not self.DEBUG :
        self.pir.wait_for_motion()
      
      #start bg sound
      self.background_thread = threading.Thread(target=self.background_sound)
      self.background_thread.start()
      
      
      
      while(self.loop):
        self.loop_step()
    
    #loop continuously running
    def loop_step(self):
      
      
      global step_info
      with open('/fax/performance.json') as f:
          json_data = json.load(f)
          if(self.current_step >= len(json_data)) :
            self.loop = False
            return
          step_info = json_data[self.current_step]
      
      #print(step_info)
      
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
          
          
          #check if needs playing
          should_play = True
          if "playIf" in sound_info :
            value = asterisk.get_from_database(sound_info["playIf"]["key"])
            if not (value in sound_info["playIf"]["values"]) :
              should_play = False
              continue
          if not should_play:
            continue

          #start playing sound and obtain duration in seconds
          duration = sounds.play_sound(sound_info["sound"], diegetic=True)
          if("wait" in sound_info) :
            duration = sound_info["wait"]
          
          #if there is no condition to stop sound, play until end
          if not "nextSoundIf" in sound_info :
            utils.countdown(duration)
            continue
          
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
      
      
      #duration = sounds.play_sound('/fax/sounds/step_change.wav', diegetic_sound=True)
      sounds.diegetic_player.pause()
      
      #wait one second in between steps
      utils.countdown(1)
            
      self.current_step += 1
        

manager = Manager(1,10)

#startButton = Button(23)
#startButton.wait_for_press()

run_threads = True

manager.startShow()

run_threads = False

manager.background_thread.join()