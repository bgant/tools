#!/usr/bin/bash
if ! zpool status -x | grep -q 'all pools are healthy'; then
    zenity --warning --width=300 --height=100 \
	   --text "<span foreground='red'><b>ZFS Error.  Contact Brandon\!</b></span>"
fi 
