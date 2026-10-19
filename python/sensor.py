#from gpiozero import LED
from gpiozero import MotionSensor

pir = MotionSensor(26)

while True:
  print("waiting for motion")
  pir.wait_for_motion()
  print("motion detected")
  pir.wait_for_no_motion()
  print("no motion")
