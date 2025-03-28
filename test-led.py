import schedule
import time
import pigpio



class LedSchedule:
    def __init__(self, turn_on, turn_off, GPIO_pin):
        self.turn_on = turn_on
        self.turn_off = turn_off
        self.GPIO_pin = GPIO_pin
        self.pi = pigpio.pi()


    def init_schedule(self):
        #Set the schedule for the red led
        schedule.every(1).minute.at(self.turn_on).do(self.on)
        schedule.every(1).minute.at(self.turn_off).do(self.off)

    def on(self):
        self.pi.set_PWM_dutycycle(self.GPIO_pin, 5)
    
    def off(self):
        self.pi.set_PWM_dutycycle(self.GPIO_pin, 0)


if __name__ == "__main__":
    #Create the red led object
    red = LedSchedule(":01", ":03", 20)
    red.init_schedule()
    blue = LedSchedule("", "00:01", 13)
    blue.init_schedule()

    #schedule.every().minute.at(self.turn_on).do(self.turn_on_red)
    #schedule.every().minute.at(self.turn_off).do(self.turn_off_red)



    while True:
        schedule.run_pending()
        time.sleep(1)