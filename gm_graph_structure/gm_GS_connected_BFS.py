## gm_GS_connected_BFS.py: Coded by Kinya MIURA, 240207
## graph structure: connected: breadth first serch

# ---------------------------------------------------------
print('*** GS_BFS; graph structure: connected ***')

# =========================================================
## --- main routine --- ##

from collections import deque

N, M = map(int, input().split())
S, = map(lambda x: int(x)-1, input().split())

Links = [[] for _ in range(N)]
for _ in range(M):
    uu, vv = map(lambda x: int(x)-1, input().split())
    Links[uu].append(vv)
    Links[vv].append(uu)
print(f'{Links = }')

def BFS(nodeo):
    global visited
    visited = [False for _ in range(N)]
    visited[nodeo] = True
    nodes = deque([nodeo])
    while len(nodes) > 0:
        nodeo = nodes.popleft()
        for node in Links[nodeo]:
            if not visited[node]:
                visited[node] = True
                nodes.append(node)
        print(f'{nodeo = }, {nodes = }, {visited = }')
    return

visited = []
BFS(S)
print(f'{visited = }')
if False not in visited:
    print('connected')
else:
    print('not connected')

'''
[case a]  tree structure
9 8
1
1 2
1 3
2 4
2 5
3 6
4 7
6 8
6 9

[case b]  looped route
9 9
1
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
*** GS_BFS; graph structure: connected ***
9 8
1
1 2
1 3
2 4
2 5
3 6
4 7
6 8
6 9
Links = [[1, 2], [0, 3, 4], [0, 5], [1, 6], [1], [2, 7, 8], [3], [5], [5]]
nodeo = 0, nodes = deque([1, 2]), visited = [True, True, True, False, False, False, False, False, False]
nodeo = 1, nodes = deque([2, 3, 4]), visited = [True, True, True, True, True, False, False, False, False]
nodeo = 2, nodes = deque([3, 4, 5]), visited = [True, True, True, True, True, True, False, False, False]
nodeo = 3, nodes = deque([4, 5, 6]), visited = [True, True, True, True, True, True, True, False, False]
nodeo = 4, nodes = deque([5, 6]), visited = [True, True, True, True, True, True, True, False, False]
nodeo = 5, nodes = deque([6, 7, 8]), visited = [True, True, True, True, True, True, True, True, True]
nodeo = 6, nodes = deque([7, 8]), visited = [True, True, True, True, True, True, True, True, True]
nodeo = 7, nodes = deque([8]), visited = [True, True, True, True, True, True, True, True, True]
nodeo = 8, nodes = deque([]), visited = [True, True, True, True, True, True, True, True, True]
visited = [True, True, True, True, True, True, True, True, True]
connected

'''
