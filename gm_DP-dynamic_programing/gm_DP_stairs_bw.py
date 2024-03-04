# gm_DP_stairs_bw.py: coded by Kinya MIURA 240303
## :: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ab

# ---------------------------------------------------------
print('*** DP; dynamic programing: stairs_backward ***')

# =========================================================
## --- main routine --- ##
N = 4  # number of stairs
# N = 45

DP = [0 for _ in range(N+1)]

DP[0] = 1
DP[1] = DP[0]
for ii in range(2, N+1):
    DP[ii] = DP[ii-2] + DP[ii-1]

print(f'{DP = }')
print(DP[-1])

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** DP; dynamic programing: stairs_backward ***
DP = [1, 1, 2, 3, 5]
5
'''
