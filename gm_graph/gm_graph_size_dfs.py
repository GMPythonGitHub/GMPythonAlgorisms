## gm_graph_size_dfs.py: Coded by Kinya MIURA, 240207
## graph structure: size: depth first serch

import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())

UV = [[] for _ in range(N)]
for Li in L:
    uu, vv = map(lambda x: int(x)-1, Li.split())
    UV[uu].append(vv)
    UV[vv].append(uu)
print(f'{UV = }')
# -----------------------------

def dfsrc(nodeo):
    global visited, distance
    for node in UV[nodeo]:
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

distmax = max(distance)
for ii, dst in enumerate(distance):
    if dst < distmax:
        checked[ii] = True
print(f'{checked = }')

for S, chk in enumerate(checked):
    if chk:
        continue
    print(f'{S = }')
    dfs(S)
    print(f'{visited = }')
    print(f'{distance = }')
    distmax = max(distmax, max(distance))
print(distmax)


'''
[case a]
9 8
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

