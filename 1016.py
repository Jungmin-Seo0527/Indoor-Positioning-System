import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split

tf.set_random_seed(777)  # for reproducibility

x_data_all = np.loadtxt('txt2py_x_data.txt',delimiter=',',skiprows=1,dtype='float32')
y_data_all = np.loadtxt('txt2py_y_data.txt',delimiter=',',skiprows=1,dtype='float32')

x_train,x_test,y_train,y_test = train_test_split(x_data_all,y_data_all,test_size=0.2,random_state=123)


X = tf.placeholder("float", [None, 18])
Y = tf.placeholder("int32", [None, 224])
nb_classes = 224

##Y_one_hot = tf.one_hot(Y, nb_classes)  # one hot
##print("one_hot:", Y_one_hot)
##Y_one_hot = tf.reshape(Y_one_hot, [-1, nb_classes])
##print("reshape one_hot:", Y_one_hot)

W = tf.Variable(tf.random_normal([18, nb_classes]), name='weight')
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')

# tf.nn.softmax computes softmax activations
# softmax = exp(logits) / reduce_sum(exp(logits), dim)
logits = tf.matmul(X, W) + b
hypothesis = tf.nn.softmax(logits)

# Cross entropy cost/loss
cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logits, 
                                                 labels=Y)
cost = tf.reduce_mean(cost_i)


optimizer = tf.train.AdamOptimizer(learning_rate=1e-2).minimize(cost)
is_correct = tf.equal(tf.arg_max(hypothesis,1),tf.arg_max(Y,1))
accuracy=tf.reduce_mean(tf.cast(is_correct,tf.float32))
# Launch graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
            _, cost_val = sess.run([optimizer, cost], feed_dict={X: x_train, Y: y_train})

            if step % 200 == 0:
                print(step, cost_val)

    print('--------------')
    # Testing & One-hot encoding
    a = sess.run(hypothesis, feed_dict={X: x_test})
    print(sess.run(tf.argmax(a, 1)))
    print('Accuracy:', sess.run(accuracy, feed_dict={X: x_test, Y: y_test}))
