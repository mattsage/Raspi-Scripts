from sense_hat import SenseHat
sh = SenseHat()
X = [255, 255, 255] # White
O = [0, 0, 0] # Blank
G = [145, 145, 145] #grey

Skull = [
O, O, X, X, X, X, X, O,
O, X, X, X, X, X, X, X,
X, O, O, X, O, O, X, X,
X, G, O, X, G, O, X, X,
G, X, X, O, X, X, X, X,
O, X, X, X, X, X, G, O,
O, X, G, X, G, X, O, O,
O, O, O, O, O, O, O, O
]
sh.set_pixels(Skull)
