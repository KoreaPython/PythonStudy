__author__ = 'leftpark'


# class of Ball
class Ball(object):
    def __init__(self, x, y, r):
        self._x = x
        self._y = y
        self._r = r

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value):
        self._r = value

    #draw itself
    def draw(self, qp_evnt, qp):
        qp.drawEllipse(self._x, self._y, self._r, self._r)
