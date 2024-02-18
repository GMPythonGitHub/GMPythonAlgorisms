## matrix.py: Coded by Kinya MIURA, 240218

def addm(ma, mb):
    if len(ma) == len(mb) and len(ma[0]) == len(mb[0]):
        return [[maij + mbij for maij, mbij in zip(mai, mbi)] for mai, mbi in zip(ma, mb)]
    else: return None
def subm(ma, mb):
    if len(ma) == len(mb) and len(ma[0]) == len(mb[0]):
        return [[maij - mbij for maij, mbij in zip(mai, mbi)] for mai, mbi in zip(ma, mb)]
    else: return None
def mulm(ma, mb):
    if len(ma) == len(mb) and len(ma[0]) == len(mb[0]):
        return [[maij * mbij for maij, mbij in zip(mai, mbi)] for mai, mbi in zip(ma, mb)]
    else: return None
def divm(ma, mb):
    if len(ma) == len(mb) and len(ma[0]) == len(mb[0]):
        return [[maij / mbij for maij, mbij in zip(mai, mbi)] for mai, mbi in zip(ma, mb)]
    else: return None

def addms(m, sc):
    return [[mij + sc for mij in mi] for mi in m]
def subms(m, sc):
    return [[mij - sc for mij in mi] for mi in m]
def mulms(m, sc):
    return [[mij * sc for mij in mi] for mi in m]
def divms(m, sc):
    return [[mij / sc for mij in mi] for mi in m]

def tdvm(m, sc):
    return [[mij // sc for mij in mi] for mi in m]
def modm(m, sc):
    return [[mij % sc for mij in mi] for mi in m]

def trnm(m):
    return [[m[jj][ii] for jj in range(len(m))] for ii in range(len(m[0]))]
def dotvv(ma, mb):
    if len(ma) == len(mb):
        return sum([mai * mbi for mai, mbi in zip(ma, mb)])
    else: return None
def dotmv(m, v):
    if len(m[0]) == len(v):
        return [dotvv(mi, v) for mi in m]
    else: return None
def dotmm(ma, mb):
    if len(ma[0]) == len(mb):
        mbt = trnm(mb)
        return [[dotvv(mai, mbtj) for mbtj in mbt] for mai in ma]
    else: return None

# --------------------

aa, bb = [[0,1,2],[3,4,5]], [[10,11,12],[13,14,15]]
print(f'{aa = }, {bb = }\n')
print(f'{addm(aa,bb) = }\n{subm(aa,bb) = }\n{mulm(aa,bb) = }\n{divm(aa,bb) = }\n')
print(f'{addms(aa,2) = }\n{subms(aa,2) = }\n{mulms(aa,2) = }\n{divms(aa,2) = }\n')
print(f'{tdvm(aa,3) = }\n{modm(aa,2) = }\n')

# --------------------

pp, qq = [0,1,2], [6,7,8]
print(f'{pp = }. {qq = }')
print(f'{dotvv(pp,qq) = }\n')
pp, qq = [[0,1,2],[3,4,5]], [6,7,8]
print(f'{pp = }. {qq = }')
print(f'{dotmv(pp,qq) = }\n')
pp, qq = [[0,1,2],[3,4,5]], [[6,9],[7,10],[8,11]]
print(f'{pp = }. {qq = }')
print(f'{trnm(pp) = }, {trnm(qq) = }')
print(f'{dotmm(pp,qq) = }')

