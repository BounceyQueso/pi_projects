import RPi.GPIO as GPIO

ledPin = 11
buttonPin = 12
ledState = False

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttonEvent(channel):
    global ledState
    print ('buttonEvent GPIO%d' %channel)
    ledState = not ledState
    if ledState :
        print ('Led turned on >>>>')
    else :
        print ('Led turned off <<<<')
        
    GPIO.output(ledPin,ledState)
    
def loop():
    GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback = buttonEvent, bouncetime = 300)
    while True:
        pass
    
def destroy():
    GPIO.cleanup()
    
if __name__ == '__main__':
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
