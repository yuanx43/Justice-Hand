import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
#訊號輸出pin(PWM)
MotorPin=12
#訊號輸出pin設置
GPIO.setup(MotorPin,GPIO.OUT)
#50 : 頻率(Hz)
PWM_FREQ = 50
pwm_motor = GPIO.PWM(MotorPin, PWM_FREQ)
# 設定一開始的Duty Cycle為 7.5
pwm_motor.start(7.5)
# +90度：( 0.8 ms ／ 20 ms ) * 100 = 4
# +60度：( 0.9 ms ／ 20 ms ) * 100 = 4.5
#   0度：( 1.5 ms ／ 20 ms ) * 100 = 7.5
# -60度：( 2.1 ms ／ 20 ms ) * 100 = 10.5
# -90度：( 2.2 ms ／ 20 ms ) * 100 = 11
def angle_to_duty_cycle(angle=0):
    duty_cycle = int((0.5 * PWM_FREQ + (1.9 * PWM_FREQ * angle / 180)))
    return duty_cycle

while True:
        for a in range(100):
            #頻寬百分比 +90 = 4
            # pwm_motor.ChangeDutyCycle(4.5)
            pwm_motor.ChangeDutyCycle(4.5)
            time.sleep(0.25)
            print ("【To+60】",a)
#       pwm_motor.stop()
        # for b in range(100):
            #頻寬百分比 60度 = 4.5    
            pwm_motor.ChangeDutyCycle(11)
            time.sleep(0.25)
            print ("【To-60】")