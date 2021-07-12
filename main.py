import schedule
import time
from gpiozero import LED, Button    # might not work on the Pi

wBtn = Button(0) # update button number
wLED = LED(0)       # update LED number
yBtn = Button(0) # update button number
yLED = LED(0)       # update LED number

# Every day at 07:00 and 18:00 timeToFeed() is called
def timeToFeed():
    wLED.on     # turn on Willie's LED
    yLED.on     # turn on Yoda's LED
    print("Both lights have turned on")

schedule.every().day.at("07:00").do(timeToFeed)
schedule.every().day.at("18:00").do(timeToFeed)

# When either button is pressed, turn off its respective LED
def wPressed():
    wLED.off
    print("Willie has been fed")
def yPressed():
    yLED.off
    print("Yoda has been fed")

# Wait for either button to be pressed
wBtn.is_released = wPressed  #  these occur in seperate threads
yBtn.is_released = yPressed  # so that the next loop may run forever

def checkSchedule():
    while True:
        schedule.run_pending()  # infinitely checks for pending tasks
        time.sleep(1)           # loops every second
