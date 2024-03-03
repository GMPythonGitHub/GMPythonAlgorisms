# gm_recurrence_formula_3.py: coded by Kinya MIURA 240303
## :: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_au
## :: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_av

# ---------------------------------------------------------
print('*** recurrence formula 3: ***')
print('    a(n) = a(n-1) + a(n-2) + a(n-3), a(1) = 1, a(2) = 1, a(3) = 1')

# =========================================================

numbers = 10
aa1, aa2, aa3 = 1, 1, 1
print(f'a(1) = {aa3}')
print(f'a(2) = {aa2}')
print(f'a(3) = {aa1}')

for ii in range(4, numbers+1):
	aao = aa1 + aa2 + aa3
	print(f'a({ii}) = {aao}')
	aa1, aa2, aa3 = aao, aa1, aa2

# =============================================================
# terminal log / terminal log / terminal log /
'''
*** recurrence formula 3: ***
    a(n) = a(n-1) + a(n-2) + a(n-3), a(1) = 1, a(2) = 1, a(3) = 1
a(1) = 1
a(2) = 1
a(3) = 1
a(4) = 3
a(5) = 5
a(6) = 9
a(7) = 17
a(8) = 31
a(9) = 57
a(10) = 105
'''