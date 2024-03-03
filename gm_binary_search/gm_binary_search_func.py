# gm_binary_search_list.py: coded by Kinya MIURA 240302
# ---------------------------------------------------------
print('*** binary search: func ***')

# =========================================================
## --- main routine --- ##
def func(x):
    return x * x
lst = [i*i for i in range(10)]
print(f'{lst = } \n')

aa, bb = 0, 10
val = 16

while bb - aa > 0.01:
    cc = (aa + bb) / 2
    if func(cc) < val:
        aa = cc
    else:
        bb = cc
    print(f'{aa = }, {cc = }, {bb = }')
    print(f'{func(aa) = }, {func(cc) = }, {func(bb) = }')

print(f'{aa = }, {cc = }, {bb = }')
print(f'{func(aa) = }, {func(cc) = }, {func(bb) = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''

'''
