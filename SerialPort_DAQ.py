'''
Created on Mar 29, 2021

@author: Elliott
'''
import serial
from time import gmtime, strftime

ser = serial.Serial("COM4", 115200) #configures COM port connected to arduino and buadrate
#Setting the time for file
actual_time = strftime("%Y-%m-%d %H-%M-%S", gmtime())
fileName = ("cap_data-" + str(actual_time) + ".csv") #name of file being generated
file = open(fileName, "w") #opens files and writes.
samples = 30 

i = 0


while (i <= samples):

    data = ser.readline(50)
    print(data.decode());

    file = open(fileName, "a") #appends data to file
    file.write(data.decode());
    i = i + 1;


file.close()
