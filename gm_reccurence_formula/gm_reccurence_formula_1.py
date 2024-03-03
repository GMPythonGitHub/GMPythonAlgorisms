# gm_recurrence_formula_1.py: coded by Kinya MIURA 240303
## :: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_au
## :: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_av

# ---------------------------------------------------------
print('*** recurrence formula 1: ***')
print('    a(n) = a(n-1) + 2, a(1) = 1')

# =========================================================

numbers = 10
aa1 = 1
print(f'a(1) = {aa1}')

for ii in range(2, numbers+1):
	aao = aa1 + 2
	print(f'a({ii}) = {aao}')
	aa1 = aao

# =============================================================
# terminal log / terminal log / terminal log /
'''
*** recurrence formula 1: ***
    a(n) = a(n-1) + 2, a(1) = 1
a(1) = 1
a(2) = 3
a(3) = 5
a(4) = 7
a(5) = 9
a(6) = 11
a(7) = 13
a(8) = 15
a(9) = 17
a(10) = 19
'''