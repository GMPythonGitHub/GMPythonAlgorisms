# gm_sort_array.py: coded by Kinya MIURA 231229
# ---------------------------------------------------------
print('*** Sort: array ***')
# ---------------------------------------------------------
import numpy as np

# =========================================================
## --- sorting array --- ##
ary = np.array([0, 5, 9, 2, 8, 4, 6, 1, 3, 7])
print(f'{ary = }')
print(f'{np.sort(ary) = }')  # sorting
print(f'{np.sort(ary)[::-1] = }')
ary_sorted = np.sort(ary)
print(f'{ary_sorted = }')
ary_sortedr = np.sort(ary)[::-1]
print(f'{ary_sortedr = }')
print()
print(f'{np.argsort(ary) = }')  # sorting indices
print(f'{np.argsort(ary)[::-1] = }')

print()
## --- sorting 2d array --- ##
ary2d = np.array([[0, 5, 7], [2, 8, 4], [6, 1, 3]])  # sorting
print(f'{ary2d = }')
print(f'{np.sort(ary2d, axis=0) = }')
print(f'{np.sort(ary2d, axis=0)[::-1] = }')
print(f'{np.sort(ary2d, axis=1) = }')
print(f'{np.sort(ary2d, axis=1)[::,::-1] = }')
print()
print(f'{np.argsort(ary2d, axis=0) = }')  # sorting indices
print(f'{np.argsort(ary2d, axis=0)[::-1] = }')
print(f'{np.argsort(ary2d, axis=1) = }')
print(f'{np.argsort(ary2d, axis=1)[::,::-1] = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Sort: array ***
ary = array([0, 5, 9, 2, 8, 4, 6, 1, 3, 7])
np.sort(ary) = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.sort(ary)[::-1] = array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
ary_sorted = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
ary_sortedr = array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

np.argsort(ary) = array([0, 7, 3, 8, 5, 1, 6, 9, 4, 2], dtype=int64)
np.argsort(ary)[::-1] = array([2, 4, 9, 6, 1, 5, 8, 3, 7, 0], dtype=int64)

ary2d = array([
       [0, 5, 7],
       [2, 8, 4],
       [6, 1, 3]])
np.sort(ary2d, axis=0) = array([
       [0, 1, 3],
       [2, 5, 4],
       [6, 8, 7]])
np.sort(ary2d, axis=0)[::-1] = array([
       [6, 8, 7],
       [2, 5, 4],
       [0, 1, 3]])
np.sort(ary2d, axis=1) = array([
       [0, 5, 7],
       [2, 4, 8],
       [1, 3, 6]])
np.sort(ary2d, axis=1)[::,::-1] = array([
       [7, 5, 0],
       [8, 4, 2],
       [6, 3, 1]])

np.argsort(ary2d, axis=0) = array([
       [0, 2, 2],
       [1, 0, 1],
       [2, 1, 0]], dtype=int64)
np.argsort(ary2d, axis=0)[::-1] = array([
       [2, 1, 0],
       [1, 0, 1],
       [0, 2, 2]], dtype=int64)
np.argsort(ary2d, axis=1) = array([
       [0, 1, 2],
       [0, 2, 1],
       [1, 2, 0]], dtype=int64)
np.argsort(ary2d, axis=1)[::,::-1] = array([
       [2, 1, 0],
       [1, 2, 0],
       [0, 2, 1]], dtype=int64)
'''
