## gm_vector.py: Coded by Kinya MIURA, 240218

def addv(va, vb):
    if len(va) == len(vb):
        return [vai + vbi for vai, vbi in zip(va, vb)]
    else: return None
def subv(va, vb):
    if len(va) == len(vb):
        return [vai - vbi for vai, vbi in zip(va, vb)]
    else: return None
def mulv(va, vb):
    if len(va) == len(vb):
        return [vai * vbi for vai, vbi in zip(va, vb)]
    else: return None
def divv(va, vb):
    if len(va) == len(vb):
        return [vai / vbi for vai, vbi in zip(va, vb)]
    else: return None
def addvs(v, sc):
    return [vi + sc for vi in v]
def subvs(v, sc):
    return [vi - sc for vi in v]
def mulvs(v, sc):
    return [vi * sc for vi in v]
def divvs(v, sc):
    return [vi / sc for vi in v]
def tdvv(v, sc):
    return [vi // sc for vi in v]
def modv(v, sc):
    return [vi % sc for vi in v]

def dstv(va, vb):
    if len(va) == len(vb):
        return sum([(vbi - vai) ** 2 for vai, vbi in zip(va, vb)]) ** 0.5
    else: return None
def innerv(va, vb):
    if len(va) == len(vb):
        return sum([vai * vbi for vai, vbi in zip(va, vb)])
    else: return None
def innervt(vo, vp, vq):
    return innerv(subv(vp, vo), subv(vq, vo))
def outerv(va, vb):
    return [[vai * vbj for vbj in vb] for vai in va]
def outervt(vo, vp, vq):
    return outerv(subv(vp, vo), subv(vq, vo))

# --------------------

aa, bb = [1000,1000,1000], [-1000, 1000, 2000]
print(f'{aa = }, {bb = }\n')
print(f'{addv(aa,bb) = }\n{subv(aa,bb) = }\n{mulv(aa,bb) = }\n{divv(aa,bb) = }\n')
print(f'{addvs(aa,500) = }\n{subvs(aa,500) = }\n{mulvs(aa,5) = }\n{divvs(aa,5) = }\n')
print(f'{tdvv(aa,7) = }\n{modv(aa,7) = }\n')
print(f'{dstv(aa,bb) = }\n{innerv(aa,bb) = }\n{outerv(aa,bb) = }\n')

# --------------------

oo, pp, qq = [1000,1000,1000], [2000,2000,2000], [0, 2000, 3000]
print(f'{oo = }, {pp = }, {qq = }\n')
print(f'{innervt(oo,pp,qq) = }\n{outervt(oo,pp,qq) = }\n')

