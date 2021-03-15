# Lab 7 Learning rate and Evaluation
import tensorflow as tf
import matplotlib.pyplot as plt
import random
import numpy as np



tf.set_random_seed(777)  # reproducibility

# Check out https://www.tensorflow.org/get_started/mnist/beginners for
# more information about the mnist dataset
#mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
x_data = np.array([[1000/13, 1000/113], [1000/109, 1000/569], [1000/73, 1000/53],
                   [1000/1125, 1000/575], [1000/277, 1000/937],
                   [1000/233, 1/853], [1000/193, 1000/773],
                   [1000/157, 1000/697]], dtype=np.float32)
y_data = np.array([[0,5], [0,5], [5,0], [5,0], [0,5],
                   [0,5], [0,5], [0,5]], dtype=np.float32)

x_test = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
y_test = np.array([[0], [1], [1], [0]], dtype=np.float32)
# input place holders
X = tf.placeholder(tf.float32, [None, 2])
Y = tf.placeholder(tf.float32, [None, 2])
nb_classes = 2

W = tf.Variable(tf.random_normal([2, 2]), name='weight')
b = tf.Variable(tf.random_normal([2]), name='bias')
# parameters
learning_rate = 1e-2
batch_size = 1
num_epochs = 5000
num_iterations = 100

hypothesis = tf.matmul(X, W) + b

# define cost/loss & optimizer
cost = tf.reduce_mean(tf.square(hypothesis - Y))

train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

#correct_prediction = tf.equal(tf.argmax(hypothesis, axis=1), tf.argmax(Y, axis=1))
#accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# train my model
with tf.Session() as sess:
    # initialize
    sess.run(tf.global_variables_initializer())

    for epoch in range(num_epochs):
        avg_cost = 0

        for iteration in range(num_iterations):
           # batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            _, cost_val = sess.run([train, cost], feed_dict={X: x_data, Y: y_data})
            avg_cost += cost_val / num_iterations

        print(f"Epoch: {(epoch + 1):04d}, Cost: {avg_cost:.9f}")

    print("Learning Finished!")

    # Test model and check accuracy
##    print(
##        "Accuracy:",
##        sess.run(accuracy, feed_dict={X: mnist.test.images, Y: mnist.test.labels}),
##    )
