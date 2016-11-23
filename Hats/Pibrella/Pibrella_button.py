#!/usr/bin/env python
from time import sleep
import pibrella
while True:
       if pibrella.button.read() == 1:
           pibrella.light.red.on()
           sleep(120)
           pibrella.light.red.off()
           pibrella.light.amber.fade(100, 0, 60)
           sleep(60)
           pibrella.light.green.pulse(1, 1, 1, 1)
           sleep(15)
