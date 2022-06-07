# demonstrate simulated distance readings

import time
import simulated_sensor

# define pins
TRIGGER_PIN = 4
ECHO_PIN = 5

sensor = simulated_sensor.HCSR04(TRIGGER_PIN, ECHO_PIN)

print("Simulated distance example. Ctrl + c to exit.")

while True:
    distance = sensor.distance_mm()
    print("Distance: {0:.0f} mm     ".format(distance), end='\r')
    time.sleep(1)
