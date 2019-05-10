file = open("README")

while True:
    text = file.readline()

    # 判断是否读取到内容
    if not text:
        break

    print(text)

file.close()

"""
readline 方法可以一次读取一行内容
方法执行后，会把 文件指针 移动到下一行，准备再次读取
"""
