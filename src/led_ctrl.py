import RPi.GPIO as gpio
import config

gpio.setwarnings(False)

redPin = config.led_red_pin
greenPin = config.led_green_pin
bluePin = config.led_blue_pin

def turnOn(pin):
	gpio.setmode(gpio.BOARD)
	gpio.setup(pin, gpio.OUT)
	gpio.output(pin, gpio.HIGH)

def turnOff(pin):
	gpio.setmode(gpio.BOARD)
	gpio.setup(pin, gpio.OUT)
	gpio.output(pin, gpio.LOW)

def redOn():
	turnOn(redPin)

def redOff():
	turnOff(redPin)

def greenOn():
	turnOn(greenPin)

def greenOff():
	turnOff(greenPin)

def blueOn():
	turnOn(bluePin)

def blueOff():
	turnOff(bluePin)

def yellowOn():
	turnOn(redPin)
	turnOn(greenPin)

def yellowOff():
	turnOff(redPin)
	turnOff(greenPin)

def whiteOn():
	turnOn(redPin)
	turnOn(greenPin)
	turnOn(bluePin)

def whiteOff():
	turnOff(redPin)
	turnOff(greenPin)
	turnOff(bluePin)

def main():
	while True:
		cmd = input("-->")

		if cmd == "red on":
			redOn()
		elif cmd == "red off":
			redOff()
		elif cmd == "green on":
			greenOn()
		elif cmd == "green off":
			greenOff()
		elif cmd == "yellow on":
			yellowOn()
		elif cmd == "yellow off":
			yellowOff()
		elif cmd == "blue on":
			blueOn()
		elif cmd == "blue off":
			blueOff()
		elif cmd == "white on":
			whiteOn()
		elif cmd == "white off":
			whiteOff()
		else:
			print("Not a valid input")

	return
#main()
