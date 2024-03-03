# gm_recurrence_formula_1_dp.py: coded by Kinya MIURA 240303
## :: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_au
## :: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_av

# ---------------------------------------------------------
print('*** recurrence formula 1: dynamic programing ***')
print('    a(n) = a(n-1) + 2, a(1) = 1')

# =========================================================

numbers = 10
aa = [None for _ in range(numbers)]
aa[0] = 1

for ii in range(1, numbers):
	aa[ii] = aa[ii-1] + 2
print(f'{aa = }')

# =============================================================
# terminal log / terminal log / terminal log /
'''
*** recurrence formula 1: dynamic programing ***
    a(n) = a(n-1) + 2, a(1) = 1
aa = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

'''