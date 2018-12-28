import cv2
import math
import numpy as np

file_src = 'src.png'
file_dst = 'dst.png'

img_src = cv2.imread(file_src, 0)

cv2.namedWindow('src')
cv2.namedWindow('dst')

# ここに核となる処理を記述する

# denoiseのためのフォーマット変換
img_src = cv2.cvtColor(img_src,cv2.COLOR_GRAY2BGR)

# denoise
img_src = cv2.fastNlMeansDenoisingColored(img_src,None,10,10,7,21)


# ルックアップテーブルの生成
    
look_up_table = np.ones((256, 1), dtype = 'uint8' ) * 0

for i in range(256):
    if i <= 0:
       look_up_table[i][0] = 0
    elif i < 32:
       look_up_table[i][0] = 32
    elif i < 64:
       look_up_table[i][0] = 64
    elif i < 96:
       look_up_table[i][0] = 96
    elif i < 128:
       look_up_table[i][0] = 128
    elif i < 160:
       look_up_table[i][0] = 160
    elif i < 192:
       look_up_table[i][0] = 192
    elif i < 224:
       look_up_table[i][0] = 224
    else:
       look_up_table[i][0] = 255



#postrization実行
img_src = cv2.LUT(img_src, look_up_table)

#Canny

img_dst = cv2.Canny(img_src,0,0,3)

#bit反転
img_dst = cv2.bitwise_not(img_dst)

cv2.imshow('src', img_src) # 入力画像を表示
cv2.imshow('dst', img_dst) # 出力画像を表示
cv2.imwrite(file_dst, img_dst) # 処理結果の保存

cv2.waitKey(0) # キー入力待ち
cv2.destroyAllWindows()
