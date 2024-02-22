## gm_graph_connected_dfs.py: Coded by Kinya MIURA, 240207
## graph structure: connected: depth first serch

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

def dfsrc(nodeo):
    global visited
    for node in links[nodeo]:
        if not visited[node]:
            visited[node] = True
            dfsrc(node)
    print(f'{nodeo = }, {visited = }')
    return

def dfs(nodeo):
    global visited
    visited = [False for _ in range(N)]
    visited[nodeo] = True
    dfsrc(nodeo)
    return

visited = []
dfs(S)
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



