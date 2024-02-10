## gm_graph_distance_bfs.py: Coded by Kinya MIURA, 240207
## graph structure: distance: breadth first serch

from collections import deque

HW = '4 4'
M = ['...s', '....', '....', '.g..']
# -----------------------------

H, W = map(int, HW.split())
C = [['#'] + list(M[i-1]) + ['#'] if 1 <= i <= H else list('#'*(W+2)) for i in range(H+2)]
D =[(1,0),(0,1),(-1,0),(0,-1)]
for Ci in C: print(''.join(Ci))
S, G = None, None
for i in range(1,H+1):
    for j in range(1,W+1):
        if C[i][j] == 's':
            S = (i, j)
            C[i][j] = '.'
        if C[i][j] == 'g':
            G = (i, j)
            C[i][j] = '.'
        if S is not None and G is not None:
            break

def bfs(grido):
    global C
    grids = deque([grido])
    C[grido[0]][grido[1]] = 0
    while len(grids) > 0:
        grido = grids.popleft()
        for Di in D:
            grid = (grido[0] + Di[0], grido[1] + Di[1])
            Cgrid = C[grid[0]][grid[1]]
            dist = C[grido[0]][grido[1]] + 1
            if (Cgrid == '.' or (Cgrid != '#' and Cgrid > dist)):
                C[grid[0]][grid[1]] = dist
                grids.append(grid)
        print(f'{grido = }, {grids = }')
    return

bfs(S)
for Ci in C: print(''.join(map(str,Ci)))
if C[G[0]][G[1]] == '.':
    print('No')
else:
    print('Yes')


'''
######
#...s#
#....#
#....#
#.g..#
######
grido = (1, 4), grids = deque([(2, 4), (1, 3)])
grido = (2, 4), grids = deque([(1, 3), (3, 4), (2, 3)])
grido = (1, 3), grids = deque([(3, 4), (2, 3), (1, 2)])
grido = (3, 4), grids = deque([(2, 3), (1, 2), (4, 4), (3, 3)])
grido = (2, 3), grids = deque([(1, 2), (4, 4), (3, 3), (2, 2)])
grido = (1, 2), grids = deque([(4, 4), (3, 3), (2, 2), (1, 1)])
grido = (4, 4), grids = deque([(3, 3), (2, 2), (1, 1), (4, 3)])
grido = (3, 3), grids = deque([(2, 2), (1, 1), (4, 3), (3, 2)])
grido = (2, 2), grids = deque([(1, 1), (4, 3), (3, 2), (2, 1)])
grido = (1, 1), grids = deque([(4, 3), (3, 2), (2, 1)])
grido = (4, 3), grids = deque([(3, 2), (2, 1), (4, 2)])
grido = (3, 2), grids = deque([(2, 1), (4, 2), (3, 1)])
grido = (2, 1), grids = deque([(4, 2), (3, 1)])
grido = (4, 2), grids = deque([(3, 1), (4, 1)])
grido = (3, 1), grids = deque([(4, 1)])
grido = (4, 1), grids = deque([])
######
#3210#
#4321#
#5432#
#6543#
######
Yes
'''

