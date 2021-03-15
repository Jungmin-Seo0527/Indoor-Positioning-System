import tensorflow as tf

# Import MINST data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

learning_rate = 0.001
training_epochs = 15
batch_size = 100
display_step = 1

x = tf.placeholder(tf.float32, [None, 784]) # MNIST data image of shape 28 * 28 = 784
y = tf.placeholder(tf.float32, [None, 10]) # 0-9 digits recognition => 10 classes

W1 = tf.Variable(tf.random_normal([784,256]))
W2 = tf.Variable(tf.random_normal([256,256]))
W3 = tf.Variable(tf.random_normal([256,10]))

b1 = tf.Variable(tf.random_normal([256]))
b2 = tf.Variable(tf.random_normal([256]))
b3 = tf.Variable(tf.random_normal([10]))

# Our hypothesis
L1 = tf.nn.relu(tf.add(tf.matmul(x, W1), b1))
L2 = tf.nn.relu(tf.add(tf.matmul(L1, W2), b2))
hypothesis = tf.add(tf.matmul(L2, W3), b3)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(hypothesis, y))
#optimizer = tf.train.AdamOptimizer(0.001).minimize(cost)
optimizer = tf.train.AdamOptimizer(0.001).minimize(cost)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples/batch_size)
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)

            sess.run(optimizer, feed_dict = {x: batch_xs, y: batch_ys})
            avg_cost += sess.run(cost, feed_dict={x: batch_xs,y: batch_ys})/total_batch

        if epoch % display_step == 0 :
            print("Epoch:", "%04d" % (epoch+1) , "cost=", "{:.9f}".format(avg_cost))

    print("Optimization Finished")

    correct_prediction = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print("Accuracy :",accuracy.eval({x: mnist.test.images, y:mnist.test.labels}))
