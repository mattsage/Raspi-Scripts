#!/bin/bash

#Copy this file to /usr/bin
#chmod 755 /usr/bin/Pushbullet.sh
#usage: Pushbullet.sh "Send this"

API=`cat /home/pi/pushbulletkey.config`
MSG="$1"

curl -u $API: https://api.pushbullet.com/v2/pushes -d type=note -d title="Alert" -d body="$MSG"
