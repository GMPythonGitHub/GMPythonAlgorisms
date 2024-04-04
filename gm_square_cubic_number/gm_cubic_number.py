# gm_cubic_number: coded by Kinya MIURA 240303
# ---------------------------------------------------------
print('*** qubic number: judging sequential numbers ***')

# =========================================================
## --- main routine --- ##
number = 8000

cubics = []  # 'list' of square numbers
for num in range(1, number+1):
    nn = round(num ** (1/3))
    if num == nn ** 3:
        cubics.append(num)
print(f'{number = }')
print(f'{cubics = }')
print(f'{len(cubics) = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** qubic number: judging sequential numbers ***
number = 8000
cubics = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859, 8000]
len(cubics) = 20
'''