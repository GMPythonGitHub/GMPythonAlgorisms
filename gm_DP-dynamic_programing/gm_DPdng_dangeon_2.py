# gm_DP_dangeon_2.py: coded by Kinya MIURA 240303
## :: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_q

# ---------------------------------------------------------
print('*** DP; dynamic programing: dangeons_2 shortest route ***')

# =========================================================
## --- main routine --- ##

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

DP = [None for i in range(N)]  # time consumption
DJ = [None for _ in range(N)]  # previous dangeon increment
DP[0] = 0; DJ[0] = 0
DP[1] = DP[0] + A[0]; DJ[1] = 1
for ii in range(2, N):
    if DP[ii-1] + A[ii-1] <= DP[ii-2] + B[ii-2]:
        DP[ii] = DP[ii-1] + A[ii-1]; DJ[ii] = 1
    else:
        DP[ii] = DP[ii-2] + B[ii-2]; DJ[ii] = 2
print(f'{DP = }')
print(f'{DJ = }')
print(DP[-1])

P = [N-1]
while P[-1] > 0:
    P.append(P[-1]-DJ[P[-1]])
print(len(P))
print(*reversed(P))

'''
[case a]  dangeon consumption time
5
2 4 1 3
5 3 3

[case b]  dangeon consumption time
10
1 19 75 37 17 16 33 18 22
41 28 89 74 98 43 42 31

'''

# =========================================================
# terminal log / terminal log / terminal log /
'''
5
2 4 1 3
5 3 3
DP = [0, 2, 5, 5, 8]
DJ = [0, 1, 2, 2, 1]
8
4
0 1 3 4
'''

