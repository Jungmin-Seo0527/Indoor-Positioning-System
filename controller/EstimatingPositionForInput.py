# maximize train // test // 80% 20%
# cross entropy
import tensorflow as tf

import numpy as np
from sklearn.model_selection import train_test_split

from controller import module2


def ESTIMATINGPOSITIONBYINPUT(lst=[]):

    x_test=lst
    x_test=x_test.reshape(-1,18)
    ##print(x_test)
    X = tf.placeholder(tf.float32, [None, 18])
    Y = tf.placeholder(tf.float32, [None, 3])

    x_arr=[]
    y_arr=[]
    z_arr=[]

    ARR = np.array([0, 0])

    # weights & bias for nn layers
    W1 = tf.get_variable("W1", shape=[18, 800],  ##tf.get_variable(<name>, <shape>, <initializer>): 입력된 이름의 변수를 생성하거나 반환함
         initializer=tf.contrib.layers.xavier_initializer())##xavier_initializer 이용해 초기값을 좋게함
    b1 = tf.Variable(tf.random_normal([800]))##난수 발생
    L1 = tf.nn.relu(tf.matmul(X, W1) + b1)
    #L1 = tf.nn.dropout(L1, keep_prob=0.7)##dropout 이용 뉴럴 네트워크에서 필요한 파라미터수 줄이는것 -->overfitting을 방

    W2 = tf.get_variable("W2", shape=[800, 600],
         initializer=tf.contrib.layers.xavier_initializer())
    b2 = tf.Variable(tf.random_normal([600]))
    L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)
    #L2 = tf.nn.dropout(L2, keep_prob=0.7)

    W3 = tf.get_variable("W3", shape=[600, 400],
         initializer=tf.contrib.layers.xavier_initializer())
    b3 = tf.Variable(tf.random_normal([400]))
    L3 = tf.nn.relu(tf.matmul(L2, W3) + b3)
    #L3 = tf.nn.dropout(L3, keep_prob=0.7)
    W4 = tf.get_variable("W4", shape=[400, 3],
         initializer=tf.contrib.layers.xavier_initializer())
    b4 = tf.Variable(tf.random_normal([3]))  #layer 수 3 개  node 수 50

    hypothesis = tf.matmul(L3, W4) + b4

    # define cost/loss & optimizer
    learning_rate = 1e-4
    cost = (tf.reduce_mean(tf.sqrt(tf.reduce_sum(tf.square(hypothesis - Y),axis=-1))))
    train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

    #correct_prediction = tf.equal(tf.argmax(hypothesis, axis=1), tf.argmax(Y, axis=1))
    #accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    save_file='controller/train_model3.ckpt-999'
    saver=tf.train.Saver()
    # train my model
    with tf.Session() as sess:
        # initialize
        saver.restore(sess,save_file)

        h= sess.run(
            [hypothesis], feed_dict={X: x_test}
        )
        ARR= np.array(sess.run([hypothesis], feed_dict={X: x_test}))
        x=ARR[0,0,0] # 가운데 있는놈이 몇번-1
        y=ARR[0,0,1]
        z=ARR[0,0,2]
        x_arr.append(x)
        y_arr.append(y)
        z_arr.append(z)

        print("\nposition prediction : ""x:",x_arr[0],"y:",y_arr[0],"z:",z_arr[0])
     #  print(module2.cell(x_arr[0],y_arr[0],z_arr[0]))
        return module2.cell(x_arr[0],y_arr[0],z_arr[0])