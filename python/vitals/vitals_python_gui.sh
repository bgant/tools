#!/usr/bin/bash
#
# ln -s ~/.source/bgant/tools/python/vitals/vitals_python_gui.sh ~/.local/bin/vitals

if [ -d ~/.source ]
then 
    cd ~/.source/bgant/tools/python/vitals/
else
    cd ~/source/bgant/tools/python/vitals/
fi
/usr/bin/python vitals_python_gui.py
