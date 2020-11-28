# 패키지 임포트
import RPi.GPIO as GPIO
import time
import os
import ultrasonic
import linetracer

# 모터 동작에 관련된 핀 번호
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13
EchoPin = 0
TrigPin = 1
TrackSensorLeftPin1 = 3
TrackSensorLeftPin2 = 5
TrackSensorRightPin1 = 4
TrackSensorRightPin2 = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 모터 초기화
def motor_init():
    global pwm_ENA
    global pwm_ENB
    global delaytime
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)

# 전진
def run(delaytime, power):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(power)
    pwm_ENB.ChangeDutyCycle(power)
    time.sleep(delaytime)

# 후진
def back(delaytime, power):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(power)
    pwm_ENB.ChangeDutyCycle(power)
    time.sleep(delaytime)

# 좌회전
def left(delaytime, power):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(power)
    pwm_ENB.ChangeDutyCycle(power)
    time.sleep(delaytime)

# 우회전
def right(delaytime, power):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(power)
    pwm_ENB.ChangeDutyCycle(power)
    time.sleep(delaytime)

# 제자리 좌회전
def spin_left(delaytime, power):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(power)
    pwm_ENB.ChangeDutyCycle(power)
    time.sleep(delaytime)

# 제자리 우회전
def spin_right(delaytime, power):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(power)
    pwm_ENB.ChangeDutyCycle(power)
    time.sleep(delaytime)

 # 정지
def brake(delaytime, power):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(power)
    pwm_ENB.ChangeDutyCycle(power)
    time.sleep(delaytime)


if __name__=="__main__":
    try:
    # 작동되는 시간을 변경하고 싶으면 바로 아래에 있는 변수를 수정할 것 (단위 : 초, 소수점 가능)
    # 시간이 너무 길어지면 제어가 불가능해짐, 제어가 불가능 한 경우 Ctrl + C 키를 눌러서 바로 동작을 중지시킬 것
        running_time = 10
    ##################################################################################
    # 동작 세기를 변경하고 싶으면 바로 아래에 있는 변수를 수정할 것 (0 ~ 100 사이의 정수만 가능)
    # 10 이상의 세기를 사용할 경우 무조건 들고 사용할 것
        power = 10
    ##################################################################################
    
    
        motor_init()
        lineinit()
        ultrainit()
        Distance()
        distance = Distance()

        while True:
            os.system("clear")
            print("명렁어 목록 : forward, back, left, right, leftspin, rightspin, avoid, linetracer")
            print("명령어를 입력해주세요 : ", end="")
            command = input()
        
            print()
            if command == "forward":
                print("전진 / Duration : {0} / Power : {1}".format(running_time, power))
                run(running_time, power)
                brake(running_time, power)
            elif command == "back":
                print("후진 / Duration : {0} / Power : {1}".format(running_time, power))
                back(running_time, power)
                brake(running_time, power)
            elif command == "left":
                print("좌회전 / Duration : {0} / Power : {1}".format(running_time, power))
                left(running_time, power)
                brake(running_time, power)
            elif command == "right":
                print("우회전 / Duration : {0} / Power : {1}".format(running_time, power))
                right(running_time, power)
                brake(running_time, power)
            elif command == "leftspin":
                print("제자리 좌회전 / Duration : {0} / Power : {1}".format(running_time, power))
                spin_left(running_time, power)
                brake(running_time, power)
            elif command == "rightspin":
                print("제자리 우회전 / Duration : {0} / Power : {1}".format(running_time, power))
                spin_right(running_time, power)
                brake(running_time, power)
            elif command == "avoid":
                while True:

                    if distance > 30:
                        run(running_time, power)
                        if distance <= 30:
                            brake(running_time, power)
                            time.sleep(0.3)
                            spin_right(running_time, power)
                            time.sleep(0.3)
                            if distance > 30:
                                continue
                            elif distance <= 30:
                                spin_left(running_time*2, power)
                                time.sleep(0.3)
                                if distance > 30:
                                    continue
                                elif distance <= 30:
                                    spin_right(running_time, power)
                                    time.sleep(0.3)
                                    back(running_time*2, power)
                                    continue
            elif command == "linetracer":
                 while True:
                  

        #4 tracking pins level status
        # 0 0 X 0
        # 1 0 X 0
        # 0 1 X 0
        #Turn right in place,speed is 50,delay 80ms
        #Handle right acute angle and right right angle
                    if (TrackSensorLeftValue1 == False or TrackSensorLeftValue2 == False) and  TrackSensorRightValue2 == False:
                        spin_right(35, 35)
	                    time.sleep(0.08)
 
        #4 tracking pins level status
        # 0 X 0 0       
        # 0 X 0 1 
        # 0 X 1 0       
       #Turn right in place,speed is 50,delay 80ms   
       #Handle left acute angle and left right angle 
                    elif TrackSensorLeftValue1 == False and (TrackSensorRightValue1 == False or  TrackSensorRightValue2 == False):
                        spin_left(running_time, power)
	                    time.sleep(0.08)
  
        # 0 X X X
        #Left_sensor1 detected black line
                    elif TrackSensorLeftValue1 == False:
                        spin_left(running_time, power)
     
        # X X X 0
        #Right_sensor2 detected black line
                    elif TrackSensorRightValue2 == False:
                        spin_rightrunning_time, power)
   
        #4 tracking pins level status
        # X 0 1 X
                    elif TrackSensorLeftValue2 == False and TrackSensorRightValue1 == True:
                        left(running_time, power)
   
        #4 tracking pins level status
        # X 1 0 X  
                    elif TrackSensorLeftValue2 == True and TrackSensorRightValue1 == False:
                        right(running_time, power)
   
        #4 tracking pins level status
        # X 0 0 X
                    elif TrackSensorLeftValue2 == False and TrackSensorRightValue1 == False:
	                    run(running_time, power)
   
        #When the level of 4 pins are 1 1 1 1 , the car keeps the previous running state.



            else:
                continue
        time.sleep(0.5)
    except KeyboardInterrupt:
        pass

pwm_ENA.stop()
pwm_ENB.stop()
GPIO.cleanup() 

