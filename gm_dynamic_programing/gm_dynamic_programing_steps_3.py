# gm_dynamic_programing_steps_3.py: coded by Kinya MIURA 240303
## :: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ab

# ---------------------------------------------------------
print('*** dynamic programing: steps_3 ***')

# =========================================================
## --- main routine --- ##
N = 4
# N = 45

DP = [None for _ in range(N+1)]
DP[0] = 1
DP[1] = 1

for ii in range(2, N+1):
    DP[ii] = DP[ii-2] + DP[ii-1]
print(DP[-1])

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** dynamic programing: steps_3 ***
5
'''
