## gm_GS_connected_DFS.py: Coded by Kinya MIURA, 240207
## graph structure: connected: depth first serch

# ---------------------------------------------------------
print('*** GS_DFS; graph structure: connected ***')

# =========================================================
## --- main routine --- ##

import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
S, = map(lambda x: int(x)-1, input().split())

links = [[] for _ in range(N)]
for _ in range(M):
    uu, vv = map(lambda x: int(x)-1, input().split())
    links[uu].append(vv)
    links[vv].append(uu)
print(f'{links = }')

def DFSrc(nodeo):
    global visited
    for node in links[nodeo]:
        if not visited[node]:
            visited[node] = True
            DFSrc(node)
    print(f'{nodeo = }, {visited = }')
    return

def DFS(nodeo):
    global visited
    visited = [False for _ in range(N)]
    visited[nodeo] = True
    DFSrc(nodeo)
    return

visited = []
DFS(S)
print(f'{visited = }')
if False not in visited:
    print('connected')
else:
    print('not connected')


'''
[case a]  tree structure
9 8
1
1 2
1 3
2 4
2 5
3 6
4 7
6 8
6 9

[case b]  looped route
9 9
1
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
*** GS_DFS; graph structure: connected ***
9 8
1
1 2
1 3
2 4
2 5
3 6
4 7
6 8
6 9
links = [[1, 2], [0, 3, 4], [0, 5], [1, 6], [1], [2, 7, 8], [3], [5], [5]]
nodeo = 6, visited = [True, True, False, True, False, False, True, False, False]
nodeo = 3, visited = [True, True, False, True, False, False, True, False, False]
nodeo = 4, visited = [True, True, False, True, True, False, True, False, False]
nodeo = 1, visited = [True, True, False, True, True, False, True, False, False]
nodeo = 7, visited = [True, True, True, True, True, True, True, True, False]
nodeo = 8, visited = [True, True, True, True, True, True, True, True, True]
nodeo = 5, visited = [True, True, True, True, True, True, True, True, True]
nodeo = 2, visited = [True, True, True, True, True, True, True, True, True]
nodeo = 0, visited = [True, True, True, True, True, True, True, True, True]
visited = [True, True, True, True, True, True, True, True, True]
connected

'''

