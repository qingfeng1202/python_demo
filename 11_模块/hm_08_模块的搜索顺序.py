import random

rand = random.randint(0, 10)

print(rand)

# 模块内置属性 __file__ 可以查看 模块的完整路径
print(random.__file__)

"""
python 的解释器在 导入模块 时，会：
1.搜索 当前目录指定模块名的文件，如果有就直接导入
2.如果没有，在搜索 系统目录
所有 在开发时，给文件起名，不要和 系统的模块文件 重名
"""