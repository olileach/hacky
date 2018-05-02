#!/usr/bin/env python
import os
from time import sleep
import pandas as pd
import numpy as np
from ina219 import INA219
from ina219 import DeviceRangeError

SHUNT_OHMS = 0.1
#I2C_INTERFACE_NO = 5
#IC2_ADDRESS = 0x41

devices = ['chainsaw', 'hedge trimmer']
telem = ['voltage (V)', 'current (mA)', 'power (mW)', 'shunt (mV)', 'rpm']
data = np.array([])

def get_rpm(voltage, current, ratio):
    if (voltage*current)*ratio < 0:
        return 0.0
    else:
        return (voltage*current)*ratio

def get_data():
    chainsaw = INA219(SHUNT_OHMS, busnum=5, address=0x40)
    trimmer = INA219(SHUNT_OHMS, busnum=5, address=0x41)
    for device in [chainsaw, trimmer]:
        device.configure()
    try:
        data = np.array([[chainsaw.voltage()*10, chainsaw.current(), chainsaw.power(), chainsaw.shunt_voltage(), get_rpm(chainsaw.voltage(), chainsaw.current(), 0.8)],
                        [trimmer.voltage()*10, trimmer.current(), trimmer.power(), trimmer.shunt_voltage(), get_rpm(trimmer.voltage(), trimmer.current(), 0.55)]])
        #print data
    except DeviceRangeError as e:
        print e

    return data

if __name__ == "__main__":
    try:
        while 1:
            #read()
            os.system('clear')
            df = pd.DataFrame(get_data(), devices, telem)
            print df
            sleep(1)
    except KeyboardInterrupt:
        print "\nCtrl-C Pressed. Program Exiting..."
