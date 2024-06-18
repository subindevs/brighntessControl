import datetime
import screen_brightness_control as sbc


start_hour = 8
start_minute = 0
stop_hour = 24
stop_minute = 0
day_brightness = 100
night_brightness = 50

start_time = datetime.time(hour=start_hour,minute=start_minute)
stop_time = datetime.time(hour=stop_hour,minute=stop_minute)


def set_brightness(brightness_level):
    sbc.set_brightness(brightness_level)


def adjust_brightness():
    current_hour = datetime.datetime.now()

    if start_time <= current_hour.time() < stop_time:
        set_brightness(day_brightness) 
    else:
        set_brightness(night_brightness)  

if __name__ == "__main__":
    adjust_brightness()
