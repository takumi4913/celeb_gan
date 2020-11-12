
#OpenCVのインポート
import cv2
 
#カスケード型分類器に使用する分類器のデータ（xmlファイル）を読み込み
HAAR_FILE = "haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(HAAR_FILE)
 
#画像ファイルの読み込み
image_picture = "example.png"
 
img = cv2.imread(image_picture)
 
#グレースケールに変換する
img_g = cv2.imread(image_picture,0)
 
#カスケード型分類器を使用して画像ファイルから顔部分を検出する
face = cascade.detectMultiScale(img_g)
 
#顔部分を切り取る
for x,y,w,h in face:
    face_cut = img[y:y+h, x:x+w]
 
#画像の出力
cv2.imwrite('face_cut.png', face_cut)