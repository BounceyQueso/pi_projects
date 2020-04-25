import RPi.GPIO as GPIO
import time
import random

pins = {'redPin':11, 'greenPin':12, 'bluePin':13}

def setup():
    global pwmRed, pwmGreen, pwmBlue
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pins, GPIO.OUT)
    GPIO.setup(pins, GPIO.HIGH)
    pwmRed = GPIO.PWM(pins['redPin'], 2000)
    pwmRed.start(0)
    pwmGreen = GPIO.PWM(pins['greenPin'], 2000)
    pwmGreen.start(0)
    pwmBlue = GPIO.PWM(pins['bluePin'], 2000)
    pwmBlue.start(0)
    
def setColor(r_val, g_val, b_val):
    pwmRed.ChangeDutyCycle(r_val)
    pwmGreen.ChangeDutyCycle(g_val)
    pwmBlue.ChangeDutyCycle(b_val)

def loop():
    while True:
        r=random.randint(0,100)
        g=random.randint(0,100)
        b=random.randint(0,100)
        setColor(r,g,b)
        print ('r=%d, g=%d, b=%d' %(r,g,b))
        time.sleep(0.3)
            
def destroy():
    pwmRed.stop()
    pwmGreen.stop()
    pwmBlue.stop()
    GPIO.cleanup()
    
if __name__ == '__main__':
    print ('Program is starting... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()