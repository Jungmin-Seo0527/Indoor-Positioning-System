#cross entropy with adamoptimizer 80%learn 20%test
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split

tf.set_random_seed(777)  # for reproducibility

x_data_all = np.loadtxt('txt2py_x_data.txt',delimiter=',',skiprows=1,dtype='float32')
y_data_all = np.loadtxt('txt2py_y_data.txt',delimiter=',',skiprows=1,dtype='float32')

x_train,x_test,y_train,y_test = train_test_split(x_data_all,y_data_all,test_size=0.2)

#x_test= np.loadtxt('txt2py_x_data_test.txt',delimiter=',',skiprows=1,dtype='float32')
#y_test= np.loadtxt('txt2py_y_data_test.txt',delimiter=',',skiprows=1,dtype='float32')

nb_classes = 224

X = tf.placeholder(tf.float32, [None, 18])
Y = tf.placeholder(tf.float32, [None, 224])

W1 = tf.get_variable("W1", shape=[18, 50],
     initializer=tf.contrib.layers.xavier_initializer())
b1 = tf.Variable(tf.random_normal([50]))
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)
L1 = tf.nn.dropout(L1, keep_prob=0.8)

W2 = tf.get_variable("W2", shape=[50, 100],
     initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal([100]))
L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)
L2 = tf.nn.dropout(L2, keep_prob=0.8)


W3 = tf.get_variable("W3", shape=[100, 200],
     initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random_normal([200]))
L3 = tf.nn.relu(tf.matmul(L2, W3) + b3)
L3 = tf.nn.dropout(L3, keep_prob=0.8)


W4 = tf.get_variable("W4", shape=[200, 224],
     initializer=tf.contrib.layers.xavier_initializer())
b4 = tf.Variable(tf.random_normal([224]))
# tf.nn.softmax computes softmax activations
# softmax = exp(logits) / reduce_sum(exp(logits), dim)
logits = tf.matmul(L3, W4) + b4
hypothesis = tf.nn.softmax(logits)

# Cross entropy cost/loss
cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logits, 
                                                 labels=Y)
cost = tf.reduce_mean(cost_i)

optimizer = tf.train.AdamOptimizer(learning_rate=1e-1).minimize(cost)
is_correct = tf.equal(tf.arg_max(hypothesis,1),tf.arg_max(Y,1))
accuracy=tf.reduce_mean(tf.cast(is_correct,tf.float32))
# Launch graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(5001):
            _, cost_val = sess.run([optimizer, cost], feed_dict={X: x_train, Y: y_train})

            if step % 500 == 0:
                print(step, cost_val)

    print('--------------')
    # Testing & One-hot encoding
    a = sess.run(hypothesis, feed_dict={X: x_test})
    print(sess.run(tf.argmax(a, 1)))
    print('Accuracy:', sess.run(accuracy, feed_dict={X: x_test, Y: y_test}))


   
