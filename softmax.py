import tensorflow as tf
import numpy as np
tf.set_random_seed(777)  # for reproducibility

x_data = np.loadtxt('txt2py_x_data.txt',delimiter=',',skiprows=1,dtype='float32')
y_data = np.loadtxt('txt2py_y_data.txt',delimiter=',',skiprows=1,dtype='float32')

x_test= np.loadtxt('txt2py_x_test.txt',delimiter=',',skiprows=1,dtype='float32')
y_test= np.loadtxt('txt2py_y_test.txt',delimiter=',',skiprows=1,dtype='float32')

X = tf.placeholder("float", [None, 18])
Y = tf.placeholder("float", [None, 224])
nb_classes = 224

W = tf.Variable(tf.random_normal([18, nb_classes]), name='weight')
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')

# tf.nn.softmax computes softmax activations
# softmax = exp(logits) / reduce_sum(exp(logits), dim)
hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)

# Cross entropy cost/loss
cost = tf.reduce_mean(tf.square(hypothesis-Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5).minimize(cost)

# Launch graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(201):
            _, cost_val = sess.run([optimizer, cost], feed_dict={X: x_data, Y: y_data})

            if step % 200 == 0:
                print(step, cost_val)

    print('--------------')
    # Testing & One-hot encoding


    print('--------------')
    a = sess.run(hypothesis, feed_dict={X: x_test})
    print(a, sess.run(tf.argmax(a, 1)))

