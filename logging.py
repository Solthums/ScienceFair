# import necessary libraries
import serial
import time

# Create a serial connection
connection = serial.Serial('/dev/tty.usbmodem1421', 115200) 
# Wait for the serial connection to resolve

force = 0
pulse = 0

threshold = 645
isBreathing = False

while True:
    	line = connection.readline()
    	parts = line.split(":")
    	if len(parts) == 2:
            	if parts[0] == "0":
                		if parts[1] != '0':
                				force = int(parts[1])
        if parts[0] == "1":
                if parts[1] != '0':
                		pulse = int(parts[1])
        if force <= threshold:
            	isBreathing = True
            	print "You took a breath at Force of: " + str(force)
        else:
	       		isBreathing = False
	        	print "no breath at Force of: " + str(force)
    
			# print "Force is " + str(force) + " and pulse is " + str(pulse)



