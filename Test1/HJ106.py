# HJ106 字符逆序

while True:
    try:
        string = str(input().strip())
        print(string[::-1])
    except:
        break


# 简单  通过率：45.12%  时间限制：1秒  空间限制：32M
# 知识点 字符串
# warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。

# 描述
# 将一个字符串str的内容颠倒过来，并输出。

# 数据范围：1 <= len(str) = 10000
# 输入描述：
# 输入一个字符串，可以有空格

# 输出描述：
# 输出逆序的字符串

# 示例1
# 输入：
# I am a student

# 输出：
# tneduts a ma I

# 示例2
# 输入：
# nowcoder

# 输出：
# redocwon