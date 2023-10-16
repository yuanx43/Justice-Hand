from gpiozero import MCP3008, Button
import time

sound = MCP3008(0)
loop = 1
running = True
digital_sound = Button(4)
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
            if(Avg > 0.1):
                print("【too loud!!!!!】")
            print("--------")
            print("Average:",Avg)
            print("--------")
            AvgArr = []
    except KeyboardInterrupt:
        running = False
