# gm_DP_stairs_bw.py: coded by Kinya MIURA 240303
## :: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ab

# ---------------------------------------------------------
print('*** DP; dynamic programing: stairs_backward ***')

# =========================================================
## --- main routine --- ##
N = int(input())

DP = [0 for _ in range(N+1)]

DP[0] = 1
DP[1] = DP[0]
for ii in range(2, N+1):
    DP[ii] = DP[ii-2] + DP[ii-1]

print(f'{DP = }')
print(DP[-1])

'''
[case a]  stairs
5

[case b]  dangeon consumption time
45

'''

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** DP; dynamic programing: stairs_backward ***
5
DP = [1, 1, 2, 3, 5, 8]
8

'''
