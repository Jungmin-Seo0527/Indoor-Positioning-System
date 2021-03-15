import numpy as np
def cell(x,y,z):
    X,XT=divmod(x,3)
    Y,YT=divmod(y,3)

    if z<=3:
        if Y==7:
            return 1,X
        elif Y==6:
            return 1,X+14
        elif Y==5:
            return 1,X+14*2
        elif Y==4:
            return 1,X+14*3
        elif Y==3:
            return 1,X+14*4
        elif Y==2:
            return 1,X+14*5
        elif Y==1:
            return 1,X+14*6
        elif Y==0:
            return 1,X+14*7
    elif z>3:
        if Y==7:
            return 2,X
        elif Y==6:
            return 2,X+14
        elif Y==5:
            return 2,X+14*2
        elif Y==4:
            return 2,X+14*3
        elif Y==3:
            return 2,X+14*4
        elif Y==2:
            return 2,X+14*5
        elif Y==1:
            return 2,X+14*6
        elif Y==0:
            return 2,X+14*7
