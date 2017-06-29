import dothat.lcd as lcd
import dothat.backlight as backlight

print("""
This example shows a basic "Hello World" on the LCD.
You should see "Hello World" displayed on your LCD!
Press CTRL+C to exit.
""")


# Clear the LCD and display Hello World
backlight.rgb(138,43,226)
lcd.clear()
lcd.write("Hail to the King")
