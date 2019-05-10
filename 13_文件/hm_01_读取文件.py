# 1.打开文件
file = open("README")

# 2.读取文件内容
text = file.read()
print(text)

# 3.关闭文件
file.close()

"""
open 函数的第一个参数就是要打开的文件名（文件名区分大小写）
如果文件存在，返回文件操作对象
如果文件不存在，会抛出异常
"""
