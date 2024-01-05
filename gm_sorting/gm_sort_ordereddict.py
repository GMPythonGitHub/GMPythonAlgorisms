# gm_sort_ordereddict.py: coded by Kinya MIURA 231229
# ---------------------------------------------------------
print('*** Sort: ordereddict, collections ***')
# ---------------------------------------------------------
import collections

# =========================================================
## --- creating ordereddict --- ##
lst = [('a', 2), ('e', 1), ('d', 3), ('b', 0), ('c', 4)]
orddct = collections.OrderedDict(lst)
print(f'{orddct = }')

print()
orddct_sorted_key = collections.OrderedDict(
    sorted(orddct.items(), key=lambda x: x[0]) )
print(f'{orddct_sorted_key = }')
orddct_sorted_value = collections.OrderedDict(
    sorted(orddct.items(), key=lambda x: x[1], reverse=True) )
print(f'{orddct_sorted_value = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Sort: ordereddict, collections ***
orddct = OrderedDict([('a', 2), ('e', 1), ('d', 3), ('b', 0), ('c', 4)])

orddct_sorted_key = OrderedDict([('a', 2), ('b', 0), ('c', 4), ('d', 3), ('e', 1)])
orddct_sorted_value = OrderedDict([('c', 4), ('d', 3), ('a', 2), ('e', 1), ('b', 0)])
'''
