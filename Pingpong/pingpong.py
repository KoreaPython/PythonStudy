__author__ = 'leftpark'

# coding: utf-8

#import PyQt module
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import class_ball


class Form(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.init_all()

        # Setting Timer
        self.timer = QtCore.QBasicTimer()
        self.timer.start(1000, self)

    def timerEvent(self, QTimerEvent):
        pass


    def init_all(self):
        self.ball = class_ball.Ball(100, 100, 50)


    def paintEvent(self, QPaintEvent):
        qp = QtGui.QPainter()
        qp.begin(self)
        #USER CODE
        self.ball.draw(QPaintEvent, qp)
        qp.end()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())





#QObject > ... > QtWidget
#paintEvent(self, QPaintEvent)
#keyEvent()