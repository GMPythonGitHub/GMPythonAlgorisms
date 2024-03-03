# gm_recurrence_formula_2.py: coded by Kinya MIURA 240303
## :: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_au
## :: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_av

# ---------------------------------------------------------
print('*** recurrence formula 2: ***')
print('    a(n) = a(n-1) + a(n-2), a(1) = 1, a(2) = 1')
print('*** Fibonacci series ***')

# =========================================================

numbers = 10

aa1, aa2 = 1, 1
print(f'a(1) = {aa2}')
print(f'a(2) = {aa1}')

for ii in range(3, numbers+1):
	aao = aa1 + aa2
	print(f'a({ii}) = {aao}')
	aa1, aa2 = aao, aa1

# =============================================================
# terminal log / terminal log / terminal log /
'''
*** recurrence formula 2: ***
    a(n) = a(n-1) + a(n-2), a(1) = 1, a(2) = 1
*** Fibonacci series ***
a(1) = 1
a(2) = 1
a(3) = 2
a(4) = 3
a(5) = 5
a(6) = 8
a(7) = 13
a(8) = 21
a(9) = 34
a(10) = 55
'''