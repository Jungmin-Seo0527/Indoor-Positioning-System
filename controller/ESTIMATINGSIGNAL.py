import numpy as np
import module2
import ROUNDING

def estimating_signal(x,y,z):
    
    x_test= np.loadtxt('txt2py_x_data_input_signal_.txt',delimiter=',',skiprows=1,dtype='float32')
    y_test= np.loadtxt('txt2py_y_data_input_position_.txt',delimiter=',',skiprows=1,dtype='float32')
    
    y_test=np.round(y_test,1)

    xp=ROUNDING.rounding(x)
    yp=ROUNDING.rounding(y)
##
##    if z>=3:
##        zp=4.5
##    elif z<3:
##        zp=1.5
##        
    if z<=1.5:
        zp = 1.0
    elif (z>1.5)and(z<=2.5):
        zp = 2.0
    elif (z>2.5)and(z<=3.5):
        zp = 3.0
    elif (z>3.5)and(z<=4.5):
        zp = 4.0
    elif (z>4.5)and(z<=5.5):
        zp = 5.0
    elif z>5.5:
        zp = 6.0

    l = len(x_test)

    pos=[]
    dic=dict()

    for skimming in range(l):
        pos.insert(skimming,tuple(y_test[skimming])) 

    for skimming in range(l):
        dic[pos[skimming]]= x_test[skimming]
##    print(xp)
##    print(yp)
##    print(zp)
#    print(dic[(xp,yp,zp)])
# print(dic[(0.0,1.5,1.5)]) # 다음과 같이 dic의 key값으로 좌표를 넣어주면 출력을 다음과 같이 해준다
    return dic[(xp,yp,zp)]
