## gm_graph_tree_shortest_dfs.py: Coded by Kinya MIURA, 240207
## graff tee structure: shortest: depth first serch

import sys
sys.setrecursionlimit(1000000)

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

def dfsrc(nodeo):
    global visited, distance
    for node in links[nodeo]:
        dist = distance[nodeo] + 1
        if not visited[node] or distance[node] > dist :
            visited[node] = True
            distance[node] = dist
            dfsrc(node)
    # print(f'{nodeo = }, {visited = }, {distance = }')
    return

def dfs(nodeo):
    global visited, distance
    visited = [False for _ in range(N)]
    distance = [0 for _ in range(N)]
    visited[nodeo] = True
    dfsrc(nodeo)
    return

checked = [False for _ in range(N)]
visited, distance = [], []
S = 0
checked[S] = True
dfs(S)
print(f'{visited = }')
print(f'{distance = }')

dst_max = max(distance)
for ii, dst in enumerate(distance):
    if dst < dst_max:
        checked[ii] = True
print(f'{checked = }')

for S, chk in enumerate(checked):
    if chk:
        continue
    print(f'{S = }')
    dfs(S)
    print(f'{visited = }')
    print(f'{distance = }')
    dst_max = max(dst_max, max(distance))
print(dst_max)


'''

'''

