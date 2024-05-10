# gm_matrix_equation_a1_bb_arrray: coded by Kinya MIURA 231104
# ---------------------------------------------------------
print('\n*** Matrix Equation with array: aa * xx = bb; find bb ***')
# ---------------------------------------------------------
print('### --- section_module: importing items from module --- ###')
from numpy import array

# =========================================================
print('### --- section_setting --- ###')
aa1 = ( (1, 1, 1, 1), (1, 2, 1, 1),
        (1, 1, 3, 1), (1, 1, 1, 4) )
aa2 = ( (1, 1, 1, 1), (1, 1, 2, 1),
        (1, 3, 1, 1), (4, 1, 1, 1) )
xx = (1, 2, 3, 4)
bb = (0, 0, 0, 0)

aa = array(aa1, dtype='float64')
xx = array(xx, dtype='float64')
bb = array(bb, dtype='float64')

# =========================================================
print('### --- section_solving --- ###')
for i, aai in enumerate(aa):
    bb[i] = sum(aai * xx)
print(f'{aa = }\n{xx = }\n{bb = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Matrix Equation with array: aa * xx = bb; find bb ***
aa = array( [ [1, 1, 1, 1], [1, 2, 1, 1],
              [1, 1, 3, 1], [1, 1, 1, 4] ] )
xx = array([1, 2, 3, 4])
bb = array([10, 12, 16, 22])

aa = array( [ [1, 1, 1, 1], [1, 1, 2, 1],
              [1, 3, 1, 1], [4, 1, 1, 1] ] )
xx = array([1, 2, 3, 4])
bb = array([10, 13, 14, 13])
'''