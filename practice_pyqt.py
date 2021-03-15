import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image
import reloading_func

form_class = uic.loadUiType("1.ui")[0]
form_class2= uic.loadUiType("chang.ui")[0]

class Aloitus(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.InitAloitus()

    def InitAloitus(self):
       
        self.show()
        self.btn4.setEnabled(False)
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
        self.btn9.clicked.connect(self.btn9func)

    def btn1func(self):#건물구조 보기
##        a=popupimage2()
##        a.exec_()
        reloading_func.execfile("silsun.py")
    def btn2func(self):#한 층의 평면도 보기
        aa=popupimage()
        aa.exec_()
    def btn3func(self):#이미 러닝된 데이터 불러오기
        self.a=chang()
       
    def btn4func(self):#딥러닝 새롭게 시작
        print("구현안할거야")

    def btn9func(self):#딥러닝 모델보기
        a=popupimage3()
        a.exec_()

        

class chang(QMainWindow,form_class2):

    def __init__(self):
        super().__init__()
        self.setupUi(self)##불러온 ui파일 세팅

        self.initWindow()

    def initWindow(self):
        self.show()
        self.btn5.clicked.connect(self.btn5func)
        self.btn6.clicked.connect(self.btn6func)
        self.btn7.clicked.connect(self.btn7func)
        self.btn8.clicked.connect(self.btn8func)
        self.btn10.clicked.connect(self.btn10func)
        self.btn11.clicked.connect(self.btn11func)
        
    def btn5func(self):#코스트 줄어드는거
        print("코스트 줄어드는 사진")
    def btn6func(self):#센서별 세기
        a=changg()#x:31,y:10,z:2
        a.exec_()
    def btn7func(self):#실제좌표와 예상좌표
        a=changg_3()#x:25,y:11,z:4
        a.exec_()
       
    def btn8func(self):#추정할 좌표 골라보기
        a=changg_5()#x:23,y:16,z:5
        a.exec_()
    def btn10func(self):#추정할 좌표 골라보기
        a=changg_2()#x:28,y:11,z:5
        a.exec_()
    def btn11func(self):#추정할 좌표 골라보기
        a=changg_4()#x:2,y:11,z:2
        a.exec_()

 
if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Aloitus()
    sys.exit(app.exec_())
