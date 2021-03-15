import numpy as np
import os
from scipy import io

os.getcwd()


mat_file = io.loadmat('test_signal_data_case5')

mat_file_position = io.loadmat('test_pos_data_case5')

sig=mat_file['dBm_noised_received_power']
np.savetxt('txt2py_test_x_data_case5.txt',sig,fmt='%f32',delimiter=',',header='x_data')


pos=mat_file_position['pos']
np.savetxt('txt2py_test_y_data_case5.txt',pos,fmt='%f32',delimiter=',',header='y_data')


file_1 = io.loadmat('strength_1st_case5')

MAP_1=file_1['S_1st']

np.savetxt('txt2py_map_1_data_case5.txt',MAP_1,fmt='%f32',delimiter=',',header='map_1_data')

file_2 = io.loadmat('strength_2st_case5')

MAP_2=file_2['S_2st']

np.savetxt('txt2py_map_2_data_case5.txt',MAP_2,fmt='%f32',delimiter=',',header='map_2_data')


# case n 으로 변
