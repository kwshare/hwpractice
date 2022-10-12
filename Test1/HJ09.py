# HJ9 提取不重复的整数

# a = input()
# a = a[::-1]
# num = []
# for i in a:
#     if i in num:
#         continue
#     else:
#         num.append(i)
#         print(i,end='')

# 入门  通过率：44.27%  时间限制：1秒  空间限制：32M
# 知识点 数组 哈希

# 描述
# 输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
# 保证输入的整数最后一位不是0 。

# 数据范围： 1 <= n <= 10^8


# 输入描述：
# 输入一个int型整数

# 输出描述：
# 按照从右向左的阅读顺序，返回一个不含重复数字的新的整数

# 示例1
# 输入：
# 9876673

# 输出：
# 37689

n = input()
n1 = n[::-1]
print(n1)
l = []
for i in n1:
    if i in l:
        continue
    else:
        l.append(i)
        print(i, end='')