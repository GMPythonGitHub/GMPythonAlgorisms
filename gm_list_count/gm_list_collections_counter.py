# gm_list_counter: coded by Kinya MIURA 231229
# ---------------------------------------------------------
print('*** List counter: module collections ***')
# ---------------------------------------------------------
import collections

# =========================================================
## --- main routine --- ##
ls = ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'd', 'd', 'd', 'e']
conts = collections.Counter(ls)

print()
print(f'{conts = }')
print(f'{conts["a"] = }')
print(f'{conts["b"] = }')
print(f'{conts["c"] = }')

print()
print(list(conts.keys()))
print(list(conts.values()))
print(list(conts.items()))

print()
print(conts.most_common())
print(conts.most_common(2))


# =========================================================
# terminal log / terminal log / terminal log /
'''
*** List counter: module collections ***
conts = Counter({'a': 5, 'd': 3, 'b': 2, 'e': 1})

conts["a"] = 5
conts["b"] = 2
conts["c"] = 0

['a', 'b', 'd', 'e']
[5, 2, 3, 1]
[('a', 5), ('b', 2), ('d', 3), ('e', 1)]

[('a', 5), ('d', 3), ('b', 2), ('e', 1)]
[('a', 5), ('d', 3)]
'''
