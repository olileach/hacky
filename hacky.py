from modules import hackySub, hackyPub
import json
import time
import random
import datetime
import random
import string

def main():

#sub = hackySub.IotSubscribe()
#sub.main()


# example payload data
#model
#manufacturedDate
#serialNumber
#chainAge
#location
#wattage
#ambientTemperature
#deviceTemperature

# structure is model number, manufacturing date, serialnum, chainInstallation date, 
    models = [('hsqv3e2234', '1/2009', 'a111234455562', '6/2011'), ('hsqv3e2235','8/2011', 'a112332134455833223', '7/2012'),('hsqv3e2236','4/2012', 'a112332136555213', '4/2012'),('hsqv3e2235','8/2011', 'a11233213', '9/2011')]

    numberInRange = lambda x, y: random.randint(x, y)
    message = {}
    message['lastModifiedDate'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        while True:


            letter = ''.join(random.choice(string.letters) for x in range(5))
            num = numberInRange(10000,99999)
            serialnumber = letter + str(num)
            
            secure_random = random.SystemRandom()
            model = random.choice(models)
            message['lastModifiedDate'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
            message['manufacturedDate'] = model[1]
            message['wattage'] = numberInRange(300, 400) # no idea if that's meant to be a wattage!
            message['RPM'] = numberInRange(1400, 1600) # again, no idea if that's the normal range for a chainsaw
            message['revolutions'] = numberInRange(1000, 100000)
            message['ambientTemperature'] = numberInRange(7, 22) 
            message['deviceTemperature'] = numberInRange(50, 75) 
            message['chainAge'] = model[3]
            message['serialNumber'] = serialnumber
            pub = hackyPub.IoTPublish(serialnumber=model[2], topic='chainsaw/data', message=json.dumps(message))
            print("\nconnecting to queue")
            pub.connect()
            print("\nmessage published")
            time.sleep(3)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    
    try:
        main()
    except Exception as e:
        main()
        print("KeyboardInterrupt: Exiting program")

