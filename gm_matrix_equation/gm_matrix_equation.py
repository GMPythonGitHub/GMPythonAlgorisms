# gm_matrix_equation.py: coded by Kinya MIURA 230418
# ---------------------------------------------------------
print('*** class GMMatrixEq: solving matrix equation ***')
# ---------------------------------------------------------
print('### --- section_module: (GMMatrixEq) importing items from, module --- ###')
from numpy import (
    ndarray, array, dot, ix_, linalg, logical_not as loginot)

# =========================================================
print('### --- section_class: (GMMatrixEq) declaring class --- ###')
class GMMatrixEq():
    ## --- section_a: initializing class instance --- ##
    def __init__(self,
            aa: tuple = ((1., 1., 1.), (1., 2., 1.), (1., 1., 3.)),
            xx: tuple = (1., 2., 3.),
            bb: tuple = (6., 8., 12.),
            fixxx: tuple = None, fixbb: tuple = None) -> None:
        self._aa, self._xx, self._bb = None, None, None
        self._fixxx, self._fixbb = None, None
        self.set_matrix_eq(
            aa=aa, xx=xx, bb=bb, fixxx=fixxx, fixbb=fixbb)
    ## --- section_b: setting functions --- ##
    def set_matrix_eq(self,
            aa: tuple = None, xx: tuple = None, bb: tuple = None,
            fixxx: tuple = None, fixbb: tuple = None) -> None:
        if aa is not None:
            self._aa = array(aa)
            self._fixbb = (True,) * len(self._aa)
            self._fixxx = (False,) * len(self._aa)
        if xx is not None: self._xx = array(xx)
        if bb is not None: self._bb = array(bb)
        if fixxx is not None: self._fixxx = tuple(fixxx)
        if fixbb is not None: self._fixbb = tuple(fixbb)
    ## --- section_c: getting functions --- ##
    def aa(self) -> ndarray: return self._aa
    def xx(self) -> ndarray: return self._xx
    def bb(self) -> ndarray: return self._bb
    def fixxx(self) -> tuple: return self._fixxx
    def fixbb(self) -> tuple: return self._fixbb
    ## --- section_d: string function for print() --- ##
    def __str__(self) -> str:
        return (
            f'(GMMatrixEq): \n'
            f'    aa = {self._aa}\n    xx = {self._xx}\n    bb = {self._bb}\n'
            f'    fixxx = {self._fixxx}\n    fixbb = {self._fixbb}' )
    ## --- section_e: solving matrix equation --- ##
    def solve(self) -> None:
        if all(self._fixbb):
            self._xx = linalg.solve(self._aa, self._bb)
        elif any(self._fixbb):
            aa_wk = self._aa[ix_(self._fixbb, loginot(self._fixxx))]
            bb_wk = self._bb[ix_(self._fixbb)]
            bb_wk -= dot(
                self._aa[ix_(self._fixbb, self._fixxx)],
                self._xx[ix_(self._fixxx)] )
            xx_wk = linalg.solve(aa_wk, bb_wk)  # solving equation
            self._xx[loginot(self._fixxx)] = xx_wk
            self._bb[loginot(self._fixbb)] = dot(
                self._aa[ix_(loginot(self._fixbb))], self._xx)
        else:
            self._bb = dot(self._aa, self._xx)

