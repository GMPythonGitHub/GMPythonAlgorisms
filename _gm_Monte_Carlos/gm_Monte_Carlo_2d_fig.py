# gm_Monte_Carlo_2d_fig: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Monte Carlo Method: Circle, figure ver. ***')
# ---------------------------------------------------------
import numpy as np

# =========================================================
## --- main routine --- ##
num, cnt = 1000, 0
xxi, yyi, xxo, yyo = [], [], [], []
for i in range(num):
    xx = np.random.rand() * 2. - 1.
    yy = np.random.rand() * 2. - 1.
    # square area; 2 * 2
    if np.sqrt(xx * xx + yy * yy) < 1.:
        cnt += 1  # counting points inside circle
        xxi.append(xx); yyi.append(yy)  # points inside circle
    else:
        xxo.append(xx); yyo.append(yy)  # points outside circle
pai = 4 * cnt / num  # estimating pai
print('total number of points: ', f'{num = :d}')
print('number of points inside circle: ', f'{cnt = :d}')
print('estimated value of pai: ', f'{pai = :g}')

## --- drawing figure --- ##
from matplotlib import (pyplot as plt, patches as pat)

fig, ax = plt.subplots(figsize=(6., 4.))
fig.suptitle('Monte Carlo Simulation')
ax.set_xlim([-1,1]); ax.set_ylim([-1,1])
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.scatter(xxi, yyi, marker='o', s=4., color='C0', edgecolor='C0')
ax.scatter(xxo, yyo, marker='o', s=4., color='C1', edgecolor='C1')
ptc = pat.Arc(
    xy=(0,0), width=2, height=2, theta1=0, theta2=360,
    linestyle='--', linewidth=1., edgecolor='C2')
ax.add_patch(ptc)
ax.set_aspect('equal')
fig.savefig('gm_Monte_Carlo_2d.png')
plt.show()

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Monte Carlo Method: Circle, figure ver. ***
total number of points:  num = 1000
number of points inside circle:  cnt = 801
estimeted value of pai:  pai = 3.204
'''