# 将形如”序号1_名字_XXXXXXXXXX“的文件全部重命名为名字
import os

# 读取文件夹下所有文件
files = os.listdir("images/member_photo")
for file in files:
    # 判断文件名是否符合要求
    if file.startswith("序号"):
        # 重命名文件
        os.rename("images/member_photo/" + file, "images/member_photo/" + file.split("_")[1] + ".png")