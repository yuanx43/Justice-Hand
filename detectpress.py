import threading
import RPi.GPIO as gpio
import time
from gpiozero import MCP3008, Button
import pygame
from telegram.ext import Updater # 更新者
from telegram.ext import CommandHandler, CallbackQueryHandler # 註冊處理 一般用 回答用
from telegram.ext import MessageHandler, Filters # Filters過濾訊息
from telegram import InlineKeyboardMarkup, InlineKeyboardButton # 互動式按鈕

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

# global variables
loop = 1
running = True
AvgArr =[]
input_result = True

# bot start 
def start(update, context):
    global running, input_result, detecting_thread, previous
    # = press the Btn1
    input_result = False
    running = True
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="start ok!")
    print("=============Start================",chat_id)
    
    detecting_thread = None
    detecting_thread = threading.Thread(target=detectDB)
    detecting_thread.start()
    previous = True

# bot stop
def stop(update,context):
    global running, detecting_thread, previous
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="stop ok!")
    # print("=============Start================")
    print("=============Stop================",chat_id)
    running = False
    detecting_thread = None
    previous = False

# bot play background music
def DBZ(update,context):
    play('/home/pi/mp3/DBZq.wav')
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="A MI TO FOOl，A MI TO FOOl~~")
    print("=============A-MI-TO-FOOL================")

def DBZ(update,context):
    play('/home/pi/mp3/DBZq.wav')
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="A MI TO FOOl，A MI TO FOOl~~")
    print("=============A-MI-TO-FOOL================")

# play stop 
def DBZstop(update,context):
    # 暫停音樂
    pygame.mixer.Channel(0).stop()
    print('music stop_playing')
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="A MI stop，A MI stop~~")
    print("=============A-MI-stop================")


# detect voice 
def detectDB():
    global loop ,running, AvgArr, input_result
    # 開始運作bot
    print("read stop function")
    while running :
        print('{}-SoundValue:{:.4f}, ButtonValue:{}'.format(loop, sound.value, digital_sound.value))
        AvgArr.append(sound.value)
        time.sleep(0.1)
        
        loop += 1
        if (loop%5 == 0):
            Avg = sum(AvgArr)/5
            #如果太大聲
            if(Avg > 0.57):
                print("【too loud!!!!!】",Avg)
                # 拍牆壁
                for a in range(5):
                    #頻寬百分比 +90 = 4
                    # pwm_motor.ChangeDutyCycle(4.5)
                    pwm_motor.ChangeDutyCycle(4.5)
                    time.sleep(0.3)
                    print ("【To+60】",a)
                    pwm_motor.ChangeDutyCycle(11)
                    time.sleep(0.3)
                    print ("【To-60】")
                pwm_motor.ChangeDutyCycle(7.5)
                pygame.mixer.music.load('/home/pi/mp3/hanweivoice.mp3')
                pygame.mixer.music.play(0,0.6)
                time.sleep(1)
            print("--------")
            print("Average:",Avg)
            print("--------")
            AvgArr = []

def play(file) :
    player = pygame.mixer.Sound(file)
    pygame.mixer.Channel(0).play(player)

def detectBtn():
    global input_result, running, previous
    while True:
        # 放開 = 1 = True
        # 按下 = 0 = False
        #接收到按鈕輸入
        input_result = gpio.input(btn)
        print("【Btn1_In】",input_result)

        ####大悲咒按鈕####
        input_result2 = gpio.input(btn2)
        print("【Btn2_In】",input_result2)
        
        #當Btn2 被按下去時
        if input_result2 == False:
            # 開始播背景音樂
            if pygame.mixer.Channel(0).get_busy() == False:
                # 載入、播放音樂
                play('/home/pi/mp3/DBZq.wav')
                print("Playing",input_result)
            else:
            # 暫停音樂
                pygame.mixer.Channel(0).stop()
                print('Isnotplaying')
                
        #################
        # when Btn1 pressed
        if input_result == False :
            # 剛才沒按過
            if previous == False :
                print("=============Start================")
                # start to detect
                running = True
                previous = True
                detecting_thread = None
                # add thread to detect voice
                detecting_thread = threading.Thread(target=detectDB)
                detecting_thread.start()
            # 剛才按過
            else :
                running = False
                previous = False
                detecting_thread = None
        time.sleep(delaysec)


def main():
    # 設定 bot token
    token = '想看阿'
    # 初始化bot
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    # set Command
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('play', DBZ))
    dispatcher.add_handler(CommandHandler('stop', stop))
    dispatcher.add_handler(CommandHandler('playstop', DBZstop))
    updater.start_polling()
    # 監測車子上的按鈕
    detectBtn()

# global 
detecting_thread = None
previous = False

if __name__ == "__main__":
    try :
        main() 
        # pass
    except KeyboardInterrupt:
        detecting_thread = None
        gpio.cleanup()
