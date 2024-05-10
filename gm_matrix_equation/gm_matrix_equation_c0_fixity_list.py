# gm_matrix_equation_c0_fixity_list: coded by Kinya MIURA 231104
# ---------------------------------------------------------
print('\n*** Matrix Equation with list: aa * xx = bb; solve with fixity ***')
# ---------------------------------------------------------

# =========================================================
print('### --- section_setting --- ###')
aa1 = [ [1, 1, 1, 1], [1, 2, 1, 1],
        [1, 1, 3, 1], [1, 1, 1, 4] ]
xx1 = [1, 0, 0, 4]
bb1 = [0, 12, 16, 0]
fix_xx1 = (True, False, False, True)
fix_bb1 = (False, True, True, False)
aa2 = [ [1, 1, 1, 1], [1, 1, 2, 1],
        [1, 3, 1, 1], [4, 1, 1, 1] ]
xx2 = [0, 2, 0, 4]
bb2 = [0, 13, 0, 13]
fix_bb2 = (False, True, False, True)
fix_xx2 = (False, True, False, True)

aa = aa1
xx = xx1
bb = bb1
fix_xx = fix_xx1
fix_bb = fix_bb1
rank = len(bb)

# =========================================================
print('### --- section_solving --- ###')
# setting working space
aa_wk, bb_wk = [], []
for i in range(rank):
    if fix_bb[i]:
        aai = []
        for j in range(rank):
            if not fix_xx[j]: aai.append(aa[i][j])
        aa_wk.append(aai)
        bbi = bb[i]
        for j in range(rank):
            if fix_xx[j]: bbi -= aa[i][j] * xx[j]
        bb_wk.append(bbi)
rank_wk = len(bb_wk)
# forward elimination with pivoting
for i in range(rank_wk):
    for j in range(i+1,rank_wk):  # pivoting partial
        if abs(aa_wk[i][i]) < abs(aa_wk[j][i]):
            for k in range(i,rank_wk):
                aa_wk[i][k], aa_wk[j][k] = aa_wk[j][k], aa_wk[i][k]
            bb_wk[i], bb_wk[j] = bb_wk[j], bb_wk[i]
    for j in range(i+1,rank_wk):  # eliminating
        ratio = aa_wk[j][i] / aa_wk[i][i]
        for k in range(i,rank_wk):
            aa_wk[j][k] -= aa_wk[i][k] * ratio
        bb_wk[j] -= bb_wk[i] * ratio
# backward substitution
for i in range(rank_wk-1,-1,-1):
    for j in range(i-1,-1,-1):
        ratio = aa_wk[j][i] / aa_wk[i][i]
        for k in range(i,rank_wk):
            aa_wk[j][k] -= aa_wk[i][k] * ratio
        bb_wk[j] -= bb_wk[i] * ratio
# normalization
xx_wk = []
for i in range(rank_wk):
    xx_wk.append(bb_wk[i] / aa_wk[i][i])
# calculating vectors
jj = 0
for j in range(rank):
    if not fix_xx[j]:
        xx[j] = xx_wk[jj]
        jj += 1
for i in range(rank):
    bb[i] = 0
    for j in range(rank):
        bb[i] += aa[i][j] * xx[j]
print(f'{aa = }\n{xx = }\n{bb = }\n{fix_bb = }\n{fix_xx = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Matrix Equation with list: aa * xx = bb; solve with fixity ***
aa = [ [1.0, 1.0, 1.0, 1.0], [1.0, 2.0, 1.0, 1.0], 
       [1.0, 1.0, 3.0, 1.0], [1.0, 1.0, 1.0, 4.0] ]
xx = [1.0, 2.0, 3.0, 4.0]
bb = [10.0, 12.0, 16.0, 22.0]
fix_bb = (False, True, True, False)
fix_xx = (True, False, False, True)

aa = [ [1.0, 1.0, 1.0, 1.0], [1.0, 2.0, 1.0, 1.0], 
       [1.0, 1.0, 3.0, 1.0], [1.0, 1.0, 1.0, 4.0] ]
xx = [1.0, 2.0, 3.0, 4.0]
bb = [10.0, 12.0, 16.0, 22.0]
fix_bb = (False, True, True, False)
fix_xx = (True, False, False, True)
'''