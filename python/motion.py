from gpiozero import MotionSensor

sensor = MotionSensor(26)


sensor.wait_for_motion()
sensor.wait_for_no_motion()

sensor.wait_for_motion()
print('motion!')