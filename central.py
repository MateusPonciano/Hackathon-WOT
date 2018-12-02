import time
import paho.mqtt.client as mqtt
import requests

def on_connect(client, userdata, flags, rc):
    client.subscribe("pirSensor")

def on_message(client, userdata, msg):
    message = msg.payload.decode('utf-8')
    print(message)
    sensors.append(message)
        
def check_data(sensors, client):
    if '1' in sensors:
        payload = {'command': 'ON'}
        r = requests.get('http://127.0.0.1:1880/sensor', params=payload)
        print(r.content)
        print('on')
        client.publish('commands', 'ON')
    if not '1' in sensors:
        payload = {'command': 'OFF'}
        r = requests.get('http://127.0.0.1:1880/sensor', params=payload)
        print(r.content)
        print('off')
        client.publish('commands', 'OFF')
        
    print('fim check')

client = mqtt.Client()
client.username_pw_set("olxfatkr", password="lpgA6DFdpMvG")
client.connect("m15.cloudmqtt.com", 11128, 60)
client.on_connect = on_connect
client.on_message = on_message

sensors = []
while len(sensors) <= 5:
    client.loop()
    if len(sensors) == 5:
        check_data(sensors, client)
        sensors = []

