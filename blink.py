import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	client.subscribe("commands")

def on_message(client, userdata, msg):
    command = msg.payload.decode('utf-8')
    print(command)
    if command == "OFF":
        turn_leds_off()
    else:
        turn_leds_on()
             
def turn_leds_off():
    GPIO.output(27, 0)
    GPIO.output(23, 0)
    GPIO.output(22, 0)
    
def turn_leds_on():
    GPIO.output(27, 1)
    GPIO.output(23, 1)
    GPIO.output(22, 1)

client = mqtt.Client()
client.username_pw_set("olxfatkr", password="lpgA6DFdpMvG")
client.connect("m15.cloudmqtt.com", 11128, 60)
client.on_connect = on_connect
client.on_message = on_message

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)     	#Read output from PIR motion sensor
GPIO.setup(4, GPIO.OUT)         #LED output pin
GPIO.setup(18, GPIO.OUT)         #LED output pin
GPIO.setup(27, GPIO.OUT)         #LED output pin
GPIO.setup(22, GPIO.OUT)         #LED output pin
GPIO.setup(23, GPIO.OUT)         #LED output pin
GPIO.setup(24, GPIO.OUT)         #LED output pin
GPIO.output(4, 1)
GPIO.output(18, 1)
GPIO.output(27, 1)
GPIO.output(22, 1)
GPIO.output(23, 1)
GPIO.output(24, 1)

while True:
	i=GPIO.input(17)
	client.publish("pirSensor", i)
	time.sleep(1)
	client.loop()