## gm_graph_connected_dfs.py: Coded by Kinya MIURA, 240207
## graph structure: connected: depth first serch

import sys
sys.setrecursionlimit(1000000)

NM = '9 8'
S = '1'
L = ['1 2', '1 3', '2 4', '2 5', '3 6', '4 7', '6 8', '6 9']
# -----------------------------

N, M = map(int, NM.split())
S = int(S) - 1

links = [[] for _ in range(N)]
for Li in L:
    uu, vv = map(lambda x: int(x)-1, Li.split())
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

