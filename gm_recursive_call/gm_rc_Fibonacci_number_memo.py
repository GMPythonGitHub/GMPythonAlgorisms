# gm_rc_Fibonacci_number_memo.py: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Recursive call: Fibonacci numbers with memory ***')

# =========================================================
## --- defining function --- ##
def rc_fibonacci_memo(nn) -> int:
    if nn < 0:
        return None
    elif fibonaccis[nn] is not None:
        return fibonaccis[nn]
    else:
        print(f'called: {nn = }  ', end='')
        fibonaccis[nn] = rc_fibonacci_memo(nn-1) + rc_fibonacci_memo(nn-2)
        if nn == 2: print()
        return fibonaccis[nn]

## --- main routine --- ##
nn = 6; print(f'{nn = }')
fibonaccis = [None if ii > 1 else ii for ii in range(nn+1)]
print(f'{rc_fibonacci_memo(nn) = }')
print()
for i in range(nn+1):
    print(f'{i = :02d}, {rc_fibonacci_memo(i) = }')

# =============================================================
# terminal log / terminal log / terminal log /
'''
*** Recursive call: Fibonacci numbers ***
nn = 6
called: nn = 6  called: nn = 5  called: nn = 4  called: nn = 3  called: nn = 2  
called: nn = 2  
called: nn = 3  called: nn = 2  
called: nn = 4  called: nn = 3  called: nn = 2  
called: nn = 2  
rc_fibonacci(nn) = 8

i = 00, rc_fibonacci(i) = 0
i = 01, rc_fibonacci(i) = 1
called: nn = 2  
i = 02, rc_fibonacci(i) = 1
called: nn = 3  called: nn = 2  
i = 03, rc_fibonacci(i) = 2
called: nn = 4  called: nn = 3  called: nn = 2  
called: nn = 2  
i = 04, rc_fibonacci(i) = 3
called: nn = 5  called: nn = 4  called: nn = 3  called: nn = 2  
called: nn = 2  
called: nn = 3  called: nn = 2  
i = 05, rc_fibonacci(i) = 5
called: nn = 6  called: nn = 5  called: nn = 4  called: nn = 3  called: nn = 2  
called: nn = 2  
called: nn = 3  called: nn = 2  
called: nn = 4  called: nn = 3  called: nn = 2  
called: nn = 2  
i = 06, rc_fibonacci(i) = 8
'''