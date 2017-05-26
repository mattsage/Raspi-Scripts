import explorerhat as eh
from time import sleep

eh.motor.one.forward(100)
eh.motor.two.backward(100)

sleep(10)

eh.motor.one.stop()
eh.motor.two.stop()

eh.motor.one.backward(100)
eh.motor.two.forward(100)

sleep(10)

eh.motor.one.stop()
eh.motor.two.stop()

