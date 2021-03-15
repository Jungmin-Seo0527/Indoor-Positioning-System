# maximize train // test // 80% 20%
# cross entropy
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split

x_data_all = np.loadtxt('txt2py_x_data.txt',delimiter=',',skiprows=1,dtype='float32')
y_data_all = np.loadtxt('txt2py_y_data.txt',delimiter=',',skiprows=1,dtype='float32')

x_train,x_test,y_train,y_test = train_test_split(x_data_all,y_data_all,test_size=0.2,random_state=42)


X = tf.placeholder(tf.float32, [None, 18])
Y = tf.placeholder(tf.float32, [None, 3])
keep_prob = tf.placeholder(tf.float32)

# weights & bias for nn layers
W1 = tf.get_variable("W1", shape=[18, 400],  ##tf.get_variable(<name>, <shape>, <initializer>): 입력된 이름의 변수를 생성하거나 반환함
     initializer=tf.contrib.layers.xavier_initializer())##xavier_initializer 이용해 초기값을 좋게함
b1 = tf.Variable(tf.random_normal([400]))##난수 발생 
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)
L1 = tf.nn.dropout(L1, keep_prob=0.7)##dropout 이용 뉴럴 네트워크에서 필요한 파라미터수 줄이는것 -->overfitting을 방

W2 = tf.get_variable("W2", shape=[400, 300],
     initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal([300]))
L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)
L2 = tf.nn.dropout(L2, keep_prob=0.7)

W3 = tf.get_variable("W3", shape=[300, 200],
     initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random_normal([200]))
L3 = tf.nn.relu(tf.matmul(L2, W3) + b3)
L3 = tf.nn.dropout(L3, keep_prob=0.7)

W4 = tf.get_variable("W4", shape=[200, 3],
     initializer=tf.contrib.layers.xavier_initializer())
b4 = tf.Variable(tf.random_normal([3]))  #layer 수 3 개  node 수 50

hypothesis = tf.matmul(L3, W4) + b4

# define cost/loss & optimizer
learning_rate = 1e-4
cost = (tf.reduce_mean(tf.sqrt(tf.reduce_sum(tf.square(hypothesis - Y),axis=-1))))

cost_sum=tf.summary.scalar('cost',cost)
##cost_train=tf.summary.scalar('cost_train1',cost) #텐서보드 display용
##cost_test=tf.summary.scalar('cost_test1',cost) #텐서보드 display용
train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)
##merged_summary=tf.summary.merge_all() #텐서보드 display용
# parameters
save_file='./train_model3.ckpt'

num_epochs = 5
num_iterations = 10
saver=tf.train.Saver()


# train my model
with tf.Session() as sess:
    # initialize
##    train_writer=tf.summary.FileWriter('./tensorboard_log5',sess.graph) #텐서보드 display용
##    test_writer=tf.summary.FileWriter('./tensorboard_log5',sess.graph) #텐서보드
   

    merged_summary=tf.summary.merge_all()
    train_writer=tf.summary.FileWriter('./tensorboard_log5/a') #텐서보드 display용
    test_writer=tf.summary.FileWriter('./tensorboard_log5/b') #텐서보드

    train_writer.add_graph(sess.graph)
    test_writer.add_graph(sess.graph)
    sess.run(tf.global_variables_initializer())
    for epoch in range(num_epochs):
        avg_cost = 0
        summary_test_cost_train = tf.Summary()
        summary_test_cost_test = tf.Summary()
        
        summary_test_cost_train.value.add(tag="Cost_train")
        summary_test_cost_test.value.add(tag="Cost_test")
        
        test_writer.add_summary(summary_test_cost_train, global_step=epoch)
        test_writer.add_summary(summary_test_cost_test, global_step=epoch)
        summary3=sess.run(merged_summary,feed_dict={X: x_train, Y: y_train})
        summary4=sess.run(merged_summary,feed_dict={X: x_test, Y: y_test})
        train_writer.add_summary(summary3,epoch)#텐서보드 display용 epoch당 cost
        test_writer.add_summary(summary4,epoch)#텐서보드 display용 epoch당 cost
        for iteration in range(num_iterations):
            _, cost_val = sess.run([train, cost], feed_dict={X: x_train, Y: y_train, keep_prob: 0.7})
            avg_cost += cost_val / num_iterations

        print("Epoch: {(epoch + 1):04d}, Cost: {avg_cost:.9f}") #f
    saver.save(sess,save_file)
                        
    print("Learning Finished!")

    h= sess.run(
        [hypothesis], feed_dict={X: x_test, Y: y_test}
    )
    
    print("\nHypothesis:\n{h} ") #f
    saver.save(sess,save_file)
    print('Trained Model Saved.')
    
