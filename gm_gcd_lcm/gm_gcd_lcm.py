# gm_Example_gcm_lcm: coded by Kinya MIURA 230415
# ---------------------------------------------------------
print('*** Greatest common divisor and Least common multiple ***')

# =========================================================
## --- main routine --- ##
numbera, numberb = 36, 120
print(f'{numbera = }, {numberb = }')
# greatest common divisor
num_min = min([numbera, numberb])
for div in reversed(range(1,num_min)):
    if numbera % div == 0 and numberb % div == 0:
        gcd = div
        break
print(f'{gcd = }')
print()
# least common multiple
num_max = max(numbera, numberb)
for mul in range(num_max, numbera*numberb):
    if mul % numbera == 0 and mul % numberb == 0:
        lcm = mul
        break
print(f'{lcm = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Greatest common divisor and Least common multiple ***
numbera = 36, numberb = 120
gcd = 12
lcm = 360
'''