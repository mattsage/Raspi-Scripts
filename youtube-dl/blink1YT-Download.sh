#!/bin/bash

cd /media/pi/Samsung\ USB1/

echo "Video or Audio (A/V?)"
read choice

if [ $choice = "A" ] #Option A: Audio
	then
	echo "Please enter URL"
	read URL
	youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 "$URL"
	sudo /home/pi/blink1/commandline/blink1-tool --green --glimmer=50
elif [ $choice = "V" ] #Option V: Video
        then
        echo "Please enter URL"
        read URL
        youtube-dl -f 22 "$URL"
	sudo /home/pi/blink1/commandline/blink1-tool --green --glimmer=50
else
	echo "Invalid Choice"
	exit 
fi
