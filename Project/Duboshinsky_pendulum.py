import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from math import sin, cos
# plt.style.use('seaborn-pastel')

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

fig = plt.figure()
ax = plt.axes(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5))
line, = ax.plot([], [])
plt.grid()


def init():
    line.set_data([], [])
    return line,


def animate(i):
    x = [0, sin(fi[i])]
    y = [0, -cos(fi[i])]
    line.set_data(x, y)
    return line,


anim = FuncAnimation(fig, animate, init_func=init,
                     frames=400, interval=0.1, blit=True)

anim.save('sine_wave.gif', writer='imagemagick')
