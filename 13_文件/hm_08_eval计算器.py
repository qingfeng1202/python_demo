# input_str = input("请输入算术题")
#
# print(eval(input_str))

# 基本的数学计算
print(eval("(1+1)*2"))

# 字符串重复
print(eval("'*' * 10"))

# 将字符串转换成列表
print(type(eval("[1, 2, 3, 4, 5]")))

# 将字符串转换成字典
print(type(eval("{'name': 'xiaoming', 'age': 18}")))

"""
eval()函数--将字符串 当成 有效的表达式 来求值 并 返回计算结果
开发时千万不要使用 eval 直接转换 input 的结果
例：__import__('os').system('ls') 直接调用终端命令操作文件，十分危险
"""
