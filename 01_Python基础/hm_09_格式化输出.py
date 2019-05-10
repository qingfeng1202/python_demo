"""
格式化字符串
格式化操作符
%s 字符串
%d 整数        %06d  使输出的数字为6位长度，少于6位，前面补零，超过6位，就不改变数据
%f 浮点数      %.2f  表示小数点后面显示2位
%% 输出%
"""

# 定义字符串变量  name, 输出 我的名字叫 小明，请多多关照
name = "小明"
print("我的名字叫 %s,请多多关照" % name)

# 定义整数变量 student_no，输出 我的学号是 000001
student_no = 1
print("我的学号是 %06d" % student_no)

# 定义小数 price weight money
# 输出 苹果单价 9.00元/斤，购买了5.00斤，需要支付45.00元
price = 8.5
weight = 7.5
money = price * weight
print("苹果单价 %.2f元/斤，购买了%.2f斤，需要支付%.2f元" % (price, weight, money))

# 定义一个小数scale，输出 数据比例是10.00%
scale = 0.25
print("数据比例是 %.2f%%" % (scale * 100))
