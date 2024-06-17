import datetime
import time
import screen_brightness_control as sbc


start_hour = 16
start_minute = 23
stop_hour = 18
stop_minute = 26
day_brightness = 100
night_brightness = 50

start_time = datetime.time(hour=start_hour,minute=start_minute)
stop_time = datetime.time(hour=stop_hour,minute=stop_minute)


def set_brightness(brightness_level):
    sbc.set_brightness(brightness_level)


def adjust_brightness():
    current_hour = datetime.datetime.now()

    if start_time <= current_hour.time() < stop_time:
        set_brightness(60)  # Set brightness to 50% from 9 AM to 5 PM
    else:
        set_brightness(30)  # Set brightness to 30% from 5 PM to 9 AM

if __name__ == "__main__":
    adjust_brightness()
