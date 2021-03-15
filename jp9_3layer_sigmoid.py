import tensorflow as tf
import numpy as np

x_data = np.array([[1/13, 1/113], [1/109, 1/569], [1/73, 1/53],
                   [1/1125, 1/575], [1/277, 1/937], [1/233, 1/853], [1/193, 1/773],
                   [1/157, 1/697]], dtype=np.float32)
y_data = np.array([[17,13], [5,7], [18,18], [30,40], [1,1],
                   [2,2], [3,3], [4,4]], dtype=np.float32)

x_test = np.array([[1/221, 1/41]], dtype=np.float32)
y_test = np.array([[29, 15]], dtype=np.float32)

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_normal([2, 2]), name='weight1')
b1 = tf.Variable(tf.random_normal([2]), name='bias1')
layer1 = tf.nn.relu(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.random_normal([2, 2]), name='weight2')
b2 = tf.Variable(tf.random_normal([2]), name='bias2')
layer2 = tf.nn.relu(tf.matmul(X, W2) + b2)

W3 = tf.Variable(tf.random_normal([2, 2]), name='weight3')
b3 = tf.Variable(tf.random_normal([2]), name='bias3')

hypothesis = tf.nn.relu(tf.matmul(layer2, W3) + b3)




# cost/loss function
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.1e-3).minimize(cost)

# Accuracy computation
# True if hypothesis>0.5 else False
# predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
#accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

# Launch graph
with tf.Session() as sess:
   # Initialize TensorFlow variables
   sess.run(tf.global_variables_initializer())

   for step in range(10001):
       sess.run(train, feed_dict={X: x_data, Y: y_data})
       if step % 500 == 0:
           print(step, sess.run(cost, feed_dict={X: x_data, Y: y_data}), sess.run(W3))

   # Accuracy report
   h  = sess.run([hypothesis], feed_dict={X: x_test, Y: y_test})
   print("\nHypothesis: ", h)
