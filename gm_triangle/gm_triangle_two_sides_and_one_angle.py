# gm_triangle_two_sides_and_one_angle.py: coded by Kinya MIURA 240206
# ---------------------------------------------------------
print('*** Triangle: two sides and one angle ***')
# ---------------------------------------------------------
import numpy as np

# =========================================================
## --- setting three sides --- ##
sa, sb, ac = 3, 4, 90
print(f'{sa = }, {sb = }, {ac = }')

print()
## --- another side: cosine theorem --- ##
sc = np.sqrt(sa**2 + sb**2 - 2*sa*sb * np.cos(np.deg2rad(ac)))
print(f'{sc = }')

print()
## --- area from sides: Heron's formula  --- ##
area =  sa * sb * np.sin(np.sin(np.deg2rad(ac))) / 2
print(f'{area = }')

print()
## --- included angles from three sides: cosine theorem  --- ##
aa = np.rad2deg(np.arccos((sb**2 + sc**2 - sa**2) / (2*sb*sc)))
ab = np.rad2deg(np.arccos((sc**2 + sa**2 - sb**2) / (2*sc*sa)))
print(f'{aa = }, {ab = }')


# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Triangle: three sides ***
sa = 3, sb = 4, sc = 5

area = 6.0

aa = 36.86989764584401, ab = 53.13010235415599, ac = 73.04223669999585
'''
