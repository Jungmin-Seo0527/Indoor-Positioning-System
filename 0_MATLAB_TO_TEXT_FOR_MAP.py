import numpy as np
import os
from scipy import io

os.getcwd()


file_1 = io.loadmat('strength_1st')

MAP_1=file_1['S_1st']

np.savetxt('txt2py_map_1_data.txt',MAP_1,fmt='%f32',delimiter=',',header='map_1_data')

file_2 = io.loadmat('strength_2st')

MAP_2=file_2['S_2st']

np.savetxt('txt2py_map_2_data.txt',MAP_2,fmt='%f32',delimiter=',',header='map_2_data')

