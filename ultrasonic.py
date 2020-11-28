# 패키지 임포트
import RPi.GPIO as GPIO
import time
import os

# 초음파 센서 핀 번호
EchoPin = 0
TrigPin = 1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def ultrainit():
    GPIO.setup(EchoPin,GPIO.IN)
    GPIO.setup(TrigPin,GPIO.OUT)

def Distance():
    GPIO.output(TrigPin,GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(TrigPin,GPIO.LOW)
    while not GPIO.input(EchoPin):
        pass
    t1 = time.time()
    while GPIO.input(EchoPin):
        pass
    t2 = time.time()
    os.system("clear")
    print ("거리(cm) :  %d" % (((t2 - t1)* 340 / 2) * 100))
    time.sleep(0.01)
    return ((t2 - t1)* 340 / 2) * 100
 
try:
    init()
    while True:
        distance = Distance()
except Exception as e:
    pass
GPIO.cleanup()
