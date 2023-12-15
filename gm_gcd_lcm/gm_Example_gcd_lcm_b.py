# gm_Example_greatest_common_divisor_b: coded by Kinya MIURA 230415
# -----------------------------------------------------------------------------
print('\n*** ------------ ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
aa, bb = numbera, numberb = 36, 120
while bb:
    aa, bb = bb, aa % bb
greatest_common_divisor = aa

print(f'{numbera = }, {numberb = }')
print(f'{greatest_common_divisor = }')
print('# ------------')

least_common_multiple = (numbera * numberb) // greatest_common_divisor
print(f'{numbera = }, {numberb = }')
print(f'{least_common_multiple = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** ------------ ***
# -----------------------------------------------------------------------------
numbera = 36, numberb = 120
greatest_common_divisor = 12
# ------------
numbera = 36, numberb = 120
least_common_multiple = 360
'''