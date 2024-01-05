# gm_sort_dict.py: coded by Kinya MIURA 231229
# ---------------------------------------------------------
print('*** Sort: dict ***')

# =========================================================
## --- main routine --- ##
lst = [('a', 2), ('e', 1), ('d', 3), ('b', 0), ('c', 4)]
dct = dict(lst)
print(f'{dct = }')

print()
dct_sorted_key = dict(
    sorted(dct.items(), key=lambda x: x[0]) )
print(f'{dct_sorted_key = }')
dct_sorted_value = dict(
    sorted(dct.items(), key=lambda x: x[1], reverse=True) )
print(f'{dct_sorted_value = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Sort: dict ***
dct = {'a': 2, 'e': 1, 'd': 3, 'b': 0, 'c': 4}

dct_sorted_key = {'a': 2, 'b': 0, 'c': 4, 'd': 3, 'e': 1}
dct_sorted_value = {'c': 4, 'd': 3, 'a': 2, 'e': 1, 'b': 0}
'''

