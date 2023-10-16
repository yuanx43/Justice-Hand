import RPi.GPIO as gpio
import time
import pygame

pygame.mixer.init()


#wait_time = 0.2

gpio.setmode(gpio.BCM)
gpio.setup(btn, gpio.IN, pull_up_down=gpio.PUD_UP)
#gpio.setup(btn2, gpio.IN, pull_up_down=gpio.PUD_UP)

btn = 25
#btn2=18

pre_status = None
pre_status2 = None
#pre_time = time.time()
current_time = None
playing = False

# 按鈕被按 = TRUE
# while 
try:
    while True:
        # 如果正在撥音樂
        if pre_status == 0 and playing == True:
            if pygame.mixer.music.get_busy() == True:
                get_btn = gpio.input(btn)
                print(' Already Play get',get_btn)
                print(' Already Play pre',pre_status)
                if get_btn == 1 and pre_status == 0:
                    print('button pressed!', time.ctime())
                    print('busy:',pygame.mixer.music.get_busy())
                    pygame.mixer.music.stop()
                    playing == False
        # 如果還沒放音樂
        if pygame.mixer.music.get_busy() == False:
            
            get_btn = gpio.input(btn)
            print('Not yet get_btn',get_btn)
            # get_btn2 = gpio.input(btn2)
            current_time = time.time()
            if get_btn == gpio.LOW and pre_status == gpio.HIGH :
                pre_time = current_time
                print('button pressed!', time.ctime())
                print('busy:',pygame.mixer.music.get_busy())
                # 載入、撥放音樂
                pygame.mixer.music.load('/home/pi/mp3/snowman.mp3')
                pygame.mixer.music.play(0, 6)
            # if get_btn2 == gpio.LOW and pre_status2 == gpio.HIGH and (current_time - pre_time) > wait_time:
            #     pre_time = current_time
            #     print('button2 pressed!', time.ctime())
            #     # 載入、撥放音樂
            #     # pygame.mixer.music.load('/home/pi/mp3/snow.mp3')
            #     pygame.mixer.music.stop()
                playing = True
            pre_status = get_btn
            # pre_status2 = get_btn2
            time.sleep(1)
        print('-------------------------------------')
        print('one time detect busy:',pygame.mixer.music.get_busy())
        print('pre_status',pre_status)
        print('get_btn',get_btn)
        print('-------------------------------------')
except KeyboardInterrupt:
    print('keyboard interrupt')
finally:
    gpio.cleanup()