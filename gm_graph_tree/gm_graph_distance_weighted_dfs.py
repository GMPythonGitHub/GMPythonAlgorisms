## gm_graph_distance_weighted_dfs.py: Coded by Kinya MIURA, 240207
## graph structure: weighted distance: depth first serch

import sys
sys.setrecursionlimit(1000000)

NM = '9 8'
S = '1'
L = ['1 2 10', '1 3 20', '2 4 30', '2 5 40', '3 6 20', '4 7 30', '6 8 40', '6 9 10']
# -----------------------------

N, M = map(int, NM.split())
S = int(S) - 1

links = [[] for _ in range(N)]
for Li in L:
    uu, vv, ww = map(int, Li.split())
    uu, vv = uu - 1, vv - 1
    links[uu].append((vv, ww))
    links[vv].append((uu, ww))
print(f'{links = }')

def dfsrc(nodeo):
    global visited, distance
    for node, weight in links[nodeo]:
        dist = distance[nodeo] + weight
        if not visited[node] or distance[node] > dist :
            visited[node] = True
            distance[node] = dist
            dfsrc(node)
    print(f'{nodeo = }, {visited = }, {distance = }')
    return

def dfs(nodeo):
    global visited, distance
    visited = [False for _ in range(N)]
    distance = [0 for _ in range(N)]
    visited[nodeo] = True
    dfsrc(nodeo)
    return

visited, distance = [], []
dfs(S)
print(f'{visited = }')
print(f'{distance = }')


'''
links = [[(1, 10), (2, 20)], [(0, 10), (3, 30), (4, 40)], [(0, 20), (5, 20)], [(1, 30), (6, 30)], [(1, 40)], [(2, 20), (7, 40), (8, 10)], [(3, 30)], [(5, 40)], [(5, 10)]]
nodeo = 6, visited = [True, True, False, True, False, False, True, False, False], distance = [0, 10, 0, 40, 0, 0, 70, 0, 0]
nodeo = 3, visited = [True, True, False, True, False, False, True, False, False], distance = [0, 10, 0, 40, 0, 0, 70, 0, 0]
nodeo = 4, visited = [True, True, False, True, True, False, True, False, False], distance = [0, 10, 0, 40, 50, 0, 70, 0, 0]
nodeo = 1, visited = [True, True, False, True, True, False, True, False, False], distance = [0, 10, 0, 40, 50, 0, 70, 0, 0]
nodeo = 7, visited = [True, True, True, True, True, True, True, True, False], distance = [0, 10, 20, 40, 50, 40, 70, 80, 0]
nodeo = 8, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 10, 20, 40, 50, 40, 70, 80, 50]
nodeo = 5, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 10, 20, 40, 50, 40, 70, 80, 50]
nodeo = 2, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 10, 20, 40, 50, 40, 70, 80, 50]
nodeo = 0, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 10, 20, 40, 50, 40, 70, 80, 50]
visited = [True, True, True, True, True, True, True, True, True]
distance = [0, 10, 20, 40, 50, 40, 70, 80, 50]
'''

