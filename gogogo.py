import nanopower
import inputing
import ESTIMATINGSIGNAL
import ESTIMATING_POSITION_temp_for_inputing
import math
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
#import xyz
def play(x,y,z):
    #print(nanopower.making_nanopower(ESTIMATINGSIGNAL.estimating_signal(28,11,5)))
    power=nanopower.making_nanopower(ESTIMATINGSIGNAL.estimating_signal(x,y,z))
 #   pos= xyz.xyz(x,y,z)

    map1 = np.array([[4.5,19.5,power[0]],
                     [13.5,19.5,power[1]],
                     [28.5,19.5,power[2]],
                     [37.5,19.5,power[3]],
                     [4.5,4.5,power[4]],
                     [13.5,4.5,power[5]],
                     [28.5,4.5,power[6]],
                     [37.5,4.5,power[7]],
                     [21,12,power[8]]])

    map2 = np.array([[4.5,19.5,power[9]],
                     [13.5,19.5,power[10]],
                     [28.5,19.5,power[11]],
                     [37.5,19.5,power[12]],
                     [4.5,4.5,power[13]],
                     [13.5,4.5,power[14]],
                     [28.5,4.5,power[15]],
                     [37.5,4.5,power[16]],
                     [21,12,power[17]]])
    #map1= np.loadtxt('txt2py_map_1_data_case1_for_map.txt',delimiter=',',skiprows=1,dtype='float32')
    #map2= np.loadtxt('txt2py_map_2_data_case1_for_map.txt',delimiter=',',skiprows=1,dtype='float32')

    ############################################ 이거사용!!!!!!!!!!!!!!!!!
    ###print(map1[:][0]) # 이건 xyz
    ##print(map1) # 이건 xyz
    ##print(map2) # 이건 xyz


    ##print(map1[:,0]) #x좌표
    ##print(map1[:,1]) #y좌표
    ##print(map1[:,2]) #z좌표

    #style.use('ggplot')

    fig = plt.figure()
    ax1 = fig.add_subplot(212,projection='3d')

    x3 = map1[:,0] # x좌표
    y3 = map1[:,1] # y좌표
    z3 = np.zeros(9) # 고정

    dx = np.ones(9) # 두께
    dy = np.ones(9) # 두께
    dz = map1[:,2] # z좌표

    ax1.bar3d(x3,y3,z3,dx,dy,dz)
    ##ax1.set_xlabel('x axis')
    ##ax1.set_ylabel('y axis')
    ax1.set_zlabel('nano power')
    ax1.set_title('1st Floor')
    ax1.set_zlim([0,500])

    #plt.hold(True)


    if z<=3:
        plt.scatter(x,y,50)

    #!!!!!!!!!!!!plt.scatter(31,10,50)

    # 31, 10, 2

    ax2 = fig.add_subplot(211,projection='3d')

    x3_2 = map2[:,0] # x좌표
    y3_2 = map2[:,1] # y좌표
    z3_2 = np.zeros(9) # 고정

    dx_2 = np.ones(9) # 두께
    dy_2 = np.ones(9) # 두께
    dz_2 = map2[:,2] # z좌표

    ax2.bar3d(x3_2,y3_2,z3_2,dx_2,dy_2,dz_2)
    ##ax2.set_xlabel('x axis')
    ##ax2.set_ylabel('y axis')
    ax2.set_zlabel('nano power')
    ax2.set_title('2st Floor')
    ax2.set_zlim([0,500])

    if z>3:
        plt.scatter(x,y,50)


    ##ax1.view_init(0,-84)
    ##ax2.view_init(0,-84)

    plt.show()




