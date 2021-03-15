
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import pyqtSlot
import sys

class Aloitus(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitAloitus()

    def InitAloitus(self):
        self.button=QPushButton("Ok",self)
        self.button.move(200,200)
        self.button.clicked.connect(self.continue2)
        self.setGeometry(600,200,500,300)
        self.show()

    def continue2(self):
        self.close()
        self.next=Aloitus()
        

class Second(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title="Alkutiedot"
        self.top=600
        self.left=200
        self.width=500
        self.height=500

        self.initWindow()

    def initWindow(self):

        self.button=QPushButton("Ok", self)
        self.button.move(100,400)
        self.button.clicked.connect(self.ok)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def ok(self):
        print('close clicked')
        self.close()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Aloitus()
    sys.exit(app.exec_())
