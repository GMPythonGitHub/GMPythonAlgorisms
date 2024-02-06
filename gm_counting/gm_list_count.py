# gm_list_counting.py: coded by Kinya MIURA 231229
# ---------------------------------------------------------
print('*** List: count ***')

# =========================================================
## --- main routine --- ##
ls = [0, 0, 0, 0, 0, 1, 1, 3, 3, 3, 4]
print(f'{ls = } \n')

print(f'{ls.count(0) = }')
print(f'{ls.count(1) = }')
print(f'{ls.count(2) = } \n')

itms = range(6)
counts = [ls.count(itm) for itm in itms]
print(counts)
counts_dic = {itm: ls.count(itm) for itm in itms}
print(counts_dic, '\n')

print(f'{counts_dic.keys() = }')
print(f'{counts_dic.values() = }')
print(f'{counts_dic.items() = } \n')

print(f'{counts_dic[0] = }')
print(f'{counts_dic[1] = }')
print(f'{counts_dic[2] = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** List: count ***
ls = [0, 0, 0, 0, 0, 1, 1, 3, 3, 3, 4] 

ls.count(0) = 5
ls.count(1) = 2
ls.count(2) = 0 

[5, 2, 0, 3, 1, 0]
{0: 5, 1: 2, 2: 0, 3: 3, 4: 1, 5: 0} 

counts_dic.keys() = dict_keys([0, 1, 2, 3, 4, 5])
counts_dic.values() = dict_values([5, 2, 0, 3, 1, 0])
counts_dic.items() = dict_items([(0, 5), (1, 2), (2, 0), (3, 3), (4, 1), (5, 0)]) 

counts_dic[0] = 5
counts_dic[1] = 2
counts_dic[2] = 0
'''
