# gm_itertools_combinations_with_replacement: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** itertools: combinations_with_replacement ***')
# ---------------------------------------------------------
import itertools
from collections import defaultdict

# =========================================================
## --- main routine --- ##
print(f'{list(itertools.combinations_with_replacement(range(3), 3)) = }')
print(f'{list(itertools.combinations_with_replacement(range(3), 2)) = }')
print(f'{list(itertools.combinations_with_replacement(range(3), 1)) = } \n')

lst = (0,0,1,2)
print(f'{lst = }')
print(f'{list(itertools.combinations_with_replacement(lst, 2)) = }')
print(f'{set(itertools.combinations_with_replacement(lst, 2)) = } \n')

tpl = tuple(itertools.combinations_with_replacement(lst, 2))
dftdct = defaultdict(int)
for tp in tpl:
    dftdct[tp] += 1
print(f'{dftdct = } \n')

# =============================================================
# terminal log / terminal log / terminal log /
'''
*** itertools: combinations_with_replacement ***
list(itertools.combinations_with_replacement(range(3), 3)) = [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 1), (0, 1, 2), (0, 2, 2), (1, 1, 1), (1, 1, 2), (1, 2, 2), (2, 2, 2)]
list(itertools.combinations_with_replacement(range(3), 2)) = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
list(itertools.combinations_with_replacement(range(3), 1)) = [(0,), (1,), (2,)] 

lst = (0, 0, 1, 2)
list(itertools.combinations_with_replacement(lst, 2)) = [(0, 0), (0, 0), (0, 1), (0, 2), (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
set(itertools.combinations_with_replacement(lst, 2)) = {(0, 1), (1, 2), (0, 0), (1, 1), (0, 2), (2, 2)} 

dftdct = defaultdict(<class 'int'>, {(0, 0): 3, (0, 1): 2, (0, 2): 2, (1, 1): 1, (1, 2): 1, (2, 2): 1}) 
'''