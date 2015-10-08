__author__ = 'leftpark'

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

# class of Ball
class Ball(QtWidgets.QWidget):

    margin = 1


    def __init__(self, x, y, r, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setGeometry(x, y, r+self.margin, r+self.margin)
        self._x = x
        self._y = y
        self._r = r
        self._theta = 0.5
        self._velocity = 5


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


    def paintEvent(self, QPaintEvent):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setPen(QtGui.QColor('black'))
        qp.drawEllipse(0, 0, self._r, self._r)
        qp.end()
