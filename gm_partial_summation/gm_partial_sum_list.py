# gm_partial_sum_list.py: coded by Kinya MIURA 240326
# ---------------------------------------------------------
print('*** Partial summation of list: cumulative summation ***')
# ---------------------------------------------------------

# =========================================================
## --- partial sum of list --- ##

def accum(lst):
    aclst = [0]
    for lsti in lst:
        aclst.append(aclst[-1]+lsti)
    return aclst

N = int(input())
A = list(map(int, input().split()))
print(f'{A = }')

acmA = accum(A)
print(f'acmA = accum(A): {acmA}')

M = int(input())
for _ in range(M):
    aa, bb = map(int, input().split())
    print(acmA[bb+1] - acmA[aa])

'''
[case a]
10
0 1 2 3 4 5 6 7 8 9
7
0 2
0 4
0 6
0 8
3 5
3 7
3 9

[case b]
10
9 8 7 6 5 4 3 2 1 0
7
0 2
0 4
0 6
0 8
3 5
3 7
3 9

[case c]
10
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
*** Partial summation of list: cumulative summation ***
0 1 2 3 4 5 6 7 8 9
7
0 2
0 4
0 6
0 8
3 5
3 7
3 9
A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
acmAa = accum(A): [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
acmAb = accum(A, init=0): [0, 0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
3
10
21
36
12
25
42
'''
