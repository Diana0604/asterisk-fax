import utils, time
import asterisk
import lights, sounds, calls
import random_player_manager


PRE_IDLE = 0
AWAITING_CALL = 1
INCOMING_CALL = 2
CONNECTED_CALL = 3
POST_CALL = 4
OUTGOING_CALL = 5
PRE_CALL = 6

class StateMachine:
  global PRE_IDLE
  global AWAITING_CALL
  global INCOMING_CALL
  global POST_CALL
  global OUTGOING_CALL
  global PRE_CALL

  state = PRE_IDLE
  current_call = None
  #will need status has changed for diegetics launching only once but not implemented yet

  def __init__(self,step):
    utils.debug("init of state machine")
    if(step == '00'):
      self.pre_idle(step)
      return
    if(step == '01'):
      self.incoming_call(step)
      return
    if(step == '15'):
      self.post_call(step)
    if(calls.step_has_call()):
      self.pre_call(step)
      return
    self.awaiting_call(step)
    
  def start_background(self, step):
    utils.debug("================================ STARTING BACKGROUNDS ==================================")
    lights.launch_background_lights(step)
    sounds.launch_background_sounds(step)

  def keep_background_alive(self,step):
    while(not asterisk.fax_available()):
      self.start_background(step)
      time.sleep(1)
      continue

  def pre_idle(self, step):
    utils.debug("state: pre_idle")
    self.state = PRE_IDLE
    self.start_background(step)
    utils.countdown(10)
    asterisk.add_one_to_step(step)
    self.incoming_call(asterisk.check_current_step())

  def pre_call(self, step):
    self.state = PRE_CALL
    utils.debug("we are on pre call")
    self.start_background(step)
    sounds.launch_pre_call_sound(random_player_manager.get_random_number())
    utils.debug("finishing diegetic")
    sounds.finish_diegetic_sounds()
    self.incoming_call(step)


  def awaiting_call(self, step):
    utils.debug("state: awaiting call")
    self.state = AWAITING_CALL
    self.start_background(step)
    asterisk.wait_for_fax_busy()
    self.current_call = OUTGOING_CALL
    self.connected_call(step)

  def incoming_call(self, step):
    self.current_call = INCOMING_CALL
    asterisk.set_call_off()
    utils.debug("state: incoming call")
    self.state = INCOMING_CALL
    utils.debug("launching call for step: " + step)
    self.keep_background_alive(step)
    #asterisk.wait_for_fax_free()
    if(calls.launch_main_call(step)):
      self.connected_call(step)
      return
    self.incoming_call(self, step)
  
  def connected_call(self, step):
    utils.debug("state: connected call")
    self.state = CONNECTED_CALL
    self.start_background(step)

    #quite spagheti - must refactor
    counter = 0
    if(step == '03'):
      while(not asterisk.call_on()):
        time.sleep(1)
        if(asterisk.init_call_on() and asterisk.fax_free()):
          self.incoming_call(step)
          return

    sounds.launch_connected_call_sound(step)
    while(not asterisk.fax_free()):
      self.start_background(step)
    utils.debug("fax seems free")
    if(asterisk.call_on()):
      utils.debug("call was on at end")
      if(self.current_call == INCOMING_CALL):
        sounds.stop_call_sounds()
        self.incoming_call(step)
        return
      asterisk.set_call_off()
    sounds.finish_diegetic_sounds()
    self.post_call(step)

  def post_call(self, step):
    self.state = POST_CALL
    utils.debug("we are on post call")
    sounds.launch_post_call_sound(step)
    lights.launch_diegetic_lights(step)
    sounds.finish_diegetic_sounds()
    lights.finish_diegetic_lights()
    asterisk.add_one_to_step(step)
    self.current_call = None

    #if at end of sharing - UNCOMMENT TO TEST AND SEND
    if(int(asterisk.check_current_step()) >= 15):
      utils.debug('powering off')
      utils.countdown(20)
      asterisk.add_to_database("step", "00")
      os.system('poweroff')

    if(calls.step_has_call()):
      utils.countdown(5)
      self.pre_call(asterisk.check_current_step())
      return
    self.awaiting_call(asterisk.check_current_step())


    #next step
