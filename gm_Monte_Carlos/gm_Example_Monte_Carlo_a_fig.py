# gm_Example_Monte_Carlo_a_fig: coded by Kinya MIURA 230414
# -----------------------------------------------------------------------------
print('\n*** Monte Carlo Method: Circle ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
import numpy as np

num, cnt = 1000, 0
xxi, yyi, xxo, yyo = [], [], [], []
for i in range(num):
    xx, yy = np.random.rand(), np.random.rand()
    if np.sqrt(xx * xx + yy * yy) < 1:
        cnt += 1
        xxi.append(xx); yyi.append(yy)  # collecting points inside circle
    else:
        xxo.append(xx); yyo.append(yy)  # collection points outside circle
pai = 4 * cnt / num
print(f'{pai = }')

# -----------------------------------------------------------------------------
from matplotlib import (pyplot as plt, patches as pat)

fig, ax = plt.subplots(figsize=(6., 4.))
fig.suptitle('Monte Carlo Simlation')
ax.set_xlim([0,1]); ax.set_ylim([0,1])
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.scatter(xxi, yyi, marker='o', s=4., color='C0', edgecolor='C0')
ax.scatter(xxo, yyo, marker='o', s=4., color='C1', edgecolor='C1')
ptc = pat.Arc(
    xy=[0,0], width=2, height=2, theta1=0, theta2=90,
    linestyle='--', linewidth=1., edgecolor='C2')
ax.add_patch(ptc)
ax.set_aspect('equal')
fig.savefig('gm_Example_Monte_Carlo_a.png')
plt.show()

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Monte Carlo Method: Circle ***
# -----------------------------------------------------------------------------
pai = 3.6
'''