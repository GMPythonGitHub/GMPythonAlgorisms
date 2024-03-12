# gm_DP_stairs_fw.py: coded by Kinya MIURA 240303
## :: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ab

# ---------------------------------------------------------
print('*** DP; dynamic programing: stairs_forward ***')

# =========================================================
## --- main routine --- ##
N = 4  # number of stairs
# N = 45

DP = [0 for _ in range(N)]

DP[0], DP[1] = 1, 1  # from step 0
for ii in range(0, N-1):
    DP[ii+1] += DP[ii]
    if ii+2 < N:
        DP[ii+2] += DP[ii]

print(f'{DP = }')
print(DP[-1])

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** DP; dynamic programing: stairs_forward ***
DP = [1, 2, 3, 5]
5
'''
