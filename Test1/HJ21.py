# HJ21 简单密码

# while True:
#     try:
#         s = input()
#         res = []
#         for i in s:
#             if i.isdigit():
#                 res.append(i)
#             elif i.isupper() and i != 'Z':
#                 res.append(chr(ord(i.lower()) + 1))
#             elif i == 'Z':
#                 res.append('a')
#             else:
#                 if i in 'abc':
#                     res.append('2')
#                 elif i in 'def':
#                     res.append('3')
#                 elif i in 'ghi':
#                     res.append('4')
#                 elif i in 'jkl':
#                     res.append('5')
#                 elif i in 'mno':
#                     res.append('6')
#                 elif i in 'pqrs':
#                     res.append('7')
#                 elif i in 'tuv':
#                     res.append('8')
#                 else:
#                     res.append('9')
#         print(''.join(res))
#     except:
#         break
while True:
    try:
        A="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        B="22233344455566677778889999bcdefghijklmnopqrstuvwxyza0123456789"
        list1 = []
        list2 = []
        for i in A:
            list1.append(i)
        for i in B:
            list2.append(i)
        C=[]
        a=input()
        for i in a:
            if i in list1:
                C.append(list2[list1.index(i)])
            else:
                C.append(i)
        print(''.join(C))
    except:
        break



# 描述:
# 现在有一种密码变换算法。
# 九键手机键盘上的数字与字母的对应： 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0，把密码中出现的小写字母都变成九键键盘对应的数字，如：a 变成 2，x 变成 9.
# 而密码中出现的大写字母则变成小写之后往后移一位，如：X ，先变成小写，再往后移一位，变成了 y ，例外：Z 往后移是 a 。
# 数字和其它的符号都不做变换。
# 数据范围： 输入的字符串长度满足 1 <= n <= 100

# 输入描述：
# 输入一组密码，长度不超过100个字符。

# 输出描述：
# 输出密码变换后的字符串

# 示例1
# 输入：
# YUANzhi1987

# 输出：
# zvbo9441987