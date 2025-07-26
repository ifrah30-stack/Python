import time
import os

alarm_time = input("Set alarm (HH:MM): ")
while True:
    now = time.strftime("%H:%M")
    if now == alarm_time:
        os.system("start alarm.mp3")
        break
    time.sleep(30)
