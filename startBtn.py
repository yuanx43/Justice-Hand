import subprocess
import RPi.GPIO as gpio
import time
import pygame
from gpiozero import MCP3008, Button
# 按按鈕下去打開
# 按按鈕下去
btn = 27
# 循環間隔時間
delaysec = 0.3
gpio.setmode(gpio.BCM)
gpio.setup(btn, gpio.IN, pull_up_down=gpio.PUD_UP)
global input_result,excecute
def showResult():
    excecute = False
    while True:
        # 放開 = 1 = True
        # 按下 = 0 = False
        #接收到按鈕輸入
        input_result = gpio.input(btn)
        print("【input result】",input_result)
        if input_result == False:#當被按下去時
            # 尚未開啟
            if excecute == False :
                #呼叫 Detect.py 這個檔案
                print("call Detect!!")
                print("Orignal",excecute)
                excecute = not excecute
                Detect.main()
                print("excecute change: ",excecute)
            else:
            # 已經開啟
                # 停止呼叫這個檔案
                print("stop!!")
                # Detect.destroy()
                # destroy()
                excecute = not excecute
                print("excecute change: ",excecute)
                
                
        time.sleep(delaysec)
def detect():
    global loop ,running, AvgArr
    loop = 1
    running = True
    AvgArr =[]
    while running:
        try:
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
                    pygame.mixer.music.load('/home/pi/mp3/hanweivoice.mp3')
                    pygame.mixer.music.play(0,0.6)
                    time.sleep(1)
                        # t.join()
                    # time.sleep(0.2)
                print("--------")
                print("Average:",Avg)
                print("--------")
                AvgArr = []
                print("startBtn.input_resultttttttttdsss",startBtn.input_result)
            # startBtninput_result = gpio.input(btn)
            if startBtn.input_result == False:#當被按下去時
                print("----")
                print("Detecttttttttt", startBtn.excecute)
                if startBtn.excecute == True :
                    destroy()
                    running = False
def destroy():
    print('keyboard interrupt') 
    gpio.cleanup()
def main():
    try:
        showResult()
    except KeyboardInterrupt:
        destroy()
if __name__ == "__main__":
    main()