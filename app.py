import RPI.GPIO as GPIO
from gpiozero import PWMLED
import time import sleep
import smbus


PUMP_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUMP_PIN, GPIO.OUT)
GPIO.output(PUMP_PIN, GPIO.HIGH)

class MCP3021:
    bus = smbus.SMBus(1)

    def __init__(self, address = 0x4b):
        self.address = address

    def read_raw(self):
        rd = self.bus.read_word_data(self.address, 0)
        data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
        return data >> 2
    
    def read_percentage(self):
        raw_value = self.read_raw()
    
        adc1 = 311
        adc2 = 677
        a = (adc2 - adc1) / 100
        percentage = ((raw_value - adc1) / (adc2 - adc1)) * 100


        percentage = max(0, min (percentage, 100))

        return percentage
 
    """
    def read_percentage(self):
        raw_value = self.read_raw()
        percentage = 100 - ((raw_value / 1023) * 100)
        max_percentage = 
        return percentage
    """

adc = MCP3021()


#led.value = 0.5  
#sleep(1)
#led.value = 0   
#sleep(1)
led = PWMLED(20)
led.value = 1   
sleep(1)

try:

    while True:
        raw = adc.read_raw()
        moisture = adc.read_percentage()
        print(moisture)
        print(f"RAw :  {raw}, Moisture: {moisture:.2f}%")

        for duty_cycle in range(0, 100, 1):
            led.value = duty_cycle/100.0
            sleep(0.05)

        for duty_cycle in range(100, 0, -1):
            led.value = duty_cycle/100.0
            sleep(0.05)
      

        if moisture < 30:
            print("Moisure low")
            GPIO.output(PUMP_PIN, GPIO.LOW)

      else :
          print("moisture OK")
          GPIO.output(PUMP_PIN, GPIO.HIGH)

     time.sleep(1)
except KeyboardInterrupt:
    print("Stopping program and turning off leds")
    led.value = 0
    GPIO.cleanup()


      


 
