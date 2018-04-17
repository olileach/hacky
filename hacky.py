from modules import hackySub, hackyPub
import time

instance = hackyPub.IoTPublish(serialnumber='a2138789127398', message = 'something else')
while True:
    instance.connect()
    time.sleep(3)
