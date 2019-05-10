# python 中有两种 多值参数
# 参数名前增加一个 * 可以接收元组， 元组参数习惯使用 *args 作为参数名
# 参数名前增加两个 * 可以接收字典， 字典参数习惯使用 **kwargs 作为参数名
def demo(num, *nums, **personn):

    print(num)
    print(nums)
    print(personn)


# demo(1)
demo(1, 2, 3, 4, 5, name="小明", age=18)

