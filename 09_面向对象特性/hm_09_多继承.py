class A:

    def test(self):
        print("test 方法")


class B:

    def demo(self):
        print("demo 方法")


# 多继承语法： class 子类名(父类名1,父类名2...)
class C(A, B):
    """多继承可以让子类对象，同时具有多个父类的属性和方法"""
    pass


# 创建子类对象
c = C()

c.test()
c.demo()
