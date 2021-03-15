import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image
img=Image.open("한층.png")
img2=Image.open("20190122_154349.jpg")


#UI파일 연결
form_class = uic.loadUiType("1.ui")[0]
form_class2= uic.loadUiType("2.ui")[0]
form_class3= uic.loadUiType("3.ui")[0]
form_class4= uic.loadUiType("4.ui")[0]
# Class 선언
class popupimage(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        img.show()
class popupimage2(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
    def setupUI(self):
        img2.show()
class chang(QDialog,form_class2) :#이미 러닝된 데이터 불러오기 눌렀을때 다음창
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.btn5.clicked.connect(self.btn5func)
        self.btn6.clicked.connect(self.btn6func)
        self.btn7.clicked.connect(self.btn7func)
        self.btn8.clicked.connect(self.btn8func)
    def btn5func(self):#코스트 줄어드는거
        print("코스트 줄어드는 사진")
    def btn6func(self):#센서별 세기
        print("센서별 세기 사진")
    def btn7func(self):#실제좌표와 예상좌표
        a=changg()#다음창으로
        a.exec_()
       
    def btn8func(self):#추정할 좌표 골라보기
        a=changgg()#다음창으로
        a.exec_()
        
class changg(QDialog,form_class3) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

class changgg(QDialog,form_class4) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
class WindowClass(QMainWindow, form_class) :#제일 먼저 켜지는 메인 윈도우
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('재난상황에서 최적의 탈출경로 찾기')#제목
        self.setGeometry(300, 300, 400, 200)#위치설정
        self.show()
        self.btn4.setEnabled(False)
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
    def btn1func(self):#건물구조 보기
        a=popupimage2()
        a.exec_()
    def btn2func(self):#한 층의 평면도 보기
        aa=popupimage()
        aa.exec_()
    def btn3func(self):#이미 러닝된 데이터 불러오기
        a=chang()
        a.exec_()
       
    def btn4func(self):#딥러닝 새롭게 시작
        print("구현안할거야")


        
        

        

        

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
