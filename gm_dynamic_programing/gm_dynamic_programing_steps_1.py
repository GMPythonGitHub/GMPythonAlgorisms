# gm_dynamic_programing_steps_1.py: coded by Kinya MIURA 240303
## :: https://atcoder.jp/contests/dp/tasks/dp_a
## :: https://atcoder.jp/contests/dp/tasks/dp_b

# ---------------------------------------------------------
print('*** dynamic programing: steps_1 ***')

# =========================================================
## --- main routine --- ##
# N, hh = 4, [10, 30, 40, 20]
N, hh = 6, [30, 10, 60, 10, 60, 50]

DP = [None for _ in range(N)]
DP[0] = 0
DP[1] = abs(hh[1] - hh[0])

for ii in range(2, N):
    DP[ii] = min(DP[ii-2]+abs(hh[ii]-hh[ii-2]), DP[ii-1]+abs(hh[ii]-hh[ii-1]))

print(DP[-1])

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** dynamic programing: steps_1 ***
40
'''
