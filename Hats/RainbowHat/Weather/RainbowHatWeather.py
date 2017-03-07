#!/usr/bin/env python

#TO DO:
#Wrap into Function
#Add RainbowHat

import subprocess
import signal
#import rainbowhat
import datetime
import time

Location = raw_input("Please Enter a Location e.g. Tromso,Norway: ")
print(Location)
#Location = "Tromso,Norway"

key = open('apikey.config', 'r').read() #Place Weather Underground apikey in a file called apikey.config
key = key.strip('\n')
#print "API Key =",key

fetch="pywu fetch %s '%s'" % (key,Location)
print fetch
subprocess.check_output(fetch, shell=True)

temp="pywu current temp_c"
currenttemp = subprocess.check_output(temp, shell=True)
print currenttemp

condition="pywu current condition"
currentcondition = subprocess.check_output(condition, shell=True)
print currentcondition

if 'Cloudy' in currentcondition:
	print "Cloudy"
elif 'Clouds' in currentcondition:
	print "Clouds"
elif 'Rain' in currentcondition:
	print "Rain"
elif 'Drizzle' in currentcondition:
	print "Drizzle"
elif 'Snow' in currentcondition:
	print "Snow"
elif 'Ice' in currentcondition:
	print "Ice"
elif 'Hail' in currentcondition:
	print "Hail"
elif 'Mist' in currentcondition:
	print "Mist"
elif 'Fog' in currentcondition:
	print "Fog"
elif 'Haze' in currentcondition:
	print "Haze"
elif 'Thunderstorm' in currentcondition:
	print "Thunderstorm"
elif 'Freezing' in currentcondition:
	print "Freezing"
elif 'Overcast' in currentcondition:
	print "Overcast"
elif 'Clear' in currentcondition:
	print "Clear"
elif 'Unknown' in currentcondition:
	print "Unknown"	
else:
	print "Weather Not Found"
