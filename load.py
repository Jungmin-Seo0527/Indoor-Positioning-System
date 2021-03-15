# maximize train // test // 80% 20%
# cross entropy
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
import module1

x_test= np.loadtxt('txt2py_test_x_data.txt',delimiter=',',skiprows=1,dtype='float32')
y_test= np.loadtxt('txt2py_test_y_data.txt',delimiter=',',skiprows=1,dtype='float32')


X = tf.placeholder(tf.float32, [None, 18])
Y = tf.placeholder(tf.float32, [None, 3])

x_arr=[]
y_arr=[]
z_arr=[]

ARR = np.array([0, 0])

# weights & bias for nn layers
W1 = tf.get_variable("W1", shape=[18, 500],  ##tf.get_variable(<name>, <shape>, <initializer>): 입력된 이름의 변수를 생성하거나 반환함
     initializer=tf.contrib.layers.xavier_initializer())##xavier_initializer 이용해 초기값을 좋게함
b1 = tf.Variable(tf.random_normal([500]))##난수 발생 
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)

W2 = tf.get_variable("W2", shape=[500, 150],
     initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal([150]))
L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)

W3 = tf.get_variable("W3", shape=[150, 3],
     initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random_normal([3]))  #layer 수 3 개  node 수 50

learning_rate = 1e-4

hypothesis = tf.matmul(L2, W3) + b3


num_epochs = 1001
num_iterations = 150
# define cost/loss & optimizer
cost = (tf.reduce_mean(tf.square(hypothesis - Y)))**0.5
train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

#correct_prediction = tf.equal(tf.argmax(hypothesis, axis=1), tf.argmax(Y, axis=1))
#accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# train my model
sess = tf.Session()


# 저장된 모델 파라미터를 가져옵니다.
model_path = "/tmp/model.saved"
saver = tf.train.Saver()

saver.restore(sess, model_path)
print("Model restored from file: %s" % model_path)
    
h= sess.run([hypothesis], feed_dict={X: x_test})
ARR= np.array(sess.run([hypothesis], feed_dict={X: x_test}))
x=ARR[0,0,0] # 가운데 있는놈이 몇번-1
y=ARR[0,0,1]
z=ARR[0,0,2]
x_arr.append(x)
y_arr.append(y)
z_arr.append(z)
                       
x=ARR[0,1,0] # 가운데 있는놈이 몇번-2
y=ARR[0,1,1]
z=ARR[0,1,2]
x_arr.append(x)
y_arr.append(y)
z_arr.append(z)
                   
        
x=ARR[0,2,0] # 가운데 있는놈이 몇번-3
y=ARR[0,2,1]
z=ARR[0,2,2]
x_arr.append(x)
y_arr.append(y)
z_arr.append(z)
for epoch in range(num_epochs):
        avg_cost = 0

        for iteration in range(num_iterations):
            _, cost_val = sess.run([train, cost], feed_dict={X: x_train, Y: y_train, keep_prob: 0.7})
            avg_cost += cost_val / num_iterations
    
        print(f"Epoch: {(epoch + 1):04d}, Cost: {avg_cost:.9f}")
##cost = (tf.reduce_mean(tf.square(hypothesis - Y)))**0.5

##  #    print(f"\nHypothesis:\n{h} ")
##print("\nfirst position prediction : ""x:",x_arr[0],"y:",y_arr[0],"z:",z_arr[0])
##print(module1.cell(x_arr[0],y_arr[0],z_arr[0]))
##print("second position prediction : ""x:",x_arr[1],"y:",y_arr[1],"z:",z_arr[1])
##print(module1.cell(x_arr[1],y_arr[1],z_arr[1]))
##print("Third position prediction : ""x:",x_arr[2],"y:",y_arr[2],"z:",z_arr[2])
##print(module1.cell(x_arr[2],y_arr[2],z_arr[2]))
sess.close()
