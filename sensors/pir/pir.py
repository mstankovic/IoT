import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
PIR_PIN=7
GPIO.setup(PIR_PIN, GPIO.IN)
print ("PIR Module Test (Ctrl+C to exit)")
time.sleep(2)
print ("Ready")
i=0
while True:
    if GPIO.input(PIR_PIN):
        i=i+1
        print ('Motion Detected! No: {}'.format(i))
    time.sleep(1)
