# HJ7 取近似值

# n = float(input())    # 将输入转换成浮点数
# res = n // 1            #计算整数部分
# tep = n - res            #计算小数部分
# # 判断小数部分的数值是否大于0.5，并输出结果
# if tep >= 0.5:
#     print(int(res+1))
# else:
#     print(int(res))


# 入门  通过率：50.10%  时间限制：1秒  空间限制：32M
# 知识点 基础数学 语法题

# 描述
# 写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于 0.5 ,向上取整；小于 0.5 ，则向下取整。

# 数据范围：保证输入的数字在 32 位浮点数范围内

# 输入描述：
# 输入一个正浮点数值

# 输出描述：
# 输出该数值的近似整数值

# 示例1
# 输入：
# 5.5

# 输出：
# 6

# 说明：
# 0.5>=0.5，所以5.5需要向上取整为6

# 示例2
# 输入：
# 2.499

# 输出：
# 2

# 说明：
# 0.499<0.5，2.499向下取整为2

while True:
    try:
        f = float(input())
        f1 = f // 1
        x = f - f1
        if x >= 0.5:
            print(int(f1+1))
        else:
            print(int(f1))
    except:
        break