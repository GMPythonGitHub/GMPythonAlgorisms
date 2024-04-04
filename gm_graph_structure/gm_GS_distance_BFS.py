## gm_GS_distance_BFS.py: Coded by Kinya MIURA, 240207
## graph structure: distance: breadth first serch

# ---------------------------------------------------------
print('*** GS_BFS; graph structure: distance ***')

# =========================================================
## --- main routine --- ##

from collections import deque

N, M = map(int, input().split())

links = [[] for _ in range(N)]
for _ in range(M):
    uu, vv = map(lambda x: int(x)-1, input().split())
    links[uu].append(vv)
    links[vv].append(uu)
print(f'{links = }')

S = 8 - 1

def BFS(nodeo):
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
BFS(S)
print(f'{visited = }')
print(f'{distance = }')

'''
[case a]  tree structure
9 9
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
*** GS_BFS; graph structure: distance ***
9 9
1 2
1 3
2 4
2 5
3 6
4 7
6 8
6 9
7 9
links = [[1, 2], [0, 3, 4], [0, 5], [1, 6], [1], [2, 7, 8], [3, 8], [5], [5, 6]]
nodeo = 7, nodes = deque([5]), visited = [False, False, False, False, False, True, False, True, False], distance = [0, 0, 0, 0, 0, 1, 0, 0, 0]
nodeo = 5, nodes = deque([2, 8]), visited = [False, False, True, False, False, True, False, True, True], distance = [0, 0, 2, 0, 0, 1, 0, 0, 2]
nodeo = 2, nodes = deque([8, 0]), visited = [True, False, True, False, False, True, False, True, True], distance = [3, 0, 2, 0, 0, 1, 0, 0, 2]
nodeo = 8, nodes = deque([0, 6]), visited = [True, False, True, False, False, True, True, True, True], distance = [3, 0, 2, 0, 0, 1, 3, 0, 2]
nodeo = 0, nodes = deque([6, 1]), visited = [True, True, True, False, False, True, True, True, True], distance = [3, 4, 2, 0, 0, 1, 3, 0, 2]
nodeo = 6, nodes = deque([1, 3]), visited = [True, True, True, True, False, True, True, True, True], distance = [3, 4, 2, 4, 0, 1, 3, 0, 2]
nodeo = 1, nodes = deque([3, 4]), visited = [True, True, True, True, True, True, True, True, True], distance = [3, 4, 2, 4, 5, 1, 3, 0, 2]
nodeo = 3, nodes = deque([4]), visited = [True, True, True, True, True, True, True, True, True], distance = [3, 4, 2, 4, 5, 1, 3, 0, 2]
nodeo = 4, nodes = deque([]), visited = [True, True, True, True, True, True, True, True, True], distance = [3, 4, 2, 4, 5, 1, 3, 0, 2]
visited = [True, True, True, True, True, True, True, True, True]
distance = [3, 4, 2, 4, 5, 1, 3, 0, 2]


'''

