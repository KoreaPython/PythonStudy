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


    def paintEvent(self, QPaintEvent):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setPen(QtGui.QColor('black'))
        qp.drawEllipse(0, 0, self._r, self._r)
        qp.end()
