## gm_GS_distance_WFM.py: Coded by Kinya MIURA, 240207
## graph structure: distance: depth first serch

# ---------------------------------------------------------
print('*** GS_WFM; graph structure: distance ***')

# =========================================================
## --- main routine --- ##

import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
inf = float('inf')

S = 8 - 1
dists = [[inf for _ in range(N)] for _ in range(N)]
for _ in range(M):
    uu, vv = map(lambda x: int(x)-1, input().split())
    dists[uu][vv] = 1
    dists[vv][uu] = 1
for dist in dists: print(f'{dist = }')

for kk in range(N):
    for ii in range(N):
        for jj in range(N):
            dists[ii][jj] = min(dists[ii][jj], dists[ii][kk]+dists[kk][jj])
for dist in dists: print(f'{dist = }')

'''
[case a]  tree structure
9 9
1 2
1 3
2 4
2 5
3 6
4 7
6 8
6 9
7 9

'''

'''
# =========================================================
# terminal log / terminal log / terminal log /
*** GS_DFS; graph structure: distance ***


'''

