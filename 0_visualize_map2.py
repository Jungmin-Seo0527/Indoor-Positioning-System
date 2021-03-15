from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

map1= np.loadtxt('txt2py_map_1_data_case2.txt',delimiter=',',skiprows=1,dtype='float32')
map2= np.loadtxt('txt2py_map_2_data_case2.txt',delimiter=',',skiprows=1,dtype='float32')


#print(map1[:][0]) # 이건 xyz
##print(map1) # 이건 xyz
##print(map2) # 이건 xyz


##print(map1[:,0]) #x좌표
##print(map1[:,1]) #y좌표
##print(map1[:,2]) #z좌표

#style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(212,projection='3d')
ax2 = fig.add_subplot(211,projection='3d')

x3 = map1[:,0] # x좌표
y3 = map1[:,1] # y좌표
z3 = np.zeros(9) # 고정

dx = np.ones(9) # 두께
dy = np.ones(9) # 두께
dz = map1[:,2] # z좌표

ax1.bar3d(x3,y3,z3,dx,dy,dz)
##ax1.set_xlabel('x axis')
##ax1.set_ylabel('y axis')
ax1.set_zlabel('relative power')
ax1.set_title('1st Floor')
ax1.set_zlim([0,35])

x3_2 = map2[:,0] # x좌표
y3_2 = map2[:,1] # y좌표
z3_2 = np.zeros(9) # 고정

dx_2 = np.ones(9) # 두께
dy_2 = np.ones(9) # 두께
dz_2 = map2[:,2] # z좌표

ax2.bar3d(x3_2,y3_2,z3_2,dx_2,dy_2,dz_2)
##ax2.set_xlabel('x axis')
##ax2.set_ylabel('y axis')
ax2.set_zlabel('relative power')
ax2.set_title('2st Floor')
ax2.set_zlim([0,35])


plt.show()
