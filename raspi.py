import RPi.GPIO as GPIO

SENSOR_PIN  = 22
LED_PIN     = 23

class Raspi(object):

  def __init__(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR_PIN, GPIO.IN)
    GPIO.setup(LED_PIN, GPIO.OUT)

  def read_sensor(self):
    return GPIO.input(SENSOR_PIN)

  def change_led(self, value):
    GPIO.output(LED_PIN, value)
