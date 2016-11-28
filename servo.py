import machine
import time

__author__ = 'Roland'


class servo:
    """ Servo class uses currently pin 15.
    """

    def __init__(self, speed = 0.1, pin = 15):
        self.min_duty = 37
        self.max_duty = 125
        self.duty_start = self.max_duty
        self.speed = speed

        self.pin = machine.Pin(pin)
        self.pwm = machine.PWM(self.pin, duty = self.duty_start, freq = 50)
        time.sleep_ms(1000)
        self.pwm.duty(0)

    def move(self, duty_end):
        if self.duty_start is not duty_end:
            if self.duty_start > duty_end:
                for dut in range(self.duty_start, duty_end - 1, -1):
                    self.pwm.duty(dut)
                    time.sleep_ms(int(self.speed * 1000))
            else:
                for dut in range(self.duty_start, duty_end + 1, 1):
                    self.pwm.duty(dut)
                    time.sleep_ms(int(self.speed * 1000))
            self.duty_start = duty_end
            # Wait for final movement
            time.sleep_ms(200)
        self.pwm.duty(0)

    def angle(self, degree):
        if degree >= 0 and degree <= 180:
            duty_end = int(((self.max_duty - self.min_duty)/180.0 * (180 - degree)) + self.min_duty)
            self.move(duty_end)

    def setToFail(self):
        self.angle(4)

    def above20(self):
        self.angle(14)

    def minutes(self, minutes):
        min_val = 17
        max_val = 177
        range = 19
        if minutes > 0 and minutes < 21:
            angleRange = max_val - min_val
            minRange = range - (minutes - 1)
            angle = int (angleRange / range * minRange + min_val)
            self.angle(angle)
        else:
            self.above20()

