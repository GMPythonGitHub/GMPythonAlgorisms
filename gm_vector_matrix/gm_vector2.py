## gm_vector2.py: Coded by Kinya MIURA, 240218

def addv2(va, vb):
    return([va[0]+vb[0], va[1]+vb[1]])
def subv2(va, vb):
    return([va[0]-vb[0], va[1]-vb[1]])
def mulv2(va, vb):
    return([va[0]*vb[0], va[1]*vb[1]])
def divv2(va, vb):
    return([va[0]/vb[0], va[1]/vb[1]])
def tdvv2(v, dev):
    return([v[0]//dev, v[1]//dev])
def modv2(v, mod):
    return([v[0]%mod, v[1]%mod])

def dstv2(va, vb):
    return ((va[0]-vb[0])**2 + (va[1]-vb[1])**2)**0.5
def innerv2(va, vb):
    return va[0]*vb[0] + va[1]*vb[1]
def innervt2(vo, vp, vq):
    return innerv2(subv2(vp, vo), subv2(vq, vo))
def outerv2(va, vb):
    return [
        [va[0]*vb[0], va[0]*vb[1]],
        [va[1]*vb[0], va[1]*vb[1]] ]
def outervt2(vo, vp, vq):
    return outerv2(subv2(vp, vo), subv2(vq, vo))
def crossv2(va, vb):
    return va[0]*vb[1] - va[1]*vb[0]
def crossvt2(vo, vp, vq):
    return crossv2(subv2(vp, vo), subv2(vq, vo))

aa, bb = [1000,1000], [-1000, 1000]
print(f'{addv2(aa,bb) = }\n{subv2(aa,bb) = }\n{mulv2(aa,bb) = }\n{divv2(aa,bb) = }')
print(f'{dstv2(aa,bb) = }\n{innerv2(aa,bb) = }\n{outerv2(aa,bb) = }\n{crossv2(aa,bb) = }')

oo, pp, qq = [1000,1000], [2000,2000], [0, 2000]
print(f'{innervt2(oo,pp,qq) = }\n{outervt2(oo,pp,qq) = }\n{crossvt2(oo,pp,qq) = }')

