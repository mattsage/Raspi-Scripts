#!/bin/bash
FILE=""
DIR="/home/pi/Pictures"
# init
# look for empty dir 
if [ "$(ls -A $DIR)" ]; then
     echo "Take action $DIR is not Empty"
else
    echo "$DIR is Empty"
fi
# rest of the logic
