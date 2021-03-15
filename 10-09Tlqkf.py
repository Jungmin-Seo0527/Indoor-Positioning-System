import module1
import tensorflow as tf
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import numpy as np
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


x_data = np.loadtxt('txt2py_x_data.txt',delimiter=',',skiprows=1,dtype='float32')
y_data = np.loadtxt('txt2py_y_data.txt',delimiter=',',skiprows=1,dtype='int')

x_test= np.loadtxt('txt2py_x_data_test.txt',delimiter=',',skiprows=1,dtype='float32')
y_test= np.loadtxt('txt2py_y_data_test.txt',delimiter=',',skiprows=1,dtype='int')


X = tf.placeholder(tf.float32, [None, 18])
Y = tf.placeholder(tf.float32, [None, 224])

np.expand_dims (X, axis = 0)
x_arr=[]
y_arr=[]
z_arr=[]

ARR = np.array([0, 0])
arr_y=tf.placeholder(tf.float32)
arr_z=tf.placeholder(tf.float32)

keep_prob = tf.placeholder(tf.float32)

# weights & bias for nn layers
W1 = tf.get_variable("W1", shape=[18, 50],
     initializer=tf.contrib.layers.xavier_initializer())
b1 = tf.Variable(tf.random_normal([50]))
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)
L1 = tf.nn.dropout(L1, keep_prob=0.7)

W2 = tf.get_variable("W2", shape=[50, 50],
     initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal([50]))
L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)
L2 = tf.nn.dropout(L2, keep_prob=0.7)


W3 = tf.get_variable("W3", shape=[50, 50],
     initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random_normal([50]))
L3 = tf.nn.relu(tf.matmul(L2, W3) + b3)
L3 = tf.nn.dropout(L3, keep_prob=0.7)


W4 = tf.get_variable("W4", shape=[50, 224],
     initializer=tf.contrib.layers.xavier_initializer())
b4 = tf.Variable(tf.random_normal([224]))



 #layer 수 3 개  node 수 50

# parameters
learning_rate = 0.1
num_epochs = 10
num_iterations = 100 #한번에 처리할 데이터의 양 

#hypothesis = tf.matmul(L3, W4) + b4
hypothesis = tf.nn.softmax(tf.matmul(L3, W4) + b4)

# cost function
#cost = tf.reduce_mean(tf.square(hypothesis-Y))
#cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))
#cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=hypothesis,
 #                                                                labels=tf.stop_gradient([Y])))
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=hypothesis, labels=Y))

tf.summary.scalar('cost',cost) #텐서보드 display용


train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)# adam optimizer 이용하여 cost 줄임 

merged=tf.summary.merge_all() #텐서보드 display용

# train my model
with tf.Session() as sess:
    # initialize
    
    tensorboard_writer=tf.summary.FileWriter('./tensorboard_log2',sess.graph) #텐서보드 display용
    sess.run(tf.global_variables_initializer())
    
    for epoch in range(num_epochs):
        avg_cost = 0
        summary=sess.run(merged,feed_dict={X: x_data, Y: y_data})
        tensorboard_writer.add_summary(summary,epoch)#텐서보드 display용 epoch당 cost 추이
        
        for iteration in range(num_iterations):
           
            _, cost_val = sess.run([train, cost], feed_dict={X: x_data, Y: y_data, keep_prob: 0.7})
            avg_cost += cost_val / num_iterations
        print(f"Epoch: {(epoch + 1):04d}, Cost: {avg_cost:.9f}")



    print("러닝완료!")

    all = sess.run(hypothesis, feed_dict={X: [x_test]})
    print(all, sess.run(tf.argmax(all, 1)))





##
##print(module1.cell(x_arr[5],y_arr[5],z_arr[5]))

##fig = plt.figure()
##ax = fig.add_subplot(111, projection='3d')
##
##color = ['k','g','b','y','m','r']

##ax.scatter(x_arr[0],y_arr[0],z_arr[0],s=30,c=color[0],marker='o')
##ax.scatter(x_arr[1],y_arr[1],z_arr[1],s=30,c=color[1],marker='o')
##ax.scatter(x_arr[2],y_arr[2],z_arr[2],s=30,c=color[2],marker='o')
##ax.scatter(x_arr[3],y_arr[3],z_arr[3],s=30,c=color[3],marker='o')
##ax.scatter(x_arr[4],y_arr[4],z_arr[4],s=30,c=color[4],marker='o')
##ax.scatter(x_arr[5],y_arr[5],z_arr[5],s=30,c=color[5],marker='o')
#ax.scatter(x_arr[6],y_arr[6],z_arr[6],s=30,c=color[6],marker='o')
#ax.scatter(x_arr[7],y_arr[7],z_arr[7],s=30,c=color[7],marker='o')
#ax.scatter(x_arr[8],y_arr[8],z_arr[8],s=30,c=color[8],marker='o')
##
##ax.set_xlabel('42M')
##ax.set_ylabel('24M')
##ax.set_zlabel('3M')
##plt.suptitle('실제 위치와 추정위치')
##ax.legend(['실제값','60회','120회','180회','240회','300회'])
##
##plt.show()
