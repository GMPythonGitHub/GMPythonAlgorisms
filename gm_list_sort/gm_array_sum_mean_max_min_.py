# gm_list_sum: coded by Kinya MIURA 231229
# ---------------------------------------------------------
print('*** Array: sum, mean, max, min ***')
# ---------------------------------------------------------
import numpy as np

# =========================================================
## --- main routine --- ##
ar = np.arange(12)
print(f'{ar = }')
print(f'{len(ar) = }')
print(f'{np.sum(ar) = }')
print(f'{np.mean(ar) = }')
print(f'{np.max(ar) = }')
print(f'{np.min(ar) = }')
print(f'{np.std(ar) = }')
print(f'{np.var(ar) = }')

print()
ar_2d = np.arange(12).reshape(3, 4)
print(f'{ar_2d = }')
print(f'{ar_2d.ndim = }')
print(f'{ar_2d.shape = }')
print(f'{ar_2d.size = }')
print(f'{np.sum(ar_2d) = }')
print(f'{np.mean(ar_2d) = }')
print(f'{np.max(ar_2d) = }')
print(f'{np.min(ar_2d) = }')

print()
print(f'{np.sum(ar_2d, axis=0) = }')
print(f'{np.mean(ar_2d, axis=0) = }')
print(f'{np.max(ar_2d, axis=0) = }')
print(f'{np.min(ar_2d, axis=0) = }')
print()
print(f'{np.sum(ar_2d, axis=1) = }')
print(f'{np.mean(ar_2d, axis=1) = }')
print(f'{np.max(ar_2d, axis=1) = }')
print(f'{np.min(ar_2d, axis=1) = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Array: sum, mean, max, min ***
ar = array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
len(ar) = 12
np.sum(ar) = 66
np.mean(ar) = 5.5
np.max(ar) = 11
np.min(ar) = 0
np.std(ar) = 3.452052529534663
np.var(ar) = 11.916666666666666

ar_2d = array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
ar_2d.ndim = 2
ar_2d.shape = (3, 4)
ar_2d.size = 12
np.sum(ar_2d) = 66
np.mean(ar_2d) = 5.5
np.max(ar_2d) = 11
np.min(ar_2d) = 0

np.sum(ar_2d, axis=0) = array([12, 15, 18, 21])
np.mean(ar_2d, axis=0) = array([4., 5., 6., 7.])
np.max(ar_2d, axis=0) = array([ 8,  9, 10, 11])
np.min(ar_2d, axis=0) = array([0, 1, 2, 3])

np.sum(ar_2d, axis=1) = array([ 6, 22, 38])
np.mean(ar_2d, axis=1) = array([1.5, 5.5, 9.5])
np.max(ar_2d, axis=1) = array([ 3,  7, 11])
np.min(ar_2d, axis=1) = array([0, 4, 8])
'''
