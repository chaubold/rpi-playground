import RPi.GPIO as GPIO
import time
import atexit

# set up cleanup method
@atexit.register
def onExit():
	print("Cleanup being called")
	GPIO.cleanup()

# setup inputs/outputs
GPIO.setmode(GPIO.BCM)

led = 21
GPIO.setup(led, GPIO.OUT)

button = 19
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# main loop
while True:
	inputState = GPIO.input(button)
	if inputState == False:
		print("Button pressed!")
		time.sleep(0.1)
		GPIO.output(led, 1)
	else:
		GPIO.output(led, 0)
	time.sleep(0.2)
