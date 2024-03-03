# gm_binary_section_list.py: coded by Kinya MIURA 240302
## :: https://atcoder.jp/contests/abc205/tasks/abc205_d

# ---------------------------------------------------------
print('*** binary section: list ***')

# =========================================================
## --- import bisect --- ##
from bisect import (
    bisect_right, bisect_left, insort_left, insort_right )

## --- main routine --- ##
lst = [i*i for i in range(10)]
print(f'{lst = } \n')

val = 36
print(f'{bisect_left(lst, val) = }, {bisect_right(lst, val) = }')
lft, rgt = bisect_left(lst, val), bisect_right(lst, val)
print(f'{val = }, {lst[lft] = }, {lst[rgt] = }')

print()
lst = [i//2 for i in range(20)]
print(f'{lst = } \n')

val = 5
print(f'{bisect_left(lst, val) = }, {bisect_right(lst, val) = }')
lft, rgt = bisect_left(lst, val), bisect_right(lst, val)
print(f'{val = }, {lst[lft] = }, {lst[rgt] = }')


# =========================================================
# terminal log / terminal log / terminal log /
'''

'''
