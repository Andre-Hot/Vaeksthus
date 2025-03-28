gpiozero import PWMLED
from time import sleep

led = PWMLED(20)

led.value = 1   
sleep(1)
#led.value = 0.5  
#sleep(1)
#led.value = 0   
#sleep(1)

try:
  while True:
    for duty_cycle in range(0, 100, 1):
      led.value = duty_cycle/100.0
      sleep(0.05)

    for duty_cycle in range(100, 0, -1):
      led.value = duty_cycle/100.0
      sleep(0.05)
      
except KeyboardInterrupt:
  print("Stopping program, turning off the LED")
  led.value = 0
  pass