import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image
img=Image.open("20190122_154349.jpg")
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("1.ui")[0]
form_class2= uic.loadUiType("2.ui")[0]
form_class3= uic.loadUiType("3.ui")[0]
form_class4= uic.loadUiType("4.ui")[0]
#화면을 띄우는데 사용되는 Class 선언
class popupimage(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        img.show()

class chang(QDialog,form_class2) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.btn5.clicked.connect(self.btn5func)
        self.btn6.clicked.connect(self.btn6func)
        self.btn7.clicked.connect(self.btn7func)
        self.btn8.clicked.connect(self.btn8func)
    def btn5func(self):
        print("눌림5")
    def btn6func(self):
        print("눌림6")
    def btn7func(self):#다음창으로 넘어가는거
        a=changg()
        a.exec_()
       
    def btn8func(self):
        a=changgg()
        a.exec_()
        
class changg(QDialog,form_class3) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

class changgg(QDialog,form_class4) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('재난상황에서 최적의 탈출경로 찾기')
        self.setGeometry(300, 300, 400, 200)
        self.show()
        
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
    def btn1func(self):
        print("눌림")
    def btn2func(self):
        aa=popupimage()
        aa.exec_()
    def btn3func(self):#다음창으로 넘어가는거
        a=chang()
        a.exec_()
       
    def btn4func(self):
        print("눌림4")


        
        

        

        

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
