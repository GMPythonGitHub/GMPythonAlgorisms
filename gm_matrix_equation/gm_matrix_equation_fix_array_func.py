# gm_matrix_equation_fix_array_func: coded by Kinya MIURA 231104
# ---------------------------------------------------------
print('\n*** Matrix Equation with array func: aa * xx = bb; solve with fixity ***')
# ---------------------------------------------------------
## --- importing item from module ---
from numpy import (array, dot, ix_, linalg, logical_not as loginot)

# =========================================================
## --- setting matrix equation ---
aa1 = array([ [1., 1., 1., 1.], [1., 2., 1., 1.],
              [1., 1., 3., 1.], [1., 1., 1., 4.] ])
bb1 = array([0., 12., 16., 0.])
xx1 = array([1., 0., 0., 4.])
fix_bb1 = [False, True, True, False]
fix_xx1 = [True, False, False, True]
aa2 = array([ [1., 1., 1., 1.], [1., 1., 2., 1.],
              [1., 3., 1., 1.], [4., 1., 1., 1.] ])
bb2 = array([0., 13., 0., 13.])
xx2 = array([0., 2., 0., 4.])
fix_bb2 = [False, True, False, True]
fix_xx2 = [False, True, False, True]
aa, bb, xx, fix_bb, fix_xx = aa1, bb1, xx1, fix_bb1, fix_xx1

# =========================================================
## --- main process --- ##
aa_wk = aa[ix_(fix_bb,loginot(fix_xx))]
bb_wk = bb[fix_bb] - dot(aa[ix_(fix_bb,loginot(fix_xx))], xx[fix_xx])
xx_wk = linalg.solve(aa_wk, bb_wk)  # solving equation
xx[loginot(fix_xx)] = xx_wk
bb = dot(aa, xx)
print(f'{aa = }\n{xx = }\n{bb = }\n{fix_bb = }\n{fix_xx = }')

# =========================================================
# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Matrix Equation with array func: aa * xx = bb; solve with fixity ***
aa = array([[1., 1., 1., 1.], [1., 2., 1., 1.],
    [1., 1., 3., 1.], [1., 1., 1., 4.]])
xx = array([1., 2., 3., 4.])
bb = array([10., 12., 16., 22.])

aa = array([[1., 1., 1., 1.], [1., 1., 2., 1.],
    [1., 3., 1., 1.], [4., 1., 1., 1.]])
xx = array([1., 2., 3., 4.])
bb = array([10., 13., 14., 13.])
'''