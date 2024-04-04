## gm_GS_distance_weighted_DFM.py: Coded by Kinya MIURA, 240207
## graph structure: weighted distance: depth first serch

import sys
sys.setrecursionlimit(1000000)

NM = '9 8'
S = '1'
L = ['1 2 10', '1 3 20', '2 4 30', '2 5 40', '3 6 20', '4 7 30', '6 8 40', '6 9 10']
# -----------------------------

N, M = map(int, NM.split())
S = int(S) - 1
inf = float('inf')

dists = [[inf for _ in range(N)] for _ in range(N)]
for Li in L:
    uu, vv, ww = map(int, Li.split())
    uu, vv = uu - 1, vv - 1
    dists[uu][vv] = ww
    dists[vv][uu] = ww
for dist in dists: print(f'{dist = }')

for kk in range(N):
    for ii in range(N):
        for jj in range(N):
            dists[ii][jj] = min(dists[ii][jj], dists[ii][kk]+dists[kk][jj])
for dist in dists: print(f'{dist = }')


'''
links = [[(1, 10), (2, 20)], [(0, 10), (3, 30), (4, 40)], [(0, 20), (5, 20)], [(1, 30), (6, 30)], [(1, 40)], [(2, 20), (7, 40), (8, 10)], [(3, 30)], [(5, 40)], [(5, 10)]]
nodeo = 6, visited = [True, True, False, True, False, False, True, False, False], distance = [0, 10, 0, 40, 0, 0, 70, 0, 0]
nodeo = 3, visited = [True, True, False, True, False, False, True, False, False], distance = [0, 10, 0, 40, 0, 0, 70, 0, 0]
nodeo = 4, visited = [True, True, False, True, True, False, True, False, False], distance = [0, 10, 0, 40, 50, 0, 70, 0, 0]
nodeo = 1, visited = [True, True, False, True, True, False, True, False, False], distance = [0, 10, 0, 40, 50, 0, 70, 0, 0]
nodeo = 7, visited = [True, True, True, True, True, True, True, True, False], distance = [0, 10, 20, 40, 50, 40, 70, 80, 0]
nodeo = 8, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 10, 20, 40, 50, 40, 70, 80, 50]
nodeo = 5, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 10, 20, 40, 50, 40, 70, 80, 50]
nodeo = 2, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 10, 20, 40, 50, 40, 70, 80, 50]
nodeo = 0, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 10, 20, 40, 50, 40, 70, 80, 50]
visited = [True, True, True, True, True, True, True, True, True]
distance = [0, 10, 20, 40, 50, 40, 70, 80, 50]
'''

