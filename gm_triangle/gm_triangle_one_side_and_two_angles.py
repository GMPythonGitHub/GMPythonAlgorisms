# gm_triangle_one_side_and_two_angles.py: coded by Kinya MIURA 240206
# ---------------------------------------------------------
print('*** Triangle: one side_and two angles ***')
# ---------------------------------------------------------
import numpy as np

# =========================================================
## --- setting three sides --- ##
sa, ab, ac = 3, 60, 60
print(f'{sa = }, {ab = }, {ac = }')

print()
## --- another angle: sum of interior angles --- ##
aa = 180 - ab - ac
print(f'{aa = }')

print()
## --- another sides: sine theorem --- ##  sa / sin(aa) = sb / sin(ab) = sc / sin(ac)
sb = sa * np.sin(np.deg2rad(ab)) / np.sin(np.deg2rad(aa))
sc = sa * np.sin(np.deg2rad(ac)) / np.sin(np.deg2rad(aa))
print(f'{sb = }, {sc = }')

print()
## --- area from sides: Heron's formula  --- ##
ss = (sa + sb + sc) / 2
area = np.sqrt(ss * (ss-sa) * (ss-sb) * (ss-sc))
print(f'{area = }')


# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Triangle: one side_and two angles ***
sa = 3, ab = 60, ac = 60

aa = 60

sb = 3.0000000000000004, sc = 3.0000000000000004

area = 3.8971143170299727
'''
