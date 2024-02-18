## vector.py: Coded by Kinya MIURA, 240210

# a1, a2, a3 = 1, 1, 2
# an = an-1 + an-2 + an-3

N, = map(int, '3'.split())
mod = 10**9 + 7
vct = [2, 1, 1]
mtx = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]



def modv(v, sc):
    return [vi % sc for vi in v]
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

num = N - 3
while num > 0:
    if num % 2 == 1:
        vct = modv(dotmv(mtx, vct), mod)
    mtx = modm(dotmm(mtx, mtx), mod)
    num //= 2
# print(f'{vct = }\n{mtx = }')
print(vct[0])

