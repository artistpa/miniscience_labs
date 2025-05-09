import numpy as np
import matplotlib.pyplot as plt
import time
from math import cos, sin


f = open("t.csv")
t = []
for line in f:
    t.append(float(line))
f.close()

f = open("fi.csv")
fi = []
for line in f:
    fi.append(float(line))
f.close()

x = [sin(i) for i in fi]
y = [-cos(i) for i in fi]

plt.ion()
fig = plt.figure(figsize=(5, 5))
ax = plt.axes(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5))
line, = ax.plot([x[0], 0], [y[0], 0], marker='.', label="Какие то параметры системы")
ax.set_title("Анимация Маятника Дубошинского")
ax.legend()
plt.grid()

for i in range(len(fi)):
    line.set_data([x[i], 0], [y[i], 0])
    plt.draw()
    plt.gcf().canvas.flush_events()

    time.sleep(0.001)

plt.ioff()
plt.show()
