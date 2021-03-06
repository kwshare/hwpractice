# HJ11 数字颠倒

# print(input()[::-1])

# print(input()[-1::-1])

nums = input()
i = len(nums) - 1
ans = []
while i >= 0:
    ans.append(nums[i])
    i = i - 1

rev = ''.join(ans)  # list to string
print(rev)


# 简单  通过率：58.52%  时间限制：1秒  空间限制：32M
# 知识点
# 字符串

# warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。

# 描述
# 输入一个整数，将这个整数以字符串的形式逆序输出
# 程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001


# 数据范围： 0 <=  n <=  2^{30}-1

# 输入描述：
# 输入一个int整数

# 输出描述：
# 将这个整数以字符串的形式逆序输出

# 示例1
# 输入：
# 1516000

# 输出：
# 0006151

# 示例2
# 输入：
# 0

# 输出：
# 0