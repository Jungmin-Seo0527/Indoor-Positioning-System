import tensorflow as tf
import random
import numpy as np
# import matplotlib.pyplot as plt


x_data = np.loadtxt('txt2py_x_data.txt',delimiter=',',skiprows=1,dtype='float32')
y_data = np.loadtxt('txt2py_y_data.txt',delimiter=',',skiprows=1,dtype='float32')

x_test= np.loadtxt('txt2py_x_test.txt',delimiter=',',skiprows=1,dtype='float32')
y_test= np.loadtxt('txt2py_y_test.txt',delimiter=',',skiprows=1,dtype='float32')# Check out https://www.tensorflow.org/get_started/mnist/beginners for
# more information about the mnist dataset

# parameters
learning_rate = 0.001
training_epochs = 15


# input place holders
X = tf.placeholder(tf.float32, [None, 18])
Y = tf.placeholder(tf.float32, [None, 224])

# weights & bias for nn layers
W1 = tf.Variable(tf.random_normal([18, 300]))
b1 = tf.Variable(tf.random_normal([300]))
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.random_normal([300, 300]))
b2 = tf.Variable(tf.random_normal([300]))
L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)

W3 = tf.Variable(tf.random_normal([300, 224]))
b3 = tf.Variable(tf.random_normal([224]))
hypothesis = tf.nn.softmax(L2, W3) + b3

# define cost/loss & optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    logits=hypothesis, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# initialize
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(201):
            _, cost_val = sess.run([optimizer, cost], feed_dict={X: x_data, Y: y_data})

            if step % 200 == 0:
                print(step, cost_val)

    print('--------------')
    print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.9f}'.format(avg_cost))

print('Learning Finished!')

# Test model and check accuracy
correct_prediction = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print('Accuracy:', sess.run(accuracy, feed_dict={
      X: x_test, Y: y_test}))

# Get one and predict

print("Prediction: ", sess.run(
    tf.argmax(hypothesis, 1), feed_dict={X: x_test}))
