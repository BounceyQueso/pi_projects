import RPi.GPIO as GPIO

ledPin = 11
buttonPin = 12

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
def loop():
    while True:
        if GPIO.input(buttonPin)==GPIO.LOW:
            GPIO.output(ledPin, GPIO.HIGH)
            print ('led turned on >>>>')
        else :
            GPIO.output(ledPin, GPIO.LOW)
            print ('led turned off <<<<')

def destroy ():
    GPIO.cleanup()
    
if __name__ == '__main__':
    print ('Program is starting... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()