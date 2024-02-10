## gm_graph_connected_bfs.py: Coded by Kinya MIURA, 240207
## graph structure: connected: breadth first serch

from collections import deque

NM = '9 8'
S = '0'
L = ['1 2', '1 3', '2 4', '2 5', '3 6', '4 7', '6 8', '6 9']
# -----------------------------

N, M = map(int, NM.split())

links = [[] for _ in range(N)]
for Li in L:
    uu, vv = map(lambda x: int(x)-1, Li.split())
    links[uu].append(vv)
    links[vv].append(uu)
print(f'{links = }')
S = int(S) - 1

def bfs(nodeo):
    global visited
    visited = [False for _ in range(N)]
    visited[nodeo] = True
    nodes = deque([nodeo])
    while len(nodes) > 0:
        nodeo = nodes.popleft()
        for node in links[nodeo]:
            if not visited[node]:
                visited[node] = True
                nodes.append(node)
        print(f'{nodeo = }, {nodes = }, {visited = }')
    return

visited = []
bfs(S)
print(f'{visited = }')
if False not in visited:
    print('connected')
else:
    print('not connected')

