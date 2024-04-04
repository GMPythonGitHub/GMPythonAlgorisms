## gm_GS_distance_DFS.py: Coded by Kinya MIURA, 240207
## graph structure: distance: depth first serch

# ---------------------------------------------------------
print('*** GS_DFS; graph structure: distance ***')

# =========================================================
## --- main routine --- ##

import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())

links = [[] for _ in range(N)]
for _ in range(M):
    uu, vv = map(lambda x: int(x)-1, input().split())
    links[uu].append(vv)
    links[vv].append(uu)
print(f'{links = }')

S = 8 - 1

def DFSrc(nodeo):
    global visited, distance
    for node in links[nodeo]:
        dist = distance[nodeo] + 1
        if not visited[node] or distance[node] > dist :
            visited[node] = True
            distance[node] = dist
            DFSrc(node)
    print(f'{nodeo = }, {visited = }, {distance = }')
    return

def DFS(nodeo):
    global visited, distance
    visited = [False for _ in range(N)]
    distance = [0 for _ in range(N)]
    visited[nodeo] = True
    DFSrc(nodeo)
    return

visited, distance = [], []
DFS(S)
print(f'{visited = }')
print(f'{distance = }')

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
links = [[1, 2], [0, 3, 4], [0, 5], [1, 6], [1], [2, 7, 8], [3, 8], [5], [5, 6]]
nodeo = 8, visited = [True, True, True, True, False, True, True, True, True], distance = [3, 4, 2, 5, 0, 1, 6, 0, 7]
nodeo = 6, visited = [True, True, True, True, False, True, True, True, True], distance = [3, 4, 2, 5, 0, 1, 6, 0, 7]
nodeo = 3, visited = [True, True, True, True, False, True, True, True, True], distance = [3, 4, 2, 5, 0, 1, 6, 0, 7]
nodeo = 4, visited = [True, True, True, True, True, True, True, True, True], distance = [3, 4, 2, 5, 5, 1, 6, 0, 7]
nodeo = 1, visited = [True, True, True, True, True, True, True, True, True], distance = [3, 4, 2, 5, 5, 1, 6, 0, 7]
nodeo = 0, visited = [True, True, True, True, True, True, True, True, True], distance = [3, 4, 2, 5, 5, 1, 6, 0, 7]
nodeo = 2, visited = [True, True, True, True, True, True, True, True, True], distance = [3, 4, 2, 5, 5, 1, 6, 0, 7]
nodeo = 3, visited = [True, True, True, True, True, True, True, True, True], distance = [3, 4, 2, 4, 5, 1, 3, 0, 2]
nodeo = 6, visited = [True, True, True, True, True, True, True, True, True], distance = [3, 4, 2, 4, 5, 1, 3, 0, 2]
nodeo = 8, visited = [True, True, True, True, True, True, True, True, True], distance = [3, 4, 2, 4, 5, 1, 3, 0, 2]
nodeo = 5, visited = [True, True, True, True, True, True, True, True, True], distance = [3, 4, 2, 4, 5, 1, 3, 0, 2]
nodeo = 7, visited = [True, True, True, True, True, True, True, True, True], distance = [3, 4, 2, 4, 5, 1, 3, 0, 2]
visited = [True, True, True, True, True, True, True, True, True]
distance = [3, 4, 2, 4, 5, 1, 3, 0, 2]


'''
