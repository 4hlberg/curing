import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list wiht pin numbers

PINLIST = [22, 27, 17, 18]

#loop through pins and set mode and state to 'high'

for i in PINLIST:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)
    
#time to sleeo between operations in the main loop
    
    sleeptimeL = 1
    
# main loop

try:
    GPIO.output(22, GPIO.LOW)
    print("one"),
    time.sleep(sleeptimeL);
    GPIO.output(27, GPIO.LOW)
    print("two"),
    time.sleep(sleeptimeL);
    GPIO.output(17, GPIO.LOW)
    print("three"),
    time.sleep(sleeptimeL);
    GPIO.output(18, GPIO.LOW)
    print("four"),
    time.sleep(sleeptimeL);
    GPIO.cleanup()
    print("done")
    
except KeyboardInterrupt:
    print("COWARD")
    
    GPIO.cleanup()
    
