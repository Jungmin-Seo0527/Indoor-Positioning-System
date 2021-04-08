import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PIL import Image

import estimateTest

import webbrowser

import watch_where_func
from controller import gogogo, ESTIMATING_POSITION_temp_for_inputing, mola, inputing, ESTIMATINGSIGNAL
from controller.estimatingPosition.EstimatingPosition import EstimatingPosition
from controller.showCurrentPosition import showCurrentPosition
from view.mainWindow.DisplayBuildingStructure import DisplayBuildingStructure
from view.mainWindow.silsun import silsun
from view.visualizeMap.VisualizeMap import VisualizeMap


class TestCaseList(QMainWindow, uic.loadUiType("ui/changCopy.ui")[0]):  # 이미 러닝된 데이터 불러오기 눌렀을때 다음창
    def __init__(self):
        super().__init__()
        self.setupUi(self)  ##불러온 ui파일 세팅
        self.setWindowTitle('테스트 케이스 리스트')  # 제목

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
        self.a = TestCase1()  # x:31,y:10,z:2

    def btn7func(self):  # 실제좌표와 예상좌표
        self.a = TestCase3()  # x:25,y:11,z:4

    def btn8func(self):  # 추정할 좌표 골라보기
        self.a = TestCase5()  # x:23,y:16,z:5

    def btn10func(self):  # 추정할 좌표 골라보기
        self.a = TestCase2()  # x:28,y:11,z:5

    def btn11func(self):  # 추정할 좌표 골라보기
        self.a = TestCase4()  # x:2,y:11,z:2

    def btn12func(self):
        self.a = TestCase6User()


class TestCase1(QMainWindow, uic.loadUiType("ui/testCase1.ui")[0]):  # x:31,y:10,z:2
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(300, 300, 400, 300)  # 위치설정
        self.show()
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)

    def btn1func(self):  # 현 위치에서 각 센서들의 RSSI값
        # reloading_func.execfile("view/visualizeMap/0_visualize_map_temp_case1.py")
        visualize=VisualizeMap('view/visualizeMap/dataCaseForMap/txt2py_map_1_data_case1_for_map.txt',
                               'view/visualizeMap/dataCaseForMap/txt2py_map_2_data_case1_for_map.txt')
        visualize.showMap()

    def btn2func(self):  # DNN을 이용하여 예상 한 값
        # reloading_func.execfile("controller/estimatingPosition/0_ESTIMATING_POSITION_temp1.py")
        xDataPath = "./controller/estimatingPosition/dataSet/txt2py_test_x_data_case1.txt"
        yDataPath = "./controller/estimatingPosition/dataSet/txt2py_test_y_data_case1.txt"
        temp = "controller/estimatingPosition/train_model3.ckpt-999"
        test = EstimatingPosition(xDataPath, yDataPath, temp)
        test.showPosition()

    def btn3func(self):  # 건물구조에서 사람의 현재위치
        showCurrentPosition(34, 10, 2)


class TestCase2(QMainWindow, uic.loadUiType("ui/testCase2.ui")[0]):  # x:28,y:11,z:5
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(300, 300, 400, 300)  # 위치설정
        self.show()
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)

    def btn1func(self):  # 현 위치에서 각 센서들의 RSSI값
        # reloading_func.execfile("view/visualizeMap/0_visualize_map_temp_case1.py")
        visualize=VisualizeMap('view/visualizeMap/dataCaseForMap/txt2py_map_1_data_case2_for_map.txt',
                               'view/visualizeMap/dataCaseForMap/txt2py_map_2_data_case2_for_map.txt')
        visualize.showMap()

    def btn2func(self):  # DNN을 이용하여 예상 한 값
        # reloading_func.execfile("controller/estimatingPosition/0_ESTIMATING_POSITION_temp1.py")
        xDataPath = "./controller/estimatingPosition/dataSet/txt2py_test_x_data_case2.txt"
        yDataPath = "./controller/estimatingPosition/dataSet/txt2py_test_y_data_case2.txt"
        temp = "controller/estimatingPosition/train_model3.ckpt-999"
        test = EstimatingPosition(xDataPath, yDataPath, temp)
        test.showPosition()

    def btn3func(self):  # 건물구조에서 사람의 현재위치
        showCurrentPosition(28, 11, 5)


class TestCase3(QMainWindow,  uic.loadUiType("ui/testCase3.ui")[0]):  # x:25,y:11,z:4
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(300, 300, 400, 300)  # 위치설정
        self.show()
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)

    def btn1func(self):  # 현 위치에서 각 센서들의 RSSI값
        # reloading_func.execfile("view/visualizeMap/0_visualize_map_temp_case1.py")
        visualize = VisualizeMap('view/visualizeMap/dataCaseForMap/txt2py_map_1_data_case3_for_map.txt',
                                 'view/visualizeMap/dataCaseForMap/txt2py_map_2_data_case3_for_map.txt')
        visualize.showMap()

    def btn2func(self):  # DNN을 이용하여 예상 한 값
        # reloading_func.execfile("controller/estimatingPosition/0_ESTIMATING_POSITION_temp1.py")
        xDataPath = "./controller/estimatingPosition/dataSet/txt2py_test_x_data_case3.txt"
        yDataPath = "./controller/estimatingPosition/dataSet/txt2py_test_y_data_case3.txt"
        temp = "controller/estimatingPosition/train_model3.ckpt-999"
        test = EstimatingPosition(xDataPath, yDataPath, temp)
        test.showPosition()

    def btn3func(self):  # 건물구조에서 사람의 현재위치
        showCurrentPosition(25, 11, 4)


