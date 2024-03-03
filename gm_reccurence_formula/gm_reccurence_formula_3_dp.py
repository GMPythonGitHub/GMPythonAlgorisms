# gm_recurrence_formula_3_dp.py: coded by Kinya MIURA 240303
## :: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_au
## :: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_av

# ---------------------------------------------------------
print('*** recurrence formula 3: ***')
print('    a(n) = a(n-1) + a(n-2) + a(n-3), a(1) = 1, a(2) = 1, a(3) = 1')

# =========================================================

numbers = 10
aa = [None for _ in range(numbers)]
aa[0], aa[1], aa[2] = 1, 1, 1

for ii in range(3, numbers):
	aa[ii] = aa[ii-1] + aa[ii-2] + aa[ii-3]
print(f'{aa = }')

# =============================================================
# terminal log / terminal log / terminal log /
'''
*** recurrence formula 3: ***
    a(n) = a(n-1) + a(n-2) + a(n-3), a(1) = 1, a(2) = 1, a(3) = 1
aa = [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
'''