# =========================================================
if __name__ == '__main__':
    print('### --- section_main: (GMMatrixEq) main process --- ###')
    ## --- section_m0: setting matrix equation --- ##
    rank = ('4x4', '6x6')[1]
    type = ('type-1', 'type-2')[1]
    fixc = ('xx', 'bb', 'fix')[2]
    if rank == '4x4':
        if type == 'type-1':
            aa = ( (1., 1., 1., 1.), (1., 2., 1., 1.),
                   (1., 1., 3., 1.), (1., 1., 1., 4.))
            if fixc == 'xx':
                xx = (1., 2., 3., 4.)
                bb = (0., 0., 0., 0.)
                fixxx = (True, True, True, True)
                fixbb = (False, False, False, False)
            elif fixc == 'bb':
                xx = (0., 0., 0., 0.)
                bb = (10., 12., 16., 22.)
                fixxx = (False, False, False, False)
                fixbb = (True, True, True, True)
            elif fixc == 'fix':
                xx = (1., 0., 0., 4.)
                bb = (0., 12., 16., 0.)
                fixxx = (True, False, False, True)
                fixbb = (False, True, True, False)
        elif type == 'type-2':
            aa = ( (1., 1., 1., 1.), (1., 1., 2., 1.),
                   (1., 3., 1., 1.), (4., 1., 1., 1.))
            if fixc == 'xx':
                xx = (1., 2., 3., 4.)
                bb = (0., 0., 0., 0.)
                fixxx = (True, True, True, True)
                fixbb = (False, False, False, False)
            elif fixc == 'bb':
                xx = (0., 0., 0., 0.)
                bb = (10., 12., 16., 22.)
                fixxx = (False, False, False, False)
                fixbb = (True, True, True, True)
            elif fixc == 'fix':
                xx = (0., 2., 0., 4.)
                bb = (0., 13., 0., 13.)
                fixxx = (False, True, False, True)
                fixbb = (False, True, False, True)
    elif rank == '6x6':
        if type == 'type-1':
            aa = ( (1., 1., 1., 1., 1., 1.), (1., 2., 1., 1., 1., 1.),
                   (1., 1., 3., 1., 1., 1.), (1., 1., 1., 4., 1., 1.),
                   (1., 1., 1., 1., 5., 1.), (1., 1., 1., 1., 1., 6.) )
            if fixc == 'xx':
                xx = (1., 2., 3., 4., 5., 6.)
                bb = (0., 0., 0., 0., 0., 0.)
                fixxx = (True, True, True, True, True, True)
                fixbb = (False, False, False, False, False, False)
            elif fixc == 'bb':
                xx = (0., 0., 0., 0., 0., 0.)
                bb = (21., 23., 27., 33., 41., 51.)
                fixxx = (False, False, False, False, False, False)
                fixbb = (True, True, True, True, True, True)
            elif fixc == 'fix':
                xx = (1., 0., 0., 4., 5., 6.)
                bb = (0., 23., 27., 0., 0., 51.)
                fixxx = (True, False, False, True, True, False)
                fixbb = (False, True, True, False, False, True)
        elif type == 'type-2':
            aa = ( (1., 1., 1., 1., 1., 1.), (1., 1., 1., 1., 2., 1.),
                   (1., 1., 1., 3., 1., 1.), (1., 1., 4., 1., 1., 1.),
                   (1., 5., 1., 1., 1., 1.), (6., 1., 1., 1., 1., 1.) )
            if fixc == 'xx':
                xx = (1., 2., 3., 4., 5., 6.)
                bb = (0., 0., 0., 0., 0., 0.)
                fixxx = (True, True, True, True, True, True)
                fixbb = (False, False, False, False, False, False)
            elif fixc == 'bb':
                xx = (0., 0., 0., 0., 0., 0.)
                bb = (21., 26., 29., 30., 29., 26.)
                fixxx = (False, False, False, False, False, False)
                fixbb = (True, True, True, True, True, True)
            elif fixc == 'fix':
                xx = (0., 2., 3., 0., 0., 6.)
                bb = (0., 26., 29., 0., 0., 26.)
                fixxx = (False, True, True, False, False, True)
                fixbb = (False, True, True, False, False, True)
    ## --- section_m1: solving matrix equation --- ##
    matrixeq = GMMatrixEq(aa=aa, xx=xx, bb=bb, fixxx=fixxx, fixbb=fixbb)
    matrixeq.solve()
    print(matrixeq)

    # =========================================================
    # terminal log / terminal log / terminal log /
    '''
    *** class GMMatrixEq: solving matrix equation ***
    ### --- section_module: (GMMatrixEq) importing items from, module --- ###
    ### --- section_class: (GMMatrixEq) declaring class --- ###
    ### --- section_main: (GMMatrixEq) main process --- ###
    (GMMatrixEq): 
        aa = [ [1. 1. 1. 1. 1. 1.] [1. 2. 1. 1. 1. 1.]
               [1. 1. 3. 1. 1. 1.] [1. 1. 1. 4. 1. 1.]
               [1. 1. 1. 1. 5. 1.] [1. 1. 1. 1. 1. 6.] ]
        xx = [1. 2. 3. 4. 5. 6.]
        bb = [21. 23. 27. 33. 41. 51.]
        fixxx = (True, False, False, True, True, False)
        fixbb = (False, True, True, False, False, True)
    '''
