## gm_GS_distance_weighted_BFS.py: Coded by Kinya MIURA, 240207
## graph structure: weighted distance: breadth first serch

# ---------------------------------------------------------
print('*** GS_BFS; graph structure: distance weighted ***')

# =========================================================
## --- main routine --- ##

from collections import deque

N, M = map(int, input().split())

links = [[] for _ in range(N)]
for _ in range(M):
    uu, vv, ww = map(int, input().split())
    uu, vv = uu - 1, vv - 1
    links[uu].append((vv, ww))
    links[vv].append((uu, ww))
print(f'{links = }')

S = 1 - 1

def bfs(nodeo):
    global visited, distance
    visited = [False for _ in range(N)]
    distance = [0 for _ in range(N)]
    visited[nodeo] = True
    nodes = deque([nodeo])
    while len(nodes) > 0:
        nodeo = nodes.popleft()
        for node, weight in links[nodeo]:
            dist = distance[nodeo] + weight
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
[case a]  tree structure
9 8
1 2 10
1 3 20
2 4 30
2 5 40
3 6 20
4 7 30
6 8 40
6 9 10

'''


'''
# =========================================================
# terminal log / terminal log / terminal log /
*** GS_BFS; graph structure: distance weighted ***
9 8
1 2 10
1 3 20
2 4 30
2 5 40
3 6 20
4 7 30
6 8 40
6 9 10
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


