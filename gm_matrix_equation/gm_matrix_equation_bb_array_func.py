# gm_matrix_equation_bb_arrray_func: coded by Kinya MIURA 231104
# ---------------------------------------------------------
print('\n*** Matrix Equation with array func: aa * xx = bb; find bb ***')
# ---------------------------------------------------------

# =========================================================
## --- importing item from module --- ##
from numpy import (array, dot)
## --- setting matrix equation --- ##
aa1 = array([ [1., 1., 1., 1.], [1., 2., 1., 1.],
              [1., 1., 3., 1.], [1., 1., 1., 4.] ])
aa2 = array([ [1., 1., 1., 1.], [1., 1., 2., 1.],
              [1., 3., 1., 1.], [4., 1., 1., 1.] ])
xx = array([1., 2., 3., 4.])
bb = array([0., 0., 0., 0.])
aa = aa2

# =========================================================
## --- main process --- ##
bb = dot(aa, xx)
print(f'{aa = }\n{xx = }\n{bb = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Matrix Equation with array func: aa * xx = bb; find bb ***
aa = array([ [1., 1., 1., 1.], [1., 2., 1., 1.],
             [1., 1., 3., 1.], [1., 1., 1., 4.] ])
xx = array([1., 2., 3., 4.])
bb = array([10., 12., 16., 22.])

aa = array([ [1., 1., 1., 1.], [1., 1., 2., 1.],
             [1., 3., 1., 1.], [4., 1., 1., 1.] ])
xx = array([1., 2., 3., 4.])
bb = array([10., 13., 14., 13.])
'''