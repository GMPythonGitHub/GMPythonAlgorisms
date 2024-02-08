## gm_graph_tree_shortest_bfs.py: Coded by Kinya MIURA, 240207
## graff tee structure: shortest: breadth first serch

from collections import deque

NM = '9 8'
SG = '7 5'
L = ['1 2', '1 3', '2 4', '2 5', '3 6', '4 7', '6 8', '6 9', '7 9']
# -----------------------------

N, M = map(int, NM.split())
S, G = map(lambda x: int(x)-1, SG.split())

links = [[] for _ in range(N)]
for Li in L:
    uu, vv = map(lambda x: int(x)-1, Li.split())
    links[uu].append(vv)
    links[vv].append(uu)
print(f'{links = }')

visited = [False for _ in range(N)]
distance = [0 for _ in range(N)]
visited[S] = True
distance[S] = 0
bfs = deque([S])
while len(bfs) > 0:
    nodeo = bfs.popleft()
    dist = distance[nodeo] + 1
    for node in links[nodeo]:
        if not visited[node] or distance[node] > dist:
            visited[node] = True
            distance[node] = dist
            bfs.append(node)
    print(f'{nodeo = }, {bfs = }, {visited = }, {distance = }')
print(f'{visited = }')
print(f'{distance = }')
if not visited[G]:
    print('not connected')
else:
    print(distance[G])


'''
links = [[1, 2], [0, 3, 4], [0, 5], [1, 6], [1], [2, 7, 8], [3], [5], [5]]
nodeo = 0, bfs = deque([1, 2]), distance = [0, 1, 1, 10, 10, 10, 10, 10, 10]
nodeo = 1, bfs = deque([2, 3, 4]), distance = [0, 1, 1, 2, 2, 10, 10, 10, 10]
nodeo = 2, bfs = deque([3, 4, 5]), distance = [0, 1, 1, 2, 2, 2, 10, 10, 10]
nodeo = 3, bfs = deque([4, 5, 6]), distance = [0, 1, 1, 2, 2, 2, 3, 10, 10]
nodeo = 4, bfs = deque([5, 6]), distance = [0, 1, 1, 2, 2, 2, 3, 10, 10]
nodeo = 5, bfs = deque([6, 7, 8]), distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
nodeo = 6, bfs = deque([7, 8]), distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
nodeo = 7, bfs = deque([8]), distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
nodeo = 8, bfs = deque([]), distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
3
'''

