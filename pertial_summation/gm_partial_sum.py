# gm_partial_sum.py: coded by Kinya MIURA 240106
# ---------------------------------------------------------
print('*** Partial summation: cumulative summation ***')
# ---------------------------------------------------------
import numpy as np

# =========================================================
## --- partial summation of array --- ##
nums = np.arange(50)
print(f'{nums = }')
numa, numb = 15, 45
print(f'{numa = }, {numb = }')

print()
## --- using for-loope --- ##
ss = 0
for i in range(numa, numb+1):
    ss += i
print(f'for_loop: {ss = }')

print()
## --- analytical --- ##
ss = (numa + numb) * (numb - numa + 1) // 2
print(f'analytical_1: {ss = }')

print()
## --- analytical with function --- ##
def sum_list(num) -> int:
    return num * (num + 1) // 2

ss = sum_list(numb) - sum_list(numa-1)
print(f'analytical_2: {ss = }')

print()
## --- cumulative summation --- ##
cumss = nums.cumsum()
print(f'{cumss = }')
ss = cumss[numb] - cumss[numa-1]
print(f'cumulative summation: {ss = }')

print()
## --- multiple partial summations --- ##
numab = ((1, 15), (5, 25), (10, 35), (15, 45))
for numa, numb in numab:
    ss = cumss[numb] - cumss[numa-1]
    print(f'(numa, numb) = ({numa},{numb}) :  {ss = }')

print()
## --- random array --- ##
import random
random.seed(0)
nums = np.array([random.sample(range(50), k=50)])
print(f'{nums = }')
cumss = nums.cumsum()
print(f'{cumss = }')
numab = ((1, 15), (5, 25), (10, 35), (15, 45))
for numa, numb in numab:
    ss = cumss[numb] - cumss[numa-1]
    print(f'(numa, numb) = ({numa},{numb}) :  {ss = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Partial summation: cumulative summation ***
nums = array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
       34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49])
numa = 15, numb = 45

for_loop: ss = 930

analytical_1: ss = 930

analytical_2: ss = 930

cumss = array([   0,    1,    3,    6,   10,   15,   21,   28,   36,   45,   55,
         66,   78,   91,  105,  120,  136,  153,  171,  190,  210,  231,
        253,  276,  300,  325,  351,  378,  406,  435,  465,  496,  528,
        561,  595,  630,  666,  703,  741,  780,  820,  861,  903,  946,
        990, 1035, 1081, 1128, 1176, 1225])
cumulative summation: ss = 930

(numa, numb) = (1,15) :  ss = 120
(numa, numb) = (5,25) :  ss = 315
(numa, numb) = (10,35) :  ss = 585
(numa, numb) = (15,45) :  ss = 930

nums = array([[24, 48, 26,  2, 16, 32, 31, 25, 19, 30, 22, 37, 13, 44,  8, 18,
        35,  6, 45, 29, 17, 39, 42, 41,  4,  9,  3, 46, 21, 10, 15, 40,
        23, 11, 38,  5, 49, 20, 34, 33,  7, 47, 27,  0, 12, 36, 14, 28,
         1, 43]])
cumss = array([  24,   72,   98,  100,  116,  148,  179,  204,  223,  253,  275,
        312,  325,  369,  377,  395,  430,  436,  481,  510,  527,  566,
        608,  649,  653,  662,  665,  711,  732,  742,  757,  797,  820,
        831,  869,  874,  923,  943,  977, 1010, 1017, 1064, 1091, 1091,
       1103, 1139, 1153, 1181, 1182, 1225])
(numa, numb) = (1,15) :  ss = 371
(numa, numb) = (5,25) :  ss = 546
(numa, numb) = (10,35) :  ss = 621
(numa, numb) = (15,45) :  ss = 762
'''
