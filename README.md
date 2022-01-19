# Justice Hand
- [Concept Development](#Concept_Develop)
- [硬體設備](#device)
- [安裝&設定過程](#install_setting)
- [補充: telegram bot](#telegram);
- [LSA課堂知識運用](#LSAClass)
- [Usage 如何使用](#Usge)
- [Justice Hand Car 照](#picture)
- [Job Assignment](#Job_Assign)
- [References](#References)
- [未來展望](#future)
- [溫馨感謝愛心助教](#thankTA)
## [ppt連結](https://docs.google.com/presentation/d/1XCrpMcQiEwSbro5FNwrldORE6NMPBbfv1iDoVzJy5oo/edit?usp=sharing)
## <a id="Concept_Develop"></a>Concept Development 發展理念
* 起因:
    1. 因為只要每到晚上，就會聽到隔壁總是會聽到奇怪的噪音，嚴重影響睡眠品質。但是我們又害怕被看到臉會被惡意報復，所以我們決定開著遙控車車反擊!
    2. 賴床
* 發想: 我們想要以牙還牙，每次當鄰居房間開始製造噪音時，我們就在自己房間感應分貝大小自動啟動假手裝置開始拍打牆壁，藉此來提醒鄰居
* 功能:
    - 能偵測對方音量，超過規定分貝，啟動假手
    - 假手會借用馬達來拍打牆壁，產生噪音攻擊
    - 可手動開啟/關閉
    - 額外功能
        - **賴床打臉器**(後來就沒用了)
            - 可以定時，時間到了就朝臉開打
        - **遙控車子移動**
            - 假手放置在車子上
            - 再由遙控器控制移動到指定位置
## <a id="device"></a>硬體設備(有用到的東東)
| 設備名稱 | 圖片網址 |來源|
| ---- | ---- |---|
|Raspberry Pi 4|<img src="https://user-images.githubusercontent.com/63627053/148636518-a1c42d3c-4008-4157-9f72-9f28854be120.png" width="150px"/>|友情贊助(助教贊助)|
|mbot車車|<img src="http://images.1111.com.tw/discussPic/45/51648645_75727617.5286941.png" width="150px"/>|親情贊助(林宜蔓同學提供)|
|伺服馬達|<img src="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQdHe04RWYSRtZouKLoIqJVSUAHOdwwLwoS2U1VbY9P8XX47X45" width="150px"/>|網購|
|伺服馬達多功能支架|<img src="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcR1F1oO-9AuM34WaAzLDipg7UaQwz7DDYseE0q9gmgRe5HKEC4N" width="150px"/>|網購|
|伺服機擺臂|<img src="https://user-images.githubusercontent.com/63627053/148635985-48353e50-b2a5-4dc3-9d99-78b1a281846e.png" width="150px"/>|蝦皮|
|分貝感測器|<img src="https://img.pcstore.com.tw/~prod/M79772911/_sE_9391353439.jpg?pimg=static&P=1621835550" width="150px"/>|蝦皮|
|MCP3008|<img src="https://user-images.githubusercontent.com/63627053/148636025-e9eeb48a-419a-4f4e-857c-625c74be03ac.png" width="150px"/>|蝦皮|
|開關鍵|<img src="https://img.shoplineapp.com/media/image_clips/6052c25107ec3137c14b48e4/original.jpg?1616036433" width="150px"/>|親情贊助(林宜蔓同學提供)|
|喇叭|<img src="https://i.imgur.com/FQPKH8K.jpg" width="150px"/>|蕭鈺宸同學提供|
|杜邦線*n(公母、公公、母母)|<img src="https://user-images.githubusercontent.com/63627053/148636593-841e6c5d-9666-4362-8700-3c6160984a3a.png" width="150px"/>|親情贊助(林宜蔓同學提供)|
|麵包板|<img src="https://img.eclife.com.tw/photo2011/prod_2017/7/K1020189-A.jpg" width="150px"/>|親情贊助(林宜蔓同學提供)|
|假手|<img src="https://i1.wp.com/henglong.gr/wp-content/uploads/2021/04/premier-soft-hand-a.jpg?fit=600%2C600&ssl=1" width="150px"/>|蝦皮|
|4號電池|<img src="https://user-images.githubusercontent.com/63627053/148636983-af1f6cdf-38dd-4381-8f68-1aad00c402cb.png" width="150px"/>|蝦皮|
|pi camara|<img src="https://www.taiwaniot.com.tw/wp-content/uploads/2019/12/raspberry-pi-camera-v2-camera-600x450.png" width="150px"/>|友情贊助(第七組)|

## <a id="install_setting"></a>安裝&設定過程
### GPIO&設備
#### GPIO
<img src="https://i.imgur.com/9zIuu4Q.png" width="500px"/>

#### 按鈕
| 按鈕接口 | Raspberry Pi 接口 | 
| -------- | -------- |
| OUT  | GPIO27 |
| VCC   | 5v |
| GND   | GND |
#### 分貝感測器
| 分貝感測器接口 | Raspberry Pi 接口 | 
| -------- | -------- |
| AOUT   |  MCP3008 CH0 (GPIO4)  |
| DOUT   | GPIO17    |
| GND   |  GND  |
| VCC   |   5v |
#### MCP3008
- MCP3008 pinout description 
    </br><img src="https://i.imgur.com/2siPlth.png" width="400px"/>
    > 來源：MCP3008 Datasheet
    > 
    
    <img src="https://i.imgur.com/6yepSYS.png" width="400px"/>

| MCP3008接口 | Raspberry Pi 接口 |
| ----------- | ----------------- |
| CH0         | GPIO4             |
| VDD         | 5V                |
| VREF        | 5V                |
| AGND        | GND               |
| CLK         | GPIO11            |
| DOUT        | GPIO9             |
| DIN         | GPIO10            |
| CS/SHDN     | GPIO8             |
| DGND        | GND               |
#### 伺服馬達
| 伺服馬達接口 | Raspberry Pi 接口 | 
| -------- | -------- |
| OUT(橘)   | GPIO18 |
|VCC(紅)    | 5V     |
| GND(棕)   | GND    |


### 開啟 SPI
#### 開啟原因: 
- 樹莓派本身並不支援類比輸入(Analog Input)
    - 因此需要使用額外的AD轉換器（Analog to Digital Conveter）來，讀取類比資訊
- 此次使用的ADC IC為 MCP3008
- ADC IC需要使用 SPI介面來溝通，交換資訊
- MCP3008 & Raspberry pi 特殊GPIO(SPI)接法
    - GPIO 07 ~ 11: 專門給SPI介面使用
    <img src="https://i.imgur.com/OeeeJK3.png" width="500px"/>
#### 實作
- 進入設定介面 
```terminal=
sudo raspi-config
```
- 選擇 Interfacing Option3
    </br><img src="https://i.imgur.com/FpJh8lV.png" width="500px"/>
- 選擇SPI
    </br><img src="https://i.imgur.com/zvEaRg8.png" width="500px"/>
- SPI enabled(yes)
    - 選擇yes-> OK
    </br><img src="https://i.imgur.com/EdCZa98.png" width="350px"/><img src="https://i.imgur.com/M6UGHY8.png" width="350px"/>
- 重新開機
    ```terminal=
    sudo reboot
    ```
- 檢查是否開啟成功SPI
    - 顯示`spi_bcm2835`表示成功開啟SPI
    ```terminal=
    lsmod | grep spi
    ```
    <img src="https://i.imgur.com/wPdjmFe.png" width="300px"/>
### 先更新套件
```terminal=
sudo apt update
sudo apt upgrade
```
### 程式編輯器: vim
```terminal=
sudo apt install vim
```
### python
```terminal=
sudo apt install python3-pip
``` 
### 播放音樂 pygame.mixer()
- pygame.mixer() : 是一個用來處理聲音的模組
- 要先安裝pygame&音樂相關套件
    ```terminal=
    sudo pip3 install pygame
    sudo apt install libsdl2-dev
    sudo apt install libsdl2-mixer-dev
    ``` 
- 引入模組&套件啟動、初始化
    ```python=
    import pygame
    pygame.mixer.init()
    ``` 
- 播放音檔
    ```python=
    pygame.mixer.music.load('音檔路徑')
    pygame.mixer.music.play()
    ```
- 停止播放音檔
    ```python=
    pygame.mixer.music.stop()
    ```
- 範例:
    ```python=
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/mp3/hanweivoice.mp3')
    pygame.mixer.music.play(0,0.6)
    ```
### 分貝感測器
#### MCP3008設置
- 作用：將類比訊號轉換成數位訊號(因為Raspberry Pi沒有支援類比訊號輸入)，每個通道可依類比設備的輸入值傳回一個10位元的數值
- 安裝套件
    ```terminal=
    pip install gpiozero
    ```
- 引入套件
    ```terminal=
    from gpiozero import MCP3008, Button
    ```
- 設置變數
   ```terminal=
   #channel 0 類比訊號腳位
   sound = MCP3008(0)  
   # 數位訊號腳位
   digital_sound = Button(4)
   ```
#### 分貝感測器
- 範例 - 每0.1秒傳送偵測資料
   ```terminal=
   while running:
    try:
        print('{}-SoundValue：{:.4f}, ButtonValue：{}'.format(loop, sound.value, digital_sound.value))
        AvgArr.append(sound.value)
        time.sleep(0.1)
        loop += 1
    except KeyboardInterrupt:
        running = False
    ```

### 伺服馬達
- 腳位、頻率設定
   ```terminal=
    #訊號輸出pin(PWM)
    MotorPin=18
    #訊號輸出pin設置
    gpio.setup(MotorPin,gpio.OUT)
    #50 : 頻率(Hz)
    PWM_FREQ = 50
    pwm_motor = gpio.PWM(MotorPin, PWM_FREQ)
   ```
- 設定初始角度
  - +90度：( 0.8 ms ／ 20 ms ) * 100 = 4
  - +60度：( 0.9 ms ／ 20 ms ) * 100 = 4.5
  - 0度：( 1.5 ms ／ 20 ms ) * 100 = 7.5
  - -60度：( 2.1 ms ／ 20 ms ) * 100 = 10.5
  - -90度：( 2.2 ms ／ 20 ms ) * 100 = 11
   ```terminal=
    pwm_motor.start(7.5)
    ```
- 範例 - 從+60度轉到-90度5次，並回歸0度位
   ```terminal=
   for a in range(5):
        pwm_motor.ChangeDutyCycle(4.5)
        time.sleep(0.25)
        pwm_motor.ChangeDutyCycle(11)
        time.sleep(0.25)
    pwm_motor.ChangeDutyCycle(7.5)
    ```
### 按鈕
- 引入套件
    ```terminal=
    import RPi.GPIO as gpio
    ```
- 設置變數
   ```terminal=
    btn = 27
    # button pin setup
    gpio.setmode(gpio.BCM)
    gpio.setup(btn, gpio.IN, pull_up_down=gpio.PUD_UP)
   ```
- 接收按鈕輸入
  - 放開 = 1 = True
  - 按下 = 0 = False
    ```terminal=
    input_result = gpio.input(btn)
    ```
### Pi camera
- 安裝 pi camera套件
    ```terminal=
    pip3 install picamera
    ````
#### 影片轉檔
- 需要套件
    ```terminal=
    sudo apt install gpac
    ```
- 影片如何轉檔
    ```python=
    
    ```
### 樹梅派開機啟動按鈕偵測檔`detectpress.py`
- 要執行的內容（例如想要跑 Python 的程式等等）要寫成 Shell script
- 創建shell執行檔 `autostart.sh`
    ```terminal=
    sudo vim autostart.sh
    ```
    - 增加執行`detectpress.py`的程式碼
    ```shell=
    #! /bin/bash
    cd /home/pi
    python3 detectpress.py
    ```
- 增加此shell執行檔可以執行的權限
    ```terminal=
    chmod +x /home/pi/autostart.sh
    ```
- 新增一個 service 
 1. `sudo vim /etc/systemd/system/detectpress.service`
 ![](https://i.imgur.com/6YCnAD1.png)
 2. `sudo chmod 644 /etc/systemd/system/detectpress.service`
 3. `sudo systemctl daemon-reload`
 4. `sudo systemctl start detectpress`
 5. `sudo systemctl enable detectpress`
- service 執行結果
 ![](https://i.imgur.com/KsNbEzw.png)




    
## <a id="telegram"></a>Telegram bot
### Telegram bot
- telegram 搜尋 @BotFather 

- 按 /start 
<img src="https://i.imgur.com/OsqLOHX.png" width="250px"/>

- 創造機器人 /newbot
    - 輸入機器人的name
    - 輸入機器人的username</br>
    - 成功後即可獲得機器人的連結&token 

</br><img src="https://user-images.githubusercontent.com/85755825/148934909-3f610766-0c6c-4061-b4fe-49fb84123c1a.JPG" width="250px"/><img src="https://user-images.githubusercontent.com/85755825/148937414-eda0bb71-ef42-4423-846d-f6f9de4689ba.JPG" width="250px"/>

- 接下來輸入 `/mybots`
    - 選擇剛才創造的bot
    <img src="https://i.imgur.com/v2BlNnQ.png" width="300px"/>
- /setcommand，接下來選擇 `@yourbot`
    - 輸入以下commend
        ```typescript=
        start - 開始偵測
        play - 撥放背景音樂
        stop - 停止偵測
        playstop - 停止播放音樂
        photo - 拍照
        video - 錄影
        ```

- 切換到 `@yourbot`
        <img src="https://i.imgur.com/aZcbHYg.png" width="300px" height="600px"/>
   

- 建立群組group&telegram bot
    - Enable telegram bot join groups
        <img src="https://i.imgur.com/zmvwYyC.png" width="300px"/>
    - 自行建立群組+ 邀請telegram bot至group
    - 成果照
        <img src="https://i.imgur.com/1e4M8jz.png" width="300px"/>
### python 套件 python-telegram-bot
- 安裝pip套件 python-telegram-bot
```python=
pip install python-telegram-bot
```
- 匯入模組&初始化bot&設定token
```python=
# 匯入相關套件
from telegram.ext import Updater # 更新者
from telegram.ext import CommandHandler, CallbackQueryHandler # 註冊處理 一般用 回答用
from telegram.ext import MessageHandler, Filters # Filters過濾訊息
from telegram import InlineKeyboardMarkup, InlineKeyboardButton # 互動式按鈕
token = 'add your token here'
# 初始化bot
updater = Updater(token=token, use_context=False)
```

- 設定調度器 & 新增handler並加入dispatcher
    - 輸入 `/start`的時候，robot會去執行start()
    ```python=
    dispatcher = updater.dispatcher
    # 定義收到訊息後的動作(新增handler)
    def start(bot, update): # 新增指令/start
        #robot 回覆在聊天室的訊息
        update.message.reply_text(text='HI  ' + str(chat['id']))    
    #新增handler且加入dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    ```
- 開始運作bot
    ```python=
    # 開始運作bot
    updater.start_polling()        
    ```
    <img src="https://i.imgur.com/0RZs69k.png" width="200px"/>
    ```
- 【**JusticeHand 聊天室**】 畫面
![]()
<img src="https://i.imgur.com/vwBm4g8.png" width="250px"/>

## <a id="LSAClass"></a>LSA課堂知識運用
### 安裝軟體
- sudo apt install vim
- sudo apt install python3-pip
### 編輯程式碼
- (sudo) vim `檔案名稱` 
> 依檔案權限決定是否需要sudo
### 查看程式碼
- cat `檔案名稱`
### 遠端連線
- ssh
### 樹苺派相關
- 燒錄SD卡
- Wi-Fi 設定
- 其他初始設定(開啟ssh設定等等)
### service
- `sudo service <servicename> start `
- `sudo service <servicename> stop`
- `sudo service <servicename> status`

## <a id="Usge"></a>Usage 如何使用
【開機即執行偵測按鈕1】
1. 按下按鈕1(or telegram bot 輸入 `/start`): 開始感測聲音
2. 再次按下按鈕1(or telegram bot 輸入 `/stop`): 停止感測聲音
3. 按下按鈕2(or telegram bot 輸入 `/play`): 撥放背景音樂(ex: 阿彌陀佛)
4. 遙控車子到門前偵測惡鄰居聲音
5. 假如超過設定分貝門檻: Justice Hand開始拍打
6. 拍打完，喇叭播放: 你好吵!!!
7. 額外功能 telegram 輸入 
    - `/video`:錄影
    - `/photo`:拍照
    > 檔案皆會傳至聊天室內
## 成果影片&聊天室畫面
- 聊天室畫面
    
    <img src="https://i.imgur.com/03enHxf.png" width="600px"/>
- 照片畫面
    
    <img src="https://i.imgur.com/Bgex5e3.png" width="600px"/>

- [車車打門影片連結](https://youtu.be/IVrHOSAWFUo)
- [惡鄰居開門了!!](https://youtu.be/wfshMPJA0M0)


## <a id="Usge"></a>Job_Assign
| 組員   | 工作分配        |
| ------ | --------------- |
| 楊心慈 | 程式，PPT       |
| 蕭沁沅 | 程式，Github    |
| 蕭鈺宸 | 程式，Github          |
| 林宜蔓 | 採購, 設備，PPT |
|全部人| 硬體組裝  |

## <a id="References"></a>References
* [更改字體](https://blog.crysu.com/2020/09/25/size/)
* [使用WinSCP戶傳文件](https://zanrobot.com/raspberry-pi/2775/)
- 伺服馬達
    * [Raspberry Pi GPIO (三) 控制伺服馬達](https://p501lab.blogspot.com/2014/07/raspberry-pi-gpio.html)
    * [Raspberry Pi Pico筆記(11)：控制伺服馬達Servo](https://atceiling.blogspot.com/2021/04/raspberry-pi-pico11servo.html)
- 分貝感測器
    * [樹莓派4B之聲音感測器模組（python3）](https://www.gushiciku.cn/pl/p5kQ/zh-tw)
    * [聲音感測器實作範例](https://s761111.gitbook.io/raspi-sensor/yin-gan-qi)
- MCP3008
    * [MCP3008](https://atceiling.blogspot.com/2014/04/raspberry-pi-mcp3008.html)
    * [樹莓派：類比轉數位處理](https://s761111.gitbook.io/raspi-sensor/pai-bi-wei-li) 
- 聲音播放
    * [樹莓派+Ubuntu終端命令列播放音樂(mp3)](https://www.gushiciku.cn/pl/gqJL/zh-tw)
    * [myplayer](https://www.itread01.com/content/1526740705.html)
- 按鈕
    * [樹梅派小實驗 | 製作一個音樂盒](https://blog.csdn.net/qq_45032341/article/details/105756334)
    * [使用python播放.mp4並檢查是否/仍在播放](https://www.itread01.com/question/NXYwbmc=.html)
    * [Push button + LED + sound](https://raspberrypi.stackexchange.com/questions/51088/push-button-led-sound)
    * [按鈕開關](https://s761111.gitbook.io/raspi-sensor/an) 
    * [pygame語法](https://spimet.com/blog/archives/685)
- telegram robot
    - [Python Telegram Bot 教學 (by 陳達仁)](https://hackmd.io/@truckski/HkgaMUc24)
    - [【Telegram API】Python打造Telegram機器人手把手教學：最輕鬆最詳細的方法](https://pixnashpython.pixnet.net/blog/post/32391757-%E3%80%90telegram-api%E3%80%91python%E6%89%93%E9%80%A0telegrame%E6%A9%9F%E5%99%A8%E4%BA%BA%E6%89%8B%E6%8A%8A%E6%89%8B%E6%95%99)
- 新增service
    - [Linux 建立自訂 Systemd 服務教學與範例](https://blog.gtwang.org/linux/linux-create-systemd-service-unit-for-python-echo-server-tutorial-examples/)
## <a id="future"></a>未來展望
- 影像辨識:
    - 將惡鄰居的樣貌拍起來
    - 如果有人對我們投以好奇的目光就用喇叭撥放:看屁阿!!!!
    - 增加鬧鐘功能：時間到了就會打你打到起來關掉
- 電子花車
    - 增加第三組的繽紛LED氣氛燈
    - 接上步進馬達，並放置小姐公仔在上面旋轉展示 

## <a id="thankTA"></a>溫馨感謝愛心助教 :heart:
- 漢偉 @UncleHanWei :題材發想、提供音檔來源、提供硬體設備、參與錄影、debug(tech support)
- 蔣媽 @yuting0412 : 題材發想、提供硬體設備
- 郭子偉 @vincentinttsh : support Raspberry pi 4、debug(tech support)、提供硬體設備 、 write github README.md ，提供全方位服務請撥打:0800029000
