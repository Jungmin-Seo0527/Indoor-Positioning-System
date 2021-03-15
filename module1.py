import numpy as np
def cell(x,y,z):
##    x=4
##    y=14
##    z=7
    position=[x,y,z]
    a= [0 for _ in range(113)]
    a2= [0 for _ in range(113)]

    for j in range (0,113):
        a[j]= (f"1st_floor_cell_{j}")
        a2[j]=(f"2nd_floor_cell_{j}")
        

    p=14
    ##if z<=3:
    ##    for i in range (1,14):
    ##        print(i)
    ##        if x<=3*i&y<=3:
    ##            pos=a[i]
    ##        elif x<=3*i&y<=6:
    ##            pos=a[i+14]
    ##        elif x<=3*i&y<=9:
    ##            pos=a[i+28]
    ##        elif x<=3*i&y<=12:
    ##            pos=a[i+42]
    ##        elif x<=3*i&y<=15:
    ##            pos=a[i+56]
    ##        elif x<=3*i&y<=18:
    ##            pos=a[i+70]
    ##        elif x<=3*i&y<=21:
    ##            pos=a[i+84]
    ##        elif x<=3*i&y<=24:
    ##            pos=a[i+98]
    ##if z<=3:
    ##    for i in range (1,14):  ##1,15로해야되나?
    ##        for k in range (1,8):
    ##            if x<=3*i&y<=3*k:
    ##                pos=a[i+14*(k-1)]
    ##
    if z<=3:
        if y<=3:
            if x<=3:
                pos=a[1]
            elif x<=6:
                pos=a[2]
            elif x<=9:
                pos=a[3]
            elif x<=12:
                pos=a[4]
            elif x<=15:
                pos=a[5]
            elif x<=18:
                pos=a[6]
            elif x<=21:
                pos=a[7]
            elif x<=24:
                pos=a[8]
            elif x<=27:
                pos=a[9]
            elif x<=30:
                pos=a[10]
            elif x<=33:
                pos=a[11]
            elif x<=36:
                pos=a[12]
            elif x<=39:
                pos=a[13]
            elif x<=42:
                pos=a[14]


        elif y<=6: 
            
            if x<=3:
                pos=a[1+p]
            elif x<=6:
                pos=a[2+p]
            elif x<=9:
                pos=a[3+p]
            elif x<=12:
                pos=a[4+p]
            elif x<=15:
                pos=a[5+p]
            elif x<=18:
                pos=a[6+p]
            elif x<=21:
                pos=a[7+p]
            elif x<=24:
                pos=a[8+p]
            elif x<=27:
                pos=a[9+p]
            elif x<=30:
                pos=a[10+p]
            elif x<=33:
                pos=a[11+p]
            elif x<=36:
                pos=a[12+p]
            elif x<=39:
                pos=a[13+p]
            elif x<=42:
                pos=a[14+p]


        elif y<=9: 
            
            if x<=3:
                pos=a[1+2*p]
            elif x<=6:
                pos=a[2+2*p]
            elif x<=9:
                pos=a[3+2*p]
            elif x<=12:
                pos=a[4+2*p]
            elif x<=15:
                pos=a[5+2*p]
            elif x<=18:
                pos=a[6+2*p]
            elif x<=21:
                pos=a[7+2*p]
            elif x<=24:
                pos=a[8+2*p]
            elif x<=27:
                pos=a[9+2*p]
            elif x<=30:
                pos=a[10+2*p]
            elif x<=33:
                pos=a[11+2*p]
            elif x<=36:
                pos=a[12+2*p]
            elif x<=39:
                pos=a[13+2*p]
            elif x<=42:
                pos=a[14+2*p]

        elif y<=12: 
            
            if x<=3:
                pos=a[1+3*p]
            elif x<=6:
                pos=a[2+3*p]
            elif x<=9:
                pos=a[3+3*p]
            elif x<=12:
                pos=a[4+3*p]
            elif x<=15:
                pos=a[5+3*p]
            elif x<=18:
                pos=a[6+3*p]
            elif x<=21:
                pos=a[7+3*p]
            elif x<=24:
                pos=a[8+3*p]
            elif x<=27:
                pos=a[9+3*p]
            elif x<=30:
                pos=a[10+3*p]
            elif x<=33:
                pos=a[11+3*p]
            elif x<=36:
                pos=a[12+3*p]
            elif x<=39:
                pos=a[13+3*p]
            elif x<=42:
                pos=a[14+3*p]


        elif y<=15: 
            
            if x<=3:
                pos=a[1+4*p]
            elif x<=6:
                pos=a[2+4*p]
            elif x<=9:
                pos=a[3+4*p]
            elif x<=12:
                pos=a[4+4*p]
            elif x<=15:
                pos=a[5+4*p]
            elif x<=18:
                pos=a[6+4*p]
            elif x<=21:
                pos=a[7+4*p]
            elif x<=24:
                pos=a[8+4*p]
            elif x<=27:
                pos=a[9+4*p]
            elif x<=30:
                pos=a[10+4*p]
            elif x<=33:
                pos=a[11+4*p]
            elif x<=36:
                pos=a[12+4*p]
            elif x<=39:
                pos=a[13+4*p]
            elif x<=42:
                pos=a[14+4*p]
        elif y<=18: 
            
            if x<=3:
                pos=a[1+5*p]
            elif x<=6:
                pos=a[2+5*p]
            elif x<=9:
                pos=a[3+5*p]
            elif x<=12:
                pos=a[4+5*p]
            elif x<=15:
                pos=a[5+5*p]
            elif x<=18:
                pos=a[6+5*p]
            elif x<=21:
                pos=a[7+5*p]
            elif x<=24:
                pos=a[8+5*p]
            elif x<=27:
                pos=a[9+5*p]
            elif x<=30:
                pos=a[10+5*p]
            elif x<=33:
                pos=a[11+5*p]
            elif x<=36:
                pos=a[12+5*p]
            elif x<=39:
                pos=a[13+5*p]
            elif x<=42:
                pos=a[14+5*p]

        elif y<=21: 
            
            if x<=3:
                pos=a[1+6*p]
            elif x<=6:
                pos=a[2+6*p]
            elif x<=9:
                pos=a[3+6*p]
            elif x<=12:
                pos=a[4+6*p]
            elif x<=15:
                pos=a[5+6*p]
            elif x<=18:
                pos=a[6+6*p]
            elif x<=21:
                pos=a[7+6*p]
            elif x<=24:
                pos=a[8+6*p]
            elif x<=27:
                pos=a[9+6*p]
            elif x<=30:
                pos=a[10+6*p]
            elif x<=33:
                pos=a[11+6*p]
            elif x<=36:
                pos=a[12+6*p]
            elif x<=39:
                pos=a[13+6*p]
            elif x<=42:
                pos=a[14+6*p]


        elif y<=24: 
            
            if x<=3:
                pos=a[1+7*p]
            elif x<=6:
                pos=a[2+7*p]
            elif x<=9:
                pos=a[3+7*p]
            elif x<=12:
                pos=a[4+7*p]
            elif x<=15:
                pos=a[5+7*p]
            elif x<=18:
                pos=a[6+7*p]
            elif x<=21:
                pos=a[7+7*p]
            elif x<=24:
                pos=a[8+7*p]
            elif x<=27:
                pos=a[9+7*p]
            elif x<=30:
                pos=a[10+7*p]
            elif x<=33:
                pos=a[11+7*p]
            elif x<=36:
                pos=a[12+7*p]
            elif x<=39:
                pos=a[13+7*p]
            elif x<=42:
                pos=a[14+7*p]



    elif z<=6:
        if y<=3:
            if x<=3:
                 pos=a2[1]
            elif x<=6:
                pos=a2[2]
            elif x<=9:
                pos=a2[3]
            elif x<=12:
                pos=a2[4]
            elif x<=15:
                pos=a2[5]
            elif x<=18:
                pos=a2[6]
            elif x<=21:
                pos=a2[7]
            elif x<=24:
                pos=a2[8]
            elif x<=27:
                pos=a2[9]
            elif x<=30:
                pos=a2[10]
            elif x<=33:
                pos=a2[11]
            elif x<=36:
                pos=a2[12]
            elif x<=39:
                pos=a2[13]
            elif x<=42:
                pos=a2[14]


        elif y<=6: 
            p=14
            if x<=3:
                pos=a2[1+p]
            elif x<=6:
                pos=a2[2+p]
            elif x<=9:
                pos=a2[3+p]
            elif x<=12:
                pos=a2[4+p]
            elif x<=15:
                pos=a2[5+p]
            elif x<=18:
                pos=a2[6+p]
            elif x<=21:
                pos=a2[7+p]
            elif x<=24:
                pos=a2[8+p]
            elif x<=27:
                pos=a2[9+p]
            elif x<=30:
                pos=a2[10+p]
            elif x<=33:
                pos=a2[11+p]
            elif x<=36:
                pos=a2[12+p]
            elif x<=39:
                pos=a2[13+p]
            elif x<=42:
                pos=a2[14+p]


        elif y<=9: 
            
            if x<=3:
                pos=a2[1+2*p]
            elif x<=6:
                pos=a2[2+2*p]
            elif x<=9:
                pos=a2[3+2*p]
            elif x<=12:
                pos=a2[4+2*p]
            elif x<=15:
                pos=a2[5+2*p]
            elif x<=18:
                pos=a2[6+2*p]
            elif x<=21:
                pos=a2[7+2*p]
            elif x<=24:
                pos=a2[8+2*p]
            elif x<=27:
                pos=a2[9+2*p]
            elif x<=30:
                pos=a2[10+2*p]
            elif x<=33:
                pos=a2[11+2*p]
            elif x<=36:
                pos=a2[12+2*p]
            elif x<=39:
                pos=a2[13+2*p]
            elif x<=42:
                pos=a2[14+2*p]

        elif y<=12: 
            
            if x<=3:
                pos=a2[1+3*p]
            elif x<=6:
                pos=a2[2+3*p]
            elif x<=9:
                pos=a2[3+3*p]
            elif x<=12:
                pos=a2[4+3*p]
            elif x<=15:
                pos=a2[5+3*p]
            elif x<=18:
                pos=a2[6+3*p]
            elif x<=21:
                pos=a2[7+3*p]
            elif x<=24:
                pos=a2[8+3*p]
            elif x<=27:
                pos=a2[9+3*p]
            elif x<=30:
                pos=a2[10+3*p]
            elif x<=33:
                pos=a2[11+3*p]
            elif x<=36:
                pos=a2[12+3*p]
            elif x<=39:
                pos=a2[13+3*p]
            elif x<=42:
                pos=a2[14+3*p]


        elif y<=15: 
            
            if x<=3:
                pos=a2[1+4*p]
            elif x<=6:
                pos=a2[2+4*p]
            elif x<=9:
                pos=a2[3+4*p]
            elif x<=12:
                pos=a2[4+4*p]
            elif x<=15:
                pos=a2[5+4*p]
            elif x<=18:
                pos=a2[6+4*p]
            elif x<=21:
                pos=a2[7+4*p]
            elif x<=24:
                pos=a2[8+4*p]
            elif x<=27:
                pos=a2[9+4*p]
            elif x<=30:
                pos=a2[10+4*p]
            elif x<=33:
                pos=a2[11+4*p]
            elif x<=36:
                pos=a2[12+4*p]
            elif x<=39:
                pos=a2[13+4*p]
            elif x<=42:
                pos=a2[14+4*p]
        elif y<=18: 
            
            if x<=3:
                pos=a2[1+5*p]
            elif x<=6:
                pos=a2[2+5*p]
            elif x<=9:
                pos=a2[3+5*p]
            elif x<=12:
                pos=a2[4+5*p]
            elif x<=15:
                pos=a2[5+5*p]
            elif x<=18:
                pos=a2[6+5*p]
            elif x<=21:
                pos=a2[7+5*p]
            elif x<=24:
                pos=a2[8+5*p]
            elif x<=27:
                pos=a2[9+5*p]
            elif x<=30:
                pos=a2[10+5*p]
            elif x<=33:
                pos=a2[11+5*p]
            elif x<=36:
                pos=a2[12+5*p]
            elif x<=39:
                pos=a2[13+5*p]
            elif x<=42:
                pos=a2[14+5*p]
        elif y<=21: 
            
            if x<=3:
                pos=a2[1+6*p]
            elif x<=6:
                pos=a2[2+6*p]
            elif x<=9:
                pos=a2[3+6*p]
            elif x<=12:
                pos=a2[4+6*p]
            elif x<=15:
                pos=a2[5+6*p]
            elif x<=18:
                pos=a2[6+6*p]
            elif x<=21:
                pos=a2[7+6*p]
            elif x<=24:
                pos=a2[8+6*p]
            elif x<=27:
                pos=a2[9+6*p]
            elif x<=30:
                pos=a2[10+6*p]
            elif x<=33:
                pos=a2[11+6*p]
            elif x<=36:
                pos=a2[12+6*p]
            elif x<=39:
                pos=a2[13+6*p]
            elif x<=42:
                pos=a2[14+6*p]


        elif y<=24: 
            
            if x<=3:
                pos=a2[1+7*p]
            elif x<=6:
                pos=a2[2+7*p]
            elif x<=9:
                pos=a2[3+7*p]
            elif x<=12:
                pos=a2[4+7*p]
            elif x<=15:
                pos=a2[5+7*p]
            elif x<=18:
                pos=a2[6+7*p]
            elif x<=21:
                pos=a2[7+7*p]
            elif x<=24:
                pos=a2[8+7*p]
            elif x<=27:
                pos=a2[9+7*p]
            elif x<=30:
                pos=a2[10+7*p]
            elif x<=33:
                pos=a2[11+7*p]
            elif x<=36:
                pos=a2[12+7*p]
            elif x<=39:
                pos=a2[13+7*p]
            elif x<=42:
                pos=a2[14+7*p]



   
              
    return pos



    
