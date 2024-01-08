# gm_selecting_slice.py: coded by Kinya MIURA 240106
# ---------------------------------------------------------
print('*** Selecting: slice ***')
# ---------------------------------------------------------
import numpy as np

# =========================================================
import random
random.seed(0)
nums = np.array([random.sample(range(-15, 15), k=30)])
print(f'{nums = }')

## --- selecting with slice --- ##
print(f'{nums[nums % 2 == 0]}')
# print(f'{nums[nums % 2 == 0 and nums < 20]}') unsupported

print(f'{nums[nums >= 0]}')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Selecting: slice ***
nums = array([[ 12,  -3,   9,  -2, -14,  -7,   1,   0,  13,  -6,   7,  -4,  -9,
          8, -11,   4, -13,   6,  10,   5,  -1,  14,  11,  -8, -15, -10,
          2,   3,  -5, -12]])
[ 12  -2 -14   0  -6  -4   8   4   6  10  14  -8 -10   2 -12]
[12  9  1  0 13  7  8  4  6 10  5 14 11  2  3]
'''
