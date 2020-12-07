# -*- coding:utf-8 -*-
from PIL import Image

# アニメーションの最初の画像のオブジェクト作成
before = Image.open("user_image.jpg")

# アニメーションの最後の画像のオブジェクト作成
after = Image.open("seamlessclone.jpg")

# 画像を格納するリスト(空)を作成
frames = []

# beforeからafterへ徐々に変化させていく
for a in range(0, 101, 4):

    # beforeとafterの混ぜ具合を設定
    alpha = a / 100

    # beforeとafterをalphaの混ぜ具合でブレンド
    blended_image = Image.blend(before, after, alpha)

    # 作成した画像オブジェクトをリストに追加
    frames.append(blended_image)

# durationを格納するリスト(空)を作成
duration = []

# 各画像に対してdurationを設定
for i in range(len(frames)):
    if i == 0 or i == len(frames) - 1:
        # １枚目と最後の画像だけ2000ms表示
        duration.append(2000)
    else:
        # その他の画像は50ms表示
        duration.append(50)


# アニメーション GIF として保存
frames[0].save(
    # ファイル名
    "neko_anime.gif",

    # アニメーションとして保存
    save_all=True,

    # アニメーションに含ませる画像のリスト
    append_images=frames[1:],

    # 画像の表示時間（リストで指定）
    duration=duration,

    # ３回表示
    loop=2
)