class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    # 类方法需要用修饰器 @classmethod 来标识，告诉解释器这是一个类方法
    # 类方法的第一个参数应该是 cls
    @classmethod
    def show_tool_count(cls):

        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name

        # 让类属性的值+1
        Tool.count += 1


# 1.创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")

# 调用类方法
Tool.show_tool_count()
