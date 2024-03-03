# gm_sorting_list.py: coded by Kinya MIURA 231229
# ---------------------------------------------------------
print('*** sorting: list ***')

# =========================================================
## --- sorting list --- ##
lst = [0, 5, 9, 2, 8, 4, 6, 1, 3, 7]
print(f'{lst = }')
print(f'{sorted(lst) = }')
print(f'{sorted(lst, reverse=True) = }')
print(f'{sorted(lst)[:3] = }')
print(f'{sorted(lst, reverse=True)[:3] = }')
lst.sort()
print(f'lst.sort(): {lst = } \n')

## --- conbining key and value --- ##
lsta = ['d', 'a', 'c', 'e', 'b']
print(f'{lsta = }')
lstb = [ 2,   0,   4,   1,   3 ]
print(f'{lstb = }')
lstab = list(zip(lsta, lstb))
print(f'lstab = list(zip(lsta, lstb)): {lstab = } \n')

## --- sorting 2d list --- ##
print(f'{sorted(lstab) = }')  # sorting on first items
print(f'{sorted(lstab, key=lambda x: x[0]) = }')  # sorting on lstab[0]
print(f'{sorted(lstab, key=lambda x: x[1]) = }')  # sorting on lstab[1]


# =========================================================
# terminal log / terminal log / terminal log /
'''
*** sorting: list ***
lst = [0, 5, 9, 2, 8, 4, 6, 1, 3, 7]
sorted(lst) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sorted(lst, reverse=True) = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
sorted(lst)[:3] = [0, 1, 2]
sorted(lst, reverse=True)[:3] = [9, 8, 7]
lst.sort(): lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 

lsta = ['d', 'a', 'c', 'e', 'b']
lstb = [2, 0, 4, 1, 3]
lstab = list(zip(lsta, lstb)): lstab = [('d', 2), ('a', 0), ('c', 4), ('e', 1), ('b', 3)] 

sorted(lstab) = [('a', 0), ('b', 3), ('c', 4), ('d', 2), ('e', 1)]
sorted(lstab, key=lambda x: x[0]) = [('a', 0), ('b', 3), ('c', 4), ('d', 2), ('e', 1)]
sorted(lstab, key=lambda x: x[1]) = [('a', 0), ('e', 1), ('d', 2), ('b', 3), ('c', 4)]
'''
