import threading
import RPi.GPIO as gpio
import time
from time import sleep
from gpiozero import MCP3008, Button
import pygame
from telegram.ext import Updater # 更新者
from telegram.ext import CommandHandler, CallbackQueryHandler # 註冊處理 一般用 回答用
from telegram.ext import MessageHandler, Filters # Filters過濾訊息
from telegram import InlineKeyboardMarkup, InlineKeyboardButton # 互動式按鈕
from picamera import PiCamera,Color
from datetime import datetime
from subprocess import call, Popen, PIPE

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
delayy = 0.3
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

# camera
camera = PiCamera()

PHOTO_PATH = ''
VIDEO_PATH = ''
VIDEO_PATH_mp4 = ''
isstart = False
isstop = True
isDBZstart = False
isDBZstop = True

# bot start 
def start(update, context):
    global running, input_result, detecting_thread, previous, isstart, isstop
    if isstart == False :
        p = Popen("ip route list", shell=True, stdout=PIPE)
        data = p.communicate()[0].decode().split()
        ip = data[data.index('src')+1]
        # = press the Btn1
        input_result = False
        running = True
        chat_id = update.message.chat_id
        context.bot.send_message(chat_id=chat_id, text="start ok!, The IP of RPi is : " + ip)
        print("=============Start================",chat_id)
        
        detecting_thread = None
        detecting_thread = threading.Thread(target=detectDB)
        detecting_thread.start()
        previous = True
        isstart = True
        isstop = False
    else:
        chat_id = update.message.chat_id
        context.bot.send_message(chat_id=chat_id, text="Already start!")

# bot stop
def stop(update,context):
    global running, detecting_thread, previous, isstop, isstart
    if isstop == False:
        chat_id = update.message.chat_id
        context.bot.send_message(chat_id=chat_id, text="stop ok!")
        # print("=============Start================")
        print("=============Stop================",chat_id)
        running = False
        detecting_thread = None
        previous = False
        isstop = True
        isstart = False
    else:
        chat_id = update.message.chat_id
        context.bot.send_message(chat_id=chat_id, text="Already stop!")


# bot play background music
def DBZ(update,context):
    global isDBZstart, isDBZstop
    if isDBZstart == False:
        play('/home/pi/mp3/DBZq.wav')
        chat_id = update.message.chat_id
        context.bot.send_message(chat_id=chat_id, text="A MI TO FOOl，A MI TO FOOl~~")
        print("=============A-MI-TO-FOOL================")
        isDBZstart = True
        isDBZstop = False
    else:
        chat_id = update.message.chat_id
        context.bot.send_message(chat_id=chat_id, text="Bot is playing!")

# bot take photo
def photo(update,context):
    # global Tbot
    # Tbot = False
    
    chat_id = update.message.chat_id
    # context.bot.send_message(chat_id=chat_id, text="stop ok!")
    # TELEGRAM_CHAT_ID = 'update.message.chat_id'
    takephoto()

    count = time_now(0)
    context.bot.send_message(chat_id, text=" Photo From Telegram Bot : %s" %count)
    context.bot.send_photo(chat_id, photo=open(PHOTO_PATH, 'rb'))
        
    
    # print("=============Start================")
    print("=============Photo================",chat_id)
    # detect()

# bot record video
def video(update,context):
    global VIDEO_PATH, VIDEO_PATH_mp4
    # Tbot = False
    
    chat_id = update.message.chat_id
    # context.bot.send_message(chat_id=chat_id, text="stop ok!")
    # TELEGRAM_CHAT_ID = 'update.message.chat_id'
    recordvideo()

    count = time_now(0)
    context.bot.send_message(chat_id, text=(" Video From Telegram Bot : %s" %count))
    context.bot.send_video(chat_id, video=open(VIDEO_PATH_mp4, 'rb'))
        
    
    # print("=============Start================")
    print("=============Video================",chat_id)
    # detect()

# play stop 
def DBZstop(update,context):
    global isDBZstart, isDBZstop
    if isDBZstop == False:
        # 暫停音樂
        pygame.mixer.Channel(0).stop()
        print('music stop_playing')
        chat_id = update.message.chat_id
        context.bot.send_message(chat_id=chat_id, text="A MI stop，A MI stop~~")
        print("=============A-MI-stop================")
        isDBZstop = True
        isDBZstart = False
    else:
        chat_id = update.message.chat_id
        context.bot.send_message(chat_id=chat_id, text="Music is stopped!")


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
        time.sleep(delayy)

# call bot to take photo
def takephoto():
    global PHOTO_PATH
    camera.start_preview()
    camera.annotate_background = Color('red')
    camera.annotate_text = "I'm the bad neighbor"
    # sleep(0.25)
    camera.rotation = 180
    PHOTO_PATH = '/home/pi/camera/image.jpg'
    camera.capture(PHOTO_PATH)
    camera.stop_preview()
    print("photo tooken")

# call bot to record video
def recordvideo():
    global VIDEO_PATH,VIDEO_PATH_mp4,count
    count = time_now(1)
    # camera.resolution = (1000, 1000)
    camera.start_preview()
    camera.annotate_background = Color('red')
    camera.annotate_text = "I'm the bad neighbor"
    camera.rotation = 180
    VIDEO_PATH = ('/home/pi/camera/video%s.h264'% count)
    VIDEO_PATH_mp4 = ('/home/pi/camera/video%s.mp4'% count)
    camera.start_recording(VIDEO_PATH)
    time.sleep(5)
    camera.stop_recording()
    camera.stop_preview()
    convert(VIDEO_PATH, VIDEO_PATH_mp4)
    print("video recorded")

# covert video format
def convert(VIDEO_PATH, VIDEO_PATH_mp4):
    # Record a 15 seconds video.
    print("Rasp_Pi => Video Recorded! \r\n")
    # Convert the h264 format to the mp4 format.
    command = "MP4Box -add " + VIDEO_PATH + " " + VIDEO_PATH_mp4
    call([command], shell=True)
    print("\r\nRasp_Pi => Video Converted! \r\n")

def time_now(type):
    # 1:檔名
    # 0: 時間字串
    if(type == 1):
        result = datetime.now().strftime("%Y%m%d%H%M%S%p")
    else:
        result = datetime.now().strftime("%Y-%m-%d %H:%M:%S %p")
    print(result)
    return result

def main():
    # 設定 bot token
    token = '5025165228:AAGTD4Lv1kojz0N4YjdEX9A6wUURRmseQK0'
    # 初始化bot
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    # set Command
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('play', DBZ))
    dispatcher.add_handler(CommandHandler('stop', stop))
    dispatcher.add_handler(CommandHandler('playstop', DBZstop))
    dispatcher.add_handler(CommandHandler('photo', photo))
    dispatcher.add_handler(CommandHandler('video', video))
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
