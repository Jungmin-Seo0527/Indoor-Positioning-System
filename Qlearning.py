import numpy as np
import random as rand
import matplotlib.pyplot as plt
import math
from matplotlib import colors

def Qlearning(case,num,input_state,input_floor) :
    col = 14
    row = 8
    output_size = 4 # action : up, down, right, left
    input_size = col*row
    # environment size
    fire = -100
    block = -100
    exit = 3
    road = -2
    # 각각의 상황에 대한 reward

    dis = .85
    a = .7
    num_episodes = 3000
    N = num
    #현재 state에서 사람의 수 
    input_state = input_state
    # 입력받은 현재 state
    input_floor = input_floor
    # 입력받은 현재 floor
    case = case


    first_reward_array1 = np.zeros(input_size)
    # 1층에서 모든 exit에 대해서 Q-learning을 할 environment
    second_reward_array1 = np.zeros(input_size)
    # 2층에서 모든 exit에 대해서 Q-learning을 할 environment
    first_reward_array2_1 = np.zeros(input_size)
    # 1층에서 최단 거리 exit를 막고 Q-learning을 할 environment
    first_reward_array2_2 = np.zeros(input_size)
    # 1층에서 최단 거리 exit를 막고 Q-learning을 할 environment
    second_reward_array2 = np.zeros(input_size)
    # 2층에서 최단 거리 exit를 막고 Q-learning을 할 environment
    reward_array1 = np.zeros(input_size)
    # 1층 environment
    reward_array2 = np.zeros(input_size)
    # 2층 environment
    xy1=np.loadtxt('forprint1.csv',delimiter=',',dtype=np.float64)
    xy2=np.loadtxt('forprint2.csv',delimiter=',',dtype=np.float64)
    cmap = colors.ListedColormap(['honeydew','mistyrose','lightgray','dimgrey','yellow','red'])

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

    if case ==1 :
        xy1[4][13]=6
        xy1[5][13]=6
        xy1[6][13]=6
        xy1[6][12]=6
        xy1[7][13]=6
        xy1[7][12]=6

        xy2[7][13]=6
        xy2[7][12]=6
        xy2[6][13]=6
    elif case ==2 :
        xy1[6][0]=6
        xy1[7][0]=6
        xy1[7][1]=6

        xy2[4][0]=6
        xy2[5][0]=6
        xy2[6][0]=6
        xy2[6][1]=6
        xy2[7][0]=6
        xy2[7][1]=6
    elif case ==3 :
        xy1[6][0]=6
        xy1[7][0]=6
        xy1[7][1]=6

        xy2[4][0]=6
        xy2[5][0]=6
        xy2[6][0]=6
        xy2[6][1]=6
        xy2[7][0]=6
        xy2[7][1]=6
    elif case ==4 :
        xy1[3][0]=6
        xy1[3][1]=6
        xy1[4][1]=6
        xy1[5][0]=6
        xy1[5][1]=6

        xy2[5][0]=6
        xy2[5][1]=6
    elif case ==5 :
        xy1[0][6]=6
        xy1[1][6]=6
        xy1[1][7]=6
        xy1[1][8]=6
        xy1[0][8]=6

        xy2[0][8]=6
        xy2[1][8]=6
    shortest_exit1 = 500
    # 1층의 현재위치에서 shortest_exit을 넣을 공간
    shortest_exit2 = 500
    # 2층의 현재 위치에서 shortest_exit을 넣을 공간
    selected_exit1 = 500
    # 2층에서 1층으로 내려가는 출구(최단거리)
    selected_exit2 = 500
    # 2층에서 1층으로 내려가는 출구(두번째 최단거리)
    isolated6 = 0
    isolated56 = 0
    isolated105 = 0
    isolated_1F = 0
    isolated_2F= 0
    isolated1 = 0
    isolated2 = 0
    # 화재에 의한 고립 여부
    env=1

    Q1 = np.zeros([input_size, output_size])
    #1층에서 최단거리
    Q2 = np.zeros([input_size, output_size])
    #2층에서 최단거리
    Q3 = np.zeros([input_size, output_size])
    #2층에서 두번째 최단거리
    Q4_1 = np.zeros([input_size, output_size])
    #1층에서 두번째 최단거리(2층에서 최단경로)
    Q4_2 = np.zeros([input_size, output_size])
    #1층에서 두번째 최단거리(2층에서 두번째 최단경로)
    Q5 = np.zeros([input_size, output_size])
    #화재가 없을 경우 1층 최단거리
    Q6 = np.zeros([input_size, output_size])
    #화재가 없을 경우 2층 최단거리

    if N>9 :
        a = 0.5
    else :
        a = -0.5*math.log(N,10)+1

    def fire_function1(reward_array):
        if case ==1 : 
            reward_array[69]=fire
            reward_array[83]=fire
            reward_array[97]=fire
            reward_array[98]=fire
            reward_array[111]=fire
            reward_array[110]=fire
        elif case ==2 :
            reward_array[84]=fire
            reward_array[98]=fire
            reward_array[99]=fire
        elif case ==3 :
            reward_array[84]=fire
            reward_array[98]=fire
            reward_array[99]=fire
        elif case ==4:
            reward_array[42]=fire
            reward_array[43]=fire
            reward_array[57]=fire
            reward_array[70]=fire
            reward_array[71]=fire
        elif case==5 :
            reward_array[6]=fire
            reward_array[8]=fire
            reward_array[20]=fire
            reward_array[21]=fire
            reward_array[22]=fire
    # 화재가 발생하는 위치 (1F)
    def fire_function2(reward_array):
        if case == 1 :
            reward_array[111]=fire
            reward_array[97]=fire
            reward_array[110]=fire
        elif case ==2:
            reward_array[56]=fire
            reward_array[70]=fire
            reward_array[84]=fire
            reward_array[85]=fire
            reward_array[98]=fire
            reward_array[99]=fire
        elif case==3 :
            reward_array[56]=fire
            reward_array[70]=fire
            reward_array[84]=fire
            reward_array[85]=fire
            reward_array[98]=fire
            reward_array[99]=fire
        elif case==4 :
            reward_array[70]=fire
            reward_array[71]=fire
        elif case==5 :
            reward_array[8]=fire
            reward_array[22]=fire
        # 화재가 발생하는 위치 (2F)
        
    def reset(reward_array):
        for i in range(input_size) : 
            reward_array[i] = block

        for i in range(2) :
            for j in range(col) :
                reward_array[(3+i)*col+j] = road

        for i in range(2) :
            for j in range(row) :
                reward_array[col * j + 6 + i] = road
                
        if floor == 1 :
            if (env==1) :
                reward_array[69] = exit
                reward_array[7] = exit
            else :
                reward_array[69] = exit
                reward_array[7] = exit
                reward_array[shortest_exit1]=fire
                
        if floor == 2 :
            if (env==1) :
                reward_array[56]=np.max(Q1[56,:])
                reward_array[6]=np.max(Q1[6,:])
                reward_array[105]=np.max(Q1[105,:])

                a = min(reward_array[56],reward_array[6],reward_array[105])
                if a < 0 :
                    b = - a + 3
                    
                    reward_array[56] = reward_array[56] + b
                    reward_array[6] = reward_array[6] + b
                    reward_array[105] = reward_array[105] + b
                if isolated56 == 1 :
                    reward_array[56]=np.max(Q1[56,:])
                if isolated6 == 1 :
                    reward_array[6]=np.max(Q1[6,:])
                if isolated105 == 1 :
                    reward_array[105]=np.max(Q1[105,:])
                
                        
            else :
                reward_array[56]=np.max(Q1[56,:])
                reward_array[6]=np.max(Q1[6,:])
                reward_array[105]=np.max(Q1[105,:])

                a = min(reward_array[56],reward_array[6],reward_array[105])
                if a < 0 :
                    b = - a + 3
                    reward_array[56] = reward_array[56] + b
                    reward_array[6] = reward_array[6] + b
                    reward_array[105] = reward_array[105] + b
                    reward_array[shortest_exit2]=fire
                    
                if isolated56 == 1 :
                    reward_array[56]=np.max(Q1[56,:])
                if isolated6 == 1 :
                    reward_array[6]=np.max(Q1[6,:])
                if isolated105 == 1 :
                    reward_array[105]=np.max(Q1[105,:])
                            
        state = rand.randrange(0,input_size)
        # 현재 state를 random하게
        state = room(state)
        # 방에서 시작하는 경우 위치 옮기기
        return (state)

    def room(state):
        for i in range(3):
             for j in range(3):
                if state==(col*i)+j:
                    state=43
                else :
                    state = state

        #room1               
        for i in range(3):
             for j in range(3):
                if state==(col*i)+j+3:
                    state=46
                else :
                    state = state
        #room2                    
        for i in range(3):
             for j in range(3):
                if state==(col*i)+j+8:
                    state=51
                else :
                    state = state
        #room3               
        for i in range(3):
             for j in range(3):
                if state==(col*i)+j+11:
                    state=54
                else :
                    state = state
        #room4 
        for i in range(3):
             for j in range(3):
                if state== 70 + (col*i)+j:
                    state=57
                else :
                    state = state
        #room5        
        for i in range(3):
             for j in range(3):
                if state== 73 + (col*i)+j:
                    state=60
                else :
                    state = state
        #room6        
        for i in range(3):
             for j in range(3):
                if state==78 + (col*i)+j:
                    state=65
                else :
                    state = state
        #room7         
        for i in range(3):
             for j in range(3):
                if state==81 + (col*i)+j:
                    state=68
                else :
                    state = state
        #room8
        return(state)
                    

    def step(action,reward_array):
        done=False
        reward=0
        if action==0: #up
            if 0<=state<col :
                next_state = state
                reward = block
                done=True
            else :
                next_state = state - col
                reward = reward_array[next_state]
                if reward == fire :
                    done = True
                if reward == block :
                    done = True

        if action == 1: #down
            if col*(row-1)<=state<col*row :
                next_state = state
                reward = block
                done = True
            else :
                next_state = state + col
                reward = reward_array[next_state]
                if reward == fire :
                    done = True
                if reward == block:
                    done = True
                    
        if action == 2: #right
            for j in range(row):
                if state == ((j+1)*col-1) :
                     next_state = state
                     reward = block
                     done = True
            if done == False :
                next_state = state + 1
                reward = reward_array[next_state]
                if reward == fire :
                    done = True
                if reward == block:
                    done = True
                    
        if action == 3: #left
            for j in range(row):
                if state == (j*col):
                    next_state = state
                    reward = block
                    done = True
                if done == False:
                    next_state = state - 1
                    reward = reward_array[next_state]
                    if reward == fire :
                        done = True
                    if reward == block:
                        done = True
                        
        if (floor == 2) and ((next_state==6)or(next_state==105)or(next_state==56)) : 
            done = True
        if (floor == 1) and ((next_state==7) or (next_state==69)) :
            done = True
        return (next_state, reward, done)


    ###############################################################################################
    for i in range( num_episodes ):
        floor = 1
        env = 1
        state = reset(reward_array1)
        done = False

        e=1/(i/10+1)
        while not done :
            if np.random.rand(1)< e :
                action = rand.randrange(0,output_size)
            else : 
                action = np.argmax(Q5[state, :])
            next_state, reward, done = step(action,reward_array1)
            Q5[state,action] = (1-a)* Q5[state,action] + a*(reward+ dis * np.max(Q5[next_state, :]))
            state=next_state
    #1F에서 화재 없이 최단거리 

    for i in range( num_episodes ):
        floor = 1
        env = 1
        state = reset(first_reward_array1)
        fire_function1(first_reward_array1)
        done = False
        
        e=1/(i/10+1)

        while not done :
            if np.random.rand(1)< e :
                action = rand.randrange(0,output_size)
            else : 
                action = np.argmax(Q1[state, :])
            next_state, reward, done = step(action,first_reward_array1)
                            
            Q1[state,action] = (1-a)* Q1[state,action] + a*(reward+ dis * np.max(Q1[next_state, :]))
            state=next_state
    #1F의 최단거리 Q-table
        
    state = 56
    done = False
    cnt = 0
    if (np.max(Q1[state,:])<-70) :
        isolated56 = 1
        done = True
    while not done :
        if (cnt > 40) :
            isolated56 = 1
            done = True
        else :     
            action = np.argmax(Q1[state, :])
            next_state, reward, done = step(action,first_reward_array1)
            cnt = cnt+1                
            state=next_state

    state = 105
    done = False
    cnt = 0
    if (np.max(Q1[state,:])<-70) :
        isolated105 = 1
        done = True    
    while not done :
        if (cnt > 40) :
            isolated105 = 1
            done = True
        else :     
            action = np.argmax(Q1[state, :])
            next_state, reward, done = step(action,first_reward_array1)
            cnt = cnt+1                
            state=next_state

    state = 6
    done = False
    cnt = 0
    if (np.max(Q1[state,:])<-70):
        isolated6 = 1
        done = True    
    while not done :
        if (cnt > 40) :
            isolated6 = 1
            done = True
        else :     
            action = np.argmax(Q1[state, :])
            next_state, reward, done = step(action,first_reward_array1)
            cnt = cnt+1                
            state=next_state
                
    ############################################################################################        
    if (input_floor == 1) :
        floor = 1
        env = 1
        state = reset(first_reward_array1)
        fire_function1(first_reward_array1)
        state = input_state
        state = room(state)
        done = False
        cnt = 0
        
        if (np.max(Q1[state,:])<-70) :
            isolated_1F = 1
            done = True
            
        while not done :
            if (cnt > 40) :
                isolated_1F = 1
                done = True
            else :     
                action = np.argmax(Q1[state, :])
                next_state, reward, done = step(action,first_reward_array1)
                cnt = cnt+1                
                state=next_state
        shortest_exit1 = state
                    
        if isolated_1F != 1 : 
            for i in range( num_episodes ):
                env = 0
                state = reset(first_reward_array2_1)
                fire_function1(first_reward_array2_1)
                done = False
            
                e=1/(i/10+1)

                while not done :
                    if np.random.rand(1)< e :
                        action = rand.randrange(0,output_size)
                    else : 
                        action = np.argmax(Q4_1[state, :])
                    next_state, reward, done = step(action,first_reward_array2_1)
                                    
                    Q4_1[state,action] = (1-a)* Q4_1[state,action] + a*(reward+ dis * np.max(Q4_1[next_state, :]))

                    state=next_state
    #1층의 2번째 최단거리를 구하는 Q-learning
               
            floor=1
            env = 0
            state = reset(first_reward_array2_1)
            fire_function1(first_reward_array2_1)
            state = input_state
            state = room(state)
            done = False
            cnt = 0
            
            if (np.max(Q4_1[state,:])<-70) :
                isolated1 = 1
                done = True
            while not done :
                if (cnt > 40) :
                    done = True
                    isolated1 = 1
                else : 
                    action = np.argmax(Q4_1[state, :])
                    next_state, reward, done = step(action,first_reward_array2_1)
                    cnt=cnt+1
                    state=next_state
            
    #########################################################################현재 위치가 1층인 경우 Q-learning
                    
    if (input_floor == 2 ) :
        for i in range( num_episodes ):
            floor = 2
            env = 1
            state = reset(reward_array2)
            done = False
            

            e=1/(i/10+1)

            while not done :
                if np.random.rand(1)< e :
                    action = rand.randrange(0,output_size)
                else : 
                    action = np.argmax(Q6[state, :])
                next_state, reward, done = step(action,reward_array2)
                                
                Q6[state,action] = (1-a)* Q6[state,action] + a*(reward+ dis * np.max(Q6[next_state, :]))
                state=next_state
    #2F에서 화재 없이 최단거리
            
        for i in range( num_episodes ):
            env = 1
            floor = 2                   
            state = reset(second_reward_array1)
            fire_function2(second_reward_array1)
            done = False
        
            e=1/(i/10+1)

            while not done :
                if np.random.rand(1)< e :
                    action = rand.randrange(0,output_size)
                else : 
                    action = np.argmax(Q2[state, :])
                next_state, reward, done = step(action,second_reward_array1)
                            
                Q2[state,action] = (1-a)* Q2[state,action] + a*(reward+ dis * np.max(Q2[next_state, :]))

                state=next_state
        
        env = 1
        state = reset(second_reward_array1)
        fire_function2(second_reward_array1)
        state = input_state
        state = room(state)
        done = False
        cnt = 0
        
        if (np.max(Q2[state,:])<-70) :
            isolated_2F = 1
            done = True
        while not done :
            if (cnt > 40) :
                done = True
                isolated_2F = 1
            else : 
                action = np.argmax(Q2[state, :])
                next_state, reward, done = step(action,second_reward_array1)
                cnt=cnt+1
                state=next_state
        selected_state1 = state
        shortest_exit2 = state
        #2F의 현재위치에서 최단거리를 Q-table을 구하고 고립되었는지 판단하는 Q-learning
        
        if isolated_2F !=1 :
            floor = 1
            env = 1
            state = reset(first_reward_array1)
            fire_function1(first_reward_array1)
            state = selected_state1
            state = room(state)
            done = False
            cnt = 0
            
            while not done :
                action = np.argmax(Q1[state, :])
                next_state, reward, done = step(action,first_reward_array1)
                cnt = cnt+1                
                state=next_state
            shortest_exit1 = state
            
            for i in range( num_episodes ):
                floor=1
                env = 0
                state = reset(first_reward_array2_1)
                fire_function1(first_reward_array2_1)
                done = False
                    
                e=1/(i/10+1)

                while not done :
                    if np.random.rand(1)< e :
                        action = rand.randrange(0,output_size)
                    else : 
                        action = np.argmax(Q4_1[state, :])
                    next_state, reward, done = step(action,first_reward_array2_1)
                    Q4_1[state,action] = (1-a)* Q4_1[state,action] + a*(reward+ dis * np.max(Q4_1[next_state, :]))
                    state=next_state
            #1층의 2번째 최단거리를 구하는 Q-learnin (2층에서 최단)
            
            for i in range( num_episodes ):
                floor=2
                env = 0
                state = reset(second_reward_array2)
                fire_function2(second_reward_array2)
                done = False
            
                e=1/(i/10+1)

                while not done :
                    if np.random.rand(1)< e :
                        action = rand.randrange(0,output_size)
                    else : 
                        action = np.argmax(Q3[state, :])
                    next_state, reward, done = step(action,second_reward_array2)
                                
                    Q3[state,action] = (1-a)* Q3[state,action] + a*(reward+ dis * np.max(Q3[next_state, :]))
                    state=next_state

            floor=2
            env = 0
            state = reset(second_reward_array2)
            fire_function2(second_reward_array2)
            state = input_state
            state = room(state)
            done = False
            cnt = 0
            
            while not done :
                action = np.argmax(Q3[state, :])
                next_state, reward, done = step(action,second_reward_array2)
                cnt=cnt+1
                state=next_state
            selected_state2 = state
            shortest_exit2 = state
            #2층의 2번째 최단거리를 구하는 Q-learning

            for i in range( num_episodes ):
                floor=1
                env = 0
                state = reset(first_reward_array2_2)
                fire_function1(first_reward_array2_2)
                done = False
                    
                e=1/(i/10+1)

                while not done :
                    if np.random.rand(1)< e :
                        action = rand.randrange(0,output_size)
                    else : 
                        action = np.argmax(Q4_2[state, :])
                    next_state, reward, done = step(action,first_reward_array2_2)
                    Q4_2[state,action] = (1-a)* Q4_2[state,action] + a*(reward+ dis * np.max(Q4_2[next_state, :]))
                    state=next_state
        #1층의 2번째 최단거리를 구하는 Q-learnin (2층에서 최단)
                        
            floor=1
            env = 0
            state = reset(first_reward_array2_1)
            fire_function1(first_reward_array2_1)
            state = selected_state1
            state = room(state)
            done = False
            cnt = 0
            
            if (np.max(Q4_1[state,:])<-70) :
                isolated1 = 1
                done = True
            while not done :
                if (cnt > 40) :
                    done = True
                    isolated1 = 1
                else : 
                    action = np.argmax(Q4_1[state, :])
                    next_state, reward, done = step(action,first_reward_array2_1)
                    cnt=cnt+1
                    state=next_state

            floor=1
            env = 0
            state = reset(first_reward_array2_2)
            fire_function1(first_reward_array2_2)
            state = selected_state2
            state = room(state)
            done = False
            cnt = 0
            
            if (np.max(Q4_2[state,:])<-70) :
                isolated2 = 1
                done = True
            while not done :
                if (cnt > 40) :
                    done = True
                    isolated2 = 1
                else : 
                    action = np.argmax(Q4_2[state, :])
                    next_state, reward, done = step(action,first_reward_array2_2)
                    cnt=cnt+1
                    state=next_state
        
    #########################################################################현재 위치가 2층인 경우 Q-learning
    r1 = np.zeros(N)
    c1 = np.zeros(N)

    r2 = np.zeros(N)
    c2 = np.zeros(N)

    r3 = np.zeros(N)
    c3 = np.zeros(N)

    state = input_state
    state = room(state)
    state1 = state
    state2 = state
    state3 = state
    state4 = state
        
    done = False
    done1 = False
    done2 = False
    done3 = False
    done4 = False
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    s6 = 0

    for i in range (N) :
        if np.random.rand(1) < a :
            s1 = s1+1
        else:
            s2 = s2+1
    if s1 != 0 :   
        if s1>9 :
            a = 0.5
        else :
            a = -0.5*math.log(s1,10)+1

        for i in range (s1) :
            if np.random.rand(1) < a :
                s3 = s3+1
            else:
                s4 = s4 +1
    if s2 != 0 :
        if s2>9 :
            a = 0.5
        else :
            a = -0.5*math.log(s2,10)+1
                
        for i in range (s2) :
            if np.random.rand(1) < a :
                s5 = s5+1
            else:
                s6 = s6+1

    if input_floor ==2:
        floor=2
        if isolated_2F == 1 :
            print('iosolated!')
            while not (done1) :
                map = np.reshape(xy2,[-1,col])
                r1=int(state1/14)
                c1=int(state1%14)
                plt.scatter(c1+0.5+0.02*i,8-r1-0.5+0.02*i,c='coral');

                temp_state1 = state1
                have_done = 0
                while(have_done==0):
                    r2=int(temp_state1/14)
                    c2=int(temp_state1%14)
                        
                    state = temp_state1
                    action = np.argmax(Q6[state,:])
                    next_state, reward, done = step(action,reward_array2) 
                    state = next_state
                    temp_state1 = state
                                
                    r3 = int(temp_state1/14)
                    c3 = int(temp_state1%14)
                    plt.plot([c2+0.5+0.02*i,c3+0.5+0.02*i],[8-r2-0.5+0.02*i,8-r3-0.5+0.02*i],'coral')
                    if done ==True:
                        have_done=1;
                        done = False

                if done1 == False :
                    state = state1
                    action = np.argmax(Q6[state, :])
                    next_state, reward, done = step(action,reward_array2)                    
                    state=next_state
                    state1 = state
                    if done == True:
                        done1 = True
                        done = False
                        
                second_floor()
                plt.imshow(map,cmap=cmap, extent=[0,14,0,8])
                plt.title('second floor')
                plt.pause(0.5)
                plt.draw()
                plt.clf()
            floor= 1    
            done1 = False    
            while not (done1) :
                map = np.reshape(xy1,[-1,col])
                r1=int(state1/14)
                c1=int(state1%14)
                plt.scatter(c1+0.5+0.02*i,8-r1-0.5+0.02*i,c='coral');

                temp_state1 = state1
                have_done = 0
                while(have_done==0):
                    r2=int(temp_state1/14)
                    c2=int(temp_state1%14)
                        
                    state = temp_state1
                    action = np.argmax(Q5[state,:])
                    next_state, reward, done = step(action,reward_array1) 
                    state = next_state
                    temp_state1 = state
                                
                    r3 = int(temp_state1/14)
                    c3 = int(temp_state1%14)
                    plt.plot([c2+0.5+0.02*i,c3+0.5+0.02*i],[8-r2-0.5+0.02*i,8-r3-0.5+0.02*i],'coral')
                    if done ==True:
                        have_done=1;
                        done = False

                if done1 == False :
                    state = state1
                    action = np.argmax(Q1[state, :])
                    next_state, reward, done = step(action,first_reward_array1)                    
                    state=next_state
                    state1 = state
                    if done == True:
                        done1 = True
                        done = False
                        
                first_floor()
                plt.imshow(map,cmap=cmap, extent=[0,14,0,8])
                plt.title('first floor')
                plt.pause(0.5)
                plt.draw()
                plt.clf()
                #2F 고립됨

        else :
            while not (done1 and done2) :
                map = np.reshape(xy2,[-1,col])
                for i in range(s1):
                    r1[i]=int(state1/14)
                    c1[i]=int(state1%14)
                    plt.scatter(c1[i]+0.5+0.02*i,8-r1[i]-0.5+0.02*i,c='coral');

                for i in range(s2):
                    r1[s1+i]=int(state2/14)
                    c1[s1+i]=int(state2%14)
                    plt.scatter(c1[s1+i]+0.5+0.02*i,8-r1[s1+i]-0.5+0.02*i,c='orange');
                if done1 == False :     
                    for i in range(s1):
                        temp_state1 = state1
                        have_done = 0
                        while(have_done==0):
                            r2[i]=int(temp_state1/14)
                            c2[i]=int(temp_state1%14)
                            
                            state = temp_state1
                            action = np.argmax(Q2[state,:])
                            next_state, reward, done = step(action,second_reward_array1) 
                            state = next_state
                            temp_state1 = state
                                    
                            r3[i] = int(temp_state1/14)
                            c3[i] = int(temp_state1%14)
                            plt.plot([c2[i]+0.5+0.02*i,c3[i]+0.5+0.02*i],[8-r2[i]-0.5+0.02*i,8-r3[i]-0.5+0.02*i],'coral')

                            if done ==True:
                                have_done=1;
                                done = False
                if done2 == False : 
                    for i in range(s2):
                        temp_state2 = state2
                        have_done = 0
                        while(have_done==0):
                            r2[s1+i]=int(temp_state2/14)
                            c2[s1+i]=int(temp_state2%14)
                            
                            state = temp_state2
                            action = np.argmax(Q3[state,:])
                            next_state, reward, done = step(action,second_reward_array2) 
                            state = next_state
                            temp_state2 = state
                    
                            r3[s1+i] = int(temp_state2/14)
                            c3[s1+i] = int(temp_state2%14)
                            plt.plot([c2[s1+i]+0.5+0.02*i,c3[s1+i]+0.5+0.02*i],[8-r2[s1+i]-0.5+0.02*i,8-r3[s1+i]-0.5+0.02*i],'orange')

                            if done ==True:
                                have_done=1;
                                done = False
                if done1 == False :
                    state = state1
                    action = np.argmax(Q2[state, :])
                    next_state, reward, done = step(action,second_reward_array1)                    
                    state=next_state
                    state1 = state
                    if done == True:
                        done1 = True
                        done = False
                if done2 == False :
                    state = state2
                    action = np.argmax(Q3[state, :])
                    next_state, reward, done = step(action,second_reward_array2)                    
                    state=next_state
                    state2 = state
                    if done == True:
                        done2 = True
                        done = False
                second_floor()
                plt.imshow(map,cmap=cmap, extent=[0,14,0,8])
                plt.title('second floor')
                plt.pause(0.5)
                plt.draw()
                plt.clf()
        
            state3=state1
            state4=state2
            floor=1
            done1=False
            done2=False
            while not (done1 and done2 and done3 and done4) :
                map = np.reshape(xy1,[-1,col])
                for i in range(s3):
                    r1[i]=int(state1/14)
                    c1[i]=int(state1%14)
                    plt.scatter(c1[i]+0.5+0.02*i,8-r1[i]-0.5+0.02*i,c='coral');

                for i in range(s4):
                    r1[s3+i]=int(state2/14)
                    c1[s3+i]=int(state2%14)
                    plt.scatter(c1[s3+i]+0.5+0.02*i,8-r1[s3+i]-0.5+0.02*i,c='orange');
                    
                for i in range(s5):
                    r1[s3+s4+i]=int(state3/14)
                    c1[s3+s4+i]=int(state3%14)
                    plt.scatter(c1[s3+s4+i]+0.5+0.02*i,8-r1[s3+s4+i]-0.5+0.02*i,c='lightsalmon');

                for i in range(s6):
                    r1[s3+s4+s5+i]=int(state4/14)
                    c1[s3+s4+s5+i]=int(state4%14)
                    plt.scatter(c1[s3+s4+s5+i]+0.5+0.02*i,8-r1[s3+s4+s5+i]-0.5+0.02*i,c='gold');
                if done1 == False :
                    for i in range(s3):
                        temp_state1 = state1
                        have_done = 0
                        while(have_done==0):
                            r2[i]=int(temp_state1/14)
                            c2[i]=int(temp_state1%14)
                            
                            state = temp_state1
                            action = np.argmax(Q1[state,:])
                            next_state, reward, done = step(action,first_reward_array1) 
                            state = next_state
                            temp_state1 = state
                                    
                            r3[i] = int(temp_state1/14)
                            c3[i] = int(temp_state1%14)
                            plt.plot([c2[i]+0.5+0.02*i,c3[i]+0.5+0.02*i],[8-r2[i]-0.5+0.02*i,8-r3[i]-0.5+0.02*i],'coral')
                            if done ==True:
                                have_done=1;
                                done = False
                if done2 == False :
                    for i in range(s4):
                        temp_state2 = state2
                        have_done = 0
                        while(have_done==0):
                            r2[s3+i]=int(temp_state2/14)
                            c2[s3+i]=int(temp_state2%14)
                            
                            state = temp_state2
                            action = np.argmax(Q1[state,:])
                            next_state, reward, done = step(action,first_reward_array1) 
                            state = next_state
                            temp_state2 = state
                    
                            r3[s3+i] = int(temp_state2/14)
                            c3[s3+i] = int(temp_state2%14)
                            plt.plot([c2[s3+i]+0.5+0.02*i,c3[s3+i]+0.5+0.02*i],[8-r2[s3+i]-0.5+0.02*i,8-r3[s3+i]-0.5+0.02*i],'orange')
                            if done ==True:
                                have_done=1;
                                done = False
                if done3 == False :
                    for i in range(s5):
                        temp_state3 = state3
                        have_done = 0
                        while(have_done==0):
                            if isolated1==1 :
                                r2[s3+s4+i]=int(temp_state3/14)
                                c2[s3+s4+i]=int(temp_state3%14)
                                state = temp_state3
                                action = np.argmax(Q1[state,:])
                                next_state, reward, done = step(action,first_reward_array1)
                                state = next_state
                                temp_state3 = state
                                r3[s3+s4+i] = int(temp_state3/14)
                                c3[s3+s4+i] = int(temp_state3%14)
                                plt.plot([c2[s3+s4+i]+0.5+0.02*i,c3[s3+s4+i]+0.5+0.02*i],[8-r2[s3+s4+i]-0.5+0.02*i,8-r3[s3+s4+i]-0.5+0.02*i],'lightsalmon')
                                if done ==True:
                                    have_done=1;
                                    done = False
                            else:
                                r2[s3+s4+i]=int(temp_state3/14)
                                c2[s3+s4+i]=int(temp_state3%14)
                                state = temp_state3
                                action = np.argmax(Q4_1[state,:])
                                next_state, reward, done = step(action,first_reward_array2_1)
                                state = next_state
                                temp_state3 = state
                                r3[s3+s4+i] = int(temp_state3/14)
                                c3[s3+s4+i] = int(temp_state3%14)
                                plt.plot([c2[s3+s4+i]+0.5+0.02*i,c3[s3+s4+i]+0.5+0.02*i],[8-r2[s3+s4+i]-0.5+0.02*i,8-r3[s3+s4+i]-0.5+0.02*i],'lightsalmon')
                                if done ==True:
                                    have_done=1;
                                    done = False
                if done4 == False :
                    for i in range(s6):
                        temp_state4 = state4
                        have_done = 0
                        while(have_done==0):
                            if (isolated2==1):
                                r2[s3+s4+s5+i]=int(temp_state4/14)
                                c2[s3+s4+s5+i]=int(temp_state4%14)
                                state = temp_state4
                                action = np.argmax(Q1[state,:])
                                next_state, reward, done = step(action,first_reward_array1) 
                                state = next_state
                                temp_state4 = state
                                r3[s3+s4+s5+i] = int(temp_state4/14)
                                c3[s3+s4+s5+i] = int(temp_state4%14)
                                plt.plot([c2[s3+s4+s5+i]+0.5+0.02*i,c3[s3+s4+s5+i]+0.5+0.02*i],[8-r2[s3+s4+s5+i]-0.5+0.02*i,8-r3[s3+s4+s5+i]-0.5+0.02*i],'gold')
                                if done ==True:
                                    have_done=1;
                                    done = False
                            else :
                                r2[s3+s4+s5+i]=int(temp_state4/14)
                                c2[s3+s4+s5+i]=int(temp_state4%14)
                                state = temp_state4
                                action = np.argmax(Q4_2[state,:])
                                next_state, reward, done = step(action,first_reward_array2_2) 
                                state = next_state
                                temp_state4 = state
                                r3[s3+s4+s5+i] = int(temp_state4/14)
                                c3[s3+s4+s5+i] = int(temp_state4%14)
                                plt.plot([c2[s3+s4+s5+i]+0.5+0.02*i,c3[s3+s4+s5+i]+0.5+0.02*i],[8-r2[s3+s4+s5+i]-0.5+0.02*i,8-r3[s3+s4+s5+i]-0.5+0.02*i],'gold')
                                if done ==True:
                                    have_done=1;
                                    done = False
                                
                if done1 == False :
                    state = state1
                    action = np.argmax(Q1[state, :])
                    next_state, reward, done = step(action,first_reward_array1)                    
                    state=next_state
                    state1 = state
                    if done == True:
                        done1 = True
                        done = False

                if done2 == False :
                    state = state2
                    action = np.argmax(Q1[state, :])
                    next_state, reward, done = step(action,first_reward_array1)                    
                    state=next_state
                    state2 = state
                    if done == True:
                        done2 = True
                        done = False
                        
                if done3 == False :
                    if isolated1 == 1:
                        state = state3
                        action = np.argmax(Q1[state, :])
                        next_state, reward, done = step(action,first_reward_array1)                    
                        state=next_state
                        state3 = state
                        if done == True:
                            done3 = True
                            done = False
                    else :
                        state = state3
                        action = np.argmax(Q4_1[state, :])
                        next_state, reward, done = step(action,first_reward_array2_1)                    
                        state=next_state
                        state3 = state
                        if done == True:
                            done3 = True
                            done = False
                            
                if done4 == False :
                    if (isolated2 == 1):
                        state = state4
                        action = np.argmax(Q1[state, :])
                        next_state, reward, done = step(action,first_reward_array1)                    
                        state=next_state
                        state4 = state
                        if done == True:
                            done4 = True
                            done = False
                    else :
                        state = state4
                        action = np.argmax(Q4_2[state, :])
                        next_state, reward, done = step(action,first_reward_array2_2)                    
                        state=next_state
                        state4 = state
                        if done == True:
                            done4 = True
                            done = False
                            
                first_floor()
                plt.imshow(map,cmap=cmap, extent=[0,14,0,8])
                plt.title('first floor')
                plt.pause(0.5)
                plt.draw()
                plt.clf()
        
            #2F 고립되지 않음
    if input_floor == 1:
        floor=1
        if isolated_1F == 1:
            print('isolated!')
            map = np.reshape(xy1,[-1,col])
            r1=int(state1/14)
            c1=int(state1%14)
            plt.scatter(c1+0.5+0.02*i,8-r1-0.5+0.02*i,c='coral');
            temp_state1 = state1
            have_done = 0
            while not (done1) :
                while(have_done==0):
                    r2=int(temp_state1/14)
                    c2=int(temp_state1%14)
                        
                    state = temp_state1
                    action = np.argmax(Q5[state,:])
                    next_state, reward, done = step(action,reward_array1) 
                    state = next_state
                    temp_state1 = state
                                
                    r3 = int(temp_state1/14)
                    c3 = int(temp_state1%14)
                    plt.plot([c2+0.5+0.02*i,c3+0.5+0.02*i],[8-r2-0.5+0.02*i,8-r3-0.5+0.02*i],'coral')
                    if done ==True:
                        have_done=1;
                        done = False

                if done1 == False :
                    state = state1
                    action = np.argmax(Q5[state, :])
                    next_state, reward, done = step(action,reward_array1)                    
                    state=next_state
                    state1 = state
                    if done == True:
                        done1 = True
                        done = False
                        
                first_floor()
                plt.imshow(map,cmap=cmap, extent=[0,14,0,8])
                plt.title('first floor')
                plt.pause(0.5)
                plt.draw()
        
        #1F 고립
        else :
            while not (done1 and done2) :
                if s2 == 0 :
                    done2 = True
                    
                map = np.reshape(xy1,[-1,col])
                for i in range(s1):
                    r1[i]=int(state1/14)
                    c1[i]=int(state1%14)
                    plt.scatter(c1[i]+0.5+0.02*i,8-r1[i]-0.5+0.02*i,c='coral');

                for i in range(s2):
                    r1[s1+i]=int(state2/14)
                    c1[s1+i]=int(state2%14)
                    plt.scatter(c1[s1+i]+0.5+0.02*i,8-r1[s1+i]-0.5+0.02*i,c='orange');
                if done1 == False :     
                    for i in range(s1):
                        temp_state1 = state1
                        have_done = 0
                        while(have_done==0):
                            r2[i]=int(temp_state1/14)
                            c2[i]=int(temp_state1%14)
                            
                            state = temp_state1
                            action = np.argmax(Q1[state,:])
                            next_state, reward, done = step(action,first_reward_array1) 
                            state = next_state
                            temp_state1 = state
                                    
                            r3[i] = int(temp_state1/14)
                            c3[i] = int(temp_state1%14)
                            plt.plot([c2[i]+0.5+0.02*i,c3[i]+0.5+0.02*i],[8-r2[i]-0.5+0.02*i,8-r3[i]-0.5+0.02*i],'coral')
                            if done ==True:
                                have_done=1;
                                done = False
                if done2 == False :               
                    for i in range(s2):
                        if isolated1 == 0:
                            temp_state2 = state2
                            have_done = 0
                            while(have_done==0):
                                r2[s1+i]=int(temp_state2/14)
                                c2[s1+i]=int(temp_state2%14)
                                    
                                state = temp_state2
                                action = np.argmax(Q4_1[state,:])
                                next_state, reward, done = step(action,first_reward_array2_1) 
                                state = next_state
                                temp_state2 = state
                            
                                r3[s1+i] = int(temp_state2/14)
                                c3[s1+i] = int(temp_state2%14)
                                plt.plot([c2[s1+i]+0.5+0.02*i,c3[s1+i]+0.5+0.02*i],[8-r2[s1+i]-0.5+0.02*i,8-r3[s1+i]-0.5+0.02*i],'orange')
                                if done ==True:
                                    have_done=1;
                                    done = False
                        else :
                            temp_state2 = state2
                            have_done = 0
                            while(have_done==0):
                                r2[s1+i]=int(temp_state2/14)
                                c2[s1+i]=int(temp_state2%14)
                                    
                                state = temp_state2
                                action = np.argmax(Q1[state,:])
                                next_state, reward, done = step(action,first_reward_array1) 
                                state = next_state
                                temp_state2 = state
                            
                                r3[s1+i] = int(temp_state2/14)
                                c3[s1+i] = int(temp_state2%14)
                                plt.plot([c2[s1+i]+0.5+0.02*i,c3[s1+i]+0.5+0.02*i],[8-r2[s1+i]-0.5+0.02*i,8-r3[s1+i]-0.5+0.02*i],'orange')
                                if done ==True:
                                    have_done=1;
                                    done = False


                if done1 == False :
                    state = state1
                    action = np.argmax(Q1[state, :])
                    next_state, reward, done = step(action,first_reward_array1)                    
                    state=next_state
                    state1 = state
                    if done == True:
                        done1 = True
                        done = False
                if done2 == False :
                    if isolated1 == 0:
                        state = state2
                        action = np.argmax(Q4_1[state, :])
                        next_state, reward, done = step(action,first_reward_array2_1)                    
                        state=next_state
                        state2 = state
                        if done == True:
                            done2 = True
                            done = False
                    else:
                        state = state2
                        action = np.argmax(Q1[state, :])
                        next_state, reward, done = step(action,first_reward_array1)                    
                        state=next_state
                        state2 = state
                        if done == True:
                            done2 = True
                            done = False


                first_floor()
                plt.imshow(map,cmap=cmap, extent=[0,14,0,8])
                plt.title('first floor')
                plt.pause(0.5)
                plt.draw()
                plt.clf()
        #################1F 고립되지 않음

    print('print Q1 : 1F shortest path Q - table')
    print(Q1[:])
    print ('------------------')
    print('print Q2 : 2F shortest path Q - table')
    print(Q2[:])
    print ('------------------')
    print('print Q3 : 2F second shortest path Q - table')
    print(Q3[:])
    print ('------------------')
    print('print Q4 : 1F second shortest path Q - table')
    print(Q4_1[:],': Q2 selected in 2F')
    print(Q4_2[:],': Q3 selected in 2F')
    print ('------------------')
    print('print Q5 : 1F , no fire Q - table')
    print(Q5[:])
    print ('------------------')
    print('print Q6 : 2F, no fire Q - table')
    print(Q6[:])

#Qlearning(case,num,input_state,input_floor)
Qlearning(1,1,66,1)
#Qlearning(2,1,65,2)
#Qlearning(3,20,88,2)
#Qlearning(4,1,56,1)
#Qlearning(5,1,35,2)
