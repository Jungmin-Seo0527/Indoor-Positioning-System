import tensorflow as tf
import numpy as np

x_data = [[1/13, 1/113], [1/109, 1/569], [1/73, 1/53], [1/1125, 1/575], [1/277, 1/937], [1/233, 1/853], [1/193, 1/773], [1/157, 1/697]]
y_data = [[17,13], [5,7], [18,18], [30,40], [1,1], [2,2], [3,3], [4,4]]

# Evaluation our model using this test dataset
x_test = [[1/221, 1/41]]
y_test = [[29, 15]]
          
X = tf.placeholder(tf.float32, shape=[None, 2])
Y = tf.placeholder(tf.float32, shape=[None, 2])
W = tf.Variable(tf.random_normal([2, 2]), name='weight')
b = tf.Variable(tf.random_normal([2]), name='bias')

hypothesis = tf.matmul(X, W) + b
cost = tf.reduce_mean(tf.square(hypothesis - Y))
# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(2001):
   cost_val, hy_val, _ = sess.run(
       [cost, hypothesis, train], feed_dict={X: x_test, Y: y_test})
   if step%200==0:
       
       print(step, "Cost: ", cost_val, "\nPrediction:\n", hy_val)
