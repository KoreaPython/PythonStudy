__author__ = 'leftpark'

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import math


# class of Figure
class Figure(QtWidgets.QWidget):


    padding = 1


    def __init__(self, x, y, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self._x = x
        self._y = y
        self._theta = (math.pi/180)*0
        self._velocity = 10


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
    def theta(self):
        return self._theta


    @theta.setter
    def theta(self, value):
        self._theta = value


    @property
    def velocity(self):
        return self._velocity


    @velocity.setter
    def velocity(self, value):
        self._velocity = value


    def paintEvent(self):
        pass



# class of Circle
class Circle(Figure):


    def __init__(self, x, y, r, parent=None):
        # Figure.__init__(self, x, y, parent=self)
        super(Circle, self).__init__(x, y, parent)
        self.setGeometry(x, y, r, r)
        self._x = x
        self._y = y
        self._r = r


    @property
    def r(self):
        return self._r


    @r.setter
    def r(self, value):
        self._r = value

    def cX(self):
        return self._x + (self._r/2)


    def cY(self):
        return self._y + (self._r/2)


    def paintEvent(self, QPaintEvent):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setPen(QtGui.QColor('black'))
        qp.drawEllipse(0, 0, self._r-self.padding, self._r-self.padding)
        qp.end()


# class of Line
class Line(Figure):


    def __init__(self, sx, sy, ex, ey, parent=None):
        super(Line, self).__init__(sx, sy, parent)
        self.setGeometry(sx, sy, ex, ey)
        self._ex = ex
        self._ey = ey


    @property
    def ex(self):
        return self._ex


    @ex.setter
    def ex(self, value):
        self._ex = value


    @property
    def ey(self):
        return self._ey


    @ey.setter
    def ey(self, value):
        self._ey = value


    def paintEvent(self, QPaintEvent):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setPen(QtGui.QColor('red'))
        qp.drawLine(self.x, self.y, self.ex-self.padding, self.ey-self.padding)
        qp.end()


# class of Rectangle
class Rectangle(Figure):


    def __init__(self, sx, sy, ex, ey, parent=None):
        super(Rectangle, self).__init__(sx, sy, parent)
        self.setGeometry(sx, sy, ex, ey)
        self._ex = ex
        self._ey = ey


    @property
    def ex(self):
        return self._ex


    @ex.setter
    def ex(self, value):
        self._ex = value


    @property
    def ey(self):
        return self._ey


    @ey.setter
    def ey(self, value):
        self._ey = value


    def paintEvent(self, QPaintEvent):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setPen(QtGui.QColor('red'))
        qp.drawRect(self.x, self.y, self.ex-self.padding, self.ey-self.padding)
        qp.end()

