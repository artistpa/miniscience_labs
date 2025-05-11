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
t1 = [(t[i + 1] - t[i]) for i in range(len(t) - 1)]
t1.append(t1[-1])

plt.ion()
fig = plt.figure(figsize=(5, 5))
ax = plt.axes(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5))
line, = ax.plot([x[0], 0], [y[0], 0], marker='.', label="")
ax.set_title("Анимация маятника Дубошинского")
ax.legend()
plt.grid()

for i in range(0, len(fi), 1):  # <- количество пропусков кадров для ускорения
    line.set_data([x[i], 0], [y[i], 0])
    plt.draw()
    plt.gcf().canvas.flush_events()

    time.sleep(t1[i])

plt.ioff()
plt.show()
