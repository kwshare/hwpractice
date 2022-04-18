# HJ46 截取字符串

# while True:
#     try:
#         data1 = input()    # 获取输入字符
#         k = int(input())    # 获取正整数k
#         list1 = []        #定义列表
#         for i in range(k):
#             list1.append(data1[i])
#         print(''.join(list1))
#     except:
#         break

while True:
    try:
        string1 = input()  # 获取输入字符
        k = int(input())  # 获取整数 k
        print(string1[:k])  # 通过切片的方式截取输入字符的前K位
    except:
        break


# 描述
# 输入一个字符串和一个整数 k ，截取字符串的前k个字符并输出
#
# 数据范围：字符串长度满足 1 <= n <= 1000， 1  <= k  <= n
# 输入描述：
# 1.输入待截取的字符串
#
# 2.输入一个正整数k，代表截取的长度
#
# 输出描述：
# 截取后的字符串
#
# 示例1
# 输入：
# abABCcDEF
# 6

# 输出：
# abABCc

# 示例2
# 输入：
# bdxPKBhih
# 6

# 输出：
# bdxPKB