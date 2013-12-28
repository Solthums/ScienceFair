# import necessary libraries
import serial
import time
import sys

# Create a serial connection
connection = serial.Serial('/dev/tty.usbmodem1421', 115200) 
# Wait for the serial connection to resolve

# Declare necessary variables
force = 0
pulse = 0
timer = 60000
threshold = 645
isBreathing = False

while True:
        # start the timer
        timer = timer-1
        # establish a connection with arduino
    	line = connection.readline()
        # trigger to separate the two numerical values
    	parts = line.split(":")
    	if len(parts) == 2:
            	if parts[0] == "0":
                		if parts[1] != '0':
                				force = int(parts[1])
        if parts[0] == "1":
                if parts[1] != '0':
                		pulse = int(parts[1])
        # determing whether breath is being taken or not
        if force <= threshold:
            	isBreathing = True
            	print "You took a breath at Force of: " + str(force) + " at a time  " + str(timer/1000) + " seconds"
                isBreathing = False
        else:
	       		isBreathing = False
	        	print "no breath at Force of: " + str(force)
        # end program at the end of timer
        if timer <= 0:
            print 'Testing is over'
            sys.exit()
    
	    print "Force is " + str(force) + " and pulse is " + str(pulse)
