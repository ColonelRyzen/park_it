import RPi.GPIO as gpio
import config

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
	gpio.cleanup()

def redOff():
	turnOff(redPin)
	gpio.cleanup()

def greenOn():
	turnOn(greenPin)
	gpio.cleanup()

def greenOff():
	turnOff(greenPin)
	gpio.cleanup()

def blueOn():
	turnOn(bluePin)
	gpio.cleanup()

def blueOff():
	turnOff(bluePin)
	gpio.cleanup()

def yellowOn():
	turnOn(redPin)
	turnOn(greenPin)
	gpio.cleanup()

def yellowOff():
	turnOff(redPin)
	turnOff(greenPin)
	gpio.cleanup()

def whiteOn():
	turnOn(redPin)
	turnOn(greenPin)
	turnOn(bluePin)
	gpio.cleanup()

def whiteOff():
	turnOff(redPin)
	turnOff(greenPin)
	turnOff(bluePin)
	gpio.cleanup()

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
main()
