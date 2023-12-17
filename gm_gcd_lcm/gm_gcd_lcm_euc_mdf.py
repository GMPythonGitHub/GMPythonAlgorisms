# gm_gcd_lcm_euc_mdf: coded by Kinya MIURA 230415
# ---------------------------------------------------------
print('*** Greatest common divisor and Least common multiple ***')
print("   *** Euclid's algorithm modified ***")

# =========================================================
## --- main routine --- ##
numbera, numberb = 36, 120
print(f'{numbera = }, {numberb = }')
# greatest common divisor
numa, numb = numbera, numberb
gcd = lcm = 1
while True:
    if numa > numb:
        numa %= numb
        if numa == 0:
            gcd = numb
            break
    elif numb > numa:
        numb %= numa
        if numa == 0:
            greatest_common_dvisor = numa
            break
print(f'{gcd = }')
# least common multiple
lcm = numbera * numberb // gcd
print(f'{lcm = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** ------------ ***
# -----------------------------------------------------------------------------
numbera = 36, numberb = 120
gcd = 12
lcm = 360
'''