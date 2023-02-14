#!/usr/bin/python3

# apk add python3
# apk add py3-pip
# pip install wheel paho-mqtt requests
# chmod +x light_control.py
# crontab -e  # Turn ON lights at 4:50 and Turn OFF at 9:15 and 10:00PM (just in case)
# 50     16       *       *       *       /root/source/bgant/tools/alpine-zfs-docker/eclipse-mosquitto/light_control.py
# 15     21       *       *       *       /root/source/bgant/tools/alpine-zfs-docker/eclipse-mosquitto/light_control.py
# 00     22       *       *       *       /root/source/bgant/tools/alpine-zfs-docker/eclipse-mosquitto/light_control.py


from datetime import datetime
import solar_api
from FrontOutsideLights import FrontOutsideLights
from time import sleep

if datetime.now() > datetime.now().replace(hour = 21, minute = 0, second = 0): 
    print("Turning front outside lights OFF")
    FrontOutsideLights('OFF')     # Turn lights OFF after 9PM
else:
    dusk = solar_api.phase('dusk')
    while datetime.now() < dusk:
        print('waiting for dusk at', dusk.strftime('%H:%M:%S'))
        sleep(600)  # Wait 10 Minutes 
    else:
        print("Turning front outside lights ON")
        FrontOutsideLights('ON')  # Turn lights ON after Dusk


'''
Jun 21 2023 'dusk': '8:58:30 PM'
Dec 21 2023 'dusk': '5:01:51 PM'
'''

