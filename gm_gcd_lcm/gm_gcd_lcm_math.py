# gm_gcd_lcm_math.py: coded by Kinya MIURA 230415
# ---------------------------------------------------------
print('*** Greatest common divisor and Least common multiple ***')
print('   *** using math function ***')
# ---------------------------------------------------------
import math

# =========================================================
## --- main routine --- ##

print(math.gcd(36, 120))
print(math.lcm(36, 120))

'''
print(math.gcd([36, 20], 120))
print(math.lcm([36, 20], 120))

print(math.gcd([36, 20], [120, 100]))
print(math.lcm([36, 20], [120, 100]))

print(math.gcd.reduce((36, 20, 120)))
print(math.lcm.reduce((36, 20, 120)))

print(math.gcd.reduce((36, 20, 120, 100)))
print(math.lcm.reduce((36, 20, 120, 100)))
'''
# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Greatest common divisor and Least common multiple ***
   *** using math functions ***
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