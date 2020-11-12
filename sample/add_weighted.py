
from __future__ import print_function
import cv2 as cv
alpha = 0.5
raw_input = input  # Python 3

input_alpha = 0.3

# [load]
gan = cv.imread(cv.samples.findFile('example.png'))
user = cv.imread(cv.samples.findFile('face_cut.png'))

#gan画像のresize
height,width,channels=user.shape[:3]
gan_resize=cv.resize(gan,(height,width))

# [blend_images]
beta = (1.0 - alpha)
dst = cv.addWeighted(gan_resize, alpha, user, beta, 0.0)
# [blend_images]
# [display]
cv.imshow('dst', dst)
cv.waitKey(0)
# [display]
cv.destroyAllWindows()