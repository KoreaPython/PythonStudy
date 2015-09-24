__author__ = 'leftpark'

# coding: utf-8

#import PyQt module
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import class_ball
import random


class Form(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.init_all()

        # Setting Timer
        self.timer = QtCore.QBasicTimer()
        self.timer.start(1000, self)

    def timerEvent(self, QTimerEvent):
        self.repaint()


    def init_all(self):
        self.ball = class_ball.Ball(100, 100, 50)


    def paintEvent(self, QPaintEvent):
        qp = QtGui.QPainter()
        qp.begin(self)
        #USER CODE
        self.ball_moving(QPaintEvent, qp)
        qp.end()

    def ball_moving(self, qp_event, qp):
        self.ball.x = random.randrange(0, 640)
        self.ball.y = random.randrange(0, 480)
        self.ball.r = random.randrange(10, 200)
        print(self.ball.x, self.ball.y, self.ball.r)
        self.ball.draw(qp_event, qp)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())





#QObject > ... > QtWidget
#paintEvent(self, QPaintEvent)
#keyEvent()