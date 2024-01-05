# gm_list.py: coded by Kinya MIURA 231229
# ---------------------------------------------------------
print('*** list ***')

# =========================================================
## --- creating list --- ##
lst = [0, 5, 9, 2, 8, 4, 6, 1, 3, 7]  # defining list
print(f'{lst = }')
lst = list((0, 5, 9, 2, 8, 4, 6, 1, 3, 7))  # constructor of list
print(f'{lst = }')
print()
lst = list(range(10))  # using generator
print(f'{lst = }')
lst = list(range(1,11))
print(f'{lst = }')
lst = list(range(1,11,2))
print(f'{lst = }')

print()
## --- slicing --- ##
lsts = list(range(10))
print(lsts, lsts[0], lsts[2], lsts[-1])  # single element
print(lsts[4:], lsts[:4], lsts[2:7], lsts[2:7:2])  # elements in a range wth step
print(lsts[::2], lsts[::-1])  # elements with step

print()
## --- arithmetic operation --- ##
lsta, lstb = [0, 1, 2], [3, 4, 5]
print(f'{lsta = }, {lstb = }')
print(f'{lsta + lstb = }')
print(f'{lsta + [3] = }')
print(f'{lsta * 3 = }')

print()
## --- append() --- ##
lstap1 = []
for i in range(10):
    lstap1.append(i)
print(f'{lstap1 = }')
lstap2 = [0, 1, 2]
lstap2.append([3, 4, 5])
print(f'{lstap2 = }')

print()
## --- extend() --- ##
lstet1 = [0, 1, 2]
lstet1.extend([3, 4, 5])
print(f'{lstet1 = }')
lstet2 = [[0, 1, 2, 3,], [4, 5,], [6], [7, 8,]]
lstet3 = []
for lstet2i in lstet2:
    lstet3.extend(lstet2i)
print(f'{lstet3 = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** list ***
lst = [0, 5, 9, 2, 8, 4, 6, 1, 3, 7]
lst = [0, 5, 9, 2, 8, 4, 6, 1, 3, 7]

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst = [1, 3, 5, 7, 9]

lsta = [0, 1, 2], lstb = [3, 4, 5]
lsta + lstb = [0, 1, 2, 3, 4, 5]
lsta + [3] = [0, 1, 2, 3]
lsta * 3 = [0, 1, 2, 0, 1, 2, 0, 1, 2]

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 0 2 9
[4, 5, 6, 7, 8, 9] [0, 1, 2, 3] [2, 3, 4, 5, 6] [2, 4, 6]
[0, 2, 4, 6, 8] [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

lstap1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lstap2 = [0, 1, 2, [3, 4, 5]]

lstet1 = [0, 1, 2, 3, 4, 5]
lstet3 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
'''
