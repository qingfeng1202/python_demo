# 1.打开
file_read = open("README")
file_wirte = open("README[复件]", "w")

# 2.读、写
text = file_read.read()
file_wirte.write(text)

# 3.关闭
file_read.close()
file_wirte.close()
