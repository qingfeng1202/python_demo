try:
    # 提示用户输入一个整数
    num = int(input("输入一个整数："))

    # 使用 8 除以用户输入的整数并输出
    result = 8 / num

    print(result)
except ZeroDivisionError:
    print("除0错误")
except ValueError:
    print("请输入正确的整数")


"""
try:
    # 尝试执行的代码
    pass
except 错误类型1：
    # 针对错误1，对应的代码处理
    pass
except (错误类型2, 错误类型3)：
    # 针对错误类型2 和 3，对应的代码处理
    pass
except Exception as result:
    print("未知错误 %s" % result)
"""
