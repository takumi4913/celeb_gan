import cv2

src = cv2.imread('add_image.jpg', -1)  # -1を付けることでアルファチャンネルも読んでくれるらしい。
dst = cv2.imread('user_image.jpg')

width, height = src.shape[:2]

mask = src[:,:,3]  # アルファチャンネルだけ抜き出す。
mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)  # 3色分に増やす。
mask = mask / 255  # 0-255だと使い勝手が悪いので、0.0-1.0に変更。

src = src[:,:,:3]  # アルファチャンネルは取り出しちゃったのでもういらない。

dst[0:height:, 0:width] *= 1 - mask  # 透過率に応じて元の画像を暗くする。
dst[0:height:, 0:width] += src * mask  # 貼り付ける方の画像に透過率をかけて加算。

cv2.imwrite('out.jpg', dst)