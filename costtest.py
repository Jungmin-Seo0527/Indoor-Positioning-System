import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
import module2

hypothesis=[0,0,0]
Y=[3,3,3]
##
cost = (np.mean(np.sqrt(np.sum(np.square(hypothesis - Y),axis=-1))))
print(cost)
cossst=np.mean([2,2,2,2])

with tf.Session() as sess:
    print(f"cossst:{(cossst)}:04d")
