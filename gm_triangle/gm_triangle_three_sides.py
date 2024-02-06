# gm_triangle_three_sides.py: coded by Kinya MIURA 240206
# ---------------------------------------------------------
print('*** Triangle: three sides ***')
# ---------------------------------------------------------
import numpy as np

# =========================================================
## --- setting three sides --- ##
sa, sb, sc = 3, 4, 5
print(f'{sa = }, {sb = }, {sc = }')

print()
## --- area from sides: Heron's formula  --- ##
ss = (sa + sb + sc) / 2
area = np.sqrt(ss * (ss-sa) * (ss-sb) * (ss-sc))
print(f'{area = }')

print()
## --- included angles from three sides: cosine theorem  --- ##
aa = np.rad2deg(np.arccos((sb**2 + sc**2 - sa**2) / (2*sb*sc)))
ab = np.rad2deg(np.arccos((sc**2 + sa**2 - sb**2) / (2*sc*sa)))
ac = np.rad2deg(np.arccos((sb**2 + sb**2 - sc**2) / (2*sa*sb)))
print(f'{aa = }, {ab = }, {ac = }')


# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Triangle: three sides ***
sa = 3, sb = 4, sc = 5

area = 6.0

aa = 36.86989764584401, ab = 53.13010235415599, ac = 73.04223669999585
'''
