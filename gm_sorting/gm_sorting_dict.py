# gm_sorting_dict.py: coded by Kinya MIURA 231229
# ---------------------------------------------------------
print('*** sorting: dict ***')

# =========================================================
## --- creating dict --- ##
lst = [('a', 2), ('e', 1), ('d', 3), ('b', 0), ('c', 4)]
dct = dict(lst)
print(f'dct = dict(lst): {dct = } \n')

## --- sorting dict --- ##
print(f'{sorted(dct) = } \n')

print(f'{dict(sorted(dct.items(), key=lambda x: x[0])) = }')
print(f'{dict(sorted(dct.items(), key=lambda x: x[0], reverse=True)) = }')
print(f'{dict(sorted(dct.items(), key=lambda x: x[1])) = }')
print(f'{dict(sorted(dct.items(), key=lambda x: x[1], reverse=True)) = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** sorting: dict ***
dct = dict(lst): dct = {'a': 2, 'e': 1, 'd': 3, 'b': 0, 'c': 4} 

sorted(dct) = ['a', 'b', 'c', 'd', 'e'] 

dict(sorted(dct.items(), key=lambda x: x[0])) = {'a': 2, 'b': 0, 'c': 4, 'd': 3, 'e': 1}
dict(sorted(dct.items(), key=lambda x: x[0], reverse=True)) = {'e': 1, 'd': 3, 'c': 4, 'b': 0, 'a': 2}
dict(sorted(dct.items(), key=lambda x: x[1])) = {'b': 0, 'e': 1, 'a': 2, 'd': 3, 'c': 4}
dict(sorted(dct.items(), key=lambda x: x[1], reverse=True)) = {'c': 4, 'd': 3, 'a': 2, 'e': 1, 'b': 0}
'''

