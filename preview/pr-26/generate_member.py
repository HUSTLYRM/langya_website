# 根据 形如 ”名字	职责	类型“的格式保存 members 的 md 格式文件

# ---
# name: 名字
# image: images/member_photo/名字.jpg
# role: 
# type: 
# links:
# description:
# ---

import os

# 输入成员信息
while True:
    str = input()
    if str == "":
        break
    members = str.split("\t")
    # 保存成员信息
    file_path = "_members/" + members[0] + ".md"
    # 如果文件不存在，创建
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("---"+ "\n")
            f.write("name: " + members[0] + "\n")
            f.write("image: images/member_photo/" + members[0] + ".png\n")
            f.write("role: " + members[1] + "\n")
            f.write("type: " + members[2] + "\n")
            f.write("links:\n")
            f.write("description:\n")
            f.write("---"+ "\n")