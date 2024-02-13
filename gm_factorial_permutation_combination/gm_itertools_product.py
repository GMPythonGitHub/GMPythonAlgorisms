# gm_itertools_product: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** itertools: pruduct ***')
# ---------------------------------------------------------
import itertools
from collections import defaultdict

# =========================================================
## --- main routine --- ##
print(f'{list(itertools.product(range(3), repeat=2)) = }')
print(f'{list(itertools.product(range(3), repeat=1)) = } \n')

lst = (0,0,1,2)
print(f'{lst = }')
print(f'{list(itertools.product(lst, repeat=2)) = }')
print(f'{set(itertools.product(lst, repeat=2)) = } \n')

tpl = tuple(itertools.product(lst, repeat=2))
dftdct = defaultdict(int)
for tp in tpl:
    dftdct[tp] += 1
print(f'{dftdct = } \n')

# =============================================================
# terminal log / terminal log / terminal log /
'''
*** itertools: pruduct ***
list(itertools.product(range(3), repeat=2)) = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
list(itertools.product(range(3), repeat=1)) = [(0,), (1,), (2,)] 

lst = (0, 0, 1, 2)
list(itertools.product(lst, repeat=2)) = [(0, 0), (0, 0), (0, 1), (0, 2), (0, 0), (0, 0), (0, 1), (0, 2), (1, 0), (1, 0), (1, 1), (1, 2), (2, 0), (2, 0), (2, 1), (2, 2)]
set(itertools.product(lst, repeat=2)) = {(0, 1), (1, 2), (2, 1), (0, 0), (1, 1), (2, 0), (0, 2), (2, 2), (1, 0)} 

dftdct = defaultdict(<class 'int'>, {(0, 0): 4, (0, 1): 2, (0, 2): 2, (1, 0): 2, (1, 1): 1, (1, 2): 1, (2, 0): 2, (2, 1): 1, (2, 2): 1}) 
'''