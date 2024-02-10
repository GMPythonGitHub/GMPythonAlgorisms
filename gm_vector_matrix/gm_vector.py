## gm_vector.py: Coded by Kinya MIURA, 240120

def add(va, vb):
    return([va[0]+vb[0], va[1]+vb[1]])
def sub(va, vb):
    return([va[0]-vb[0], va[1]-vb[1]])
def mul(va, vb):
    return([va[0]*vb[0], va[1]*vb[1]])
def div(va, vb):
    return([va[0]/vb[0], va[1]/vb[1]])

def dst(va, vb):
    return ((va[0]-vb[0])**2 + (va[1]-vb[1])**2)**0.5

def dot(va, vb):
    return va[0]*vb[0] + va[1]*vb[1]
def inner3(vo, vp, vq):
    return inner(sub(vp, vo), sub(vq, vo))
def outer(va, vb):
    return [
        [va[0]*vb[0], va[0]*vb[1]],
        [va[1]*vb[0], va[1]*vb[1]] ]
def outer3(vo, vp, vq):
    return outer(sub(vp, vo), sub(vq, vo))
def cross(va, vb):
    return va[0]*vb[1] - va[1]*vb[0]
def cross3(vo, vp, vq):
    return cross(sub(vp, vo), sub(vq, vo))

aa, bb = [10000000,10000000], [-10000000, 10000000]
print(f'{add(aa,bb) = }, {sub(aa,bb) = }, {mul(aa,bb) = }, {div(aa,bb) = }')
print(f'{dst(aa,bb) = }, {inner(aa,bb) = }, {outer(aa,bb) = }, {cross(aa,bb) = }')

oo, pp, qq = [0,0], [10000000,10000000], [-10000000, 10000000]
print(f'{inner3(oo,pp,qq) = }, {outer3(oo,pp,qq) = }, {cross3(oo,pp,qq) = }')

