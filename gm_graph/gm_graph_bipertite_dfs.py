## gm_graph_bipertite_dfs.py: Coded by Kinya MIURA, 240207
## graph structure: distance: depth first serch

import sys
sys.setrecursionlimit(1000000)

NM = '8 7'
L = ['1 5', '1 6', '2 7', '3 7', '4 6', '5 8', '6 8']
NM = '6 7'
L = ['1 6', '2 6', '3 6', '2 4', '3 5', '1 3', '1 4']
# -----------------------------

N, M = map(int, input().split())

links = [[] for _ in range(N)]
for _ in range(M):
    uu, vv = map(lambda x: int(x)-1, input().split())
    links[uu].append(vv)
    links[vv].append(uu)
print(f'{links = }')

def dfsrc(nodeo):
    global visited, colored, bipertite
    for node in links[nodeo]:
        if colored[nodeo] == colored[node]:
            bipertite = False
        else:
            if not visited[node]:
                visited[node] = True
                colored[node] = - colored[nodeo]
                dfsrc(node)
    print(f'{nodeo = }, {visited = }, {colored = }')
    return

def dfs(nodeo):
    global visited, colored, bipertite
    visited[nodeo] = True
    colored[nodeo] = 1
    dfsrc(nodeo)
    return

visited = [False for _ in range(N)]
colored = [0 for _ in range(N)]
bipertite = True
while False in visited:
    S = visited.index(False)
    print(f'{S = }')
    dfs(S)
    print(f'{visited = }')
    print(f'{colored = }')
    print(f'{bipertite = }')


'''

2部グラフの判定を行うプログラム

N := 頂点の数
M := 辺の数

A,B　:= 頂点Aから頂点Bにかけて無向の辺があることを示す

dict := 辺のつながりを格納する
　　　　 collections の　dict　だとValueに配列を格納しやすい

color　:= 頂点が何色で塗られているか




from collections import defaultdict

N,M = map(int,input().split())
dict = defaultdict(set)

for i in range(M):
    a,b = list(map(int,input().split()))

    dict[a].add(b)
    dict[b].add(a)



color = [0 for i in range(N+1)]
res = 'Yes'

def dfs(v,c,queue=[]):
    v : 現在のグラフの頂点
    c : 現在参照するフラグ,1=>-1=>1と使うので渡す必要がある
    queue : 探索したグラフの頂点を入れていく
    res : global変数を使いたくないが,再帰のreturnがよくわからないのでとりあえず

    global color
    global res
    queue.append(v)

    for i in list(dict[v]):
        if color[i] == c:#隣の頂点が同じ値を与えられている際Falseを返す
            res = 'No'
        elif i not in queue:#探索済みでなければ再帰する
            color[i] = c*-1#0ならcとは異なる値を格納
            dfs(i,-c,queue)#引数に-cとすることで,cが1=>-1=>1を繰り返す


color[1] = 1#始点色分けする
(dfs(1,1))
print(res)
'''


