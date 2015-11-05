__author__ = 'leftpark'

# coding: utf-8

# import PyQt module
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from class_figure import Line
from class_figure import Circle
from class_figure import Rectangle
import random
import moving_helper
import crash_helper


class Form(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setGeometry(100, 100, 640, 480)

        # Setting Timer
        self.timer = QtCore.QBasicTimer()
        self.timer.start(50, self)

        # New Frame
        self.frame = QtWidgets.QWidget(self)
        self.frame.setGeometry(10, 10, 620, 400)
        self.frame.setStyleSheet("background-color: yellow;")
        self.frame.show()

        self.init_ring()
        self.init_all()



    def timerEvent(self, QTimerEvent):
        self.checkCrash()
        self.ball_moving()


    def checkCrash(self):
        crash_helper.Crash.circle_in_rectangle(self.ball, self.ring)


    def init_ring(self):
        self.ring = Rectangle(0, 0, 620, 400, self.frame)

    def init_all(self):
        self.ball = Circle(400, 200, 100, self.frame)


    def ball_moving(self):
        moving_helper.MovingHelper.movingToNext(self.ball)
        self.ball.move(self.ball.x, self.ball.y)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())
