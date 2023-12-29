# gm_list_count: coded by Kinya MIURA 231229
# ---------------------------------------------------------
print('*** List count: counting items ***')

# =========================================================
## --- main routine --- ##
ls = [0, 0, 0, 0, 0, 1, 1, 3, 3, 3, 4]
print(f'{ls = }')

print()
print(f'{ls.count(0) = }')
print(f'{ls.count(1) = }')
print(f'{ls.count(2) = }')

print()
itms = range(6)
conts = [ls.count(itm) for itm in itms]
print(conts)
conts_dic = {itm: ls.count(itm) for itm in itms}
print(conts_dic)

print()
print(f'{conts_dic.keys() = }')
print(f'{conts_dic.values() = }')
print(f'{conts_dic.items() = }')

print()
print(f'{conts_dic[0] = }')
print(f'{conts_dic[1] = }')
print(f'{conts_dic[2] = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** List count: counting items ***
ls = [0, 0, 0, 0, 0, 1, 1, 3, 3, 3, 4]

ls.count(0) = 5
ls.count(1) = 2
ls.count(2) = 0

[5, 2, 0, 3, 1, 0]
{0: 5, 1: 2, 2: 0, 3: 3, 4: 1, 5: 0}

conts_dic.keys() = dict_keys([0, 1, 2, 3, 4, 5])
conts_dic.values() = dict_values([5, 2, 0, 3, 1, 0])
conts_dic.items() = dict_items([(0, 5), (1, 2), (2, 0), (3, 3), (4, 1), (5, 0)])

conts_dic[0] = 5
conts_dic[1] = 2
conts_dic[2] = 0
'''
