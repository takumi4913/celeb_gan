
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


# モデルのダウンロード
gan = hub.Module("https://tfhub.dev/google/progan-128/1")

z = (np.random.randn(1,512)-1)/2

z_values = np.reshape(z,(1,512))
images = gan(z_values)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    out = sess.run(images)

    for i, image in enumerate(out):
        Image.fromarray(np.uint8(image * 255)).save(f"example.png")