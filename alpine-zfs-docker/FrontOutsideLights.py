# python3 -m venv venv
# source venv/bin/activate
# pip install --upgrade pip
# pip install wheel paho-mqtt

import paho.mqtt.publish as publish

def FrontOutsideLights(state='OFF'):
    topic = 'zigbee2mqtt/FrontOutsideLights/set'
    hostname = 'docker-asus'
    payload = '{ "state": \"' + state + '\" }'
    print(payload)
    publish.single(topic=topic, payload=payload, hostname=hostname)

if __name__ == '__main__':
    state = input("ON or OFF? ")
    if state == 'ON' or state == 'OFF':
        FrontOutsideLights(state)
    else:
        print(f"{state} is an invalid option")

