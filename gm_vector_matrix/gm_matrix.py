## vector.py: Coded by Kinya MIURA, 240210

def add(ma, mb):
    if len(ma) == len(mb) and len(ma[0]) == len(mb[0]):
        return [[ma[i][j]+mb[i][j] for j in range(len(ma[0]))] for i in range(len(ma))]
    else:
        return None
def sub(ma, mb):
    if len(ma) == len(mb) and len(ma[0]) == len(mb[0]):
        return [[ma[i][j]-mb[i][j] for j in range(len(ma[0]))] for i in range(len(ma))]
    else:
        return None
def mul(ma, mb):
    if len(ma) == len(mb) and len(ma[0]) == len(mb[0]):
        return [[ma[i][j]*mb[i][j] for j in range(len(ma[0]))] for i in range(len(ma))]
    else:
        return None
def div(ma, mb):
    if len(ma) == len(mb) and len(ma[0]) == len(mb[0]):
        return [[ma[i][j]/mb[i][j] for j in range(len(ma[0]))] for i in range(len(ma))]
    else:
        return None

def dotvv(ma, mb):
    if len(ma) == len(mb):
        val = 0
        for mai, mbi in zip(ma,mb):
            val += mai * mbi
        return val
    else:
        return None
def dotmv(ma, mb):
    if len(ma[0]) == len(mb):
        vct = []
        for mai in ma:
            val = 0
            for maii, mbi in zip(mai,mb):
                val += maii * mbi
            vct.append(val)
        return vct
    else:
        return None
def dotmm(ma, mb):
    if len(ma[0]) == len(mb):
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

aa, bb = [[0,1,2],[3,4,5]], [[10,11,12],[13,14,15]]
print(f'{add(aa,bb) = }, {sub(aa,bb) = }, {mul(aa,bb) = }, {div(aa,bb) = }')

pp, qq = [0,1,2], [6,7,8]
print(f'{dotvv(pp,qq) = }')
pp, qq = [[0,1,2],[3,4,5]], [6,7,8]
print(f'{dotmv(pp,qq) = }')
pp, qq = [[0,1,2],[3,4,5]], [[6,7],[8,9],[10,11]]
print(f'{dotmm(pp,qq) = }')

