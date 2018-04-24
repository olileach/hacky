
'''
/*
 * Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */
 '''

from hackyAuth import IoTAuth
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time

class IotSubscribe:

    def __init__(self, topic=None, message="Can you see me"):
        
        self.topic = 'lcd/data'
        self.client = IoTAuth().client_connect(self)
        #self.clientId = "basicPubSub"
        self.clientId = "a2138789127398"

    def main(self):
        # Custom MQTT message callback
        def customCallback(client, userdata, message):
            print("Received a new message: ")
            print(message.payload)
            print("from topic: ")
            print(message.topic)
            print("--------------\n\n")

        # AWSIoTMQTTClient connection configuration
        self.client.configureAutoReconnectBackoffTime(1, 32, 20)
        self.client.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
        self.client.configureDrainingFrequency(2)  # Draining: 2 Hz
        self.client.configureConnectDisconnectTimeout(10)  # 10 sec
        self.client.configureMQTTOperationTimeout(5)  # 5 sec

        # Connect and subscribe to AWS IoT
        while True:
            self.client.connect()
            self.client.subscribe(self.topic, 1, customCallback)
            time.sleep(2)

