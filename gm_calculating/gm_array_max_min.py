# gm_array_max_min.py: coded by Kinya MIURA 231229
# ---------------------------------------------------------
print('*** Array: max, min ***')
# ---------------------------------------------------------
import numpy as np

# =========================================================
## --- main routine --- ##
ar = np.arange(12)
print(f'{ar = }')
print(f'{len(ar) = }')
print(f'{np.max(ar) = }, {np.argmax(ar) = }')
print(f'{np.min(ar) = }, {np.argmin(ar) = }')

print()
ar_2d = np.arange(12).reshape(3, 4)
print(f'{ar_2d = }')
print(f'{ar_2d.ndim = }')
print(f'{ar_2d.shape = }')
print(f'{ar_2d.size = }')
print(f'{np.max(ar_2d) = }, {np.argmax(ar_2d) = }')
print(f'{np.min(ar_2d) = }, {np.argmin(ar_2d) = }')

print()
print(f'{np.max(ar_2d, axis=0) = }, {np.argmax(ar_2d, axis=0) = }')
print(f'{np.min(ar_2d, axis=0) = }, {np.argmin(ar_2d, axis=0) = }')
print()
print(f'{np.max(ar_2d, axis=1) = }, {np.argmax(ar_2d, axis=1) = }')
print(f'{np.min(ar_2d, axis=1) = }, {np.argmin(ar_2d, axis=1) = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Array: max, min ***
ar = array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
len(ar) = 12
np.max(ar) = 11, np.argmax(ar) = 11
np.min(ar) = 0, np.argmin(ar) = 0

ar_2d = array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
ar_2d.ndim = 2
ar_2d.shape = (3, 4)
ar_2d.size = 12
np.max(ar_2d) = 11, np.argmax(ar_2d) = 11
np.min(ar_2d) = 0, np.argmin(ar_2d) = 0

np.max(ar_2d, axis=0) = array([ 8,  9, 10, 11]), np.argmax(ar_2d, axis=0) = array([2, 2, 2, 2], dtype=int64)
np.min(ar_2d, axis=0) = array([0, 1, 2, 3]), np.argmin(ar_2d, axis=0) = array([0, 0, 0, 0], dtype=int64)

np.max(ar_2d, axis=1) = array([ 3,  7, 11]), np.argmax(ar_2d, axis=1) = array([3, 3, 3], dtype=int64)
np.min(ar_2d, axis=1) = array([0, 4, 8]), np.argmin(ar_2d, axis=1) = array([0, 0, 0], dtype=int64)
'''
