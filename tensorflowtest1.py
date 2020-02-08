import tensorflow as tf
print(tf.__version__)

tf.compat.v1.disable_eager_execution()

hello = tf.constant('Hello, Welcome')

sess = tf.compat.v1.Session()

print(sess.run(hello))