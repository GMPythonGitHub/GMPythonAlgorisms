## gm_graph_distance_bfs.py: Coded by Kinya MIURA, 240207
## graph structure: distance: breadth first serch

# ---------------------------------------------------------
print('*** MS_BFS; mesh structure: distance ***')

# =========================================================
## --- main routine --- ##

from collections import deque

H, W = map(int, input().split())
MS = [['#'] + list(input()) + ['#'] if 1 <= i <= H else list('#'*(W+2)) for i in range(H+2)]
D =[(1,0),(0,1),(-1,0),(0,-1)]
for MSi in MS: print(''.join(Ci))

S = None
for i in range(1,H+1):
    for j in range(1,W+1):
        if MS[i][j] == 's':
            Sx, Sy = i, j
            MS[i][j] = '.'
            break

def BFS(Pox, Poy):
    global MS
    DQ = deque([(Pox,Poy)])
    MS[Pox][Poy] = 0
    while len(DQ) > 0:
        Px, Py = DQ.popleft()
        print(f'{(Px,Py) = }, {DQ = }')
        for Dx, Dy in D:
            Qx, Qy = Px + Dx, Py + Dy
            MSq = MS[Qx][Qy]
            dist = MS[Px][Py] + 1
            if MSq == '.' or (MSq != '#' and MSq > dist):
                MS[Qx][Qy] = dist
                DQ.append((Qx,Qy))
            print(f'{(Qx,Qy) = }, {DQ = }')
    return

BFS(Sx, Sy)
for MSi in MS: print(''.join(map(str,MSi)))

'''[case a]  tree structure
4 4
....
..s.
....
....

'''

