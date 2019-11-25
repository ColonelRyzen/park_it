import RPi.GPIO as gpio

aPin = 3 
bPin = 7
cPin = 11
dPin = 15
ePin = 24
fPin = 31
gPin = 35

def turnOn(pin):
	gpio.setmode(gpio.BOARD)
	gpio.setup(pin, gpio.OUT)
	gpio.output(pin, gpio.HIGH)
	
def turnOff(pin):
	gpio.setmode(gpio.BOARD)
	gpio.setup(pin, gpio.OUT)
	gpio.output(pin, gpio.LOW)
	
def aOn():
	turnOn(aPin)
	
def aOff():
	turnOff(aPin)
	
def bOn():
	turnOn(bPin)
	
def bOff():
	turnOff(bPin)
	
def cOn():
	turnOn(cPin)
	
def cOff():
	turnOff(cPin)

def dOn():
	turnOn(dPin)
	
def dOff():
	turnOff(dPin)
	
def eOn():
	turnOn(ePin)
	
def eOff():
	turnOff(ePin)
	
def fOn():
	turnOn(fPin)
	
def fOff():
	turnOff(fPin)
	
def gOn():
	turnOn(gPin)
	
def gOff():
	turnOff(gPin)
	
def zero():
	aOff()
	bOff()
	cOff()
	dOff()
	eOff()
	fOff()
	gOff()

def one():
	bOn()
	cOn()

def two():
	aOn()
	bOn()
	gOn()
	eOn()
	dOn()

def three():
	aOn()
	bOn()
	gOn()
	cOn()
	dOn()
	
def four():
	bOn()
	fOn()
	gOn()
	cOn()
	
def five():
	aOn()
	fOn()
	gOn()
	cOn()
	dOn()
	
def six():
	aOn()
	fOn()
	eOn()
	gOn()
	cOn()
	dOn()
	
def seven():
	aOn()
	bOn()
	cOn()
	
def eight():
	aOn()
	bOn()
	cOn()
	dOn()
	eOn()
	fOn()
	gOn()

def nine():
	aOn()
	bOn()
	gOn()
	fOn()
	cOn()
	
def main():
	while True:
		cmd = input("-->")
		
		if cmd == "a on":
			aOn()
		elif cmd == "a off":
			aOff()
		elif cmd == "b on":
			bOn()
		elif cmd == "b off":
			bOff()
		elif cmd == "c on":
			cOn()
		elif cmd == "c off":
			cOff()
		elif cmd == "d on":
			dOn()
		elif cmd == "d off":
			dOff()
		elif cmd == "e on":
			eOn()
		elif cmd == "e off":
			eOff()
		elif cmd == "f on":
			fOn()
		elif cmd == "f off":
			fOff()
		elif cmd == "g on":
			gOn()
		elif cmd == "g off":
			gOff()
		elif cmd == "zero":
			zero()
		elif cmd == "one":
			zero()
			one()
		elif cmd == "two":
			zero()
			two()
		elif cmd == "three":
			zero()
			three()
		elif cmd == "four":
			zero()
			four()
		elif cmd == "five":
			zero()
			five()
		elif cmd == "six":
			zero()
			six()
		elif cmd == "seven":
			zero()
			seven()
		elif cmd == "eight":
			zero()
			eight()
		elif cmd == "nine":
			zero()
			nine()
		else:
			print("Not a valid input")
			
	return
main()

