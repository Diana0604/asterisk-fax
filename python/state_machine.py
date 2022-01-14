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
    print("found step: " + step)
    print("needs state: " + str(STEP_TO_STATE[int(step)]))
    print("to compare with: " + str(PRE_IDLE) + " and " + str(IDLE))
    if(STEP_TO_STATE[int(step)] == PRE_IDLE):
      self.pre_idle(step)
      return
    if(STEP_TO_STATE[int(step)] == IDLE):
      self.idle(step)
      return


  def pre_idle(self, step):
    self.state = PRE_IDLE
    lights.launch_background_lights(step)
    utils.debug("set state: pre_idle")
    while(asterisk.check_current_step() == step):
      #utils.debug("pre_idle state: awaiting for next step")
      continue
    #at end of pre_idle always goes to idle
    #self.idle(asterisk.check_current_step)


  def idle(self, step):
    self.state = IDLE
    lights.launch_background_lights(step)
    sounds.launch_background_sounds(step)
    utils.debug("set state: idle")
    while(asterisk.check_current_step == step):
      #utils.debug("idle state: awaiting for next step")
      continue
