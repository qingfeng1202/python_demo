class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    # 在 定义属性或方法时，在属性名或者方法名前 增加 两个下划线，定义的就是 私有 属性或方法
    def __secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaofang = Women("小芳")

# 私有属性，在外界不能够被直接访问
print(xiaofang._Women__age)
# 私有方法，同样不允许在外界直接访问
# Python 中，并没有真正意义的私有
# 在给属性、方法命名时，实际是对名称做了一些特殊处理，使得外界无法访问到
# 处理方式：在 名称 前面加上 _类名 => _类名__名称
xiaofang._Women__secret()
