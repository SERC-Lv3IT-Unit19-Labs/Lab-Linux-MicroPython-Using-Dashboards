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
