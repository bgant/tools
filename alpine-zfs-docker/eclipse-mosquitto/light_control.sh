#!/bin/sh
docker run -it --rm -v /home/docker/source/bgant/tools/alpine-zfs-docker/eclipse-mosquitto:/usr/src/myapp -w /usr/src/myapp python-pip python light_control.py
