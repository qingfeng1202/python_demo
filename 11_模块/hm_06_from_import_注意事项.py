from hm_01_测试模块1 import say_hello
from hm_02_测试模块2 import say_hello as module2_say_hello

say_hello()
module2_say_hello()

"""
from ... import: 从某个模块中，导入 部分 工具
语法：
from 模块名 import 工具名
导入之后
不需要 通过 模块名.
可以直接使用 模块提供的工具 -- 全局变量、函数、类
注意：
如果两个模块，存在同名的函数，那么 后导入模块的函数，会 覆盖掉先导入的函数
开发时 import 代码应该统一写在代码的顶部，更容易及时发现冲突
一旦发现冲突，可以使用 as 关键字给其中一个工具起一个别名
"""