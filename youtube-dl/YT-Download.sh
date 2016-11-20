#!/bin/bash

echo "Video or Audio (A/V?)"
read choice

if [ $choice = "A" ] #Option A: Audio
	then
	echo "Please enter URL"
	read URL
	youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 "$URL"
elif [ $choice = "V" ] #Option V: Video
        then
        echo "Please enter URL"
        read URL
        youtube-dl -f 22 "$URL"
else
	echo "Invalid Choice"
	exit 
fi
