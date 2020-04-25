import RPi.GPIO as GPIO
import time

ledPin = 12

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(ledPin, GPIO.LOW)
    
    p = GPIO.PWM(ledPin, 200)
    p.start(0)

def loop():
    while True:
        for dc in range(0, 101, 1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(.75)
        for dc in range(100,-1,-1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
            
def destroy():
    GPIO.cleanup()
    
if __name__ == '__main__':
    print ('Program is starting... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()