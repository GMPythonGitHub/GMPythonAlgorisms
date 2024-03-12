## gm_graph_connected_bfs.py: Coded by Kinya MIURA, 240207
## graph structure: connected: breadth first serch

from collections import deque

N, M = map(int, input().split())
S, = map(lambda x: int(x)-1, input().split())

Links = [[] for _ in range(N)]
for _ in range(M):
    uu, vv = map(lambda x: int(x)-1, input().split())
    Links[uu].append(vv)
    Links[vv].append(uu)
print(f'{Links = }')

def bfs(nodeo):
    global visited
    visited = [False for _ in range(N)]
    visited[nodeo] = True
    nodes = deque([nodeo])
    while len(nodes) > 0:
        nodeo = nodes.popleft()
        for node in Links[nodeo]:
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

