#!/usr/bin/python
import RPi.GPIO as GPIO
#import picamera ##Camera now remove
import time
from datetime import datetime
from multiprocessing import Process


##PIN MAP ##
ms1Pin = 1  #MS1        #DEBUG#
enaPin = 7 #ENABLE
resPin = 12 #RESET      #DEBUG#
#mirPin = 14 #MIR
ldrPin = 15 # LDR
slePin = 16 #SLEEP  
stePin = 20 #STEP
dirPin = 21 #DIR
stoPin = 23 #STOP
maxPin = 24 #STOP MAX
ledPin = 18 #LED PWM


#flags#
enaTgl = 0
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
	GPIO.setup(mirPin, GPIO.IN) #Motion detector
	GPIO.setup(stoPin, GPIO.IN) #Stop switch
	GPIO.setup(maxPin, GPIO.IN) #Max Stop switch
	## OUTPUTS ##
	GPIO.setup(stePin, GPIO.OUT, initial=GPIO.LOW) #Step pin
	GPIO.setup(dirPin, GPIO.OUT, initial=GPIO.LOW) #Direction pin
	GPIO.setup(ms1Pin, GPIO.OUT, initial=GPIO.LOW) #MS1 (mode) pin #DEBUG ONLY#
	GPIO.setup(slePin, GPIO.OUT, initial=GPIO.HIGH) #SLEEP pin
	GPIO.setup(resPin, GPIO.OUT, initial=GPIO.HIGH) #RESET pin #DEBUG ONLY#
	GPIO.setup(enaPin, GPIO.OUT, initial=GPIO.LOW) #ENABLE pin
	GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW) #LED pin
	LED = GPIO.PWM(ledPin, LEDhz) #LED is PWM instance on pin 18(ch0) at 50Hz
	LED.start(0) #Start PWM with 0% on
	

def set_settings(DB, NB, DL, NL, BS, LS, B1, B2, B3, B4, L1, L2, L3, L4):
	global DayBlind, NightBlind, DayLED, NightLED, BlindSpeed, LEDspeed
	global Blind1, Blind2, Blind3, Blind4, LED1, LED2, LED3, LED4
	DayBlind = DB
	NightBlind = NB
	DayLED = DL
	NightLED = NL
	Blind1 = B1
	Blind2 = B2
	Blind3 = B3
	Blind4 = B4
	LED1 = L1
	LED2 = L2
	LED3 = L3
	LED4 = L4
	BlindSpeed = BS
	LEDspeed = LS
	file = open("userSettings.txt","w+") 
	file.write(DayBlind) 
	file.write(NightBlind)
	file.write(DayLED)
	file.write(NightLED)
	file.write(Blind1)
	file.write(Blind2)
	file.write(Blind3)
	file.write(Blind4)
	file.write(LED1)
	file.write(LED2)
	file.write(LED3)
	file.write(LED4)
	file.write(BlindSpeed)
	file.write(LEDspeed)
	file.close()

def load_settings():
	global DayBlind, NightBlind, DayLED, NightLED, BlindSpeed, LEDspeed
	global Blind1, Blind2, Blind3, Blind4, LED1, LED2, LED3, LED4
	file = open("userSettings.txt","r") 
	DayBlind = file.readline(1)
	NightBlind = file.readline(2)
	DayLED = file.readline(3)
	NightLED = file.readline(4)
	Blind1 = file.readline(5)
	Blind2 = file.readline(6)
	Blind3 = file.readline(7)
	Blind4 = file.readline(8)
	LED1 = file.readline(9)
	LED2 = file.readline(10)
	LED3 = file.readline(11)
	LED4 = file.readline(12)
	BlindSpeed = file.readline(13)
	LEDspeed = file.readline(14)
	file.close()

def reset_settings():
	global DayBlind, NightBlind, DayLED, NightLED, BlindSpeed, LEDspeed
	global Blind1, Blind2, Blind3, Blind4, LED1, LED2, LED3, LED4
	DayBlind = 2
	NightBlind = 8
	DayLED = 0
	NightLED = 60
	BlindSpeed = 1.0
	LEDspeed = 1.0

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

def lowPower1(): #Toggle basic low power state
	global enaTgl
	if enaTgl == 0:
		GPIO.output(enaPin, GPIO.HIGH)
		enaTgl = 1
		return "Motors off"
	else:
		GPIO.output(enaPin, GPIO.HIGH)
		enaTgl = 0
		return "Motors on"

def lowPower2(): #Toggle full low power state
	global sleTgl
	if sleTgl == 0:
		GPIO.output(slePin, GPIO.HIGH)
		sleTgl = 1
		return "Driver on"
	else:
		GPIO.output(slePin, GPIO.HIGH)
		sleTgl = 0
		return "Driver on"

		
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

#def capture_image(imagefile):
#	with picamera.PiCamera() as camera:
#		camera.resolution = (1920,1080) #2592x1944
#		camera.start_preview()
#		time.sleep(1) #Camera warm-up time
#		#camera.vflip = true
#		#camera.hflip = true
#		camera.capture(imagefile)

#def movement(): #Movement detected
#	Process(target=capture_image(imagefile)).start
		
def setup_triggers():
	GPIO.add_event_detect(ldrPin, GPIO.BOTH, callback=autoCheck)  
#	GPIO.add_event_detect(mirPin, GPIO.FALLING, callback=movement)
	return "Triggers set"

def reset(): #Cycle RESET pin
	GPIO.output(resPin, GPIO.LOW)
	time.sleep(0.2)
	GPIO.output(resPin, GPIO.HIGH)
	return "Reset"

def cleanExit():
	LED.stop()
	GPIO.cleanup()
	
def status():
	s = "stepNo, stepMax, stepAware, maxAware, ms1Tgl, enaTgl, sleTgl, LEDpwr"
	s += str(stepNo) + "  " + str(stepMax) + "  " + str(stopAware) + "  " + str(maxAware)
	s += "  " + str(ms1Tgl) + "  " + str(enaTgl) + "  " + str(sleTgl) + "  " + str(LEDpwr) 
	return s
