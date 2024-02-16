## gm_graph_distance_wfm.py: Coded by Kinya MIURA, 240207
## graph structure: distance: depth first serch

import sys
sys.setrecursionlimit(1000000)

NM = '9 9'
S = '8'
L = ['1 2', '1 3', '2 4', '2 5', '3 6', '4 7', '6 8', '6 9', '7 9']
# -----------------------------

N, M = map(int, NM.split())
S = int(S) - 1
inf = float('inf')

dists = [[inf for _ in range(N)] for _ in range(N)]
for Li in L:
    uu, vv = map(lambda x: int(x)-1, Li.split())
    dists[uu][vv] = 1
    dists[vv][uu] = 1
for dist in dists: print(f'{dist = }')

for kk in range(N):
    for ii in range(N):
        for jj in range(N):
            dists[ii][jj] = min(dists[ii][jj], dists[ii][kk]+dists[kk][jj])
for dist in dists: print(f'{dist = }')


'''
links = [[1, 2], [0, 3, 4], [0, 5], [1, 6], [1], [2, 7, 8], [3, 8], [5], [5, 6]]
nodeo = 2, visited = [True, True, True, True, False, True, True, False, True], distance = [0, 1, 6, 2, 0, 5, 3, 0, 4]
nodeo = 7, visited = [True, True, True, True, False, True, True, True, True], distance = [0, 1, 6, 2, 0, 5, 3, 6, 4]
nodeo = 5, visited = [True, True, True, True, False, True, True, True, True], distance = [0, 1, 6, 2, 0, 5, 3, 6, 4]
nodeo = 8, visited = [True, True, True, True, False, True, True, True, True], distance = [0, 1, 6, 2, 0, 5, 3, 6, 4]
nodeo = 6, visited = [True, True, True, True, False, True, True, True, True], distance = [0, 1, 6, 2, 0, 5, 3, 6, 4]
nodeo = 3, visited = [True, True, True, True, False, True, True, True, True], distance = [0, 1, 6, 2, 0, 5, 3, 6, 4]
nodeo = 4, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 1, 6, 2, 2, 5, 3, 6, 4]
nodeo = 1, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 1, 6, 2, 2, 5, 3, 6, 4]
nodeo = 7, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 1, 1, 2, 2, 2, 3, 3, 4]
nodeo = 8, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
nodeo = 5, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
nodeo = 2, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
nodeo = 0, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
visited = [True, True, True, True, True, True, True, True, True]
distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
'''

