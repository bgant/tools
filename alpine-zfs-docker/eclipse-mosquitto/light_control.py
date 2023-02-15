#!/usr/bin/python3

# apk add python3
# apk add py3-pip
# pip install wheel paho-mqtt requests
# chmod +x light_control.py
# crontab -e  # Turn ON lights at 4:50 and Turn OFF at 9:15 and 10:00PM (just in case)
# 30     16       *       *       *       /root/source/bgant/tools/alpine-zfs-docker/eclipse-mosquitto/light_control.py
# 01     21       *       *       *       /root/source/bgant/tools/alpine-zfs-docker/eclipse-mosquitto/light_control.py
# 00     22       *       *       *       /root/source/bgant/tools/alpine-zfs-docker/eclipse-mosquitto/light_control.py


from datetime import datetime
import solar_api
from FrontOutsideLights import FrontOutsideLights
from time import sleep
from random import randint

try:
    if datetime.now() > datetime.now().replace(hour = 21, minute = 0, second = 0): 
        sleep(randint(120,840))       # Wait 2 to 14 Minutes to avoid looking like a Timer
        print("Turning front outside lights OFF")
        FrontOutsideLights('OFF')     # Turn lights OFF after 9PM
    else:
        solar_phase = solar_api.phase('sunset')
        while datetime.now() < solar_phase:
            print('waiting for sunset at', solar_phase.strftime('%H:%M:%S'))
            sleep(randint(300,900))   # Wait 5 to 15 Minutes to avoid looking like a Timer
        else:
            print("Turning front outside lights ON")
            FrontOutsideLights('ON')  # Turn lights ON after Sunset
except KeyboardInterrupt:
    pass


'''
Jun 21 2023 'sunset': '8:25:36 PM'
Dec 21 2023 'sunset': '4:31:15 PM'

Jun 21 2023   'dusk': '8:58:30 PM'
Dec 21 2023   'dusk': '5:01:51 PM'
'''

