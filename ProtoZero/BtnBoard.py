from gpiozero import Button
import os

button = Button(4)
button2 = Button(17)
button3 = Button(25)
button4 = Button(5)
button5 = Button(19)

clear
print ("Please Choose a Button")
print ("1) Kodi")
print ("2) Desktop")
print ("3) Power Off")
print ("4) Controller Connect")
print ("5) RetroPie")

while True:
        if button.is_pressed:
                #os.system("echo kodi")
                os.system("kodi")
                exit()

        if button2.is_pressed:
                #os.system("echo startx")
                os.system("startx")
                exit()
                
        if button3.is_pressed:
                #os.system("echo poweroff")
                os.system("sudo poweroff")
                exit()
                
        if button4.is_pressed:
                #os.system("echo Controller Connect")
                os.system("./home/pi/ConntrollerConnect.sh")
                exit()
                
        if button5.is_pressed:
                #os.system("echo emulationstation")
                os.system("emulationstation")
                exit()
