#!/usr/bin/python

from astral import LocationInfo
from astral.sun import sun
import datetime
import schedule
import time
import os

city_name = "xxxx"
city_timezone = "US/Eastern"
city_lat = "xxxx"
city_long = "xxxx"

today_sunset = ""  # leave empty


def get_sunset():
    l = LocationInfo(city_name, "region", city_timezone, city_lat, city_long)
    s = sun((l.observer), tzinfo=city_timezone)
    sunrise = s["sunset"]
    today_sunset = sunrise.strftime("%H:%M")
    return(today_sunset)


def stop_camera():
    os.system('pkill -f what.py')


def take_still():
    for x in range(0, 5):
        os.system('raspistill -v -o "$(date +"%Y_%m_%d_%I_%M_%p").jpg"')
        time.sleep(60.0)


today_sunset = get_sunset()

schedule.every().day.at(today_sunset).do(stop_camera)
schedule.every().day.at(today_sunset).do(take_still)

while True:
    schedule.run_pending()
    time.sleep(1)
