# gm_Example_greatest_common_divisor_a: coded by Kinya MIURA 230415
# -----------------------------------------------------------------------------
print('\n*** ------------ ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
numbera, numberb = 36, 120
number_mul = numbera * numberb
for mul in range(1,number_mul):
    if mul % numbera == 0 and mul % numberb == 0:
        least_common_multiple = mul
        break
print(f'{numbera = }, {numberb = }')
print(f'{least_common_multiple = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** ------------ ***
# -----------------------------------------------------------------------------
numbera = 36, numberb = 120
least_common_multiple = 360
'''