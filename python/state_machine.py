import utils, time
import asterisk
import lights, sounds, calls


PRE_IDLE = 0
IDLE = 1
INCOMING_CALL = 2


STEP_TO_STATE = [PRE_IDLE, INCOMING_CALL]

class StateMachine:
  global PRE_IDLE
  global IDLE
  global INCOMING_CALL
  state = PRE_IDLE
  #will need status has changed for diegetics launching only once but not implemented yet

  def __init__(self,step):
    global STEP_TO_STATE
    if(STEP_TO_STATE[int(step)] == PRE_IDLE):
      self.pre_idle(step)
      return
    if(STEP_TO_STATE[int(step)] == IDLE):
      self.idle(step)
      return
    if(STEP_TO_STATE[int(step)] == INCOMING_CALL):
      self.incoming_call(step)
      return

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


  def idle(self, step):
    utils.debug("state: idle")
    self.state = IDLE
    self.keep_background_alive(step)
    #self.keep_background_alive(step)

  def incoming_call(self, step):
    utils.debug("state: incoming call")
    self.state = INCOMING_CALL
    utils.debug("launching call for step: " + step)
    self.start_background(step)
    calls.launch_main_call(step)
    self.keep_background_alive(step)
