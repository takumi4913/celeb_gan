
from __future__ import print_function
import cv2
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# モデルのダウンロード
gan = hub.Module("https://tfhub.dev/google/progan-128/1")

z = (np.random.randn(1,512)+1)/2

z_values = np.reshape(z,(1,512))
images = gan(z_values)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    out = sess.run(images)

    for i, image in enumerate(out):
        Image.fromarray(np.uint8(image * 255)).save(f"img/gan_image.jpg")

#カスケード分類データの読み込み
HAAR_FILE = "data/haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(HAAR_FILE)

#生成画像、ユーザ画像の代入
gan_img = cv2.imread('img/gan_image.jpg')
user_img_picture = 'img/user_image.jpg'
user_img = cv2.imread(user_img_picture)

#グレースケールへの変換
user_g = cv2.imread(user_img_picture,0)

#顔部分を検出
cut_face = cascade.detectMultiScale(user_g)

#顔部分を切り取る
for x,y,w,h in cut_face:
    face_cut = user_img[y:y+h, x:x+w]
    h=y
    w=x
   
#生成画像のリサイズ
height,width,channels=face_cut.shape[:3]
gan_resize=cv2.resize(gan_img,(height,width))

#画像の合成
add = cv2.addWeighted(gan_resize,0.6,face_cut,0.4,0.0)
cv2.imwrite('img/add_image.jpg',add)
height, width = add.shape[:2]
user_img[h:height+h, w:width+w] = add

#mask処理 1(user_img) 2(add)
#rows, cols, channels = add.shape
#roi = user_img[:rows, :cols]

#img2gray = cv2.cvtColor(add, cv2.COLOR_BGR2GRAY)

#mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY_INV)[1]
#mask_inv = cv2.bitwise_not(mask)

#img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
#img2_fg = cv2.bitwise_and(add, add, mask=mask)

#cv2.imwrite('out.png', img2_fg)

cv2.imwrite('img/result.jpg',user_img)
#cv2.imshow('add',user_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()