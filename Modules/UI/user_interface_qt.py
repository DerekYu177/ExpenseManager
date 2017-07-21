#!/usr/bin/python2.7

import sys
from PyQt4 import QtGui, QtCore

# this is a second attempt at building a UI class
# @markusc90 recommended to use PyQt instead of Tk

# to determine what OS it is
import os

def ui():
    app = QtGui.QApplication(sys.argv)
    ui = LocationQuery()
    sys.exit(app.exec_())

class LocationQuery(QtGui.QMainWindow):
    file_location = ""

    def __init__(self):
        super(LocationQuery, self).__init__()

        self.initUI()

    def initUI(self):

        okButton = QtGui.QPushButton("OK")
        cancelButton = QtGui.QPushButton("Cancel")

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

    def file_location_query_button(self):
        query_button = QtGui.QPushButton('Open', self)
        query_button.clicked.connect(self.show_dialog)
        return query_button

    def ok_button(self):
        ok_button = QtGui.QPushButton('OK', self)
        ok_button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        return ok_button

    def show_dialog(self):
        self.file_location = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')

# for testing purposes
# if __name__ == '__main__':
#     ui()
