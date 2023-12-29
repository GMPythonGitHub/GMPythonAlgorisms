# gm_list_max_min_sort: coded by Kinya MIURA 231229
# ---------------------------------------------------------
print('*** List: sort ***')

# =========================================================
## --- main routine --- ##
ls = [0, 5, 9, 2, 8, 4, 6, 1, 3, 7]
print(f'{sorted(ls) = }')
print(f'{sorted(ls, reverse=True) = }')
print(f'{sorted(ls)[:3] = }')
print(f'{sorted(ls, reverse=True)[:3] = }')

print()
ls_key = ['a', 'b', 'c', 'd', 'e']
print(f'{ls_key = }')
ls_val = [ 0,   2,   4,   1,   3 ]
print(f'{ls_val = }')
ls_item = list(zip(ls_val, ls_key))
print(f'{ls_item = }')

print()
ls_item_sorted = sorted(ls_item)
print(f'{ls_item_sorted = }')
ls_val_sorted, ls_key_sorted = zip(*ls_item_sorted)
print(f'{ls_key_sorted = }')
print(f'{ls_val_sorted = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** List sort: max, min, sort ***
[10, 12, 23, 34, 45, 56, 67, 78, 89, 90]
[90, 89, 78, 67, 56, 45, 34, 23, 12, 10]
[10, 12, 23]
[90, 89, 78]

ls_key = ['a', 'b', 'c', 'd', 'e']
ls_val = [0, 2, 4, 1, 3]
ls_item = [(0, 'a'), (2, 'b'), (4, 'c'), (1, 'd'), (3, 'e')]

ls_item_sorted = [(0, 'a'), (1, 'd'), (2, 'b'), (3, 'e'), (4, 'c')]
ls_key_sorted = ('a', 'd', 'b', 'e', 'c')
ls_val_sorted = (0, 1, 2, 3, 4)
'''
