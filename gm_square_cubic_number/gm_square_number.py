# gm_square_number: coded by Kinya MIURA 240303
# ---------------------------------------------------------
print('*** square number: judging sequential numbers ***')

# =========================================================
## --- main routine --- ##
number = 400
squares = []  # 'list' of square numbers
for num in range(1, number+1):
    nn = round(num ** (1/2))
    if num == nn ** 2:
        squares.append(num)
print(f'{number = }')
print(f'{squares = }')
print(f'{len(squares) = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** square number: judging sequential numbers ***
number = 400
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
len(squares) = 20
'''