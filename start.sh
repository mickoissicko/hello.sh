#!/bin/bash

lock_file="setup/lock.pa"
launcher="python setup/setupmenu.py"

if [ -e "$lock_file" ]; then
    $launcher
else
    touch "$lock_file"
    cd setup/
    chmod +x "int.sh"
    ./int.sh
    exit 0
fi

exit 1
