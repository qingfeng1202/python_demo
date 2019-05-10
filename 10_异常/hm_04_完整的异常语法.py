try:
    # 提示用户输入一个整数
    num = int(input("输入一个整数："))

    # 使用 8 除以用户输入的整数并输出
    result = 8 / num

    print(result)
except ValueError:
    print("请输入正确的整数")
except Exception as result:
    print("未知错误 %s" % result)
else:
    print("尝试成功")
finally:
    print("无论是否出现错误都会执行的代码")


"""
# 完整捕获异常的代码
try:
    # 尝试执行的代码
    pass
except 错误类型1：
    # 针对错误1，对应的代码处理
    pass
except (错误类型2)：
    # 针对错误类型2，对应的代码处理
    pass
except (错误类型3, 错误类型4)：
    # 针对错误类型3 和 4，对应的代码处理
    pass
except Exception as result:
    print("未知错误 %s" % result)
else:
    # 没有异常才会执行的代码
    pass
finally:
    print("无论是否有异常，都会执行的代码")
"""
