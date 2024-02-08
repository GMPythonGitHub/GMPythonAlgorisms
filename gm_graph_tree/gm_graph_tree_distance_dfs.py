## gm_graph_tree_distance_dfs.py: Coded by Kinya MIURA, 240207
## graff tee structure: distance: depth first serch

import sys
sys.setrecursionlimit(1000000)

NM = '9 9'
S = int('8')
L = ['1 2', '1 3', '2 4', '2 5', '3 6', '4 7', '6 8', '6 9', '7 9']
# -----------------------------

N, M = map(int, NM.split())

links = [[] for _ in range(N)]
for Li in L:
    uu, vv = map(lambda x: int(x)-1, Li.split())
    links[uu].append(vv)
    links[vv].append(uu)
print(f'{links = }')
S -= 1

def dfsrc(nodeo):
    global visited, distance
    for node in links[nodeo]:
        dist = distance[nodeo] + 1
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
links = [[1, 2], [0, 3, 4], [0, 5], [1, 6], [1], [2, 7, 8], [3, 8], [5], [5, 6]]
nodeo = 2, visited = [True, True, True, True, False, True, True, False, True], distance = [0, 1, 6, 2, 0, 5, 3, 0, 4]
nodeo = 7, visited = [True, True, True, True, False, True, True, True, True], distance = [0, 1, 6, 2, 0, 5, 3, 6, 4]
nodeo = 5, visited = [True, True, True, True, False, True, True, True, True], distance = [0, 1, 6, 2, 0, 5, 3, 6, 4]
nodeo = 8, visited = [True, True, True, True, False, True, True, True, True], distance = [0, 1, 6, 2, 0, 5, 3, 6, 4]
nodeo = 6, visited = [True, True, True, True, False, True, True, True, True], distance = [0, 1, 6, 2, 0, 5, 3, 6, 4]
nodeo = 3, visited = [True, True, True, True, False, True, True, True, True], distance = [0, 1, 6, 2, 0, 5, 3, 6, 4]
nodeo = 4, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 1, 6, 2, 2, 5, 3, 6, 4]
nodeo = 1, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 1, 6, 2, 2, 5, 3, 6, 4]
nodeo = 7, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 1, 1, 2, 2, 2, 3, 3, 4]
nodeo = 8, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
nodeo = 5, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
nodeo = 2, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
nodeo = 0, visited = [True, True, True, True, True, True, True, True, True], distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
visited = [True, True, True, True, True, True, True, True, True]
distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
'''

