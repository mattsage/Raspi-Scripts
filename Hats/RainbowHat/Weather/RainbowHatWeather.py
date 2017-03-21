#!/usr/bin/env python

#TO DO:
#Wrap into Function

#Import Libraries
import subprocess
import signal
#import rainbowhat as rh
import datetime
import time

Location = raw_input("Please Enter a Location e.g. Tromso,Norway: ") #User input
print(Location)

key = open('apikey.config', 'r').read() #Place Weather Underground apikey in a file called apikey.config
key = key.strip('\n') #Strip Carriage Return

fetch="pywu fetch %s '%s'" % (key,Location) #Fetch Variable
print fetch
subprocess.check_output(fetch, shell=True) #Run pywu fetch in Bash Shell

temp="pywu current temp_c" #Get Temp in celsius
currenttemp = subprocess.check_output(temp, shell=True)
currenttemp = currenttemp.strip('\n') #Strip Carriage Return
currenttemp = currenttemp.strip()
currenttemp="%s C"%(currenttemp) #Add a "C" to value
print "The current temp is:",currenttemp  
#rh.display.print_str(currenttemp) #Print to Display
#rh.display.show()

condition="pywu current condition" #Fetch Current Condition
currentcondition = subprocess.check_output(condition, shell=True)
print currentcondition

#If loop for common conditions and Light up suitable Pixel on strip
if 'Cloudy' in currentcondition:
	print "Cloudy"
	#rh.rainbow.clear()
	#rh.rainbow.set_pixel(3, 255, 255, 255)
	#rh.rainbow.show()
elif 'Clouds' in currentcondition:
	print "Clouds"
	#rh.rainbow.clear()
	#rh.rainbow.set_pixel(3, 255, 255, 255)
	#rh.rainbow.show()
elif 'Rain' in currentcondition:
	print "Rain"
	#rh.rainbow.clear()
	#rh.rainbow.set_pixel(3, 255, 255, 255)
	#rh.rainbow.show()
elif 'Drizzle' in currentcondition:
	print "Drizzle"
	#rh.rainbow.clear()
	#rh.rainbow.set_pixel(3, 255, 255, 255)
	#rh.rainbow.show()
elif 'Snow' in currentcondition:
	print "Snow"
	#rh.rainbow.clear()
	#rh.rainbow.set_pixel(3, 255, 255, 255)
	#rh.rainbow.show()
elif 'Ice' in currentcondition:
	print "Ice"
	#rh.rainbow.clear()
	#rh.rainbow.set_pixel(3, 255, 255, 255)
	#rh.rainbow.show()
elif 'Hail' in currentcondition:
	print "Hail"
	#rh.rainbow.clear()
	#rh.rainbow.set_pixel(3, 255, 255, 255)
	#rh.rainbow.show()
elif 'Mist' in currentcondition:
	print "Mist"
	#rh.rainbow.clear()
	#rh.rainbow.set_pixel(3, 255, 255, 255)
	#rh.rainbow.show()
elif 'Fog' in currentcondition:
	print "Fog"
	#rh.rainbow.clear()
	#rh.rainbow.set_pixel(3, 255, 255, 255)
	#rh.rainbow.show()
elif 'Haze' in currentcondition:
	print "Haze"
	#rh.rainbow.clear()
	#rh.rainbow.set_pixel(3, 255, 255, 255)
	#rh.rainbow.show()
elif 'Thunderstorm' in currentcondition:
	print "Thunderstorm"
	#rh.rainbow.clear()
	#rh.rainbow.set_pixel(3, 255, 255, 255)
	#rh.rainbow.show()
elif 'Freezing' in currentcondition:
	print "Freezing"
	#rh.rainbow.clear()
	#rh.rainbow.set_pixel(3, 255, 255, 255)
	#rh.rainbow.show()
elif 'Overcast' in currentcondition:
	print "Overcast"
	#rh.rainbow.clear()
	#rh.rainbow.set_pixel(3, 255, 255, 255)
	#rh.rainbow.show()
elif 'Clear' in currentcondition:
	print "Clear"
	#rh.rainbow.clear()
	#rh.rainbow.set_pixel(3, 255, 255, 255)
	#rh.rainbow.show()
elif 'Unknown' in currentcondition:
	print "Unknown"
	#rh.rainbow.clear()
	#rh.rainbow.set_all(255, 0, 0)
	#rh.rainbow.show()	
else:
	print "Weather Not Found"
