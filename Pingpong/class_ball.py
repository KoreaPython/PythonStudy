__author__ = 'leftpark'


# class of Ball
class Ball(object):
    def __init__(self, x, y, r):
        self._x = x
        self._y = y
        self._r = r

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def r(self):
        return self.r

    @r.setter
    def r(self, value):
        self._r = value

    #draw itself
    def draw(self, qp_evnt, qp):
        x = 200
        y = 100
        r = 50
        qp.drawEllipse(x, y, r, r)
