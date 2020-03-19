'''
Created on Apr 11, 2018
@author: andrewstito
'''

import paho.mqtt.client as mqtt
import time

connectionFlag = False    

    
def on_connect(client, userdata, flags, rc):
    global connectionFlag
    connectionFlag = True
    print("OK. Connected with result code " + str(rc))


def on_message(client, userdata, message):
    print(message.topic + " " + str(message.payload) + " OK. Payload received")


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("NOK. Failed to Disconnect")


def on_subscribe(client, userdata, mid, granted_qos):
    print ("Client" + client 
               + "User data" + userdata
               + "mid" + mid
               + "granted_qos" + granted_qos)

    
def on_publish(client, userdata, mid):
    print ("Client" + client 
               + "User data" + userdata
               + "mid" + mid)
        
   
def mqttConnect(topic, payload):
            
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    host = 'iot.eclipse.org'
    port = 1883
    
    client.connect(host, port, keepalive=60)
 
    client.loop_start()
    time.sleep(1)    
    client.publish(topic, payload, 2)
    print (" Published : Payload " + payload)
   
    client.loop_stop()

    
