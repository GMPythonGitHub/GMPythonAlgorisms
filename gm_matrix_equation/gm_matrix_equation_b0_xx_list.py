# gm_matrix_equation_b0_xx_list: coded by Kinya MIURA 231104
# ---------------------------------------------------------
print('\n*** Matrix Equation with list: aa * xx = bb; find xx ***')
# ---------------------------------------------------------
print('### --- section_module: importing items from module --- ###')
import copy

# =========================================================
print('### --- section_setting --- ###')
aa1 = [ [1, 1, 1, 1], [1, 2, 1, 1],
        [1, 1, 3, 1], [1, 1, 1, 4] ]
bb1 = [10, 12, 16, 22]
aa2 = [ [1, 1, 1, 1], [1, 1, 2, 1],
        [1, 3, 1, 1], [4, 1, 1, 1] ]
bb2 = [10, 13, 14, 13]
xx = [0., 0., 0., 0.]

aa, bb = aa1, bb1
rank = len(bb)

# =========================================================
print('### --- section_solving --- ###')
aa_wk = copy.deepcopy(aa)
bb_wk = copy.deepcopy(bb)
# forward elimination with pivoting
for i in range(rank):
    for j in range(i+1,rank):  # pivoting partial
        if abs(aa_wk[i][i]) < abs(aa_wk[j][i]):
            for k in range(i,rank):
                aa_wk[i][k], aa_wk[j][k] = aa_wk[j][k], aa_wk[i][k]
            bb_wk[i], bb_wk[j] = bb_wk[j], bb_wk[i]
    for j in range(i+1,rank):  # eliminating
        ratio = aa_wk[j][i] / aa_wk[i][i]
        for k in range(i,rank):
            aa_wk[j][k] -= aa_wk[i][k] * ratio
        bb_wk[j] -= bb_wk[i] * ratio
# backward substitution
for i in range(rank-1,-1,-1):
    for j in range(i-1,-1,-1):
        ratio = aa_wk[j][i] / aa_wk[i][i]
        for k in range(i,rank):
            aa_wk[j][k] -= aa_wk[i][k] * ratio
        bb_wk[j] -= bb_wk[i] * ratio
# normalization
for i in range(rank):
    xx[i] = bb_wk[i] / aa_wk[i][i]
print(f'{aa = }\n{xx = }\n{bb = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Matrix Equation with list: aa * xx = bb; find xx ***
aa = [ [1.0, 1.0, 1.0, 1.0], [1.0, 2.0, 1.0, 1.0], 
       [1.0, 1.0, 3.0, 1.0], [1.0, 1.0, 1.0, 4.0] ]
xx = [1.0, 2.0, 3.0, 4.0]
bb = [10.0, 12.0, 16.0, 22.0]

aa = [ [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 2.0, 1.0], 
       [1.0, 3.0, 1.0, 1.0], [4.0, 1.0, 1.0, 1.0] ]
xx = [1.0, 1.9999999999999998, 3.0000000000000004, 4.000000000000001]
bb = [10.0, 13.0, 14.0, 13.0]
'''