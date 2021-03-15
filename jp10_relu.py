import tensorflow as tf
import numpy as np

x_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
y_data = np.array([[0], [1], [1], [0]], dtype=np.float32)

x_test = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
y_test = np.array([[0], [1], [1], [0]], dtype=np.float32)

# input place holders
X = tf.placeholder(tf.float32, [None, 2])
Y = tf.placeholder(tf.float32, [None, 1])

# weights & bias for nn layers
W1 = tf.Variable(tf.random_normal([2, 2]))
b1 = tf.Variable(tf.random_normal([2]))
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.random_normal([2, 2]))
b2 = tf.Variable(tf.random_normal([2]))
L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)

W3 = tf.Variable(tf.random_normal([2, 1]))
b3 = tf.Variable(tf.random_normal([1]))
hypothesis = tf.sigmoid(tf.matmul(L2, W3) + b3)

cost = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits_v2(logits=hypothesis, labels=tf.stop_gradient(Y)))
train = tf.train.AdamOptimizer(learning_rate=0.1).minimize(cost)



# train my model
with tf.Session() as sess:
   # Initialize TensorFlow variables
   sess.run(tf.global_variables_initializer())

   for step in range(10001):
       sess.run(train, feed_dict={X: x_data, Y: y_data})
       if step % 500 == 0:
           print(step, sess.run(cost, feed_dict={X: x_data, Y: y_data}))


with tf.Session() as sess:
    # initialize
    sess.run(tf.global_variables_initializer())

    for epoch in range(20):
        avg_cost = 0

        for iteration in range(10):
           
            _, cost_val = sess.run([train, cost], feed_dict={X: x_data, Y: y_data})
            

        print(f"Epoch: {(epoch + 1):04d}, Cost: {cost_val:.9f}")

    print("Learning Finished!")
