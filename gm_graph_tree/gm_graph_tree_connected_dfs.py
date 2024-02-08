## gm_graph_tree_connected_dfs.py: Coded by Kinya MIURA, 240207
## graff tee structure: connected: depth first serch

import sys
sys.setrecursionlimit(1000000)

NM = '9 8'
S = int('0')
L = ['1 2', '1 3', '2 4', '2 5', '3 6', '4 7', '6 8', '6 9']
# -----------------------------

N, M = map(int, NM.split())

links = [[] for _ in range(N)]
for Li in L:
    uu, vv = map(lambda x: int(x)-1, Li.split())
    links[uu].append(vv)
    links[vv].append(uu)
print(f'{links = }')

def dfsrc(nodeo, visited):
    for node in links[nodeo]:
        if not visited[node]:
            visited[node] = True
            dfsrc(node, visited)
    print(f'{nodeo = }, {visited = }')
    return

def dfs(nodeo):
    visited = [False for _ in range(N)]
    visited[nodeo] = True
    dfsrc(nodeo, visited)
    return visited

visited = dfs(S)
print(f'{visited = }')
if False not in visited:
    print('connected')
else:
    print('not connected')

