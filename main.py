import schedule
import time
from giopzero import Button

willieButton = Button(0)    # update button number
willieLED = LED(0)
yodaButton = Button(0)      # update button number
yodaLED = LED(0)


def timeToFeed():
    # turn on both button lights
    print("Lights have turned on")

def buttonPushed():
    willieButton.when_pressed() = willie.on
    yodaButton.when_pressed() = yoda.on
    print("Recording...")       # how will I record this?

# Every day at 07:00 and 18:00 timeToFeed() is called
schedule.every().day.at("07:00").do(timeToFeed)
schedule.every().day.at("18:00").do(timeToFeed)

while True:
    schedule.run_pending()  # checks for pending tasks
    time.sleep(1)           # loops every second