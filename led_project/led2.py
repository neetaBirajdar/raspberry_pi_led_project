from gpiozero import LED
import time

led1=LED(18)
led2=LED(17)
led3=LED(27)

while True:
    for led in [led1,led2,led3]:
        led.on()
        led.blink(0.5,0.2,2,False)
        led.off()
