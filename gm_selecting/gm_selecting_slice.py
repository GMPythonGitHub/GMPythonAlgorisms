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
# print(f'{nums[nums % 2 == 0 and nums < 20]}') not accepted
print(f'{nums[nums >= 0]}')

# =========================================================
# terminal log / terminal log / terminal log /
'''

'''
