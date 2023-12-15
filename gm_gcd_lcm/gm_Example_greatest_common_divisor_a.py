# gm_Example_greatest_common_divisor_a: coded by Kinya MIURA 230415
# -----------------------------------------------------------------------------
print('\n*** ------------ ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
numbera, numberb = 36, 120
number_div = min([numbera, numberb])
for div in reversed(range(1,number_div)):
    if numbera % div == 0 and numberb % div == 0:
        greatest_common_divisor = div
        break
print(f'{numbera = }, {numberb = }')
print(f'{greatest_common_divisor = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** ------------ ***
# -----------------------------------------------------------------------------
numbera = 36, numberb = 120
greatest_common_divisor = 12
'''