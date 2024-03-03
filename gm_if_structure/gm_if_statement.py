# gm_if_statement.py: coded by Kinya MIURA 240302
## :: https://atcoder.jp/contests/abc219/tasks/abc219_a

# ---------------------------------------------------------
print('*** if statement: if-elif-else ***')

# =========================================================
## --- main routine --- ##
X = 65

if X >= 90: print('Expert')
elif X >= 70: print('Advanced', 90-X)
elif X >= 40: print('Intermediate', 70-X)
else: print('Novice', 40-X)

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** if statement: if-elif-else ***
Intermediate 5
'''
