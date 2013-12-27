# import necessary libraries
import serial
import time

# Create a serial connection
connection = serial.Serial('/dev/tty.usbmodem1421', 115200)
# Wait for the serial connection to resolve

force = 0
pulse = 0

threshold = 640
isBreathing = False

while True:
        line = connection.readline()
        parts = line.split(":")
        if len(parts) == 2:
                if parts[0] == "0":
                        force = int(parts[1])
                        print force
                if parts[0] == "1":
                        pulse = int(parts[1])
                        print pulse
                print "Force is " + str(force) + " and pulse is " + str(pulse)
