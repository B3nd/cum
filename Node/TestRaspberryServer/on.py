import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(2, gpio.OUT)
gpio.output(2, gpio.HIGH)

