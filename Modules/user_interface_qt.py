#!/usr/bin/python2.7

import sys
from PyQt4 import QtGui

# this is a second attempt at building a UI class 
# @markusc90 recommended to use PyQt instead of Tk

def ui():
    app = QtGui.QApplication(sys.argv)
    ui = UserInterface()
    sys.exit(app.exec_())


class UserInterface(QtGui.QWidget):

    def __init__(self):
        super(UserInterface, self).__init__()

        self.initUI()

    def initUI(self):
        self.resize(300, 300)
        self.center()

        self.setWindowTitle('Test')
        self.show()

    def center(self):
        window_frame = self.frameGeometry()
        center_point = QtGui.QDesktopWidget().availableGeometry().center()
        window_frame.moveCenter(center_point)
        self.move(window_frame.topLeft())
