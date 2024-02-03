#!/bin/bash

lock_file="setup/lock.pa"

if [ -e "$lock_file" ]; then
    cd setup/
    sudo python setupmenu.py
    exit
else
    touch "$lock_file"
    cd setup/
    chmod +x "int.sh"
    ./int.sh
    sudo python setupmenu.py
    exit
fi

exit
