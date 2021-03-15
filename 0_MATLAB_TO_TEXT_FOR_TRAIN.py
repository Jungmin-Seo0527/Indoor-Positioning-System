import numpy as np
import os
from scipy import io

os.getcwd()


mat_file = io.loadmat('signal_data')

mat_file_position = io.loadmat('pos_data')

sig=mat_file['dBm_noised_received_power']
np.savetxt('txt2py_x_data.txt',sig,fmt='%f32',delimiter=',',header='x_data')


pos=mat_file_position['pos']
np.savetxt('txt2py_y_data.txt',pos,fmt='%f32',delimiter=',',header='y_data')

