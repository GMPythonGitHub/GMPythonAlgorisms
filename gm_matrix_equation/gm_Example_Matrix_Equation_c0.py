# gm_Example_Matrix_Equation_c0: coded by Kinya MIURA 231104
# -----------------------------------------------------------------------------
print('\n*** Matrix Equation C0: aa * xx = bb; find xx and bb with fixity ***')
print('# -----------------------------------------------------------------------------')
import copy

# -----------------------------------------------------------------------------
aa1 = [
    [1., 1., 1., 1., 1., 1.],
    [1., 2., 1., 1., 1., 1.],
    [1., 1., 3., 1., 1., 1.],
    [1., 1., 1., 4., 1., 1.],
    [1., 1., 1., 1., 5., 1.],
    [1., 1., 1., 1., 1., 6.] ]
bb1 = [0., 23., 27., 0., 0., 51.]
xx1 = [1., 0., 0., 4., 5., 6.]
fix_bb1 = (False, True, True, False, False, True)
fix_xx1 = (True, False, False, True, True, False)
aa2 = [
    [1., 1., 1., 1., 1., 1.],
    [1., 1., 1., 1., 2., 1.],
    [1., 1., 1., 3., 1., 1.],
    [1., 1., 4., 1., 1., 1.],
    [1., 5., 1., 1., 1., 1.],
    [6., 1., 1., 1., 1., 1.] ]
bb2 = [0., 26., 29., 0., 0., 26.]
xx2 = [0., 2., 3., 0., 0., 6.]
fix_bb2 = (False, True, True, False, False, True)
fix_xx2 = (False, True, True, False, False, True)

aa, bb, xx = aa2, bb2, xx2
fix_bb, fix_xx = fix_bb2, fix_xx2
rank = len(bb)
aa_wk, bb_wk = [], []
for i in range(rank):
    if fix_bb[i]:
        aai = []
        for j in range(rank):
            if not fix_xx[j]:
                aai.append(aa[i][j])
        aa_wk.append(aai)
        bbi = bb[i]
        for j in range(rank):
            if fix_xx[j]:
                bbi -= aa[i][j] * xx[j]
        bb_wk.append(bbi)
print(f'{aa_wk = }')
print(f'{bb_wk = }')

rank_wk = len(bb_wk)
# forward elimination
for i in range(rank_wk):
    for j in range(i+1,rank_wk):  # pivotting partial
        if abs(aa_wk[i][i]) < abs(aa_wk[j][i]):
            for k in range(i,rank_wk):
                aa_wk[i][k], aa_wk[j][k] = aa_wk[j][k], aa_wk[i][k]
            bb_wk[i], bb_wk[j] = bb_wk[j], bb_wk[i]
    for j in range(i+1,rank_wk):
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
print(f'{xx_wk = }')
# calculation vectors
jj = 0
for j in range(rank):
    if not fix_xx[j]:
        xx[j] = xx_wk[jj]
        jj += 1
for i in range(rank):
    bb[i] = 0
    for j in range(rank):
        bb[i] += aa[i][j] * xx[j]

print(f'{aa = }')
print(f'{bb = }')
print(f'{xx = }')
print(f'{fix_bb = }')
print(f'{fix_xx = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Matrix Equation C0: aa * xx = bb; find xx and bb with fixity ***
# -----------------------------------------------------------------------------
aa_wk = [[1, 1, 2], [1, 3, 1], [6, 1, 1]]
bb_wk = [15.0, 18.0, 15.0]
xx_wk = [1.0000000000000002, 3.9999999999999996, 5.0]
aa = [[1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1, 1, 1, 1, 2, 1], [1, 1, 1, 3, 1, 1], [1, 1, 4, 1, 1, 1], [1, 5, 1, 1, 1, 1], [6, 1, 1, 1, 1, 1]]
bb = [21.0, 26.0, 29.0, 30.0, 29.0, 26.0]
xx = [1.0000000000000002, 2.0, 3.0, 3.9999999999999996, 5.0, 6.0]
'''