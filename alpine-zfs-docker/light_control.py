#!/usr/bin/python3

# apk add python3
# apk add py3-pip
# pip install wheel paho-mqtt requests
# chmod +x light_control.py
# crontab -e  # Turn ON lights at 4:50 and Turn OFF at 9:15 and 10:00PM (just in case)
# 50     16       *       *       *       /root/source/bgant/tools/alpine-zfs-docker/light_control.py
# 15     21       *       *       *       /root/source/bgant/tools/alpine-zfs-docker/light_control.py
# 00     22       *       *       *       /root/source/bgant/tools/alpine-zfs-docker/light_control.py


from datetime import datetime
from dusk import dusk
from FrontOutsideLights import FrontOutsideLights

dusk = dusk()
if dusk < datetime.now() < datetime.now().replace(hour = 21):
   print("Turning front outside lights ON")
   FrontOutsideLights('ON')   # Turn lights ON after Dusk and before 9PM
else:
   print("Turning front outside lights OFF")
   FrontOutsideLights('OFF')


'''
Jun 21 2023 'dusk': '8:58:30 PM'
Dec 21 2023 'dusk': '5:01:51 PM'
'''

