import os

# 重命名
# os.rename("README[复件]", "123")

# 删除
# os.remove("123")

print(os.listdir("."))

"""
listdir         目录列表              os.listdir(目录名)
mkdir           创建目录              os.mkdir(目录名)
rmdir           删除目录              os.rmdir(目录名)
getcwd          获取当前目录          os.getcwd()
chdir           修改工作目录          os.chdir(目录名)
path.isdir      判断是否是文件        os.path.isdir(文件路径)
"""