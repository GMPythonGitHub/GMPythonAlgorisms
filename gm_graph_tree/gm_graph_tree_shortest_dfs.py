## gm_graph_tree_shortest_dfs.py: Coded by Kinya MIURA, 240207
## graff tee structure: shortest: depth first serch

import sys
sys.setrecursionlimit(1000000)

NM = '9 8'
SG = '7 8'
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
def dfs(nodeo):
    global visited, distance
    for node in links[nodeo]:
        dist = distance[nodeo]+1
        if not visited[node] or distance[node] > dist :
            visited[node] = True
            distance[node] = dist
            dfs(node)
    print(f'{nodeo = }, {visited = }, {distance = }')
    return
visited[S] = True
distance[S] = 0
dfs(S)
print(f'{visited = }')
print(f'{distance = }')
if not visited[G]:
    print('not connected')
else:
    print(distance[G])


'''
links = [[1, 2], [0, 3, 4], [0, 5], [1, 6], [1], [2, 7, 8], [3], [5], [5]]
nodeo = 6, distance = [0, 1, 10, 2, 10, 10, 3, 10, 10]
nodeo = 3, distance = [0, 1, 10, 2, 10, 10, 3, 10, 10]
nodeo = 4, distance = [0, 1, 10, 2, 2, 10, 3, 10, 10]
nodeo = 1, distance = [0, 1, 10, 2, 2, 10, 3, 10, 10]
nodeo = 7, distance = [0, 1, 1, 2, 2, 2, 3, 3, 10]
nodeo = 8, distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
nodeo = 5, distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
nodeo = 2, distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
nodeo = 0, distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
distance = [0, 1, 1, 2, 2, 2, 3, 3, 3]
3
'''

