from gpiozero import LED, Button    # might not work on the Pi

wButton = Button(0) # update button number
wLED = LED(0)       # update LED number
yButton = Button(0)
yLED = LED(0)

wFed = False
yFed = False

if wButton.when_pressed():
    wLED.off
    wFed = True
if yButton.when_pressed():
    yLED.off
    yFed = True
print("Recording...")       # how will I record this?

# Every day at 07:00 and 18:00 timeToFeed() is called
def timeToFeed():
    wFed = False
    wLED.on         # turn on Willie's LED
    yFed = False
    yLED.on         # turn on Yoda's LED
    print("Lights have turned on")
