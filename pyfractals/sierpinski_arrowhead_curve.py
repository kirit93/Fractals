import  numpy                       as np
import  matplotlib.pyplot           as plt

class Error(Exception):
    pass

class InitializationError(Error):
    def __init__(self, message):
        self.message = message

class SierpinskiArrowheadCurve(object):
    """ 
    Reference https://en.wikipedia.org/wiki/Sierpi%C5%84ski_arrowhead_curve
    """
    def __init__(self, **options):
        ''' '''
        self._x_            = options.get('x', 0)
        self._y_            = options.get('y', 0)
        self._length_       = options.get('length', 1)
        self._orientation_  = 0
        self._points_       = [(self._x_, self._y_)]

    def get_points(self):
        ''' '''
        raise InitializationError("Function not initialized")

    def fractal(self, **options):
        ''' '''
        def get_points():
            return np.asarray(self._points_)

        self._order_    = options.get('order', 3)
        length          = options.get('length', self._length_)
        if 0 == (self._order_ & 1):
            self._curve_(self._order_, length, 60)
        else:
            self._orientation_ += 60
            self._curve_(self._order_, length, -60)

        # get_points can only be called after the curve has been generated
        self.get_points             = get_points

        return np.asarray(self._points_)

    def _curve_(self, order, length, angle):
        ''' 
        -1 ^ (n + 1) is used to ensure the orientation of the Sierpinski curve is always
        facing up.
        '''
        if order == 0:
            self._x_  += np.cos(np.deg2rad(self._orientation_)) * length
            self._y_  += np.sin(np.deg2rad(self._orientation_)) * length
            self._points_.append((self._x_, self._y_))
        else:
            self._curve_(order - 1, length / 2, -angle)
            self._orientation_ += ((-1) ** (self._order_ + 1)) * angle
            self._curve_(order - 1, length / 2, angle)
            self._orientation_ += ((-1) ** (self._order_ + 1)) * angle
            self._curve_(order - 1, length / 2, -angle)

    def __call__(self):
        ''' '''
        points  = self.get_points()
        plt.plot(points[:, 0], points[:, 1])
        plt.show()

    def index_to_coordinate(self, index):
        ''' '''
        points  = self.get_points()
        return points[index]

    def coordinate_to_index(self, coordinate):
        ''' '''
        points      = self.get_points()
        distances   = lambda point : (((points - point) ** 2).sum(axis = 1)) ** 0.5
        index       = np.argmin(distances(coordinate))
        return index

def run():
    
    # The order of the curve determines the number of points in the curve
    order       = 8

    # x and y represent the start of the Sierpinski curve. The length is
    # the euclidean distance between the start and end of the curve
    sac         = SierpinskiArrowheadCurve()
    points      = sac.fractal(order = 2)
    sac()

if __name__ == '__main__':
    run()
    