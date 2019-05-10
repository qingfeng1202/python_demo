class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print("%s 来了" % self.name)

    # 会在对象被销毁之前调用
    def __del__(self):

        print("%s 我去了" % self.name)


# tom 是一个全局变量
tom = Cat("Tom")
print(tom.name)

# del 关键字可以删除一个对象， 实际是调用对象的 __del__ 方法
del tom

print("-" * 50)
