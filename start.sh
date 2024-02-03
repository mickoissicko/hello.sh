#!/bin/bash

lock_file="setup/lock.pa"

if [ -e "$lock_file" ]; then
    cd setup/
    sudo python setupmenu.py
    exit 0
else
    touch "$lock_file"
    cd setup/
    chmod +x "int.sh"
    ./int.sh
    exit 0
fi

exit 1
