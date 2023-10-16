import RPi.GPIO as gpio
import time
import pygame

btn = 25
# 循環間隔時間
delaysec = 0.3
# 播放音樂的初始化
pygame.mixer.init()
gpio.setmode(gpio.BCM)
gpio.setup(btn, gpio.IN, pull_up_down=gpio.PUD_UP)
def showResult():
    while True:
        # 放開 = 1 = True
        # 按下 = 0 = False
        #接收到按鈕輸入
        input_result = gpio.input(btn)
        print("【input result】",input_result)
        if input_result == False:#當被按下去時
            # 開始撥音樂
            if pygame.mixer.music.get_busy() == False:
                # 載入、撥放音樂
                pygame.mixer.music.load('/home/pi/mp3/hanweivoice.mp3')
                pygame.mixer.music.play(0, 6)
                #print("【Playing】",input_result)
            else:
            # 暫停音樂
                pygame.mixer.music.stop()
                #print("【Stop】",input_result)
        time.sleep(delaysec)
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