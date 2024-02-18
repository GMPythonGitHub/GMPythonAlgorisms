## matrix.py: Coded by Kinya MIURA, 240218

def addm(ma, mb):
    if len(ma) == len(mb) and len(ma[0]) == len(mb[0]):
        return [[maij + mbij for maij, mbij in zip(mai, mbi)] for mai, mbi in zip(ma, mb)]
    else:
        return None
def subm(ma, mb):
    if len(ma) == len(mb) and len(ma[0]) == len(mb[0]):
        return [[maij - mbij for maij, mbij in zip(mai, mbi)] for mai, mbi in zip(ma, mb)]
    else:
        return None
def mulm(ma, mb):
    if len(ma) == len(mb) and len(ma[0]) == len(mb[0]):
        return [[maij * mbij for maij, mbij in zip(mai, mbi)] for mai, mbi in zip(ma, mb)]
    else:
        return None
def divm(ma, mb):
    if len(ma) == len(mb) and len(ma[0]) == len(mb[0]):
        return [[maij / mbij for maij, mbij in zip(mai, mbi)] for mai, mbi in zip(ma, mb)]
    else:
        return None
def addms(m, sc):
    return [[mij + sc for mij in mi] for mi in m]
def subms(m, sc):
    return [[mij - sc for mij in mi] for mi in m]
def mulms(m, sc):
    return [[mij * sc for mij in mi] for mi in m]
def divms(m, sc):
    return [[mij / sc for mij in mi] for mi in m]
def tdvms(m, sc):
    return [[mij // sc for mij in mi] for mi in m]
def modms(m, sc):
    return [[mij % sc for mij in mi] for mi in m]

def dotvv(ma, mb):
    if len(ma) == len(mb):
        return sum([mai * mbi for mai, mbi in zip(ma, mb)])
    else:
        return None
def dotmv(m, v):
    if len(m[0]) == len(v):
        return [dotvv(mi, v) for mi in m]
    else:
        return None
def dotmm(ma, mb):
    if len(ma[0]) == len(mb):
        return [[dotvv(mai, [mbi[ii] for mbi in mb]) for ii, mai in enumerate(ma)]



        mtx = []
        for i in range(len(ma)):
            vct = []
            for j in range(len(mb[0])):
                val = 0
                for k in range(len(ma[0])):
                    val += ma[i][k] * mb[k][j]
                vct.append(val)
            mtx.append(vct)
        return mtx
    else:
        return None

# --------------------

aa, bb = [[0,1,2],[3,4,5]], [[10,11,12],[13,14,15]]
print(f'{aa = }, {bb = }\n')
print(f'{addm(aa,bb) = }\n{subm(aa,bb) = }\n{mulm(aa,bb) = }\n{divm(aa,bb) = }\n')

# --------------------

pp, qq = [0,1,2], [6,7,8]
print(f'{dotvv(pp,qq) = }')
pp, qq = [[0,1,2],[3,4,5]], [6,7,8]
print(f'{dotmv(pp,qq) = }')
pp, qq = [[0,1,2],[3,4,5]], [[6,7],[8,9],[10,11]]
print(f'{dotmm(pp,qq) = }')

