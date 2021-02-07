from gpiozero import LED

import time

led1 = LED(18)
led2 = LED(17)
led3 = LED(27)

led1.on()
led1.blink(0.5,0.2,5,False)
led1.off()

led2.on()
led2.blink(0.5,0.2,5,False)
led2.off()

led3.on()
led3.blink(0.5,0.2,5,False)
time.sleep(3)
led3.off()
