from sense_hat import SenseHat
from time import sleep
sh = SenseHat()

sh.show_message("MOO!", \
text_colour=[255, 0, 0])
sleep(1)

X = [255, 255, 255] # Red
O = [0, 0, 255] # Blue
G = [0, 255, 0] #Green
B = [0, 0, 0] #Off
P = [248, 45, 176] #PINK UDDER

FOOMOO = [
X, X, X, O, O, O, O, O,
X, B, X, O, O, O, O, X,
X, X, X, X, X, X, X, O,
O, O, X, B, B, B, X, O,
O, O, X, B, B, B, X, O,
O, O, X, X, X, X, X, O,
O, O, X, O, P, P, X, O,
G, G, X, G, G, G, X, G
]
sh.set_pixels(FOOMOO)
