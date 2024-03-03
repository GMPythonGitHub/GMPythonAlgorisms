# gm_recurrence_formula_2_dp.py: coded by Kinya MIURA 240303
## :: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_au
## :: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_av

# ---------------------------------------------------------
print('*** recurrence formula 2: ***')
print('    a(n) = a(n-1) + a(n-2), a(1) = 1, a(2) = 1')
print('*** Fibonacci series ***')

# =========================================================

numbers = 10
aa = [None for _ in range(numbers)]
aa[0], aa[1] = 1, 1

for ii in range(2, numbers):
	aa[ii] = aa[ii-1] + aa[ii-2]
print(f'{aa = }')

# =============================================================
# terminal log / terminal log / terminal log /
'''
*** recurrence formula 2: ***
    a(n) = a(n-1) + a(n-2), a(1) = 1, a(2) = 1
*** Fibonacci series ***
aa = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
'''