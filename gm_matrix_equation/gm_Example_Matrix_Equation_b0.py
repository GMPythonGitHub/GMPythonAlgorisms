# gm_Example_Matrix_Equation_b0: coded by Kinya MIURA 231104
# -----------------------------------------------------------------------------
print('\n*** Matrix Equation B0: aa * xx = bb; find xx ***')
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
bb1 = [21., 23., 27., 33., 41., 51.]
aa2 = [
    [1., 1., 1., 1., 1., 1.],
    [1., 1., 1., 1., 2., 1.],
    [1., 1., 1., 3., 1., 1.],
    [1., 1., 4., 1., 1., 1.],
    [1., 5., 1., 1., 1., 1.],
    [6., 1., 1., 1., 1., 1.] ]
bb2 = [21., 26., 29., 30., 29., 26.]
xx = [0., 0., 0., 0., 0., 0.]

aa = copy.deepcopy(aa1)
bb = copy.deepcopy(bb1)
rank = len(bb)
# forward elimination
for i in range(rank):
    for j in range(i+1,rank):  # pivotting partial
        if abs(aa[i][i]) < abs(aa[j][i]):
            for k in range(i,rank):
                aa[i][k], aa[j][k] = aa[j][k], aa[i][k]
            bb[i], bb[j] = bb[j], bb[i]
    for j in range(i+1,rank):
        ratio = aa[j][i] / aa[i][i]
        for k in range(i,rank):
            aa[j][k] -= aa[i][k] * ratio
        bb[j] -= bb[i] * ratio

# backward substitution
for i in range(rank-1,-1,-1):
    for j in range(i-1,-1,-1):
        ratio = aa[j][i] / aa[i][i]
        for k in range(i,rank):
            aa[j][k] -= aa[i][k] * ratio
        bb[j] -= bb[i] * ratio
# normalization
for i in range(rank):
    xx[i] = bb[i] / aa[i][i]

print(f'{aa1 = }')
print(f'{bb1 = }')
print(f'{xx = }')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Matrix Equation A0a: aa * xx = bb; find xx ***
# -----------------------------------------------------------------------------
aa1 = [[1, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1], [1, 1, 3, 1, 1, 1], [1, 1, 1, 4, 1, 1], [1, 1, 1, 1, 5, 1], [1, 1, 1, 1, 1, 6]]
bb1 = [21, 23, 27, 33, 41, 51]
xx = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
*** Matrix Equation A0a: aa * xx = bb; find xx ***
# -----------------------------------------------------------------------------
aa2 = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2, 1], [1, 1, 1, 3, 1, 1], [1, 1, 4, 1, 1, 1], [1, 5, 1, 1, 1, 1], [6, 1, 1, 1, 1, 1]]
bb2 = [21, 26, 29, 30, 29, 26]
xx = [1.0, 2.0, 2.9999999999999996, 4.0, 5.000000000000001, 6.000000000000001]
'''