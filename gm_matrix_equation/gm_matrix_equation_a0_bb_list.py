# gm_matrix_equation_a0_bb_list: coded by Kinya MIURA 231104
# ---------------------------------------------------------
print('*** Matrix Equation with list: aa * xx = bb; find bb ***')

# =========================================================
print('### --- section_setting --- ###')
aa1 = [ [1, 1, 1, 1], [1, 2, 1, 1],
        [1, 1, 3, 1], [1, 1, 1, 4] ]
aa2 = [ [1, 1, 1, 1], [1, 1, 2, 1],
        [1, 3, 1, 1], [4, 1, 1, 1] ]
xx = [1, 2, 3, 4]
bb = [0, 0, 0, 0]
aa = aa1
rank = len(bb)

# =========================================================
print('### --- section_solving --- ###')
for i in range(rank):
    bb[i] = 0
    for j in range(rank):
        bb[i] += aa[i][j] * xx[j]
print(f'{aa = }\n{xx = }\n{bb = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Matrix Equation with list: aa * xx = bb; find bb ***
### --- section setting --- ###
### --- section solving --- ###
aa = ((1, 1, 1, 1), (1, 2, 1, 1), (1, 1, 3, 1), (1, 1, 1, 4))
xx = [1, 2, 3, 4]
bb = [10, 12, 16, 22]

aa = ((1, 1, 1, 1), (1, 1, 2, 1), (1, 3, 1, 1), (4, 1, 1, 1))
xx = [1, 2, 3, 4]
bb = [10, 13, 14, 13]
'''