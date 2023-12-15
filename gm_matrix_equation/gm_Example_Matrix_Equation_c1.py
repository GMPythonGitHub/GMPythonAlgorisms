# gm_Example_Matrix_Equation_c1: coded by Kinya MIURA 231104
# -----------------------------------------------------------------------------
print('\n*** Matrix Equation C1: aa * xx = bb; find xx and bb with fixity ***')
print('# -----------------------------------------------------------------------------')
from numpy import (array, diag)
import copy

# -----------------------------------------------------------------------------
aa1 = array([
    [1., 1., 1., 1., 1., 1.],
    [1., 2., 1., 1., 1., 1.],
    [1., 1., 3., 1., 1., 1.],
    [1., 1., 1., 4., 1., 1.],
    [1., 1., 1., 1., 5., 1.],
    [1., 1., 1., 1., 1., 6.] ])
bb1 = array([0., 23., 27., 0., 0., 51.])
xx1 = array([1., 0., 0., 4., 5., 6.])
fix_bb1 = (False, True, True, False, False, True)
fix_xx1 = (True, False, False, True, True, False)
aa2 = array([
    [1., 1., 1., 1., 1., 1.],
    [1., 1., 1., 1., 2., 1.],
    [1., 1., 1., 3., 1., 1.],
    [1., 1., 4., 1., 1., 1.],
    [1., 5., 1., 1., 1., 1.],
    [6., 1., 1., 1., 1., 1.] ])
bb2 = array([0., 26., 29., 0., 0., 26.])
xx2 = array([0., 2., 3., 0., 0., 6.])
fix_bb2 = (False, True, True, False, False, True)
fix_xx2 = (False, True, True, False, False, True)

aa, bb, xx = aa2, bb2, xx2
fix_bb, fix_xx = fix_bb2, fix_xx2
rank = len(bb)
bb_fix, bb_fre = [], []
for i, fix_bbi in enumerate(fix_bb):
    if fix_bbi:
        bb_fix.append(i)
    else:
        bb_fre.append(i)
xx_fix, xx_fre = [], []
for i, fix_xxi in enumerate(fix_xx):
    if fix_xxi:
        xx_fix.append(i)
    else:
        xx_fre.append(i)
aa_wk, bb_wk = [], []
for aai, bbi in zip(aa[bb_fix,:],bb[bb_fix]):
    aa_wk.append(aai[xx_fre])
    bb_wk.append(bbi-sum(aai[xx_fix] * xx[xx_fix]))
aa_wk, bb_wk = array(aa_wk), array(bb_wk)

rank_wk = len(bb_wk)
# forward elimination
for i in range(rank_wk):
    for j in range(i+1,rank_wk):  # pivotting partial
        if abs(aa_wk[i,i]) < abs(aa_wk[j,i]):
            aa_wk[i,i:], aa_wk[j,i:] = aa_wk[j,i:], aa_wk[i,i:].copy()
            bb_wk[i], bb_wk[j] = bb_wk[j], bb_wk[i]
    for j in range(i+1,rank_wk):
        ratio = aa_wk[j,i] / aa_wk[i,i]
        aa_wk[j,i:] -= aa_wk[i,i:] * ratio
        bb_wk[j] -= bb_wk[i] * ratio
# backward substitution
for i in range(rank_wk-1,-1,-1):
    for j in range(i-1,-1,-1):
        ratio = aa_wk[j,i] / aa_wk[i,i]
        aa_wk[j,i:] -= aa_wk[i,i:] * ratio
        bb_wk[j] -= bb_wk[i] * ratio
# normalization
xx_wk = bb_wk / diag(aa_wk)

# calculation vectors
jj = 0
for j, xx_frej in enumerate(xx_fre):
    xx[xx_frej] = xx_wk[j]
for i, aai in enumerate(aa):
    bb[i] = sum(aai * xx)

print(f'{aa = }')
print(f'{bb = }')
print(f'{xx = }')
print(f'{fix_bb = }')
print(f'{fix_xx = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Matrix Equation C1: aa * xx = bb; find xx and bb with fixity ***
# -----------------------------------------------------------------------------
aa = array([[1., 1., 1., 1., 1., 1.],
       [1., 2., 1., 1., 1., 1.],
       [1., 1., 3., 1., 1., 1.],
       [1., 1., 1., 4., 1., 1.],
       [1., 1., 1., 1., 5., 1.],
       [1., 1., 1., 1., 1., 6.]])
bb = array([21., 23., 27., 33., 41., 51.])
xx = array([1., 2., 3., 4., 5., 6.])
fix_bb = (False, True, True, False, False, True)
fix_xx = (True, False, False, True, True, False)
*** Matrix Equation C1: aa * xx = bb; find xx and bb with fixity ***
# -----------------------------------------------------------------------------
aa = array([[1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 2., 1.],
       [1., 1., 1., 3., 1., 1.],
       [1., 1., 4., 1., 1., 1.],
       [1., 5., 1., 1., 1., 1.],
       [6., 1., 1., 1., 1., 1.]])
bb = array([21., 26., 29., 30., 29., 26.])
xx = array([1., 2., 3., 4., 5., 6.])
fix_bb = (False, True, True, False, False, True)
fix_xx = (False, True, True, False, False, True)
'''