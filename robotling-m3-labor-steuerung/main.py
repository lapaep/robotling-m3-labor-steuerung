from keyboard_master import keyboard as kb

import paho.mqtt.client as mqtt
from mqtt import mqtt_broker, mqtt_port, mqtt_topic

class Main:

    def __init__(self):
        self._motorWalkspeed = 0
        self._motorTurnspeed = 0

    def connect(self):
        self.mqttc = mqtt.Client()
        self.mqttc.connect(mqtt_broker, mqtt_port, keepalive=60, bind_address="")
        print("Is connected...")

    @property
    def motorWalkspeed(self):
        return self._motorWalkspeed

    @motorWalkspeed.setter
    def motorWalkspeed(self, value):
        self._motorWalkspeed = value

    @property
    def motorTurnspeed(self):
        return self._motorTurnspeed

    @motorTurnspeed.setter
    def motorTurnspeed(self, value):
        self._motorTurnspeed = value


    def publish(self):
        self.mqttc.publish(mqtt_topic, str(self.motorWalkspeed) + "," + str(self.motorTurnspeed))

    def on_press_up(self, event):
        if event.name == "nach-oben" or event.name == "nach-unten" or event.name == "nach-links" or event.name == "nach-oben":
            self.publish()
            print(self.motorWalkspeed, self.motorTurnspeed)


    def keys(self):
        walkspeed = 0
        turnspeed = 0
        while True:
            self.motorWalkspeed = kb.is_pressed('nach-oben') * 100 + kb.is_pressed('nach-unten') * -100

            self.motorTurnspeed = kb.is_pressed('nach-links') * 30 + kb.is_pressed('nach-rechts') * -30

            kb.on_press(self.on_press_up)

            # if self.motorWalkspeed != walkspeed and self.motorTurnspeed != turnspeed:
            #     print(walkspeed,turnspeed)
            #     self.publish()
            #     walkspeed = self.motorWalkspeed
            #     turnspeed = self.motorTurnspeed
            #
            # elif self.motorWalkspeed != walkspeed:
            #     print(walkspeed,turnspeed)
            #     self.publish()
            #     walkspeed = self.motorWalkspeed
            #
            # elif self.motorTurnspeed != turnspeed:
            #     print(walkspeed,turnspeed)
            #     self.publish()
            #     turnspeed = self.motorTurnspeed
            #
            # else:
            #     pass


main = Main()
main.connect()
main.keys()
