# 计算 0-100 之间所有数字的累计求和结果
# 定义最终结果的变量
result = 0

# 1.定义一个整数变量，记录循环次数
i = 0

# 2.开始循环
while i <= 100:
    # 每一次循环， 都让 result 这个变量和 i 这个计数器相加
    result += i

    # 处理计数器
    i += 1

print("0-100 之间所有数字的求和结果 = %d" % result)
