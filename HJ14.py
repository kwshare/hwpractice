# HJ14 字符串排序

# while True:
#     try:
#         num = int(input())
#         stack=[]
#         for i in range(num):
#             stack.append(input())
#         print("\n".join(sorted(stack)))
#     except:
#         break

num = int(input())    #num记录输入的词的个数
b = []
for i in range(num):
    b.append(input())    #用列表b记录所有的输入的词汇
b.sort()    #列表排序，默认为从小到大
for i in b:
    print(i)    #按要求输出即可


# 简单  通过率：41.55%  时间限制：1秒  空间限制：32M
# 知识点
# 字符串
# 排序



# 描述
# 给定 n 个字符串，请对 n 个字符串按照字典序排列。

# 数据范围： 1 <= n <= 1000，字符串长度满足 1 <= len <= 100

# 输入描述：
# 输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。

# 输出描述：
# 数据输出n行，输出结果为按照字典序排列的字符串。

# 示例1
# 输入：
# 9
# cap
# to
# cat
# card
# two
# too
# up
# boat
# boot

# 输出：
# boat
# boot
# cap
# card
# cat
# to
# too
# two
# up