#!/usr/bin/env python

from modules import hackySub, hackyPub
from modules.hackyGet import *
from time import sleep
import random

#import datetime
import json

# device, serial, model, mDate, deviceParameter, deviceValue

chainsaws = [('Chainsaw', 'hsqv3e2234', 'h135', '2011-10-04', 'chainAge', '2017-06-15'),
            ('Chainsaw', 'hsqv3e6339', 'h135', '2015-02-18', 'chainAge', '2016-09-11')]

trimmers = [('HedgeTrimmer', 'hsqv6f1947', '122hd60', '2014-08-24', 'cuttingBarAge', '2017-06-15'),
            ('HedgeTrimmer', 'hsqv6f3654', '122hd60', '2016-05-19', 'cuttingBarAge', '2017-06-15')]

# Random device selection
#device = random.choice(devices)

if __name__ == "__main__":
    try:
        while 1:
            for chainsaw in chainsaws:
                data = json.dumps(getValues(device=chainsaw[0], serial=chainsaw[1], model=chainsaw[2], mDate=chainsaw[3], deviceParameter=chainsaw[4], deviceValue=chainsaw[5]))
                pub = hackyPub.IoTPublish(serialnumber=chainsaw[1], topic='chainsaw/data', message=data)
                pub.send(debug=True)
                sleep(1)

            for trimmer in trimmers:
                data = json.dumps(getValues(device=trimmer[0], serial=trimmer[1], model=trimmer[2], mDate=trimmer[3], deviceParameter=trimmer[4], deviceValue=trimmer[5]))
                pub = hackyPub.IoTPublish(serialnumber=trimmer[1], topic='hedgetrimmer/data', message=data)
                pub.send(debug=True)
                sleep(1)
    except KeyboardInterrupt:
        print '\nCtrl-C Pressed. Program Exiting...'
