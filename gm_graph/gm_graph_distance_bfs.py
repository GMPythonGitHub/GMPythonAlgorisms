## gm_graph_distance_bfs.py: Coded by Kinya MIURA, 240207
## graph structure: distance: breadth first serch

from collections import deque

NM = '9 9'
S = '8'
L = ['1 2', '1 3', '2 4', '2 5', '3 6', '4 7', '6 8', '6 9', '7 9']
# -----------------------------

N, M = map(int, NM.split())
S = int(S) - 1

links = [[] for _ in range(N)]
for Li in L:
    uu, vv = map(lambda x: int(x)-1, int, Li.split())
    links[uu].append(vv)
    links[vv].append(uu)
print(f'{links = }')

def bfs(nodeo):
    global visited, distance
    visited = [False for _ in range(N)]
    distance = [0 for _ in range(N)]
    visited[nodeo] = True
    nodes = deque([nodeo])
    while len(nodes) > 0:
        nodeo = nodes.popleft()
        for node in links[nodeo]:
            dist = distance[nodeo] + 1
            if not visited[node] or distance[node] > dist:
                visited[node] = True
                distance[node] = dist
                nodes.append(node)
        print(f'{nodeo = }, {nodes = }, {visited = }, {distance = }')
    return

visited, distance = [], []
bfs(S)
print(f'{visited = }')
print(f'{distance = }')


'''
links = [[(1, 10), (2, 20)], [(0, 10), (3, 30), (4, 40)], [(0, 20), (5, 20)], [(1, 30), (6, 30)], [(1, 40)], [(2, 20), (7, 40), (8, 10)], [(3, 30)], [(5, 40)], [(5, 10)]]
nodeo = 0, nodes = deque([1, 2]), visited = [True, True, True, False, False, False, False, False, False], distance = [0, 10, 20, 0, 0, 0, 0, 0, 0]
nodeo = 1, nodes = deque([2, 3, 4]), visited = [True, True, True, True, True, False, False, False, False], distance = [0, 10, 20, 40, 50, 0, 0, 0, 0]
nodeo = 2, nodes = deque([3, 4, 5]), visited = [True, True, True, True, True, True, False, False, False], distance = [0, 10, 20, 40, 50, 40, 0, 0, 0]
nodeo = 3, nodes = deque([4, 5, 6]), visited = [True, True, True, True, True, True, True, False, False], distance = [0, 10, 20, 40, 50, 40, 70, 0, 0]
nodeo = 4, nodes = deque([5, 6]), visited = [True, True, True, True, True, True, True, False, False], distance = [0, 10, 20, 40, 50, 40, 70, 0, 0]
nodeo = 5, nodes = deque([6, 7, 8]), visited = [True, True, True, True, True, True, True, True, True], distance = [0, 10, 20, 40, 50, 40, 70, 80, 50]
nodeo = 6, nodes = deque([7, 8]), visited = [True, True, True, True, True, True, True, True, True], distance = [0, 10, 20, 40, 50, 40, 70, 80, 50]
nodeo = 7, nodes = deque([8]), visited = [True, True, True, True, True, True, True, True, True], distance = [0, 10, 20, 40, 50, 40, 70, 80, 50]
nodeo = 8, nodes = deque([]), visited = [True, True, True, True, True, True, True, True, True], distance = [0, 10, 20, 40, 50, 40, 70, 80, 50]
visited = [True, True, True, True, True, True, True, True, True]
distance = [0, 10, 20, 40, 50, 40, 70, 80, 50]
'''

