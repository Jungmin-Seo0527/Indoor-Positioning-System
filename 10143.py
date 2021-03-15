import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split

sess=tf.Session()    
#First let's load meta graph and restore weights
saver = tf.train.import_meta_graph('my_test_model-1000.meta')
saver.restore(sess,tf.train.latest_checkpoint('./'))
graph = tf.get_default_graph()

X = tf.placeholder(tf.float32, [None, 18])
Y = tf.placeholder(tf.float32, [None, 224])

W1 = tf.get_variable("W1", shape=[18, 100],
     initializer=tf.contrib.layers.xavier_initializer())
b1 = tf.Variable(tf.random_normal([100]))
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)
L1 = tf.nn.dropout(L1, keep_prob=0.7)

W2 = tf.get_variable("W2", shape=[100, 50],
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
# tf.nn.softmax computes softmax activations
# softmax = exp(logits) / reduce_sum(exp(logits), dim)
##saver = tf.train.Saver(max_to_keep=4, keep_checkpoint_every_n_hours=2)
##
op_to_restore = graph.get_tensor_by_name("op_to_restore:0")
print (sess.run(op_to_restore,feed_dict))


##hypothesis = tf.nn.softmax(tf.matmul(L3, W4) + b4)
##
### Cross entropy cost/loss
##cost = tf.reduce_mean(tf.square(hypothesis-Y))
##
##optimizer = tf.train.AdamOptimizer(learning_rate=1e-3).minimize(cost)
##
##is_correct = tf.equal(tf.arg_max(hypothesis,1),tf.arg_max(Y,1))
##accuracy=tf.reduce_mean(tf.cast(is_correct,tf.float32))
##
### Launch graph
##with tf.Session() as sess:
##    sess.run(tf.global_variables_initializer())
##
##    for step in range(1001):
##            _, cost_val = sess.run([optimizer, cost], feed_dict={X: x_train, Y: y_train})
##
##            if step % 500 == 0:
##                print(step, 1000*cost_val)
##
##    print('--------------')
##    # Testing & One-hot encoding
##    a = sess.run(hypothesis, feed_dict={X: x_test})
##    print(sess.run(tf.argmax(a, 1)))
##    print('Accuracy:', sess.run(accuracy, feed_dict={X: x_test, Y: y_test}))
####    saver.save(sess, 'my_test_model',global_step=1000)
##saver = tf.train.Saver()
   
