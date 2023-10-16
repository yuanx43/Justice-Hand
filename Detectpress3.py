
import RPi.GPIO as gpio
import time
from gpiozero import MCP3008, Button
import time
import pygame


# MCP3008 設置
sound = MCP3008(0)
# MCP3008 gigital sound pin
digital_sound = Button(4)

# button pin
btn = 27
# button pin setup
gpio.setmode(gpio.BCM)
gpio.setup(btn, gpio.IN, pull_up_down=gpio.PUD_UP)

# button pin2
btn2 = 25
# button pin setup
gpio.setmode(gpio.BCM)
gpio.setup(btn2, gpio.IN, pull_up_down=gpio.PUD_UP)

# 循環間隔時間
delaysec = 0.3
pygame.mixer.init()

###馬達
#訊號輸出pin(PWM)
MotorPin=18
#訊號輸出pin設置
gpio.setup(MotorPin,gpio.OUT)
#50 : 頻率(Hz)
PWM_FREQ = 50
pwm_motor = gpio.PWM(MotorPin, PWM_FREQ)
# 設定一開始的Duty Cycle為 7.5
pwm_motor.start(7.5)
loop = 1
running = True
AvgArr =[]
input_result = True
excecute = False
dbzplaying = False
def showResult():
    global excecute ,input_result, running, dbzplaying
    while True:
        # 放開 = 1 = True
        # 按下 = 0 = False
        #接收到按鈕輸入
        input_result = gpio.input(btn)
        print("【input result】",input_result)

        ####大悲咒按鈕####
        input_result2 = gpio.input(btn2)
        print("【input result】",input_result)
        if input_result2 == False:#當被按下去時
            # 開始撥音樂
            if dbzplaying == False:
                # 載入、撥放音樂
                dbz = pygame.mixer.Sound('/home/pi/mp3/DBZq.wav')
                pygame.mixer.Sound.play(dbz)
                print('isplaying')
                dbzplaying = True
                #print("【Playing】",input_result)
            else:
            # 暫停音樂
                pygame.mixer.Sound.stop(dbz)
                print('isnotplaying')
                dbzplaying = False
                #print("【Stop】",input_result)
        #################

        if input_result == False:
            print("=============Start================")
            running = True
            detect()
        time.sleep(delaysec)
def detect():
    global loop ,running, AvgArr, input_result, excecute
    while running:
        if ckeck():
            print("=============Stop================")
            running = False
        print('{}-SoundValue：{:.4f}, ButtonValue：{}'.format(loop, sound.value, digital_sound.value))
        
        AvgArr.append(sound.value)
        time.sleep(0.1)
        
        loop += 1
        if (loop%10 == 0):
            Avg = sum(AvgArr)/10
            #如果太大聲
            if(Avg > 0.17):
                print("【too loud!!!!!】")
                # 拍牆壁
                # t.join()
                # t.start()
                for a in range(5):
                    #頻寬百分比 +90 = 4
                    # pwm_motor.ChangeDutyCycle(4.5)
                    pwm_motor.ChangeDutyCycle(4.5)
                    time.sleep(0.25)
                    print ("【To+60】",a)
                    pwm_motor.ChangeDutyCycle(11)
                    time.sleep(0.25)
                    print ("【To-60】")
                pwm_motor.ChangeDutyCycle(7.5)
                pygame.mixer.music.load('/home/pi/mp3/hanweivoice.mp3')
                pygame.mixer.music.play(0,0.6)
                time.sleep(1)
                    # t.join()
                # time.sleep(0.2)
            print("--------")
            print("Average:",Avg)
            print("--------")
            AvgArr = []

def ckeck():
    time.sleep(0.25)
    input_result = gpio.input(btn)
    if input_result == False: #當被按下去時
        return True
    else:
        return False

def destroy():
    print('keyboard interrupt') 
    gpio.cleanup()
def main():
    try:
        # button control detect
        showResult()
    except KeyboardInterrupt:
        destroy()
if __name__ == "__main__":
    main()
