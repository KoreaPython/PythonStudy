__author__ = 'leftpark'

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import math

# class of Figure
class Figure(QtWidgets.QWidget):


    def __init__(self, x, y, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self._x = x
        self._y = y
        self._theta = (math.pi/180)*45
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

    margin = 2


    def __init__(self, x, y, r, parent=None):
        # Figure.__init__(self, x, y, parent=self)
        super(Circle, self).__init__(x, y, parent)
        self.setGeometry(x, y, r+self.margin, r+self.margin)
        self._x = x
        self._y = y
        self._r = r
        self._theta = (math.pi/180)*45
        self._velocity = 10


    @property
    def r(self):
        return self._r


    @r.setter
    def r(self, value):
        self._r = value


    def paintEvent(self, QPaintEvent):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setPen(QtGui.QColor('black'))
        qp.drawEllipse(1, 1, self._r, self._r)
        qp.end()