import os
from dot3k import lcd
from dot3k import backlight

os.system('echo "Video or Audio (A/V?)"')
os.system('read choice')

os.system('if [ $choice = "A" ] || [ $choice = "a" ] #Option A: Audio')
	os.system('then')
	os.system('echo "Please enter URL"')
	os.system('read URL')
	os.system('youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 "$URL"')
	lcd.write("Download Complete")
	backlight.rgb(0,255,0)
os.system('elif [ $choice = "V" ] || [ $choice = "v" ] #Option V: Video')
        os.system('then')
        os.system('echo "Please enter URL"')
        os.system('read URL')
        os.system('youtube-dl -f 22 "$URL"')
		lcd.write("Download Complete")
		backlight.rgb(0,255,0)
os.system('else')
	os.system('echo "Invalid Choice"')
		lcd.write("Download Complete")
		backlight.rgb(255,0,0)
	os.system('exit')
os.system('fi')





choice = input('Video or Audio (A/V?)')
choice.lower()
print (choice)
if choice is "a":
  print ('You chose A')
elif choice is "v":
  print ('You chose V')
else:
  print ('other')a
