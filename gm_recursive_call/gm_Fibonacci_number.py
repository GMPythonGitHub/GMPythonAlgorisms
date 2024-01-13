# gm_Fibonacci_number.py: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Fibonacci numbers ***')

# =========================================================
## --- defining function --- ##
def fibonacci(nn):
    if nn <= 1:
        return nn
    else:
        ii = 2
        aa, bb = 0, 1
        while ii <= nn:
            aa, bb = bb, aa + bb
            ii += 1
        return bb

## --- main routine --- ##
nn = 10; print(f'{nn = }')
print(f'{nn = }: fibonacci number: {fibonacci(nn)}')
print()
for ii in range(10+1):
    print(f'{ii = }, {fibonacci(ii) = }')

# =============================================================
# terminal log / terminal log / terminal log /
'''
*** Fibonacci numbers ***
nn = 10
nn = 10: fibonacci number: 55

ii = 0, fibonacci(ii) = 0
ii = 1, fibonacci(ii) = 1
ii = 2, fibonacci(ii) = 1
ii = 3, fibonacci(ii) = 2
ii = 4, fibonacci(ii) = 3
ii = 5, fibonacci(ii) = 5
ii = 6, fibonacci(ii) = 8
ii = 7, fibonacci(ii) = 13
ii = 8, fibonacci(ii) = 21
ii = 9, fibonacci(ii) = 34
ii = 10, fibonacci(ii) = 55
'''