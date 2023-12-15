# gm_Example_Matrix_Equation_b1: coded by Kinya MIURA 231104
# -----------------------------------------------------------------------------
print('\n*** Matrix Equation B1: aa * xx = bb; find xx ***')
print('# -----------------------------------------------------------------------------')
from numpy import array
import copy

# -----------------------------------------------------------------------------
aa1 = array([
    [1., 1., 1., 1., 1., 1.],
    [1., 2., 1., 1., 1., 1.],
    [1., 1., 3., 1., 1., 1.],
    [1., 1., 1., 4., 1., 1.],
    [1., 1., 1., 1., 5., 1.],
    [1., 1., 1., 1., 1., 6.] ])
bb1 = array([21., 23., 27., 33., 41., 51.])
aa2 = array([
    [1., 1., 1., 1., 1., 1.],
    [1., 1., 1., 1., 2., 1.],
    [1., 1., 1., 3., 1., 1.],
    [1., 1., 4., 1., 1., 1.],
    [1., 5., 1., 1., 1., 1.],
    [6., 1., 1., 1., 1., 1.] ])
bb2 = array([21., 26., 29., 30., 29., 26.])
xx = array([0., 0., 0., 0., 0., 0.])

aa = copy.deepcopy(aa2)
bb = copy.deepcopy(bb2)
rank = len(aa)
# forward elimination
for i in range(rank):
    for j in range(i+1,rank):  # pivotting partial
        if abs(aa[i,i]) < abs(aa[j,i]):
            aa[i,i:], aa[j,i:] = aa[j,i:], aa[i,i:].copy()
            bb[i], bb[j] = bb[j], bb[i]
    for j in range(i+1,rank):
        ratio = aa[j,i] / aa[i,i]
        aa[j,i:] -= aa[i,i:] * ratio
        bb[j] -= bb[i] * ratio
# backward substitution
for i in range(rank-1,-1,-1):
    for j in range(i-1,-1,-1):
        ratio = aa[j,i] / aa[i,i]
        aa[j,i:] -= aa[i,i:] * ratio
        bb[j] -= bb[i] * ratio
# normalization
for i in range(rank):
    xx[i] = bb[i] / aa[i,i]

print(f'{aa2 = }')
print(f'{bb2 = }')
print(f'{xx = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Matrix Equation B1: aa * xx = bb; find xx ***
# -----------------------------------------------------------------------------
aa2 = array([[1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 2., 1.],
       [1., 1., 1., 3., 1., 1.],
       [1., 1., 4., 1., 1., 1.],
       [1., 5., 1., 1., 1., 1.],
       [6., 1., 1., 1., 1., 1.]])
bb2 = array([21., 26., 29., 30., 29., 26.])
xx = array([1., 2., 3., 4., 5., 6.])
*** Matrix Equation B1: aa * xx = bb; find xx ***
# -----------------------------------------------------------------------------
aa1 = array([[1., 1., 1., 1., 1., 1.],
       [1., 2., 1., 1., 1., 1.],
       [1., 1., 3., 1., 1., 1.],
       [1., 1., 1., 4., 1., 1.],
       [1., 1., 1., 1., 5., 1.],
       [1., 1., 1., 1., 1., 6.]])
bb1 = array([21., 23., 27., 33., 41., 51.])
xx = array([1., 2., 3., 4., 5., 6.])
'''