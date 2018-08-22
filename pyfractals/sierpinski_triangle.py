import  numpy               as np
import  matplotlib.pyplot   as plt

class Error(Exception):
    pass

class InitializationError(Error):
    def __init__(self, message):
        self.message = message

class SierpinskiTriangle(object):
    """
    Reference http://bopace.github.io/python/2016/06/09/python-turtle-sierpinski/
    """
    def __init__(self, **options):
        ''' '''
        self._x_            = options.get('x', 0)
        self._y_            = options.get('y', 0)
        self._length_       = options.get('length', 1)
        self._centers_      = []
        self._flag_         = 0
        vertices            =\
        np.array\
        (
            [
                [self._x_, self._y_],
                [self._x_ + self._length_ / 2, 0.5 * (3 ** 0.5) * self._length_],
                [self._x_ + self._length_, self._y_],
                [self._x_, self._y_]
            ]
        )

        self._vertices_     = vertices[:-1]
        plt.plot(vertices[:, 0], vertices[:, 1], color = 'C0')
        
        self._points_       = []

    def fractal(self, **options):
        ''' '''
        self._flag_         = 1
        self._depth_        = options.get('depth', 3)
        self._draw_fractal_(self._vertices_, self._depth_)
        return np.asarray(self._points_)[1:]

    def draw_triangle(self, vertices):
        ''' '''
        self._points_.append(vertices[0])
        self._points_.append(vertices[1])
        self._points_.append(vertices[2])
        self._centers_.append((vertices[0] + vertices[1] + vertices[2]) / 3)
        plt.plot(vertices[:, 0], vertices[:, 1], color = 'C0')

    def _midpoint_(self, point1, point2):
        ''' '''
        return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]
        
    def _draw_fractal_(self, vertices, level):
        ''' '''
        self.draw_triangle(vertices)
        if level > 0:
            v           =\
            np.array\
            (
                [
                    vertices[0],
                    self._midpoint_(vertices[0], vertices[1]),
                    self._midpoint_(vertices[0], vertices[2])
                ]
            )
            self._draw_fractal_(v, level - 1)

            v           =\
            np.array\
            (
                [
                    vertices[1],
                    self._midpoint_(vertices[0], vertices[1]),
                    self._midpoint_(vertices[1], vertices[2])
                ]
            )
            self._draw_fractal_(v, level - 1)

            v           =\
            np.array\
            (
                [
                    vertices[2],
                    self._midpoint_(vertices[2], vertices[1]),
                    self._midpoint_(vertices[0], vertices[2])
                ]
            )
            self._draw_fractal_(v, level - 1)

    def __call__(self, **options):
        ''' '''
        if self._flag_ == 0:
            raise InitializationError("Function not initialized")
        with_centers    = options.get('with_centers', False)
        if with_centers:
            centers     = np.asarray(self._centers_)
            plt.scatter(centers[:, 0], centers[:, 1])
        plt.show()

def run():
    ''' '''
    spt     = SierpinskiTriangle()
    points  = spt.fractal(depth = 2)
    spt()

if __name__ == '__main__':
    run()
