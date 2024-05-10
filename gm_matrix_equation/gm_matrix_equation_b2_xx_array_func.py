# gm_matrix_equation_b2_xx_array_func: coded by Kinya MIURA 231104
# ---------------------------------------------------------
print('\n*** Matrix Equation with array func: aa * xx = bb; find xx ***')
# ---------------------------------------------------------
print('### --- section_module: importing items from module --- ###')
from numpy import (array, linalg)

# =========================================================
print('### --- section_setting --- ###')
aa1 = ( (1, 1, 1, 1), (1, 2, 1, 1),
        (1, 1, 3, 1), (1, 1, 1, 4) )
bb1 = (10, 12, 16, 22)
aa2 = ( (1, 1, 1, 1), (1, 1, 2, 1),
        (1, 3, 1, 1), (4, 1, 1, 1) )
bb2 = (10, 13, 14, 13)
xx = (0, 0, 0, 0)

aa = array(aa1, dtype='float64')
xx = array(xx, dtype='float64')
bb = array(bb1, dtype='float64')

# =========================================================
print('### --- section_solving --- ###')
xx = linalg.solve(aa, bb)  # solving equation
print(f'{aa = }\n{xx = }\n{bb = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Matrix Equation with array func: aa * xx = bb; find xx ***
aa = array([ [1., 1., 1., 1.], [1., 2., 1., 1.],
             [1., 1., 3., 1.], [1., 1., 1., 4.] ])
xx = array([1., 2., 3., 4.])
bb = array([10., 12., 16., 22.])

aa = array([ [1., 1., 1., 1.], [1., 1., 2., 1.],
             [1., 3., 1., 1.], [4., 1., 1., 1.] ])
xx = array([1., 2., 3., 4.])
bb = array([10., 13., 14., 13.])
'''