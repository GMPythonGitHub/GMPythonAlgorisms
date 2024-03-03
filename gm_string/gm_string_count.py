# gm_string_count.py: coded by Kinya MIURA 240302
## :: https://atcoder.jp/contests/abc342/tasks/abc342_a

# ---------------------------------------------------------
print('*** string: conversion table ***')

# =========================================================
## --- main routine --- ##
N = int(input())
S = list(input())
Q = int(input())

CDkey = list('abcdefghijklmnopqrstuvwxyz')
CDval = list('abcdefghijklmnopqrstuvwxyz')
for _ in range(Q):
    Ci, Di = input().split()
    if Ci == Di: continue
    for iCD, CDi in enumerate(CDval):
        if CDi == Ci: CDval[iCD] = Di
print(f'{CDkey = } \n{CDval = }')
CD = dict(zip(CDkey,CDval))
print(f'{CD = }')
for iS, Si in enumerate(S):
    S[iS] = CD[Si]
print(''.join(S))

'''
[case_a]
34
supercalifragilisticexpialidocious
20
g c
l g
g m
c m
r o
s e
a a
o f
f s
e t
t l
d v
p k
v h
x i
h n
n j
i r
s i
u a
'''

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** if statement: if-elif-else ***
Intermediate 5
'''
