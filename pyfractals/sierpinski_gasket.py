import  numpy               as npy
import  matplotlib.pyplot   as plt

class Error(Exception):
    pass

class InitializationError(Error):
    def __init__(self, message):
        self.message = message

class SierpinskiGasket(object):
    """ 
    Reference http://ecademy.agnesscott.edu/~lriddle/ifs/siertri/siertri.htm
    """

    def __init__(self, **options):
        ''' '''
        self._points_       = []
        self._centers_      = []
        self._flag_         = 0

    def _tetrahedron_(self, a, b, c, d):
        ''' '''
        self._points_.append([a, b, c, d])
        center  = (a + b + c + d) / 4
        self._centers_.append(center)

    def draw_tetrahedra(self, a, b, c, d, k):
        ''' '''
        ab      = npy.zeros((3))
        bc      = npy.zeros((3))
        ac      = npy.zeros((3))
        ad      = npy.zeros((3))
        bd      = npy.zeros((3))
        cd      = npy.zeros((3))
    
        if(k > 0):
            for j in range(3):
                ab[j] = (a[j] + b[j]) / 2
            for j in range(3):
                bc[j] = (b[j] + c[j]) / 2
            for j in range(3):
                ac[j] = (a[j] + c[j]) / 2
            for j in range(3):
                ad[j] = (a[j] + d[j]) / 2
            for j in range(3):
                bd[j] = (b[j] + d[j]) / 2
            for j in range(3):
                cd[j] = (c[j] + d[j]) / 2

            self.draw_tetrahedra(a, ab, ac, ad, k-1)
            self.draw_tetrahedra(ab, b, bc, bd, k-1)
            self.draw_tetrahedra(ac, bc, c, cd, k-1)
            self.draw_tetrahedra(ad, bd, cd, d, k-1)
        else:
            self._tetrahedron_(a, b, c, d)
 
    def Points(self):
        ''' '''
        return npy.asarray(self._points_)

    def Centers(self):
        ''' '''
        return npy.asarray(self._centers_)

    def __call__(self, **options):
        ''' 
        Not sure of a better way to plot this in 3D
        PRs are welcome!
        '''
        markers             = options.get('markers', 'centers')
        points              = None
        if self._flag_ == 0:
            raise InitializationError("Function not initialized")
        else:
            if markers == 'centers':
                points     = npy.asarray(self._centers_)
            elif markers == '':
                points      = npy.asarray(self._points_)
            
        if points is not None:
            plt.scatter(points[:, 0], points[:, 1], points[:, 2])
            plt.show()

    def fractal(self, start = [0, 0, 0], length = 1, **options):
        ''' '''
        self._order_        = options.get('order', 3)
        self._flag_         = 1
        start               = npy.asarray(start)
        vertices            =\
        [
            start,
            start + [1, 0, 0] * length,
            start + [0.5, 0.86, 0] * length,
            start + [0.5, 0.28, 1] * length
        ]
        self.draw_tetrahedra(vertices[0], vertices[1], vertices[2], vertices[3], self._order_)
        
        return npy.asarray(self._points_)

def run():
    ''' '''
    spg         = SierpinskiGasket(order = 2)

    spg.fractal()
    spg()

if __name__ == '__main__':
    run()
    