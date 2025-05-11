import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

f = open("dfidt.csv")
dfidt = []
for line in f:
    dfidt.append(float(line))
f.close()

f = open("fi.csv")
fi = []
for line in f:
    fi.append(float(line))
f.close()

plt.plot(fi[0], dfidt[0], 'ro')
plt.plot(fi, dfidt)

plt.xlabel('φ')
plt.ylabel('φ'+'\u0307')
plt.title("Фазовая траектория")
plt.grid(which='major', color='gray', linestyle='-')
plt.grid(which='minor', color='gray', linestyle='--', linewidth=0.5)
plt.minorticks_on()
plt.legend()
plt.show()