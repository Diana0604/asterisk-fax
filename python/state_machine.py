import utils, time
import asterisk
import lights, sounds, calls


PRE_IDLE = 0
AWAITING_CALL = 1
INCOMING_CALL = 2
CONNECTED_CALL = 3
POST_CALL = 4
OUTGOING_CALL = 5
PRE_CALL = 6

#TO DO:
# 00 => pre idle
#if call file exists => incoming call
#else => awaiting call
STEP_TO_STATE = [PRE_IDLE, INCOMING_CALL, AWAITING_CALL, PRE_CALL, AWAITING_CALL, PRE_CALL, AWAITING_CALL, PRE_CALL, AWAITING_CALL, PRE_CALL, PRE_CALL, PRE_CALL, PRE_CALL, PRE_CALL, AWAITING_CALL, AWAITING_CALL]

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
    global STEP_TO_STATE
    if(step == '00'):
      self.pre_idle(step)
      return
    if(step == '01'):
      self.incoming_call(step)
      return
    if(calls.step_has_call()):
      self.pre_call(step)
      return
    self.awaiting_call(step)
    
  def start_background(self, step):
    lights.launch_background_lights(step)
    sounds.launch_background_sounds(step)

  def keep_background_alive(self,step):
    while(asterisk.check_current_step() == step):
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
    sounds.launch_pre_call_sound(step)
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
    self.start_background(step)
    asterisk.wait_for_fax_free()
    if(calls.launch_main_call(step)):
      self.connected_call(step)
      return
    self.incoming_call(self, step)
  
  def connected_call(self, step):
    utils.debug("state: connected call")
    self.state = CONNECTED_CALL
    self.start_background(step)
    sounds.launch_connected_call_sound(step)
    while(not asterisk.fax_free()):
      self.start_background(step)
    utils.debug("fax seems free?")
    if(asterisk.call_on()):
      if(self.current_call == INCOMING_CALL):
        self.incoming_call(step)
        return
      asterisk.set_call_off()
    sounds.finish_diegetic_sounds()
    self.post_call(step)

  def post_call(self, step):
    self.state = POST_CALL
    utils.debug("we are on post call")
    sounds.launch_post_call_sound(step)
    sounds.finish_diegetic_sounds()
    asterisk.add_one_to_step(step)
    self.current_call = None
    if(calls.step_has_call()):
      self.pre_call(asterisk.check_current_step())
      return
    self.awaiting_call(asterisk.check_current_step())


    #next step
