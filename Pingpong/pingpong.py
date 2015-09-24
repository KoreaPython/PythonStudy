__author__ = 'leftpark'

# coding: utf-8

#import PyQt module

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

#define Main Form class : 약식작성(?)
class Form(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

#get instance of MainForm and 프고르램 제어권을 Qt에 전달.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.processEvents(QtCore.QEventLoop.AllEvents)
    w = Form()
    w.show()
    sys.exit(app.exec())