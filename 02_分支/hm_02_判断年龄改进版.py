# 输入用户年龄
age = int(input("输入用户年龄:"))

# 判断是否满了18岁
if age >= 18:
    # 如果满了18岁，可以进网吧嗨皮
    print("你已经成年，欢迎进网吧嗨皮")
else:
    # 如果未满18岁，提示回家写作业
    print("你还没有成年，请回家写作业吧")

# 这句代码无论条件是否成立都会执行
print("这句代码什么时候执行")