class TestCase4(QMainWindow, uic.loadUiType("ui/testCase4.ui")[0]):  # x:2,y:11,z:2
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(300, 300, 400, 300)  # 위치설정
        self.show()
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)

    def btn1func(self):  # 현 위치에서 각 센서들의 RSSI값
        # reloading_func.execfile("view/visualizeMap/0_visualize_map_temp_case1.py")
        visualize = VisualizeMap('view/visualizeMap/dataCaseForMap/txt2py_map_1_data_case4_for_map.txt',
                                 'view/visualizeMap/dataCaseForMap/txt2py_map_2_data_case4_for_map.txt')
        visualize.showMap()

    def btn2func(self):  # DNN을 이용하여 예상 한 값
        # reloading_func.execfile("controller/estimatingPosition/0_ESTIMATING_POSITION_temp1.py")
        xDataPath = "./controller/estimatingPosition/dataSet/txt2py_test_x_data_case4.txt"
        yDataPath = "./controller/estimatingPosition/dataSet/txt2py_test_y_data_case4.txt"
        temp = "controller/estimatingPosition/train_model3.ckpt-999"
        test = EstimatingPosition(xDataPath, yDataPath, temp)
        test.showPosition()

    def btn3func(self):  # 건물구조에서 사람의 현재위치
        showCurrentPosition(2, 11, 2)


class TestCase5(QMainWindow, uic.loadUiType("ui/testCase5.ui")[0]):  # x:23,y:16,z:5
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(300, 300, 400, 300)  # 위치설정
        self.show()
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)

    def btn1func(self):  # 현 위치에서 각 센서들의 RSSI값
        # reloading_func.execfile("view/visualizeMap/0_visualize_map_temp_case1.py")
        visualize = VisualizeMap('view/visualizeMap/dataCaseForMap/txt2py_map_1_data_case5_for_map.txt',
                                 'view/visualizeMap/dataCaseForMap/txt2py_map_2_data_case5_for_map.txt')
        visualize.showMap()

    def btn2func(self):  # DNN을 이용하여 예상 한 값
        # reloading_func.execfile("controller/estimatingPosition/0_ESTIMATING_POSITION_temp1.py")
        xDataPath = "./controller/estimatingPosition/dataSet/txt2py_test_x_data_case5.txt"
        yDataPath = "./controller/estimatingPosition/dataSet/txt2py_test_y_data_case5.txt"
        temp = "controller/estimatingPosition/train_model3.ckpt-999"
        test = EstimatingPosition(xDataPath, yDataPath, temp)
        test.showPosition()

    def btn3func(self):  # 건물구조에서 사람의 현재위치
        showCurrentPosition(23, 16, 5)


class TestCase6User(QMainWindow, uic.loadUiType("ui/testCase6.ui")[0]):
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
        self.a = TestCase6()


class TestCase6(QMainWindow, uic.loadUiType("ui/testCase6_1.ui")[0]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.btn1.clicked.connect(self.btn1func)
        self.btn2.clicked.connect(self.btn2func)
        self.btn3.clicked.connect(self.btn3func)


    def btn1func(self):  # 현 위치에서 각 센서들의 RSSI값
        gogogo.play(x, y, z)

    def btn2func(self):  # DNN을 이용하여 예상 한 값
        # print(estimateTest.ESTIMATINGPOSITIONBYINPUT(inputing.inputing(x, y, z)))
        print(ESTIMATING_POSITION_temp_for_inputing.ESTIMATINGPOSITIONBYINPUT((inputing.inputing(x, y, z))))

    def btn3func(self):  # Q-Learning environmet 보기
        watch_where_func.watching(mola.look_structure_position(x, y, z))


class MainWindowClass(QMainWindow, uic.loadUiType("window/ui/MainWindow.ui")[0]):  # 제일 먼저 켜지는 메인 윈도우
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

    def btn1func(self):  # 건물구조 보기
        # reloading_func.execfile("view/mainWindow/silsun.py")
        silsun()

    def btn2func(self):  # 한 층의 평면도 보기

        strueture = DisplayBuildingStructure("view/displayCase/csvFiles/forprint1.csv", "view/displayCase/csvFiles/forprint2.csv")
        strueture.showStructure()

    def btn3func(self):  # 이미 러닝된 데이터 불러오기
        self.a = TestCaseList()

    def btn4func(self):  # 딥러닝 새롭게 시작
        print("구현안할거야")

    def btn9func(self):  # 딥러닝 모델보기
        Image.open("image/model.jpg").show()

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
    myWindow = MainWindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
