# gm_binary_search_list.py: coded by Kinya MIURA 231229
# ---------------------------------------------------------
print('*** binary search: list ***')

# =========================================================
## --- main routine --- ##
lst = [i*i for i in range(10)]
print(f'{lst = } \n')

def bisearch(lst, val):
    aa, bb = 0, len(lst) - 1
    while bb - aa > 1:
        cc = (aa + bb) // 2
        if lst[cc] < val: aa = cc
        elif lst[cc] == val: aa = bb = cc
        else: bb = cc
        # print(f'{aa = }, {cc = }, {bb = }')
        # print(f'{lst[aa] = }, {lst[cc] = }, {lst[bb] = }')
    return aa, bb

val = 30
aa, bb = bisearch(lst, val)
print(f'{aa = }, {bb = }')
print(f'{val = }, {lst[aa] = }, {lst[bb] = }')


# =========================================================
# terminal log / terminal log / terminal log /
'''

'''
