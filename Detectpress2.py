
import RPi.GPIO as gpio
import time
from gpiozero import MCP3008, Button
import pygame
# from telegram.ext import Updater # 更新者
# from telegram.ext import CommandHandler, CallbackQueryHandler # 註冊處理 一般用 回答用
# from telegram.ext import MessageHandler, Filters # Filters過濾訊息
# from telegram import InlineKeyboardMarkup, InlineKeyboardButton # 互動式按鈕

# # 設定 token
# token = '5025165228:AAGTD4Lv1kojz0N4YjdEX9A6wUURRmseQK0'

# # 初始化bot
# updater = Updater(token=token, use_context=True)

# dispatcher = updater.dispatcher



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
Tbot = True
def showResult():
    global excecute ,input_result, running
    while True:
        # 放開 = 1 = True
        # 按下 = 0 = False
        #接收到按鈕輸入
        input_result = gpio.input(btn)
        # print("【input result】",input_result)

        ####大悲咒按鈕####
        input_result2 = gpio.input(btn2)
        print("【input result】",input_result)
        if input_result2 == False:#當被按下去時
            # 開始撥音樂
            if pygame.mixer.Channel(0).get_busy() == False:
                # 載入、撥放音樂
                dbz = pygame.mixer.Sound('/home/pi/mp3/DBZq.wav')
                pygame.mixer.Channel(0).play(dbz)
                print('isplaying')
                #print("【Playing】",input_result)
            else:
            # 暫停音樂
                pygame.mixer.Channel(0).stop()
                print('isnotplaying')
                #print("【Stop】",input_result)
        #################
        # dispatcher.add_handler(CommandHandler('start', start))
        # dispatcher.add_handler(CommandHandler('play', DBZ))
        # # 開始運作bot
        # updater.start_polling()
        # 離開
        # updater.stop()
        if input_result == False:
            print("=============Start================")
            running = True
            detect()
        time.sleep(delaysec)
# def start(update, context): # 新增指令/start
#     global running, input_result
#     input_result = False
#     running = True
#     chat_id = update.message.chat_id
#     context.bot.send_message(chat_id=chat_id, text="start ok!")
#     # print("=============Start================")
#     detect()
# # bot stop
# def stop(bot, update):
#     global Tbot
#     Tbot = False
#     message = update.message
#     update.message.reply_text('Stop OK!')
#     print("=============Stop================")

# def DBZ(bot, update):
#     dbz = pygame.mixer.Sound('/home/pi/mp3/DBZq.wav')
#     pygame.mixer.Sound.play(dbz)
#     update.message.reply_text('A MI TO FOOl，A MI TO FOOl~~')
#     print("=============A-MI-TO-FOOL================")

def detect():
    global loop ,running, AvgArr, input_result, excecute
    # dispatcher.add_handler(CommandHandler('stop', stop))
    # # 開始運作bot
    # updater.start_polling()
    print("read stop function")
    while running:
        if ckeck():
            print("=============Stop================")
            running = False
        print('{}-SoundValue：{:.4f}, ButtonValue：{}'.format(loop, sound.value, digital_sound.value))
        
        AvgArr.append(sound.value)
        time.sleep(0.1)
        
         ####大悲咒按鈕####
        input_result2 = gpio.input(btn2)
        print("【input result】",input_result)
        if input_result2 == False:#當被按下去時
            # 開始撥音樂
            if pygame.mixer.Channel(0).get_busy() == False:
                # 載入、撥放音樂
                dbz = pygame.mixer.Sound('/home/pi/mp3/DBZq.wav')
                pygame.mixer.Channel(0).play(dbz)
                print('isplaying')
                #print("【Playing】",input_result)
            else:
            # 暫停音樂
                pygame.mixer.Channel(0).stop()
                print('isnotplaying')
                #print("【Stop】",input_result)
        #################
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
    global Tbot
    time.sleep(0.25)
    input_result = gpio.input(btn)
    if input_result == False or Tbot == False: #當被按下去時或是輸入
        print("Tbot",Tbot)
        return True
    else:
        return False

def destroy():
    print('keyboard interrupt') 
    gpio.cleanup()
    # 離開
    # updater.stop()
def main():
    try:
        # button control detect
        showResult()
    except KeyboardInterrupt:
        destroy()
if __name__ == "__main__":
    main()
