# gm_list_counter.py: coded by Kinya MIURA 231229
# ---------------------------------------------------------
print('*** List: counter, collections ***')
# ---------------------------------------------------------
import collections

# =========================================================
## --- main routine --- ##
ls = ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'd', 'd', 'd', 'e']
print(f'{ls = } \n')

counts = collections.Counter(ls)
print(f'{counts = }')
print(f'{counts["a"] = }')
print(f'{counts["b"] = }')
print(f'{counts["c"] = } \n')

print(list(counts.keys()))
print(list(counts.values()))
print(list(counts.items()), '\n')

print(counts.most_common())
print(counts.most_common(2))


# =========================================================
# terminal log / terminal log / terminal log /
'''
*** List: counter, collections ***
ls = ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'd', 'd', 'd', 'e'] 

counts = Counter({'a': 5, 'd': 3, 'b': 2, 'e': 1})
counts["a"] = 5
counts["b"] = 2
counts["c"] = 0 

['a', 'b', 'd', 'e']
[5, 2, 3, 1]
[('a', 5), ('b', 2), ('d', 3), ('e', 1)] 

[('a', 5), ('d', 3), ('b', 2), ('e', 1)]
[('a', 5), ('d', 3)]
'''
