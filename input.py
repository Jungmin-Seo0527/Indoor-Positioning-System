import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image
import reloading_func
form_class=uic.loadUiType("5.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.show()
        self.btn1.clicked.connect(self.btn1func)
##        self.edit1.returnPressed.connect(self.edit1func)
##        self.edit2.returnPressed.connect(self.edit2func)
##        self.edit3.returnPressed.connect(self.edit3func)
    def btn1func(self):
        a=self.edit1.text()
        b=self.edit2.text()
        c=self.edit3.text()
        print(a)
        print(b)
        print(c)
##    def edit1func(self):
##        a=self.edit1.text()
##        print(a)        


        

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
