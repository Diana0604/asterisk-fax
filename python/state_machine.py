import utils
import asterisk
import lights, sounds


PRE_IDLE = 0
IDLE = 1


STEP_TO_STATE = [PRE_IDLE, IDLE]

class StateMachine:
  global PRE_IDLE
  global IDLE
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


  def pre_idle(self, step):
    self.state = PRE_IDLE
    lights.launch_background_lights(step)
    while(asterisk.check_current_step == step):
      utils.debug("pre_idle state: awaiting for next step")
    #at end of pre_idle always goes to idle
    self.idle(asterisk.check_current_step)


  def idle(self, step):
    self.state = IDLE
    lights.launch_background_lights(step)
    sounds.launch_background_sounds(step)
    while(asterisk.check_current_step == step):
      utils.debug("idle state: awaiting for next step")
