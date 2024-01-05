# gm_sort_list.py: coded by Kinya MIURA 231229
# ---------------------------------------------------------
print('*** Sort: list ***')

# =========================================================
## --- sorting list --- ##
lst = [0, 5, 9, 2, 8, 4, 6, 1, 3, 7]
print(f'{lst = }')
print(f'{sorted(lst) = }')
print(f'{sorted(lst, reverse=True) = }')
print(f'{sorted(lst)[:3] = }')
print(f'{sorted(lst, reverse=True)[:3] = }')
lst.sort()
print(f'{lst = }')

print()
## --- conbining key and value --- ##
lsta = ['d', 'a', 'c', 'e', 'b']
print(f'{lsta = }')
lstb = [ 2,   0,   4,   1,   3 ]
print(f'{lstb = }')
lstab = list(zip(lsta, lstb))
print(f'{lstab = }')

print()
## --- sorting 2d list --- ##
lstab_sorted = sorted(lstab, key=lambda x: x[1])  # sorting on lstab[1]
print(f'{lstab_sorted = }')
lsta_sorted, lstb_sorted = zip(*lstab_sorted)
print(f'{lsta_sorted = }')
print(f'{lstb_sorted = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Sort: list ***
lst = [0, 5, 9, 2, 8, 4, 6, 1, 3, 7]
sorted(lst) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sorted(lst, reverse=True) = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
sorted(lst)[:3] = [0, 1, 2]
sorted(lst, reverse=True)[:3] = [9, 8, 7]
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lsta = ['d', 'a', 'c', 'e', 'b']
lstb = [2, 0, 4, 1, 3]
lstab = [('d', 2), ('a', 0), ('c', 4), ('e', 1), ('b', 3)]

lstab_sorted = [('a', 0), ('e', 1), ('d', 2), ('b', 3), ('c', 4)]
lsta_sorted = ('a', 'e', 'd', 'b', 'c')
lstb_sorted = (0, 1, 2, 3, 4)
'''
