# Source: http://docker-asus.localdomain:8081/#/dashboard
# Source: https://www.zigbee2mqtt.io/devices/DG6HD-1BW.html

### Setup
# python3 -m venv .venv
# source .venv/bin/activate
# pip list
# pip install --upgrade pip
# pip install wheel paho-mqtt

### Usage
# from FrontOutsideLights import FrontOutsideLights
# FrontOutsideLights('ON')
# FrontOutsideLights('OFF')


import paho.mqtt.publish as publish

def FrontOutsideLights(state='OFF'):
    topic = 'zigbee2mqtt/FrontOutsideLights/set'
    hostname = 'docker-asus'
    payload = '{ "state": \"' + state + '\" }'
    if state.upper() == 'ON' or state.upper() == 'OFF':
        payload = '{ "state": \"' + state.upper() + '\" }'
        print(payload)
        publish.single(topic=topic, payload=payload, hostname=hostname)
    else:
        print(f"ERROR: {state} is invalid option")

if __name__ == '__main__':
    state = input("ON or OFF? ")
    if state.upper() == 'ON' or state.upper() == 'OFF':
        FrontOutsideLights(state.upper())
    else:
        print(f"{state} is an invalid option")


'''
>>> data
{'results': 
  {'sunrise':     '6:57:30 AM', 
   'sunset':      '5:17:54 PM', 
   'first_light': '5:25:21 AM', 
   'last_light':  '6:50:03 PM', 
   'dawn':        '6:29:11 AM', 
   'dusk':        '5:46:14 PM', 
   'solar_noon': '12:07:42 PM', 
   'golden_hour': '4:39:06 PM', 
   'day_length': '10:20:24', 
   'timezone': 'CST'}, 
'status': 'OK'}
'''

