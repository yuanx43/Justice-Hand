# 通用型類比動態繪圖程式
from gpiozero import MCP3008
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation


adc = MCP3008(0)

# 圖形起始變數設定
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []


# 心跳資料值迭代產生器
def data_gen(t=0):
    cnt = 0
    while cnt < 1000:
        cnt += 1
        t += 0.1
        yield t, adc.value * 1023


# 圖形啟始函數
def init():
    # gpiozero ADC傳回0與1之間的轉換數值
    # ax.set_ylim(0.4, 0.8)
    # 設定Y軸高度，若使用傳回值為10位元的函數，可以改用1023為高度值
    ax.set_ylim(0, 1023)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,


# 心跳圖執行繪製
def run(data):
    # 更新資料
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,


ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
                              repeat=False, init_func=init)
plt.show()
