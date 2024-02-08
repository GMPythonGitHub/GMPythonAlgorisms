## gm_graph_tree_distance_bfs.py: Coded by Kinya MIURA, 240207
## graff tee structure: distance: breadth first serch

from collections import deque

NM = '9 8'
L = ['1 2', '1 3', '2 4', '2 5', '3 6', '4 7', '6 8', '6 9', '7 9']
# -----------------------------

N, M = map(int, NM.split())

links = [[] for _ in range(N)]
for Li in L:
    uu, vv = map(lambda x: int(x)-1, Li.split())
    links[uu].append(vv)
    links[vv].append(uu)
print(f'{links = }')
# -----------------------------

checked = [False for _ in range(N)]

visited = [False for _ in range(N)]
distance = [0 for _ in range(N)]
start = 0
checked[start] = True
visited[start] = True
distance[start] = 0
bfs = deque([start])
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

dst_max = max(distance)
start = distance.index(dst_max)
print(f'{dst_max = }, {start = }')
for ii, dst in enumerate(distance):
    if dst < dst_max:
        checked[ii] = True
print(f'{checked = }')


'''
links = [[1, 2], [0, 3, 4], [0, 5], [1, 6], [1], [2, 7, 8], [3, 8], [5], [5, 6]]
nodeo = 0, bfs = deque([1, 2]), visited = [True, True, True, False, False, False, False, False, False], distance = [0, 1, 1, 0, 0, 0, 0, 0, 0]
nodeo = 1, bfs = deque([2, 3, 4]), visited = [True, True, True, True, True, False, False, False, False], distance = [0, 1, 1, 2, 2, 0, 0, 0, 0]
nodeo = 2, bfs = deque([3, 4, 5]), visited = [True, True, True, True, True, True, False, False, False], distance = [0, 1, 1, 2, 2, 2, 0, 0, 0]
nodeo = 3, bfs = deque([4, 5, 6]), visited = [True, True, True, True, True, True, True, False, False], distance = [0, 1, 1, 2, 2, 2, 3, 0, 0]
nodeo = 4, bfs = deque([5, 6]), visited = [True, True, True, True, True, True, True, False, False], distance = [0, 1, 1, 2, 2, 2, 3, 0, 0]
nodeo = 5, bfs = deque([6, 7, 8]), visited = [True, True, True, True, True, True, True, True, True], distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
nodeo = 6, bfs = deque([7, 8]), visited = [True, True, True, True, True, True, True, True, True], distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
nodeo = 7, bfs = deque([8]), visited = [True, True, True, True, True, True, True, True, True], distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
nodeo = 8, bfs = deque([]), visited = [True, True, True, True, True, True, True, True, True], distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
visited = [True, True, True, True, True, True, True, True, True]
distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
'''

