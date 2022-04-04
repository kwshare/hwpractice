# HJ20 密码验证合格程序


def check(s):
    if len(s) <= 8:
        return 0
    a, b, c, d = 0, 0, 0, 0
    for item in s:
        if ord('a') <= ord(item) <= ord('z'):
            a = 1
        elif ord('A') <= ord(item) <= ord('Z'):
            b = 1
        elif ord('0') <= ord(item) <= ord('9'):
            c = 1
        else:
            d = 1
    if a + b + c + d < 3:
        return 0
    for i in range(len(s)-3):
        if len(s.split(s[i:i+3])) >= 3:
            return 0
    return 1

while 1:
    try:
        print('OK' if check(input()) else 'NG')
    except:
        break


# def check(pw):
#     if len(pw) <= 8:  # 判断密码的长度
#         return False
#
#     checks = [0, 0, 0, 0]  # 四种情况满足三种的辅助列表
#     for c in pw:
#         if c.isupper():  # 大写字母
#             checks[0] = 1
#         elif c.islower():  # 小写字母
#             checks[1] = 1
#         elif c.isdigit():  # 数字
#             checks[2] = 1
#         else:  # 其他字符
#             checks[3] = 1
#     if sum(checks) < 3:
#         return False
#
#     for i in range(len(pw) - 2):  # 循环遍历找到子字符串的起点
#         if pw[i:i + 3] in pw[i + 3:]:  # 在剩下的字符串中顺序查找匹配当前字符串
#             return False
#
#     return True
#
#
# while True:
#     try:
#         pw = input()
#         if check(pw):
#             print('OK')
#         else:
#             print('NG')
#     except:
#         break


# def check(pw):
#     if len(pw) <= 8:  # 判断密码的长度
#         return False
#
#     checks = [0, 0, 0, 0]  # 四种情况满足三种的辅助列表
#     for c in pw:
#         if c.isupper():  # 大写字母
#             checks[0] = 1
#         elif c.islower():  # 小写字母
#             checks[1] = 1
#         elif c.isdigit():  # 数字
#             checks[2] = 1
#         else:  # 其他字符
#             checks[3] = 1
#     if sum(checks) < 3:
#         return False
#
#     dc = {}
#     for i in range(len(pw) - 2):  # 遍历所有的子字符串起点
#         if pw[i:i + 3] in dc:  # 在字典中搜索
#             return False
#         else:  # 如果未曾经出现过则加入字典中，等待之后的判定
#             dc[pw[i:i + 3]] = 1
#
#     return True
#
#
# while True:
#     try:
#         pw = input()
#         if check(pw):
#             print('OK')
#         else:
#             print('NG')
#     except:
#         break

# def checkLegal(pswd):
#     if len(pswd) <= 8:return False
#     else:
#         #最大重复子串长度2+
#         sub = []
#         for i in range(len(pswd)-2):
#             sub.append(pswd[i:i+3])
#         if len(set(sub)) < len(sub):return False
#         #check type
#         type_ = 0
#         import re
#         Upper = '[A-Z]'
#         Lowwer = '[a-z]'
#         num = '\d'
#         chars = '[^A-Za-z0-9_]'
#         patterns = [Upper, Lowwer, num, chars]
#         for pattern in patterns:
#             pw = re.search(pattern, pswd)
#             if pw : type_ += 1
#         return True if type_ >= 3 else False
# while True:
#     try:
#         pswd = input()
#         print('OK' if checkLegal(pswd) else 'NG')
#     except:
#         break



# 中等  通过率：28.92%  时间限制：1秒  空间限制：32M
# 知识点 字符串 数组 模拟

# 描述
# 密码要求:
# 1.长度超过8位
# 2.包括大小写字母.数字.其它符号,以上四种至少三种
# 3.不能有长度大于2的不含公共元素的子串重复 （注：其他符号不含空格或换行）

# 数据范围：输入的字符串长度满足 1 <= n <= 100

# 输入描述：
# 一组字符串。

# 输出描述：
# 如果符合要求输出：OK，否则输出NG

# 示例1
# 输入：
# 021Abc9000
# 021Abc9Abc1
# 021ABC9000
# 021$bc9000

# 输出：
# OK
# NG
# NG
# OK