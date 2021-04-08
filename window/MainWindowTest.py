import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image
import ESTIMATINGSIGNAL
import inputing
import reloading_func
import ESTIMATING_POSITION_temp_for_inputing
import watch_where_func
import mola
import webbrowser
import gogogo
import nanopower
import inputQlearning
import random as rand
import matplotlib.pyplot as plt
import math
from matplotlib import colors

from pyqt_practice import TestCaseList
from view.mainWindow.DisplayBuildingStructure import DisplayBuildingStructure
from view.mainWindow.silsun import silsun

form_class3 = uic.loadUiType("ui/testCase1.ui")[0]
form_class3_2 = uic.loadUiType("ui/33-2.ui")[0]
form_class3_3 = uic.loadUiType("ui/33-3.ui")[0]
form_class3_4 = uic.loadUiType("ui/33-4.ui")[0]
form_class3_5 = uic.loadUiType("ui/33-5.ui")[0]
form_class4 = uic.loadUiType("ui/44.ui")[0]
form_class4_2 = uic.loadUiType("ui/44-2.ui")[0]
form_class4_3 = uic.loadUiType("ui/44-3.ui")[0]
form_class4_4 = uic.loadUiType("ui/44-4.ui")[0]
form_class4_5 = uic.loadUiType("ui/44-5.ui")[0]
form_class5 = uic.loadUiType("ui/5.ui")[0]
form_class6 = uic.loadUiType("ui/6.ui")[0]
form_class6_2 = uic.loadUiType("ui/6-2.ui")[0]


class MainWindowTest(QMainWindow, uic.loadUiType("/ui/MainWindow.ui")[0]):  # 제일 먼저 켜지는 메인 윈도우
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.InitAloitus()

    def InitAloitus(self):
        self.show()
        self.setWindowTitle('서정민')  # 제목
        self.setGeometry(300, 300, 400, 300)  # 위치설정

        self.btn4.setEnabled(False)
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
        self.btn9.clicked.connect(self.btn9func)
    #
    # def btn1func(self):  # 건물구조 보기
    #     # reloading_func.execfile("view/mainWindow/silsun.py")
    #     silsun()
    #
    # def btn2func(self):  # 한 층의 평면도 보기
    #
    #     strueture = DisplayBuildingStructure("view/displayCase/csvFiles/forprint1.csv", "view/displayCase/csvFiles/forprint2.csv")
    #     strueture.showStructure()
    #
    # def btn3func(self):  # 이미 러닝된 데이터 불러오기
    #     self.a = TestCaseList()
    #
    # def btn4func(self):  # 딥러닝 새롭게 시작
    #     print("구현안할거야")
    #
    # def btn9func(self):  # 딥러닝 모델보기
    #     self.a = popupimage3()


class popupimage3(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        Image.open("image/model.jpg").show()

if __name__ == "__main__":

    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = MainWindowTest()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()