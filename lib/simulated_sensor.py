'''Micropython module that simulates different sensors.'''
try:
    import urandom as random
except ImportError:
    import random

try:
    import utime as time
except ImportError:
    import time
    time.sleep_ms = lambda ms: time.sleep(ms / 1000)

random.seed(int(time.time())) # seed random with current epoch time

class TemperatureSensor:
    '''Represents a temperature sensor'''

    def __init__(self, pin):
        '''

        :param pin: pin number sensor attached to
        :type pin: int
        '''
        self.pin = pin
        self._min_range = 15
        self._max_range = 28
        self._temperature = random.randint(self._min_range*100, self._max_range*100) / 100

    def read_temperature(self):
        '''
        Returns a simulated temperature reading
        :return: Temperature
        :rtype: float
        '''

        change = random.randint(-200, 200) / 100

        if self._min_range < self._temperature + change < self._max_range:
            self._temperature += change
        else:
            self._temperature -= change

        time.sleep_ms(750)  # simulate delay reading from device
        return self._temperature

class TempHumSensor(TemperatureSensor):
    '''Represents a temperature humidty sensor'''

    def __init__(self, pin):
        '''

        :param pin: pin number sensor attached to
        :type pin: int
        '''
        super().__init__(pin)
        self._min_hum_range = 20
        self._max_hum_range = 70
        self._humidity = random.randint(self._min_hum_range*100, self._max_hum_range*100) / 100

    def read_humidity(self):
        '''
        Returns a simulated humidity reading
        :return: Humidity
        :rtype: float
        '''

        change = random.randint(-500, 500) / 100

        if self._min_hum_range < self._humidity + change < self._max_hum_range:
            self._humidity += change
        else:
            self._humidity -= change

        time.sleep_ms(250)  # simulate delay reading from device
        return self._humidity

    def read(self):
        '''
        Returns a simulated temperature and humidity reading
        :return: Temperature, Humidity
        :rtype: float, float
        '''
        return self.read_temperature(), self.read_humidity()

class HCSR04:
    '''Represents a HCSR04 ultrasonic distance sensor'''

    def __init__(self, trigger_pin, echo_pin):
        '''

        :param trigger_pin: pin number sensor trigger attached to
        :type trigger_pin: int
        :param echo_pin: pin number sensor echo attached to
        :type echo_pin: int
        '''
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        self._min_range = 7
        self._max_range = 1600
        self._distance = random.randint(self._min_range*100, self._max_range*100) / 100

    def distance_mm(self):
        '''
        Get the distance in milimeters without floating point operations.

        Returns a simulated distance reading

        :return: Distance
        :rtype: float
        '''
        jump = random.choice([0,0,1,1,1,1,2,3,5,8])
        direction = random.choice([-1,1,1,1,1])
        change = random.randint(0, 100) * jump * direction

        if self._distance - change < self._min_range:
            self._distance = self._min_range if random.randint(0,5) else self._max_range
        else:
            self._distance -= change

        time.sleep_ms(30)  # simulate delay reading from device
        return self._distance

    def distance_cm(self):
        """
        Get the distance in centimeters with floating point operations.
        It returns a float
        """
        return self.distance_mm() / 10
