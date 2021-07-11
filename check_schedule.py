import main
import schedule
import time

schedule.every().day.at("07:00").do(main.timeToFeed)
schedule.every().day.at("18:00").do(main.timeToFeed)

while True:
    schedule.run_pending()  # checks for pending tasks
    time.sleep(1)           # loops every second