#!/bin/bash

if [ `docker logs --since 25h zigbee2mqtt | grep -c Zigbee2MQTT:error` != 0 ]
then 
   echo "Errors Found in Logs... Restarting Container..."
   docker restart zigbee2mqtt
else
   echo "No Errors in Logs... Exiting"
fi
