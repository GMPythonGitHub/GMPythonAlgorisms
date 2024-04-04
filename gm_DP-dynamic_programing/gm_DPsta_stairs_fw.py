# gm_DP_stairs_fw.py: coded by Kinya MIURA 240303
## :: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ab

# ---------------------------------------------------------
print('*** DP; dynamic programing: stairs_forward ***')

# =========================================================
## --- main routine --- ##
N = int(input())

DP = [0 for _ in range(N)]

DP[0], DP[1] = 1, 1  # from step 0
for ii in range(0, N-1):
    DP[ii+1] += DP[ii]
    if ii+2 < N:
        DP[ii+2] += DP[ii]

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
*** DP; dynamic programing: stairs_forward ***
5
DP = [1, 2, 3, 5, 8]
8

'''
