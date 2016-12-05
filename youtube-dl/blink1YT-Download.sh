#!/bin/bash

apikey=`cat apikey.config`

cd /media/pi/Samsung\ USB1/

echo "Video or Audio (A/V?)"
read choice

if [ $choice = "A" ] || [ $choice = "a" ] #Option A: Audio
	then
	echo "Please enter URL"
	read URL
	youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 "$URL"
	#./home/pi/pyPushBullet/pushbullet_cmd.py $apikey note udeCmddJpl "Download Completed" "Download Completed"
	sudo /home/pi/blink1/commandline/blink1-tool --green --glimmer=500000000x
elif [ $choice = "V" ] || [ $choice = "v" ] #Option V: Video
        then
        echo "Please enter URL"
        read URL
        youtube-dl -f 22 "$URL"
	sudo /home/pi/blink1/commandline/blink1-tool --green --glimmer=50
else
	echo "Invalid Choice"
	exit 
fi
