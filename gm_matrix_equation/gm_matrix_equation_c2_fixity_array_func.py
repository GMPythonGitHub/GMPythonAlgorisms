# gm_matrix_equation_c2_fixity_array_func: coded by Kinya MIURA 231104
# ---------------------------------------------------------
print('\n*** Matrix Equation with array func: aa * xx = bb; solve with fixity ***')
# ---------------------------------------------------------
## --- importing item from module ---
from numpy import (array, dot, ix_, linalg, logical_not as loginot)

# =========================================================
print('### --- section_setting --- ###')
aa1 = ( (1, 1, 1, 1), (1, 2, 1, 1),
        (1, 1, 3, 1), (1, 1, 1, 4) )
xx1 = (1, 0, 0, 4)
bb1 = (0, 12, 16, 0)
fix_xx1 = (True, False, False, True)
fix_bb1 = (False, True, True, False)
aa2 = ( (1, 1, 1, 1), (1, 1, 2, 1),
        (1, 3, 1, 1), (4, 1, 1, 1) )
xx2 = (0, 2, 0, 4)
bb2 = (0, 13, 0, 13)
fix_xx2 = (False, True, False, True)
fix_bb2 = (False, True, False, True)

aa = array(aa1, dtype='float64')
xx = array(xx1, dtype='float64')
bb = array(bb1, dtype='float64')
fix_xx = fix_xx1
fix_bb = fix_bb1

# =========================================================
print('### --- section_solving --- ###')
aa_wk = aa[ix_(fix_bb,loginot(fix_xx))]
bb_wk = bb[ix_(fix_bb)] - dot(aa[ix_(fix_bb,fix_xx)], xx[ix_(fix_xx)])
xx_wk = linalg.solve(aa_wk, bb_wk)  # solving equation
xx[ix_(loginot(fix_xx))] = xx_wk
bb = dot(aa, xx)
print(f'{aa = }\n{xx = }\n{bb = }\n{fix_bb = }\n{fix_xx = }')

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