import schedule
import time
from gpiozero import LED, Button    # might not work on the Pi

wButton = Button(0) # update button number
wLED = LED(0)       # update LED number
yButton = Button(0) # update button number
yLED = LED(0)       # update LED number

wFed = False
yFed = False

def willieFed():
    wLED.off
    print("Wille button pressed")
def yodaFed():
    yLED.off
    print("Yoda button pressed")

# Every day at 07:00 and 18:00 timeToFeed() is called
def timeToFeed():
    wLED.on         # turn on Willie's LED
    yLED.on         # turn on Yoda's LED
    print("Both lights have turned on")

schedule.every().day.at("07:00").do(timeToFeed)
schedule.every().day.at("18:00").do(timeToFeed)
wButton.when_pressed = willieFed
yButton.when_pressed = yodaFed

while True:
    schedule.run_pending()  # checks for pending tasks
    time.sleep(1)           # loops every second
