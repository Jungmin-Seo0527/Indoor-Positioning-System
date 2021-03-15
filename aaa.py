import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image

img = Image.open("badac.png")
badac = Image.open("badac.png")


class popupimage(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        img.show()


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def btn1func(self):
        print("버튼1 클릭됨")

    def btn2func(self):
        aa = popupimage()
        aa.exec_()

    def btn3func(self):
        print("버튼3 클릭됨")

    def btn4func(self):
        print("버튼4 클릭됨")

    def initUI(self):
        label1 = QLabel('건물구조 보기', self)
        label1.move(20, 20)
        label2 = QLabel('한 층의 평면도 보기', self)
        label2.move(20, 60)
        label3 = QLabel('이미 러닝된 데이터 불러오기', self)
        label3.move(20, 100)
        label4 = QLabel('딥러닝 새롭게 시작(12시간)', self)
        label4.move(20, 140)

        btn1 = QPushButton('Button1', self)
        btn1.clicked.connect(self.btn1func)
        btn1.move(200, 13)
        btn2 = QPushButton('Button2', self)
        btn2.clicked.connect(self.btn2func)
        btn2.move(200, 53)
        btn3 = QPushButton('Button3', self)
        btn3.clicked.connect(self.btn3func)
        btn3.move(200, 93)
        btn4 = QPushButton('Button4', self)
        btn4.clicked.connect(self.btn4func)
        btn4.move(200, 133)

        self.setWindowTitle('재난상황에서 최적의 탈출경로 찾기')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


