import json
import random
import datetime
import time
from ina219 import INA219, DeviceRangeError

numberInRange = lambda x, y: random.randint(x, y)

# generate RPM values
def get_rpm(voltage, current, ratio):
    if (voltage*current)*ratio < 0:
        return 0.0
    else:
        return (voltage*current)*ratio

# generate-get values
def getValues(device='Chainsaw', serial='hsqv3e2234', model='h135', mDate='2011-10-04', deviceParameter='chainAge', deviceValue='2017-06-15'):
    # INA219 constants
    SHUNT_OHMS = 0.1
    I2C_INTERFACE_NO = 5

    # Set INA addresses for device
    if device == 'Chainsaw':
        ina = INA219(SHUNT_OHMS, busnum=I2C_INTERFACE_NO, address=0x40)
        ratio = 0.8
    elif device == 'HedgeTrimmer':
        ina = INA219(SHUNT_OHMS, busnum=I2C_INTERFACE_NO, address=0x41)
        ratio = 0.55
    ina.configure()

    data = {}
    data['deviceType'] = device
    data['deviceSN'] = serial
    data['deviceModel'] = model
    data['manufacturedDate'] = mDate
    data['devicePower'] = ina.power()
    data['deviceCurrent'] = ina.current()
    data['deviceVoltage'] = ina.voltage()*10
    #data['RPM'] = numberInRange(2900, 9000)
    data['RPM'] = get_rpm(ina.voltage(), ina.current(), ratio)
    data['ambientTemperature'] = numberInRange(7, 22)
    data['deviceTemperature'] = numberInRange(50, 75)
    data['deviceParameter'] = deviceParameter
    data['deviceValue'] = deviceValue
    data['dateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data['lastModifiedDate'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data
