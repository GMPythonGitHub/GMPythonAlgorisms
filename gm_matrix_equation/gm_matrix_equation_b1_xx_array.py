# gm_matrix_equation_b1_xx_array: coded by Kinya MIURA 231104
# ---------------------------------------------------------
print('\n*** Matrix Equation with array: aa * xx = bb; find xx ***')
# ---------------------------------------------------------
## --- importing item from module --- ##
from numpy import (array, diag)
import copy

# =========================================================
## --- setting matrix equation --- ##
aa1 = array([ [1., 1., 1., 1.], [1., 2., 1., 1.],
              [1., 1., 3., 1.], [1., 1., 1., 4.] ])
bb1 = array([10., 12., 16., 22.])
aa2 = array([ [1., 1., 1., 1.], [1., 1., 2., 1.],
              [1., 3., 1., 1.], [4., 1., 1., 1.] ])
bb2 = array([10., 13., 14., 13.])
xx = array([0., 0., 0., 0.])
aa, bb = aa2, bb2
rank = len(bb)

# =========================================================
## --- main process --- ##
aa_wk = copy.deepcopy(aa)
bb_wk = copy.deepcopy(bb)
# forward elimination with pivoting
for i in range(rank):
    for j in range(i+1,rank):  # pivoting partial
        if abs(aa_wk[i,i]) < abs(aa_wk[j,i]):
            aa_wk[i,i:], aa_wk[j,i:] = aa_wk[j,i:], copy.copy(aa_wk[i,i:])
            bb_wk[i], bb_wk[j] = bb_wk[j], bb_wk[i]
    for j in range(i+1,rank):  # eliminating
        ratio = aa_wk[j,i] / aa_wk[i,i]
        aa_wk[j,i:] -= aa_wk[i,i:] * ratio
        bb_wk[j] -= bb_wk[i] * ratio
# backward substitution
for i in range(rank-1,-1,-1):
    for j in range(i-1,-1,-1):
        ratio = aa_wk[j,i] / aa_wk[i,i]
        aa_wk[j,i:] -= aa_wk[i,i:] * ratio
        bb_wk[j] -= bb_wk[i] * ratio
# normalization
xx = bb_wk / diag(aa_wk)
print(f'{aa = }\n{xx = }\n{bb = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Matrix Equation with array: aa * xx = bb; find xx ***
aa = array([[1., 1., 1., 1.], [1., 2., 1., 1.],
    [1., 1., 3., 1.], [1., 1., 1., 4.]])
xx = array([1., 2., 3., 4.])
bb = array([10., 12., 16., 22.])
aa = array([[1., 1., 1., 1.], [1., 1., 2., 1.],
    [1., 3., 1., 1.], [4., 1., 1., 1.]])
xx = array([1., 2., 3., 4.])
bb = array([10., 13., 14., 13.])
'''