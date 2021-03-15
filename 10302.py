# maximize train // test // 80% 20%
# cross entropy
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split

#tf.set_random_seed(777)  # for reproducibility


x_data_all = np.loadtxt('txt2py_x_data.txt',delimiter=',',skiprows=1,dtype='float32')
y_data_all = np.loadtxt('txt2py_y_data.txt',delimiter=',',skiprows=1,dtype='float32')

x_train,x_test,y_train,y_test = train_test_split(x_data_all,y_data_all,test_size=0.2,random_state=42)


X = tf.placeholder(tf.float32, [None, 18])
Y = tf.placeholder(tf.float32, [None, 3])

#x_arr=[]
#y_arr=[]
#z_arr=[]

#arr_y=tf.placeholder(tf.float32)
#arr_z=tf.placeholder(tf.float32)

keep_prob = tf.placeholder(tf.float32)

# weights & bias for nn layers
W1 = tf.get_variable("W1", shape=[18, 300],  ##tf.get_variable(<name>, <shape>, <initializer>): 입력된 이름의 변수를 생성하거나 반환함
     initializer=tf.contrib.layers.xavier_initializer())##xavier_initializer 이용해 초기값을 좋게함
b1 = tf.Variable(tf.random_normal([300]))##난수 발생 
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)
L1 = tf.nn.dropout(L1, keep_prob=0.7)##dropout 이용 뉴럴 네트워크에서 필요한 파라미터수 줄이는것 -->overfitting을 방

W2 = tf.get_variable("W2", shape=[300, 150],
     initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal([150]))
L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)
L2 = tf.nn.dropout(L2, keep_prob=0.7)

W3 = tf.get_variable("W3", shape=[150, 3],
     initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random_normal([3]))  #layer 수 3 개  node 수 50
# parameters    
learning_rate = 1e-4
num_epochs = 501
num_iterations = 150

hypothesis = tf.matmul(L2, W3) + b3

# define cost/loss & optimizer
cost = (tf.reduce_mean(tf.square(hypothesis - Y)))**0.5

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
            _, cost_val = sess.run([train, cost], feed_dict={X: x_train, Y: y_train, keep_prob: 0.7})
            avg_cost += cost_val / num_iterations

        print(f"Epoch: {(epoch + 1):04d}, Cost: {avg_cost:.9f}")
   #     if (epoch>0) and (((epoch%50)==0) or (epoch==501)):
##            ARR= np.array(sess.run([hypothesis], feed_dict={X: x_test, Y: y_test}))
##            print(f"Hypothesis:{ARR} , Cost: {avg_cost:.9f}")          
##            x=ARR[0,0,0]
##            y=ARR[0,0,1]
##            z=ARR[0,0,2]
##            x_arr.append(x)
##            y_arr.append(y)
##            z_arr.append(z)
                        
    print("Learning Finished!")

    h= sess.run(
        [hypothesis], feed_dict={X: x_test, Y: y_test}
    )
    
##    y_test=np.array(y_test)
##    y_test=np.array(y_test).reshape((1,3))
##    y_test=np.array(y_test).reshape(3,1)
##
##    x_arr.insert(0,sum(sum(y_test[0:1])))
##    y_arr.insert(0,sum(sum(y_test[1:2])))
##    z_arr.insert(0,sum(sum(y_test[2:3])))
##               
##    
    print(f"\nHypothesis:\n{h} ")
##    print("x:",x_arr,"\ny:",y_arr,"\nz:",z_arr)
