# import necessary libraries
import serial
import time
import sys
import math
import matplotlib.pyplot as plt
import numpy as np
import pdb
import atexit
import thread
import copy
 

# Create a serial connection
connection = serial.Serial('/dev/tty.usbmodem1421', 115200) 
# Wait for the serial connection to resolve
connection.flush()

def closeConnection():
    print "Closing serial connection."
    connection.close()
    plt.show(block=True)
atexit.register(closeConnection)

# Declare necessary variables
graph = False
plot = 0
force = 0
buffer = []
pulse = 0
timer = 0
threshold = 645
isBreathing = False

if graph:
    plt.xlim([0, timer + 10])
    plt.ylabel('Level of force')
    plt.xlabel('Time')
    plt.ion()

def plotPoint(t, data):
    plt.xlim([0, t + 10])
    plt.scatter(t, data)
    plt.draw()
    plt.pause(0.0001)

while True:
    if graph and timer % 250 == 0:
        if timer > 1000:
            plt.xlim([timer - 1000, timer + 10])
        else:
            plt.xlim([0, timer + 10])
        plt.draw()
        plt.pause(0.00001)

    # get data from the Arduino
    line = connection.readline()
    # separate input into two values
    parts = line.split(":")
    if len(parts) == 2:
        if parts[0] == "0":
            if parts[1] != '0':
                # print "Force is: " + str(force)
                try:
                    force = int(parts[1])
                    # buffer.append(force)
                    timer = timer + 1
                    plt.scatter(timer, force)
                except ValueError:
                    print "Bad data."
        # If this is a sensor 0 reading
        if parts[0] == "1":
            if parts[1] != '0':
                    try:
                       pulse = int(parts[1])
                    except ValueError:
                        print "Bad data."
            

    # determing whether breath is being taken or not
    if force <= threshold:
        isBreathing = True
        print "You took a breath at Force of: " + str(force) + " at a time step " + str(timer)
        isBreathing = False
    else:
        isBreathing = False
        print "no breath at Force of: " + str(force) + " at a time step " + str(timer)
