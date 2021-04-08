

import math
import numpy as np

def making_nanopower(lst=[]):
    lst_temp=np.array(lst)
    #print(lst)
    #print(lst_temp)
    nano_powerlist = []
    for n in lst_temp:
        nano_powerlist.append(10**(n*0.1+6))
#    print(nano_powerlist)
    return nano_powerlist