'''
# =========================================================
# terminal log / terminal log / terminal log /
*** MS_BFS; mesh structure: distance ***
4 4
....
..s.
....
....
######
#....#
#..s.#
#....#
#....#
######
(Px,Py) = (2, 3), DQ = deque([])
(Qx,Qy) = (3, 3), DQ = deque([(3, 3)])
(Qx,Qy) = (2, 4), DQ = deque([(3, 3), (2, 4)])
(Qx,Qy) = (1, 3), DQ = deque([(3, 3), (2, 4), (1, 3)])
(Qx,Qy) = (2, 2), DQ = deque([(3, 3), (2, 4), (1, 3), (2, 2)])
(Px,Py) = (3, 3), DQ = deque([(2, 4), (1, 3), (2, 2)])
(Qx,Qy) = (4, 3), DQ = deque([(2, 4), (1, 3), (2, 2), (4, 3)])
(Qx,Qy) = (3, 4), DQ = deque([(2, 4), (1, 3), (2, 2), (4, 3), (3, 4)])
(Qx,Qy) = (2, 3), DQ = deque([(2, 4), (1, 3), (2, 2), (4, 3), (3, 4)])
(Qx,Qy) = (3, 2), DQ = deque([(2, 4), (1, 3), (2, 2), (4, 3), (3, 4), (3, 2)])
(Px,Py) = (2, 4), DQ = deque([(1, 3), (2, 2), (4, 3), (3, 4), (3, 2)])
(Qx,Qy) = (3, 4), DQ = deque([(1, 3), (2, 2), (4, 3), (3, 4), (3, 2)])
(Qx,Qy) = (2, 5), DQ = deque([(1, 3), (2, 2), (4, 3), (3, 4), (3, 2)])
(Qx,Qy) = (1, 4), DQ = deque([(1, 3), (2, 2), (4, 3), (3, 4), (3, 2), (1, 4)])
(Qx,Qy) = (2, 3), DQ = deque([(1, 3), (2, 2), (4, 3), (3, 4), (3, 2), (1, 4)])
(Px,Py) = (1, 3), DQ = deque([(2, 2), (4, 3), (3, 4), (3, 2), (1, 4)])
(Qx,Qy) = (2, 3), DQ = deque([(2, 2), (4, 3), (3, 4), (3, 2), (1, 4)])
(Qx,Qy) = (1, 4), DQ = deque([(2, 2), (4, 3), (3, 4), (3, 2), (1, 4)])
(Qx,Qy) = (0, 3), DQ = deque([(2, 2), (4, 3), (3, 4), (3, 2), (1, 4)])
(Qx,Qy) = (1, 2), DQ = deque([(2, 2), (4, 3), (3, 4), (3, 2), (1, 4), (1, 2)])
(Px,Py) = (2, 2), DQ = deque([(4, 3), (3, 4), (3, 2), (1, 4), (1, 2)])
(Qx,Qy) = (3, 2), DQ = deque([(4, 3), (3, 4), (3, 2), (1, 4), (1, 2)])
(Qx,Qy) = (2, 3), DQ = deque([(4, 3), (3, 4), (3, 2), (1, 4), (1, 2)])
(Qx,Qy) = (1, 2), DQ = deque([(4, 3), (3, 4), (3, 2), (1, 4), (1, 2)])
(Qx,Qy) = (2, 1), DQ = deque([(4, 3), (3, 4), (3, 2), (1, 4), (1, 2), (2, 1)])
(Px,Py) = (4, 3), DQ = deque([(3, 4), (3, 2), (1, 4), (1, 2), (2, 1)])
(Qx,Qy) = (5, 3), DQ = deque([(3, 4), (3, 2), (1, 4), (1, 2), (2, 1)])
(Qx,Qy) = (4, 4), DQ = deque([(3, 4), (3, 2), (1, 4), (1, 2), (2, 1), (4, 4)])
(Qx,Qy) = (3, 3), DQ = deque([(3, 4), (3, 2), (1, 4), (1, 2), (2, 1), (4, 4)])
(Qx,Qy) = (4, 2), DQ = deque([(3, 4), (3, 2), (1, 4), (1, 2), (2, 1), (4, 4), (4, 2)])
(Px,Py) = (3, 4), DQ = deque([(3, 2), (1, 4), (1, 2), (2, 1), (4, 4), (4, 2)])
(Qx,Qy) = (4, 4), DQ = deque([(3, 2), (1, 4), (1, 2), (2, 1), (4, 4), (4, 2)])
(Qx,Qy) = (3, 5), DQ = deque([(3, 2), (1, 4), (1, 2), (2, 1), (4, 4), (4, 2)])
(Qx,Qy) = (2, 4), DQ = deque([(3, 2), (1, 4), (1, 2), (2, 1), (4, 4), (4, 2)])
(Qx,Qy) = (3, 3), DQ = deque([(3, 2), (1, 4), (1, 2), (2, 1), (4, 4), (4, 2)])
(Px,Py) = (3, 2), DQ = deque([(1, 4), (1, 2), (2, 1), (4, 4), (4, 2)])
(Qx,Qy) = (4, 2), DQ = deque([(1, 4), (1, 2), (2, 1), (4, 4), (4, 2)])
(Qx,Qy) = (3, 3), DQ = deque([(1, 4), (1, 2), (2, 1), (4, 4), (4, 2)])
(Qx,Qy) = (2, 2), DQ = deque([(1, 4), (1, 2), (2, 1), (4, 4), (4, 2)])
(Qx,Qy) = (3, 1), DQ = deque([(1, 4), (1, 2), (2, 1), (4, 4), (4, 2), (3, 1)])
(Px,Py) = (1, 4), DQ = deque([(1, 2), (2, 1), (4, 4), (4, 2), (3, 1)])
(Qx,Qy) = (2, 4), DQ = deque([(1, 2), (2, 1), (4, 4), (4, 2), (3, 1)])
(Qx,Qy) = (1, 5), DQ = deque([(1, 2), (2, 1), (4, 4), (4, 2), (3, 1)])
(Qx,Qy) = (0, 4), DQ = deque([(1, 2), (2, 1), (4, 4), (4, 2), (3, 1)])
(Qx,Qy) = (1, 3), DQ = deque([(1, 2), (2, 1), (4, 4), (4, 2), (3, 1)])
(Px,Py) = (1, 2), DQ = deque([(2, 1), (4, 4), (4, 2), (3, 1)])
(Qx,Qy) = (2, 2), DQ = deque([(2, 1), (4, 4), (4, 2), (3, 1)])
(Qx,Qy) = (1, 3), DQ = deque([(2, 1), (4, 4), (4, 2), (3, 1)])
(Qx,Qy) = (0, 2), DQ = deque([(2, 1), (4, 4), (4, 2), (3, 1)])
(Qx,Qy) = (1, 1), DQ = deque([(2, 1), (4, 4), (4, 2), (3, 1), (1, 1)])
(Px,Py) = (2, 1), DQ = deque([(4, 4), (4, 2), (3, 1), (1, 1)])
(Qx,Qy) = (3, 1), DQ = deque([(4, 4), (4, 2), (3, 1), (1, 1)])
(Qx,Qy) = (2, 2), DQ = deque([(4, 4), (4, 2), (3, 1), (1, 1)])
(Qx,Qy) = (1, 1), DQ = deque([(4, 4), (4, 2), (3, 1), (1, 1)])
(Qx,Qy) = (2, 0), DQ = deque([(4, 4), (4, 2), (3, 1), (1, 1)])
(Px,Py) = (4, 4), DQ = deque([(4, 2), (3, 1), (1, 1)])
(Qx,Qy) = (5, 4), DQ = deque([(4, 2), (3, 1), (1, 1)])
(Qx,Qy) = (4, 5), DQ = deque([(4, 2), (3, 1), (1, 1)])
(Qx,Qy) = (3, 4), DQ = deque([(4, 2), (3, 1), (1, 1)])
(Qx,Qy) = (4, 3), DQ = deque([(4, 2), (3, 1), (1, 1)])
(Px,Py) = (4, 2), DQ = deque([(3, 1), (1, 1)])
(Qx,Qy) = (5, 2), DQ = deque([(3, 1), (1, 1)])
(Qx,Qy) = (4, 3), DQ = deque([(3, 1), (1, 1)])
(Qx,Qy) = (3, 2), DQ = deque([(3, 1), (1, 1)])
(Qx,Qy) = (4, 1), DQ = deque([(3, 1), (1, 1), (4, 1)])
(Px,Py) = (3, 1), DQ = deque([(1, 1), (4, 1)])
(Qx,Qy) = (4, 1), DQ = deque([(1, 1), (4, 1)])
(Qx,Qy) = (3, 2), DQ = deque([(1, 1), (4, 1)])
(Qx,Qy) = (2, 1), DQ = deque([(1, 1), (4, 1)])
(Qx,Qy) = (3, 0), DQ = deque([(1, 1), (4, 1)])
(Px,Py) = (1, 1), DQ = deque([(4, 1)])
(Qx,Qy) = (2, 1), DQ = deque([(4, 1)])
(Qx,Qy) = (1, 2), DQ = deque([(4, 1)])
(Qx,Qy) = (0, 1), DQ = deque([(4, 1)])
(Qx,Qy) = (1, 0), DQ = deque([(4, 1)])
(Px,Py) = (4, 1), DQ = deque([])
(Qx,Qy) = (5, 1), DQ = deque([])
(Qx,Qy) = (4, 2), DQ = deque([])
(Qx,Qy) = (3, 1), DQ = deque([])
(Qx,Qy) = (4, 0), DQ = deque([])
######
#3212#
#2101#
#3212#
#4323#
######
'''
