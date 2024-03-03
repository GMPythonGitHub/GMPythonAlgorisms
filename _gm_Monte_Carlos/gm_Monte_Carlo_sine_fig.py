# gm_Monte_Carlo_sine_fig: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('***  Monte Carlo Method: sine curve, figure ver. ***')
# ---------------------------------------------------------
import numpy as np

# =========================================================
num, cnt = 1000, 0
xxi, yyi, xxo, yyo = [], [], [], []
for i in range(num):
    xx, yy = np.random.rand() * np.pi, np.random.rand()
    # rectangular domain; pi * 1
    if np.sin(xx) > yy:  # counting points under sine curve
        cnt += 1
        xxi.append(xx); yyi.append(yy)  # points under sine curve
    else:
        xxo.append(xx); yyo.append(yy)  # points over sine curve
area = np.pi * cnt / num  # estimating area under sine curve
print('total number of points: ', f'{num = :d}')
print('number of points under sine curve: ', f'{cnt = :d}')
print('estimated value of area: ', f'{area = :g}')

# =========================================================
## --- drawing figure --- ##
from matplotlib import (pyplot as plt, patches as pat)

fig, ax = plt.subplots(figsize=(6., 4.))
fig.suptitle('Monte Carlo Simulation')
ax.set_xlim((0,np.pi)); ax.set_ylim([0,1])
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.scatter(xxi, yyi, marker='o', s=4., color='C0', edgecolor='C0')
ax.scatter(xxo, yyo, marker='o', s=4., color='C1', edgecolor='C1')
xx = np.linspace(0,np.pi,101)
yy = np.sin(xx)
ax.plot(xx, yy,
    linestyle='--', linewidth=1., color='C2')
ax.set_aspect('equal')
fig.savefig('gm_Monte_Carlo_sine.png')
plt.show()

# =========================================================
# terminal log / terminal log / terminal log /
'''
***  Monte Carlo Method: sine curve, figure ver. ***
total number of points:  num = 1000
number of points under sine curve:  cnt = 637
estimated value of area:  area = 2.00119
'''