# gm_dynamic_programing_steps_2.py: coded by Kinya MIURA 240303
## :: https://atcoder.jp/contests/dp/tasks/dp_a
## :: https://atcoder.jp/contests/dp/tasks/dp_b

# ---------------------------------------------------------
print('*** dynamic programing: steps_2 ***')

# =========================================================
## --- main routine --- ##
N, K, hh = 5, 3, [10, 30, 40, 50, 20]
# N, K, hh = 10, 4, [40, 10, 20, 70, 80, 10, 20, 70, 80, 60]

DP = [None for _ in range(N)]
DP[0] = 0

for ii in range(1, N):
    iio = max(0, ii-K)
    DPmin = []
    for jj in range(iio,ii):
        DPmin.append(DP[jj] + abs(hh[ii] - hh[jj]))
    DP[ii] = min(DPmin)

print(DP[-1])

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** dynamic programing: steps_2 ***
30
'''
