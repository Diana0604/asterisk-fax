from gpiozero import MotionSensor

sensor = MotionSensor(26)

i = 0
while(True) :
  i = i + 1
  sensor.wait_for_motion()
  print('motion!', i)
  if(i >= 100):
    i = i % 100