class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print("%s 来了" % self.name)

    # 会在对象被销毁之前调用
    def __del__(self):

        print("%s 我去了" % self.name)

    # __str__ 方法必须返回一个字符串
    def __str__(self):

        # 必须返回一个字符串
        return "我是小猫[%s]" % self.name


# tom 是一个全局变量
tom = Cat("Tom")
print(tom)
