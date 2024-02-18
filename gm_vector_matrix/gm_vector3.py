## gm_vector3.py: Coded by Kinya MIURA, 240218

def addv3(va, vb):
    return([va[0]+vb[0], va[1]+vb[1], va[2]+vb[2]])
def subv3(va, vb):
    return([va[0]-vb[0], va[1]-vb[1], va[2]-vb[2]])
def mulv3(va, vb):
    return([va[0]*vb[0], va[1]*vb[1], va[2]*vb[2]])
def divv3(va, vb):
    return([va[0]/vb[0], va[1]/vb[1], va[2]/vb[2]])
def tdvv3(v, dev):
    return([v[0]//dev, v[1]//dev, v[2]//dev])
def modv3(v, mod):
    return([v[0]%mod, v[1]%mod, v[2]%mod])

def dstv3(va, vb):
    return ((va[0]-vb[0])**2 + (va[1]-vb[1])**2 + (va[2]-vb[2])**2)**0.5
def innerv3(va, vb):
    return va[0]*vb[0] + va[1]*vb[1] + va[2]*vb[2]
def innervt3(vo, vp, vq):
    return innerv3(subv3(vp, vo), subv3(vq, vo))
def outerv3(va, vb):
    return [
        [va[0]*vb[0], va[0]*vb[1], va[0]*vb[2]],
        [va[1]*vb[0], va[1]*vb[1], va[1]*vb[2]],
        [va[2]*vb[0], va[2]*vb[1], va[2]*vb[2]] ]
def outervt3(vo, vp, vq):
    return outerv3(subv3(vp, vo), subv3(vq, vo))
def crossv3(va, vb):
    return [
        va[1]*vb[2] - va[2]*vb[1],
        va[2]*vb[0] - va[0]*vb[2],
        va[0]*vb[1] - va[1]*vb[0] ]

def crossvt3(vo, vp, vq):
    return crossv3(subv3(vp, vo), subv3(vq, vo))

aa, bb = [1000,1000,1000], [-1000, 1000, 2000]
print(f'{addv3(aa,bb) = }\n{subv3(aa,bb) = }\n{mulv3(aa,bb) = }\n{divv3(aa,bb) = }')
print(f'{dstv3(aa,bb) = }\n{innerv3(aa,bb) = }\n{outerv3(aa,bb) = }\n{crossv3(aa,bb) = }')

oo, pp, qq = [1000,1000,1000], [2000,2000,2000], [0, 2000, 3000]
print(f'{innervt3(oo,pp,qq) = }\n{outervt3(oo,pp,qq) = }\n{crossvt3(oo,pp,qq) = }')

