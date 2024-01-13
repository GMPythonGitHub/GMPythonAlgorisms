# gm_Fibonacci_number_memo.py: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Fibonacci numbers with memo ***')

# =========================================================
## --- main routine --- ##
nn = 10; print(f'{nn = }')
fibonaccis = [ii if ii <= 1 else None for ii in range(nn+1)]
for ii in range(2, nn+1):
    fibonaccis[ii] = fibonaccis[ii-2] + fibonaccis[ii-1]
print(f'{nn = }: fibonacci number: {fibonaccis[nn]}')
print()
for i in range(10+1):
    print(f'{i = }, {fibonaccis[i] = }')

# =============================================================
# terminal log / terminal log / terminal log /
'''
*** Fibonacci numbers with memo ***
nn = 10
nn = 10: fibonacci number: 55

i = 0, fibonaccis[i] = 0
i = 1, fibonaccis[i] = 1
i = 2, fibonaccis[i] = 1
i = 3, fibonaccis[i] = 2
i = 4, fibonaccis[i] = 3
i = 5, fibonaccis[i] = 5
i = 6, fibonaccis[i] = 8
i = 7, fibonaccis[i] = 13
i = 8, fibonaccis[i] = 21
i = 9, fibonaccis[i] = 34
i = 10, fibonaccis[i] = 55
'''