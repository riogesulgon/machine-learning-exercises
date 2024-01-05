import tensorflow as tf


x = tf.constant([[1., 2.]])
print(x) # 1x2 matrix
neg_x = tf.negative(x)

print("Eager execution: {}".format(tf.executing_eagerly()))
print("Negative:", neg_x) # 1x2 matrix

sum = tf.math.reduce_sum(x, axis=0)
print("Sum:", sum) # 1x1 matrix