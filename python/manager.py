import asterisk, utils, sounds, lights, smoke, easter_eggs
import alsaaudio, datetime, os
from gpiozero import MotionSensor, Button
from Call import Call
import json

class Manager : 
    def __init__(self, DEBUG = 0):
      #general properties
      self.loop = True
      self.current_step = 0
      self.previous_step = -1
      self.DEBUG = DEBUG
      

      #audio
      alsaaudio.Mixer(control="PCM").setvolume(100)
      
      #buttons
      self.reboot_button = Button(23)
      self.reboot_button.when_pressed = self.reboot
      
      #Motion Sensor
      self.pir = MotionSensor(26)
      #wait for 1st motion at startup
      if not self.DEBUG :
        self.pir.wait_for_motion()
        self.pir.wait_for_no_motion()

    #reboot button stops loop
    def reboot(self):
       self.loop = False
    
    #start show
    def startShow(self):
      if not self.DEBUG :
        self.pir.wait_for_motion()
      print('starting show')
      while(self.loop):
        self.loop_step()
    
    #loop continuously running
    def loop_step(self):
      
      
      global step_info
      with open('steps_description.json') as f:
          json_data = json.load(f)
          if(self.current_step >= len(json_data)) :
            self.loop = False
            return
          step_info = json_data[self.current_step]
      
      #print(step_info)
      
      #check call
      if("callFile" in step_info) :
        current_call = Call(step_info["callFile"])
        current_call.launch_call()
      
      #check sound
      if("diegeticSound" in step_info) : 
        sound_info = step_info["diegeticSound"]
        duration = sounds.play_sound(sound_info["soundFile"], diegetic=True)
        print(duration)
        utils.countdown(sound_info["duration"])
        
      
      self.current_step += 1
        

manager = Manager(1)

manager.startShow()