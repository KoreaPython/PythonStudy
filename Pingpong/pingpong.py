__author__ = 'leftpark'

# coding: utf-8

# import PyQt module
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import class_ball
import random


class Form(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setGeometry(100, 100, 640, 480)

        # Setting Timer
        self.timer = QtCore.QBasicTimer()
        self.timer.start(1000, self)

        # New Frame
        self.frame = QtWidgets.QWidget(self)
        self.frame.setGeometry(10, 10, 620, 400)
        self.frame.setStyleSheet("background-color: yellow;")
        self.frame.show()

        self.init_all()


    def timerEvent(self, QTimerEvent):
        self.checkCrash()
        self.ball_moving()


    def checkCrash(self):
        pass


    def init_all(self):
        self.ball = class_ball.Ball(0, 0, 20, self.frame)


    def ball_moving(self):
        self.ball.move(random.randrange(0, 600), random.randrange(0, 380))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())
