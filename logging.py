
# import necessary libraries
import serial
import time

# Create a serial connection
connection = serial.Serial('/dev/tty.usbmodem', 9600)
# Wait for the serial connection to resolve
time.sleep(3000)

