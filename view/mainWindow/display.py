import numpy as np
import random as rand
import matplotlib.pyplot as plt
import math
from matplotlib import colors

xy1=np.loadtxt('../displayCase/csvFiles/forprint1.csv',delimiter=',',dtype=np.float64)
xy2=np.loadtxt('../displayCase/csvFiles/forprint2.csv',delimiter=',',dtype=np.float64)
cmap = colors.ListedColormap(['honeydew','mistyrose','lightgray','yellow'])

def first_floor() :
    plt.text(1,6.5,'room1')
    plt.text(4,6.5,'room2')
    plt.text(9,6.5,'room3')
    plt.text(12,6.5,'room4')
    plt.text(1,1.5,'room5')
    plt.text(4,1.5,'room6')
    plt.text(9,1.5,'room7')
    plt.text(12,1.5,'room8')
    plt.text(7,7.5,'exit')
    plt.text(13,3.5,'exit')
def second_floor() :
    plt.text(1,6.5,'room9')
    plt.text(4,6.5,'room10')
    plt.text(9,6.5,'room11')
    plt.text(12,6.5,'room12')
    plt.text(1,1.5,'room13')
    plt.text(4,1.5,'room14')
    plt.text(9,1.5,'room15')
    plt.text(12,1.5,'room16')
    plt.text(6,7.5,'exit')
    plt.text(7,0.5,'exit')
    plt.text(0,3.5,'exit')

map = np.reshape(xy1,[-1,14])
first_floor()
plt.figure(1)
plt.title('first floor')

plt.imshow(map, cmap=cmap, extent=[0,14,0,8])
plt.pause(0.5)
plt.draw()

map = np.reshape(xy2,[-1,14])
plt.figure(2)
plt.title('second floor')
plt.imshow(map, cmap=cmap, extent=[0,14,0,8])
second_floor()
plt.pause(0.5)
plt.draw()
