# gm_Example_Matrix_Equation_cnp: coded by Kinya MIURA 231104
# -----------------------------------------------------------------------------
print('\n*** Matrix Equation Cnp: aa * xx = bb; find xx and bb with fixity ***')
print('# -----------------------------------------------------------------------------')
from numpy import (array, dot, ix_, linalg, logical_not as lognot)
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
fix_bb1 = [False, True, True, False, False, True]
fix_xx1 = [True, False, False, True, True, False]
aa2 = array([
    [1., 1., 1., 1., 1., 1.],
    [1., 1., 1., 1., 2., 1.],
    [1., 1., 1., 3., 1., 1.],
    [1., 1., 4., 1., 1., 1.],
    [1., 5., 1., 1., 1., 1.],
    [6., 1., 1., 1., 1., 1.] ])
bb2 = array([0., 26., 29., 0., 0., 26.])
xx2 = array([0., 2., 3., 0., 0., 6.])
fix_bb2 = [False, True, True, False, False, True]
fix_xx2 = [False, True, True, False, False, True]

aa, bb, xx = aa2, bb2, xx2
fix_bb, fix_xx = fix_bb2, fix_xx2

aa_wk = aa[ix_(fix_bb,lognot(fix_xx))]
bb_wk = bb[fix_bb] - dot(aa[ix_(fix_bb,fix_xx)], xx[fix_xx])
# print(f'{aa_wk = }')
# print(f'{bb_wk = }')

xx_wk = linalg.solve(aa_wk, bb_wk)
xx[lognot(fix_xx)] = xx_wk
bb = dot(aa, xx)

print(f'{aa = }')
print(f'{bb = }')
print(f'{xx = }')
print(f'{fix_bb = }')
print(f'{fix_xx = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Matrix Equation Cnp: aa * xx = bb; find xx and bb with fixity ***
# -----------------------------------------------------------------------------
aa_wk = array([[2., 1., 1.],
       [1., 3., 1.],
       [1., 1., 6.]])
bb_wk = array([13., 17., 41.])
aa = array([[1., 1., 1., 1., 1., 1.],
       [1., 2., 1., 1., 1., 1.],
       [1., 1., 3., 1., 1., 1.],
       [1., 1., 1., 4., 1., 1.],
       [1., 1., 1., 1., 5., 1.],
       [1., 1., 1., 1., 1., 6.]])
bb = array([21., 23., 27., 33., 41., 51.])
xx = array([1., 2., 3., 4., 5., 6.])
*** Matrix Equation Cnp: aa * xx = bb; find xx and bb with fixity ***
# -----------------------------------------------------------------------------
aa = array([[1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 2., 1.],
       [1., 1., 1., 3., 1., 1.],
       [1., 1., 4., 1., 1., 1.],
       [1., 5., 1., 1., 1., 1.],
       [6., 1., 1., 1., 1., 1.]])
bb = array([21., 26., 29., 30., 29., 26.])
xx = array([1., 2., 3., 4., 5., 6.])
fix_bb = [False, True, True, False, False, True]
fix_xx = [False, True, True, False, False, True]
'''