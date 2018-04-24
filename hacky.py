from modules import hackySub, hackyPub
import json
import time


sub = hackySub.IotSubscribe()
#sub.main()

message = {}
message['lastModifiedDate'] = 'date goes here'
#json_message = json.dumps(message)

#model
#manufacturedDate
#serialNumber
#chainAge
#location
#wattage
#ambientTemperature
#deviceTemperature


pub = hackyPub.IoTPublish(serialnumber='a2138789127398', message)#message = 'something else')

while True:
    pub.connect()
    time.sleep(3)
