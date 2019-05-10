name = "小明"

# 不能将 函数的调用 放在 函数的定义 上方
# say_hello()

# Python 解释器知道下方定义了一个函数


def say_hello():
    """函数的文档注释，函数定义的上方需要空出2行"""
    print("hello 1")
    print("hello 2")
    print("hello 3")


print(name)

# 只有在调用函数时，之前定义的函数才会被执行
# 函数执行完成之后，会重新回到之前的程序中，继续执行后续的代码
say_hello()

print(name)
