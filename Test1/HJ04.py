# HJ4 字符串分隔

# def fg(a):
#     if len(a) <= 8:
#         print(a.ljust(8, '0'))
#     else:
#         print(a[0:8])
#         b = a[8:len(a)]
#         fg(b)
#
#
# while True:
#     try:
#         a = input()
#         fg(a)
#     except:
#         break

# 简单  通过率：28.61%  时间限制：1秒  空间限制：32M
# 知识点    字符串

# 描述
# 连续输入字符串，请按长度为8拆分每个输入字符串并进行输出；
# 长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。

# 输入描述：
# 连续输入字符串(每个字符串长度小于等于100)

# 输出描述：
# 依次输出所有分割后的长度为8的新字符串

# 示例1
# 输入：
# abc

# 输出：
# abc00000

# 递归
def f(a):
    if len(a)<=8:
        print(a.ljust(8, '0'))
    else:
        print(a[0:8])
        b = a[8:len(a)]
        f(b)


while True:
    try:
        s = input()
        f(s)
    except:
        break