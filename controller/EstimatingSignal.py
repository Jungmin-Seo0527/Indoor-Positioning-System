import numpy as np

from controller import Rounding


def estimating_signal(x, y, z):
    
    x_test = np.loadtxt('controller/txt2py_x_data_input_signal_.txt', delimiter=',', skiprows=1, dtype='float32')
    y_test = np.loadtxt('controller/txt2py_y_data_input_position_.txt', delimiter=',', skiprows=1, dtype='float32')
    
    y_test = np.round(y_test, 1)

    xp = Rounding.rounding(x)
    yp = Rounding.rounding(y)

    if z <= 1.5:
        zp = 1.0
    elif (z > 1.5) and (z <= 2.5):
        zp = 2.0
    elif (z > 2.5) and (z <= 3.5):
        zp = 3.0
    elif (z > 3.5) and (z <= 4.5):
        zp = 4.0
    elif (z > 4.5) and (z <= 5.5):
        zp = 5.0
    elif z > 5.5:
        zp = 6.0

    l = len(x_test)

    pos=[]
    dic=dict()

    for skimming in range(l):
        pos.insert(skimming,tuple(y_test[skimming])) 

    for skimming in range(l):
        dic[pos[skimming]]= x_test[skimming]
    return dic[(xp,yp,zp)]
