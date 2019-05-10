def demo(*args, **kwargs):

    print(args)
    print(kwargs)


# 元组变量/字典变量
gl_nums = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}

# demo(gl_nums, gl_dict)
# 拆包语法，简化元组变量/字典变量的传递
# 拆包：
#      在元组变量前，增加一个 *
#      在字典变量前，增加两个 *
demo(*gl_nums, **gl_dict)

demo(1, 2, 3, name="小明", age=18)
