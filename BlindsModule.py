#!/usr/bin/python
import RPi.GPIO as GPIO
#import picamera ##Camera now remove
import time
from datetime import datetime
from multiprocessing import Process


##PIN MAP ##
ms1Pin = 24  #MS1        #DEBUG#
resPin = 12 #RESET      #DEBUG#
ldrPin = 16 # LDR
slePin = 23 #SLEEP  
stePin = 21 #STEP
dirPin = 20 #DIR
stoPin = 1 #STOP
maxPin = 7 #STOP MAX
ledPin = 18 #LED PWM


#flags#
sleTgl = 1
ms1Tgl = 0

#data#
stopAware = 0 #Has stepNo been verified
maxAware = 0 #Has stepMax been verified
stepNo = 0 #Stepper motor position
stepMin = 0 #Min step position
stepMax = 100 #Max step position
LEDpwr = 0 #LED setting
BlindDelay = 0.0001
LEDDelay = 0.1
LEDhz = 50 #50hz duty cycle

#User settings#
DayBlind = 2
NightBlind = 8
DayLED = 0
NightLED = 60
Blind1 = 0
Blind2 = 0
Blind3 = 0
Blind4 = 0
LED1 = 0
LED2 = 0
LED3 = 0
LED4 = 0
BlindSpeed = 1.0
LEDspeed = 1.0

## FUNCTIONS ##
def setup():
	GPIO.cleanup() #Reset
	GPIO.setmode(GPIO.BCM) #pin numbering scheme
	## INPUTS ##
	GPIO.setup(ldrPin, GPIO.IN) #Light sensor
	GPIO.setup(stoPin, GPIO.IN) #Stop switch
	GPIO.setup(maxPin, GPIO.IN) #Max Stop switch
	## OUTPUTS ##
	GPIO.setup(stePin, GPIO.OUT, initial=GPIO.LOW) #Step pin
	GPIO.setup(dirPin, GPIO.OUT, initial=GPIO.LOW) #Direction pin
	GPIO.setup(ms1Pin, GPIO.OUT, initial=GPIO.LOW) #MS1 (mode) pin #DEBUG ONLY#
	GPIO.setup(slePin, GPIO.OUT, initial=GPIO.HIGH) #SLEEP pin
	GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW) #LED pin
	LED = GPIO.PWM(ledPin, LEDhz) #LED is PWM instance on pin 18(ch0) at 50Hz
	LED.start(0) #Start PWM with 0% on
	

def LEDfade(power, delay = LEDDelay/LEDspeed): #Power 0-100%, Delay of 0 sets instantly
	global LEDpwr
	direction = 1
	if power < LEDpwr: #Count down if target power lower than current
		direction = - 1
	if delay:
		for pwr in range (LEDpwr, power, direction):
			LED.ChangeDutyCycle(pwr)
			time.sleep(LDelay)
	else:
		LED.ChangeDutyCycle(power)
	LEDpwr = power #Update global store of current setting
	
#Rotate motor in direction(1=up, 0=Down), for number of steps dist, with delay per step in seconds      
def move(direct, dist, delay): 
	global stepNo, stepMax, stopAware, maxAware
	GPIO.output(dirPin, direct)
	count = 0 # Start counter
	while count < dist: #Repeat dist times
		if not GPIO.input(maxPin) and not GPIO.input(stoPin):
			GPIO.output(stePin, GPIO.HIGH)
			time.sleep(delay)
			GPIO.output(stePin, GPIO.LOW)
			time.sleep(delay) #Clock step pin
			if direct: #Adjust StepNo
				stepNo += 1
			else:
				stepNo -= 1
		else: #If limits reached, grab info & force exit
			error = 0
			if GPIO.input(stoPin):
				error = stepNo - stepMin
				stepNo = stepMin
				stopAware = 1
			if GPIO.input(maxPin):
				error = stepNo - stepMax
				stepMax = stepNo
				maxAware = 1
			print "Limit reached: ", stepNo, "Error(0=none): ", error
			break
		count += 1
	GPIO.output(dirPin, GPIO.LOW) #Reset dir pin

def findLims(delay, timeout = 150): #Finds max & min values of steps 
	return "Feature not yet implemented"

def moveto(dest, delay): #Goes to step number specified
	dist = dest - stepNo #Calc dist
	direct = 0 #Direction
	if dist > 0: #Calc direct
		direct = 1
	return move(direct, abs(dist), delay)

def movetoNorm(notch, delay): #notch = 0 to 10, normalised steps
	#BDelay = BlindDelay / BlindSpeed
	interval = (stepMax - stepMin) / 10.0
	dest = int(notch * interval)
	if dest<stepMin: #Avoid min limit
		dest = stepMin + 2
	if dest>stepMax: #Avoid max limit
		dest = stepMax - 2
	return moveto(dest, delay)

def autoCheck(): #Check if night or day and perform tasks
	if GPIO.input(ldrPin):
		movetoNorm(DayBlind, BDelay)
		LEDfade(DayLED, LDelay)
	else:
		movetoNorm(NightBlind, BDelay)
		LEDfade(NightLED, LDelay)

def lowPower2(): #Toggle full low power state
	global sleTgl
	if sleTgl == 0:
		GPIO.output(slePin, GPIO.HIGH)
		sleTgl = 1
		return "Driver on"
	else:
		GPIO.output(slePin, GPIO.HIGH)
		sleTgl = 0
		return "Driver off"

		
def stepSize1(): #Toggle full-step/half-step
	global ms1Tgl
	if ms1Tgl == 0:
		GPIO.output(ms1Pin, GPIO.HIGH)
		ms1Tgl = 1
		return "Half-step"
	else:
		GPIO.output(ms1Pin, GPIO.HIGH)
		ms1Tgl = 0
		return "Full-step"
		
def setup_triggers():
	GPIO.add_event_detect(ldrPin, GPIO.BOTH, callback=autoCheck)  
	return "Triggers set"

def cleanExit():
	LED.stop()
	GPIO.cleanup()
	
def status():
	s = "stepNo "
	s += str(stepNo)
	return s
