from gpiozero import LED
import time

ledR = LED(27)
ledG = LED(17)
ledY = LED(18)

leds = {"R":ledR,"G":ledG,"Y":ledY}

try: 
    while True:
        led = leds[(input("\nOn led of colour (R/G/Y):")).upper()]
        times = int(input("\nNumber of times:"))
        led.on()
        led.blink(0.5,0.2,times,False)
        led.off()
except Exception as e:
   print("Invalid input provided.") 

