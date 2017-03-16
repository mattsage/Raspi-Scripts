from picamera import PiCamera
from os import system
from time import sleep

camera = PiCamera()
camera.resolution = (1024, 768)
loop = 0

for i in range(10):
	camera.capture('image{0:04d}.jpg'.format(i))
	loop += 1
	print loop, "Photo Taken"
	sleep(10)

print "Converting Jpg to GIF"
system('convert -delay 10 -loop 0 image*.jpg animation.gif')
print "Time Lapse Complete"
