import paho.mqtt.client as mqtt
from mqtt import mqtt_broker, mqtt_port, mqtt_topic

class Main:

    def __init__(self):

        self.motorWalkspeed = 0
        self.motorTurnspeed = 0

    def connect(self):
        self.mqttc = mqtt.Client()
        self.mqttc.connect(mqtt_broker, mqtt_port, keepalive=60, bind_address="")
        print("Is connected...")

    # @property
    # def motorWalkspeed(self):
    #     return self._motorWalkspeed
    #
    # @motorWalkspeed.setter
    # def motorWalkspeed(self, value):
    #     self._motorWalkspeed = value
    #
    # @property
    # def motorTurnspeed(self):
    #     return self._motorTurnspeed
    #
    # @motorTurnspeed.setter
    # def motorTurnspeed(self, value):
    #     self._motorTurnspeed = value

    def publish(self,w,a,s,d,boost):
        motorWalkspeed = (s * 75 - w * 75)*(1+boost)
        motorTurnspeed = (d * 35 - a * 35) *(1+boost)
        if self.motorWalkspeed == motorWalkspeed and self.motorTurnspeed == motorTurnspeed:
            pass
        else:
            self.motorWalkspeed = motorWalkspeed
            self.motorTurnspeed = motorTurnspeed
            self.mqttc.publish(mqtt_topic, str(motorWalkspeed) + "," + str(motorTurnspeed))
