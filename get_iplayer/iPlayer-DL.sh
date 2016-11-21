#!/bin/bash
cd /media/pi/Samsung\ USB1/
echo "Please enter Keyword"
read keyword
get-iplayer $keyword
echo "####################################"
echo "Please enter ID#"
read IDno
get_iplayer --get $IDno --modes best
sudo /home/pi/blink1/commandline/blink1-tool --green --glimmer=50
