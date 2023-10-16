from gpiozero import MCP3008, Button
import time
import RPi.GPIO as gpio
import pygame
import threading

sound = MCP3008(0)
loop = 1
running = True
digital_sound = Button(4)
AvgArr =[]

###放音樂的設定
btn = 25
# 循環間隔時間
delaysec = 0.3
# 播放音樂的初始化
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

# 子執行緒的工作函數
# def job():
#     pygame.mixer.music.load('/home/pi/mp3/hanweivoice.mp3')
#     for a in range(10):
#         pygame.mixer.music.play(0,0.6)
#         time.sleep(1)


# 建立一個子執行緒
# t = threading.Thread(target = job)

# 執行該子執行緒


while running:
    try:
        print('{}-SoundValue：{:.4f}, ButtonValue：{}'.format(loop, sound.value, digital_sound.value))
        AvgArr.append(sound.value)
        time.sleep(0.1)
        loop += 1
        if (loop%10 == 0):
            Avg = sum(AvgArr)/10
            #如果太大聲
            if(Avg > 0.15):
                print("【too loud!!!!!】")
                # 拍牆壁
                # t.join()
                # t.start()
                for a in range(10):
                    
                    pygame.mixer.music.load('/home/pi/mp3/hanweivoice.mp3')
                    pygame.mixer.music.play(0,0.6)
                    #頻寬百分比 +90 = 4
                    # pwm_motor.ChangeDutyCycle(4.5)
                    pwm_motor.ChangeDutyCycle(4.5)
                    time.sleep(0.25)
                    print ("【To+60】",a)
                    pwm_motor.ChangeDutyCycle(11)
                    time.sleep(0.25)
                    print ("【To-60】")
                time.sleep(1)
                    # t.join()
                # time.sleep(0.2)
            print("--------")
            print("Average:",Avg)
            print("--------")
            AvgArr = []
            
    except KeyboardInterrupt:
        running = False