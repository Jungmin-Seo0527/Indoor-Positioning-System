#test20% learning 80% -2layer ,learning rate:1e-4
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split


x_data_all = np.loadtxt('txt2py_x_data.txt',delimiter=',',skiprows=1,dtype='float32')
y_data_all = np.loadtxt('txt2py_y_data.txt',delimiter=',',skiprows=1,dtype='float32')

x_train,x_test,y_train,y_test = train_test_split(x_data_all,y_data_all,test_size=0.2,random_state=123)


X = tf.placeholder(tf.float32, [None, 18])
Y = tf.placeholder(tf.float32, [None, 224])

W1 = tf.get_variable("W1", shape=[18, 1000],
     initializer=tf.contrib.layers.xavier_initializer())
b1 = tf.Variable(tf.random_normal([1000]))
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)
L1 = tf.nn.dropout(L1, keep_prob=0.8)

W2 = tf.get_variable("W2", shape=[1000, 224],
     initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal([224]))







# tf.nn.softmax computes softmax activations
# softmax = exp(logits) / reduce_sum(exp(logits), dim)
logits = tf.matmul(L1, W2) + b2
hypothesis = tf.nn.softmax(logits)

# Cross entropy cost/loss
cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logits, 
                                                 labels=Y)
cost = tf.reduce_mean(cost_i)


optimizer = tf.train.AdamOptimizer(learning_rate=1e-4).minimize(cost)
is_correct = tf.equal(tf.arg_max(hypothesis,1),tf.arg_max(Y,1))
accuracy=tf.reduce_mean(tf.cast(is_correct,tf.float32))
# Launch graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(30001):
            _, cost_val = sess.run([optimizer, cost], feed_dict={X: x_train, Y: y_train})

            if step % 200 == 0:
                print(step, cost_val)

    print('--------------')
    # Testing & One-hot encoding
    a = sess.run(hypothesis, feed_dict={X: x_test})
    print(sess.run(tf.argmax(a, 1)))
    print('Accuracy:', sess.run(accuracy, feed_dict={X: x_test, Y: y_test}))
