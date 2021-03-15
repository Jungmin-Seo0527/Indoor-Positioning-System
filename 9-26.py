# Lab 7 Learning rate and Evaluation
import tensorflow as tf
import matplotlib.pyplot as plt
import random
import numpy as np


x_data = np.loadtxt('txt2py_x_data.txt',delimiter=',',skiprows=1,dtype='float32')
y_data = np.loadtxt('txt2py_y_data.txt',delimiter=',',skiprows=1,dtype='float32')

x_test = np.array([[44.516,46.266,48.136,49.9849,51.5922,52.5698,52.5957,46.1721,48.5721,51.4328,54.881,58.9517,62.7192,62.8085]], dtype=np.float32)
y_test = np.array([[32.5889,27.1738,0.38096]], dtype=np.float32)

X = tf.placeholder(tf.float32, [None, 14])
Y = tf.placeholder(tf.float32, [None, 3])

ARR = np.array([0, 0])
arr_y=tf.placeholder(tf.float32)
arr_z=tf.placeholder(tf.float32)

keep_prob = tf.placeholder(tf.float32)

# weights & bias for nn layers
W1 = tf.get_variable("W1", shape=[14, 500],
     initializer=tf.contrib.layers.xavier_initializer())
b1 = tf.Variable(tf.random_normal([500]))
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)
L1 = tf.nn.dropout(L1, keep_prob=0.7)

W2 = tf.get_variable("W2", shape=[500, 500],
     initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal([500]))
L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)
L2 = tf.nn.dropout(L2, keep_prob=0.7)

W3 = tf.get_variable("W3", shape=[500, 3],
     initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random_normal([3]))  #layer 수 3 개  node 수 500

# parameters
learning_rate = 1e-3
num_epochs = 300
num_iterations = 100 #한번에 처리할 데이터의 양 

hypothesis = tf.matmul(L2, W3) + b3

# cost function
cost = tf.reduce_mean(tf.square(hypothesis - Y))
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


    
    h= sess.run(
        [hypothesis], feed_dict={X: x_test, Y: y_test}
    )
    
    print(f"\nHypothesis:\n{h} ") #예상된 y_test 값
