import paho.mqtt.publish as publish
import time

# Change the MQTT broker address and port if needed
broker_address = "192.168.219.247"
broker_port = 1883

# To display a rainbow pattern
while True:
        publish.single("metamorph/test/servos", "eye", hostname=broker_address, port=broker_port)
        time.sleep(10)

# To display red color
        publish.single("metamorph/test/leds", "red", hostname=broker_address, port=broker_port)
        time.sleep(10)

# To display green color
        publish.single("metamorph/test/leds", "green", hostname=broker_address, port=broker_port)
        time.sleep(10)

        publish.single("metamorph/test/leds", "off", hostname=broker_address, port=broker_port)
        time.sleep(10)
