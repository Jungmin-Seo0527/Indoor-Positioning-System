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

# image들 연결
img = Image.open("cost.png")
##img2=Image.open("건물구조.jpg")
img3 = Image.open("model.jpg")
case1 = Image.open("case1.png")
case2 = Image.open("case2.png")
case3 = Image.open("case3.png")
case4 = Image.open("case4.png")
case5 = Image.open("case5.png")

# UI파일 연결
form_class = uic.loadUiType("1.ui")[0]
form_class2 = uic.loadUiType("chang.ui")[0]
# form_class2_2= uic.loadUiType("2-2.ui")[0]
form_class3 = uic.loadUiType("33.ui")[0]
form_class3_2 = uic.loadUiType("33-2.ui")[0]
form_class3_3 = uic.loadUiType("33-3.ui")[0]
form_class3_4 = uic.loadUiType("33-4.ui")[0]
form_class3_5 = uic.loadUiType("33-5.ui")[0]
form_class4 = uic.loadUiType("44.ui")[0]
form_class4_2 = uic.loadUiType("44-2.ui")[0]
form_class4_3 = uic.loadUiType("44-3.ui")[0]
form_class4_4 = uic.loadUiType("44-4.ui")[0]
form_class4_5 = uic.loadUiType("44-5.ui")[0]
form_class5 = uic.loadUiType("5.ui")[0]
form_class6 = uic.loadUiType("6.ui")[0]
form_class6_2 = uic.loadUiType("6-2.ui")[0]


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
        img.show() #


