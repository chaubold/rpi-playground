import RPi.GPIO as GPIO
import time
import atexit

# set up cleanup method
@atexit.register
def onExit():
    print("Cleanup being called")
    GPIO.cleanup()

# blink LED at port 21
GPIO.setmode(GPIO.BCM)
led=21
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 1)
time.sleep(5)
GPIO.output(led, 0)