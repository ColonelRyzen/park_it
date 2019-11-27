import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

TRIG = 16
ECHO = 18
max_distance_cm = 95
min_distance_cm = 70

def get_distance():
	print("Distance Measurement In Progress")

	gpio.setup(TRIG, gpio.OUT)
	gpio.setup(ECHO, gpio.IN)

	gpio.output(TRIG, False)

	print("Waiting For Sensor To Settle")

	time.sleep(2)

	gpio.output(TRIG, True)
	time.sleep(0.00001)
	gpio.output(TRIG, False)

	while gpio.input(ECHO) == 0:
		pulse_start = time.time()
		
	while gpio.input(ECHO) == 1:
		pulse_end = time.time()
		
	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150

	distance = round(distance, 2)
	print("Distance: ", distance, "cm")

	gpio.cleanup()
	return distance

def object_in_range():
	car_in_range = False
	distance = get_distance()
	if distance > min_distance_cm and distance < max_distance_cm:
		car_in_range = True
	else:
		car_in_range = False
	
	if car_in_range == True:
		print("Car is detected")
	else:
		print("Car not present")

def main():
	object_in_range()
	
main()
