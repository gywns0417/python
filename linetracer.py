# 패키지 임포트
import RPi.GPIO as GPIO
import time
import os

# 하단에 달린 라인트레이서 센서 핀 번호 
#TrackSensorLeftPin1 TrackSensorLeftPin2 TrackSensorRightPin1 TrackSensorRightPin2
#      3                 5                  4                   18
TrackSensorLeftPin1 = 3
TrackSensorLeftPin2 = 5
TrackSensorRightPin1 = 4
TrackSensorRightPin2 = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def lineinit():
    GPIO.setup(TrackSensorLeftPin1,GPIO.IN)
    GPIO.setup(TrackSensorLeftPin2,GPIO.IN)
    GPIO.setup(TrackSensorRightPin1,GPIO.IN)
    GPIO.setup(TrackSensorRightPin2,GPIO.IN)

try:
    init()
    while True:
        # 센서에 라인이 감지될 경우 (검정색 선만) 모듈 해당 부분에 불이 들어오며, 0(Low, False)가 반환 됨
        TrackSensorLeftValue1  = GPIO.input(TrackSensorLeftPin1)
        TrackSensorLeftValue2  = GPIO.input(TrackSensorLeftPin2)
        TrackSensorRightValue1 = GPIO.input(TrackSensorRightPin1)
        TrackSensorRightValue2 = GPIO.input(TrackSensorRightPin2)
        
        os.system("clear")
        print("왼쪽 1번 센서 : {0}".format(TrackSensorLeftValue1))
        print("왼쪽 2번 센서 : {0}".format(TrackSensorLeftValue2))
        print("오른쪽 1번 센서 : {0}".format(TrackSensorRightValue1))
        print("오른쪽 2번 센서 : {0}".format(TrackSensorRightValue2))
except KeyboardInterrupt:
    pass
GPIO.cleanup()

