# 读取png图片，将图片黑色变成白色，透明保持不变
import cv2
import os


image = cv2.imread('images/logo.png', cv2.IMREAD_UNCHANGED)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i, j][0] == 0 and image[i, j][1] == 0 and image[i, j][2] == 0:
            image[i, j][0] = 255
            image[i, j][1] = 255
            image[i, j][2] = 255
cv2.imwrite('images/1.png', image)
