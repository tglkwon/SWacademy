import numpy as np
import array

a = np.array([1,2,3], dtype=np.int32)
# 훨씬 c언어스러운 타입을 가진다. int16, int64 등 # perfomance를 높이는 요소
print(a, type(a), a.dtype)  # 기본 정수 데이터 타입은 int32라 따로 보여주지 않는다.
#numpy.ndarray : class명을 타입명처럼 만듬 # factory method

# 같은 데이터 타입으로 이루어짐
#x = array.array('i', [1.,2,3,4])
x = array.array('i', [1,2,3,4])


a = np.arange(24).reshape(2,3,4,1)
print(a, a.dtype, a.shape, a.ndim, a.itemsize, a.size)
# a라는 np.array의 데이터 구조를 알게 도와주는 것들, .dtype, .shape, .dim, .itemsize, .size

a = np.arange(25).reshape(5,5)
a[1] #=> array([4,5,6,7,8,9])
a[1,3:5] #=> array(8,9)
a[0,1] #=> 1

a[3:, [0,1,3]] #=> array([[15,16,18],
                        # [20,21,23])

a[2::2, ::2]    #=>array([[10,12,14],
                        # [20,22,24]])
# 2차원까지는 둘이 같다.
a[1,...]
a[1,:]
a = np.arange(24).reshape(2,3,4)
print(a[1,1,1])
print(a[:,:,3] == a[...,3])
# import tensorflow as tf
# (X_train, Y_train), (X_test, Y_test) = tf.keras.datasets.mnist.load_data()
# print(X_train.shape)
