# gm_partial_sum_mesh.py: coded by Kinya MIURA 240326
# ---------------------------------------------------------
print('*** Partial summation of mesh: cumulative summation ***')
# ---------------------------------------------------------

# =========================================================
## --- partial sum of mesh --- ##

def accum(lst):
    H, W = len(lst), len(lst[0])
    aclst = [[0 for _ in range(W+1)] for _ in range(H+1)]
    for iH in range(H):
        for iW in range(W):
            aclst[iH+1][iW+1] = lst[iH][iW] + aclst[iH+1][iW] + aclst[iH][iW+1] - aclst[iH][iW]
    return aclst

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
for Ai in A: print(f'{Ai = }')

acmA = accum(A)
for acmAi in acmA: print(f'{acmAi = }')

M = int(input())
for _ in range(M):
    Ha, Wa, Hb, Wb = map(int, input().split())
    print(acmA[Hb+1][Wb+1] + acmA[Ha][Wb+1] + acmA[Hb+1][Wa] - acmA[Ha][Wa])

'''
[case a]
5 5
0 1 2 3 4
1 1 2 3 4
2 2 2 3 4
3 3 3 3 4
4 4 4 4 4 
5
0 0 0 0
0 0 1 1
0 0 2 2
0 0 3 3
0 0 4 4

[case b]
5 5
0 1 2 3 4
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8 
5
0 0 0 0
0 0 1 1
0 0 2 2
0 0 3 3
0 0 4 4

[case c]
5 2 9 4 3 8 0 7 6 1
7
0 2
0 4
0 6
0 8
3 5
3 7
3 9

'''


# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Partial summation of mesh: cumulative summation ***
5 5
0 1 2 3 4
1 1 2 3 4
2 2 2 3 4
3 3 3 3 4
4 4 4 4 4 
5
0 0 0 0
0 0 1 1
0 0 2 2
0 0 3 3
0 0 4 4
Ai = [0, 1, 2, 3, 4]
Ai = [1, 1, 2, 3, 4]
Ai = [2, 2, 2, 3, 4]
Ai = [3, 3, 3, 3, 4]
Ai = [4, 4, 4, 4, 4]
acmAi = [0, 0, 0, 0, 0, 0]
acmAi = [0, 0, 1, 3, 6, 10]
acmAi = [0, 1, 3, 7, 13, 21]
acmAi = [0, 3, 7, 13, 22, 34]
acmAi = [0, 6, 13, 22, 34, 50]
acmAi = [0, 10, 21, 34, 50, 70]
0
3
13
34
70

'''
