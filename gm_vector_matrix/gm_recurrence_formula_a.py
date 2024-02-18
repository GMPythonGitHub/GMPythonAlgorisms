## vector.py: Coded by Kinya MIURA, 240210

N = map(int, '3'.split())
mod = 10**9 + 7
vct = [1, 1]
mtx = [[2, 1], [1, 0]]

def dotmv(ma, mb):
	if len(ma[0]) == len(mb):
		vct = []
		for mai in ma:
			val = 0
			for maii, mbi in zip(mai, mb):
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

num = N - 2
while num > 0:
	if num % 2 == 1:
		vct = dotmv(mtx, vct)
		vct = [vct[0]%mod, vct[1]%mod]
	mtx = dotmm(mtx, mtx)
	mtx = [[mtx[0][0]%mod, mtx[0][1]%mod], [mtx[1][0]%mod, mtx[1][1]%mod]]
	num //= 2
# print(f'{vct = }\n{mtx = }')
print(vct[0])

