# gm_DP_dangeon_1.py: coded by Kinya MIURA 240303
## :: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_p

# ---------------------------------------------------------
print('*** DP; dynamic programing: dangeons_1 shortest route ***')

# =========================================================
## --- main routine --- ##
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

DP = [None for i in range(N)]
DP[0] = 0
DP[1] = DP[0] + A[0]
for ii in range(2, N):
    DP[ii] = min(DP[ii-1] + A[ii-1], DP[ii-2] + B[ii-2])

print(f'{DP = }')
print(DP[-1])

'''
[case a]  dangeon consumption time
5
2 4 1 3
5 3 7

[case b]  dangeon consumption time
10
1 19 75 37 17 16 33 18 22
41 28 89 74 98 43 42 31

'''

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** DP; dynamic programing: dangeons_1 shortest route ***
5
2 4 1 3
5 3 7
DP = [0, 2, 5, 5, 8]
8
'''
