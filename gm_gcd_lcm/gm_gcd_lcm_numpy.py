# gm_gcd_lcm_numpy: coded by Kinya MIURA 230415
# ---------------------------------------------------------
print('*** Greatest common divisor and Least common multiple ***')
print('   *** using numpy function ***')
# ---------------------------------------------------------
import numpy as np

# =========================================================
## --- main routine --- ##

print(np.gcd(36, 120))
print(np.lcm(36, 120))

print(np.gcd([36, 20], 120))
print(np.lcm([36, 20], 120))

print(np.gcd([36, 20], [120, 100]))
print(np.lcm([36, 20], [120, 100]))

print(np.gcd.reduce((36, 20, 120)))
print(np.lcm.reduce((36, 20, 120)))

print(np.gcd.reduce((36, 20, 120, 100)))
print(np.lcm.reduce((36, 20, 120, 100)))

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Greatest common divisor and Least common multiple ***
   *** using built-in functions ***
12
360
[12 20]
[360 120]
[12 20]
[360 100]
4
360
4
1800
'''