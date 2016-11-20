#!/bin/bash
cd /home/pi/Scripts/github
find . -maxdepth 1 -type d -exec sh -c '(cd {} && git pull)' ';'