class popupimage3(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        img3.show()


class popupcase1(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        reloading_func.execfile("./display_case1.py")


class popupcase2(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        reloading_func.execfile("./display_case2.py")


class popupcase3(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        reloading_func.execfile("./display_case3.py")


class popupcase4(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        reloading_func.execfile("./display_case4.py")


class popupcase5(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        reloading_func.execfile("./display_case5.py")


class chang(QMainWindow, form_class2):  # 이미 러닝된 데이터 불러오기 눌렀을때 다음창
    def __init__(self):
        super().__init__()
        self.setupUi(self)  ##불러온 ui파일 세팅

        self.show()
        self.btn5.clicked.connect(self.btn5func)
        self.btn6.clicked.connect(self.btn6func)
        self.btn7.clicked.connect(self.btn7func)
        self.btn8.clicked.connect(self.btn8func)
        self.btn10.clicked.connect(self.btn10func)
        self.btn11.clicked.connect(self.btn11func)
        self.btn12.clicked.connect(self.btn12func)

    def btn5func(self):  # 코스트 줄어드는거 텐서보드 -> 미완성
        url = 'http://localhost:6006/'

        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

        webbrowser.get(chrome_path).open(url)

    def btn6func(self):  # 센서별 세기
        self.a = changg()  # x:31,y:10,z:2

    def btn7func(self):  # 실제좌표와 예상좌표
        self.a = changg_3()  # x:25,y:11,z:4

    def btn8func(self):  # 추정할 좌표 골라보기
        self.a = changg_5()  # x:23,y:16,z:5

    def btn10func(self):  # 추정할 좌표 골라보기
        self.a = changg_2()  # x:28,y:11,z:5

    def btn11func(self):  # 추정할 좌표 골라보기
        self.a = changg_4()  # x:2,y:11,z:2

    def btn12func(self):
        self.a = changggg()


class changg(QMainWindow, form_class3):  # x:31,y:10,z:2
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
        self.btn5.clicked.connect(self.btn5func)

    def btn1func(self):  # 현 위치에서 각 센서들의 RSSI값
        reloading_func.execfile("./0_visualize_map_temp_case1.py")

    def btn2func(self):  # DNN을 이용하여 예상 한 값
        reloading_func.execfile("./0_ESTIMATING_POSITION_temp1.py")

    def btn3func(self):  # Q-Learning environmet 보기
        self.a = changgg()

    def btn4func(self):  # Q-Learning 실행
        reloading_func.execfile("./Qlearning.py")

    def btn5func(self):  # 건물구조에서 사람의 현재위치
        reloading_func.execfile("./0_watch_where_1.py")


class changg_2(QMainWindow, form_class3_2):  # x:28,y:11,z:5
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
        self.btn5.clicked.connect(self.btn5func)

    def btn1func(self):  # 현 위치에서 각 센서들의 RSSI값
        reloading_func.execfile("./0_visualize_map_temp_case2.py")

    def btn2func(self):  # DNN을 이용하여 예상 한 값
        reloading_func.execfile("./0_ESTIMATING_POSITION_temp3.py")

    def btn3func(self):  # Q-Learning environmet 보기
        self.a = changgg_2()

    def btn4func(self):  # Q-Learning 실행
        print("Q러닝 실행하는 코드 넣을거임")

    def btn5func(self):  # 건물구조에서 사람의 현재위치
        reloading_func.execfile("./0_watch_where_2.py")


class changg_3(QMainWindow, form_class3_3):  # x:25,y:11,z:4
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
        self.btn5.clicked.connect(self.btn5func)

    def btn1func(self):  # 현 위치에서 각 센서들의 RSSI값
        reloading_func.execfile("./0_visualize_map_temp_case3.py")

    def btn2func(self):  # DNN을 이용하여 예상 한 값
        reloading_func.execfile("./0_ESTIMATING_POSITION_temp3.py")

    def btn3func(self):  # Q-Learning environmet 보기
        self.a = changgg_3()

    def btn4func(self):  # Q-Learning 실행
        reloading_func.execfile("./Qlearning3.py")

    def btn5func(self):  # 건물구조에서 사람의 현재위치
        reloading_func.execfile("./0_watch_where_3.py")


class changg_4(QMainWindow, form_class3_4):  # x:2,y:11,z:2
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
        self.btn5.clicked.connect(self.btn5func)

    def btn1func(self):  # 현 위치에서 각 센서들의 RSSI값
        reloading_func.execfile("./0_visualize_map_temp_case4.py")

    def btn2func(self):  # DNN을 이용하여 예상 한 값
        reloading_func.execfile("./0_ESTIMATING_POSITION_temp4.py")

    def btn3func(self):  # Q-Learning environmet 보기
        self.a = changgg_4()

    def btn4func(self):  # Q-Learning 실행
        reloading_func.execfile("./Qlearning4.py")

    def btn5func(self):  # 건물구조에서 사람의 현재위치
        reloading_func.execfile("./0_watch_where_4.py")


class changg_5(QMainWindow, form_class3_5):  # x:23,y:16,z:5
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
        self.btn5.clicked.connect(self.btn5func)

    def btn1func(self):  # 현 위치에서 각 센서들의 RSSI값
        reloading_func.execfile("./0_visualize_map_temp_case5.py")

    def btn2func(self):  # DNN을 이용하여 예상 한 값
        reloading_func.execfile("./0_ESTIMATING_POSITION_temp5.py")

    def btn3func(self):  # Q-Learning environmet 보기
        self.a = changgg_5()

    def btn4func(self):  # Q-Learning 실행
        reloading_func.execfile(".Qlearning5.py")

    def btn5func(self):  # 건물구조에서 사람의 현재위치
        reloading_func.execfile("./0_watch_where_5.py")


class changgg(QMainWindow, form_class4):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.btn1.clicked.connect(self.btn1func)

    def btn1func(self):  # 화재위치 , 사람의 수
        reloading_func.execfile("./display_case1.py")


class changgg_2(QMainWindow, form_class4_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.btn1.clicked.connect(self.btn1func)

    def btn1func(self):  # 화재위치 , 사람의 수
        reloading_func.execfile("./display_case2.py")


class changgg_3(QMainWindow, form_class4_3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.btn1.clicked.connect(self.btn1func)

    def btn1func(self):  # 화재위치 , 사람의 수
        reloading_func.execfile("./display_case3.py")


class changgg_4(QMainWindow, form_class4_4):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.btn1.clicked.connect(self.btn1func)

    def btn1func(self):  # 화재위치 , 사람의 수
        reloading_func.execfile("./display_case4.py")


class changgg_5(QMainWindow, form_class4_5):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.btn1.clicked.connect(self.btn1func)

    def btn1func(self):  # 화재위치 , 사람의 수
        reloading_func.execfile("./display_case5.py")


class changggg(QMainWindow, form_class5):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.btn1.clicked.connect(self.btn1func)

    def btn1func(self):
        global x, y, z, n
        x = float(self.edit1.text())  # x좌표
        y = float(self.edit2.text())  # y좌표
        z = float(self.edit3.text())  # z좌표
        n = float(self.edit4.text())  # 사람수
        ##        reloading_func.execfile("C:/사용자/USER/PycharmProjects/pythonProject/pythonProject2/inputing.py")
        self.a = changgggg()


class changgggg(QMainWindow, form_class6):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
        self.btn5.clicked.connect(self.btn5func)

    def btn1func(self):  # 현 위치에서 각 센서들의 RSSI값
        gogogo.play(x, y, z)

    def btn2func(self):  # DNN을 이용하여 예상 한 값
        print(ESTIMATING_POSITION_temp_for_inputing.ESTIMATINGPOSITIONBYINPUT(inputing.inputing(x, y, z)))

    def btn3func(self):  # Q-Learning environmet 보기
        # self.a=changgg_3()
        self.a = changgggg_2()

    def btn4func(self):  # Q-Learning 실행
        global stair, state
        stair, state = ESTIMATING_POSITION_temp_for_inputing.ESTIMATINGPOSITIONBYINPUT(inputing.inputing(x, y, z))
        ##        stair=float(stair)
        ##        state=float(state)

        inputQlearning.Qlearning(1, int(n), int(state), int(stair))  # 화재위치바꾸고싶으면 바꾸면

    def btn5func(self):  # 건물구조에서 사람의 현재위치
        watch_where_func.watching(mola.look_structure_position(x, y, z))


class changgggg_2(QMainWindow, form_class6_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.btn1.clicked.connect(self.btn1func)

    def btn1func(self):
        reloading_func.execfile("./display_input.py")


class WindowClass(QMainWindow, form_class):  # 제일 먼저 켜지는 메인 윈도우
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.InitAloitus()

    def InitAloitus(self):
        self.show()
        self.setWindowTitle('서정민')  # 제목
        self.setGeometry(300, 300, 400, 200)  # 위치설정

        self.btn4.setEnabled(False)
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)
        self.btn4.clicked.connect(self.btn4func)
        self.btn9.clicked.connect(self.btn9func)

    def btn1func(self):  # 건물구조 보기
        reloading_func.execfile("./silsun.py")

    def btn2func(self):  # 한 층의 평면도 보기

        # reloading_func.execfile("C:/Users/UESR/PycharmProjects/pythonProject/pythonProject2/display.py")
        reloading_func.execfile("./display.py")


    def btn3func(self):  # 이미 러닝된 데이터 불러오기
        self.a = chang()

    ##        a.exec_()

    def btn4func(self):  # 딥러닝 새롭게 시작
        print("구현안할거야")

    def btn9func(self):  # 딥러닝 모델보기
        self.a = popupimage3()


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    # sys.exit(1)


# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook

# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook

if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
