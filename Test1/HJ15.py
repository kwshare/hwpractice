# HJ15 求int型正整数在内存中存储时1的个数

# num = int(input().strip())
# n = 0
# while num > 0:
#     if num%2:
#         n += 1
#     num = num//2

# print(n)
# 调用bin()方法得到二进制数据，并使用count()方法对得到的二进制数据中1的个数进行计数
num = int(input())
print(bin(num).count('1'))



# 简单  通过率：57.07%  时间限制：1秒  空间限制：32M
# 知识点
# 位运算

# warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。

# 描述
# 输入一个 int 型的正整数，计算出该 int 型数据在内存中存储时 1 的个数。

# 数据范围：保证在 32 位整型数字范围内
# 输入描述：
#  输入一个整数（int类型）

# 输出描述：
#  这个数转换成2进制后，输出1的个数

# 示例1
# 输入：
# 5

# 输出：
# 2

# 示例2
# 输入：
# 0

# 输出：
# 0