# HJ23 删除字符串中出现次数最少的字符





s = input()
dic = {}
for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
MIN = min(dic.values())
for i in s:
    if dic[i] == MIN:
        s = s.replace(i,'')
# print(dic)
print(s)


# 简单  通过率：33.24%  时间限制：1秒  空间限制：32M
# 知识点 字符串 哈希

# warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。

# 描述
# 实现删除字符串中出现次数最少的字符，若出现次数最少的字符有多个，则把出现次数最少的字符都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。

# 数据范围：输入的字符串长度满足 1 <= n <= 20 ，保证输入的字符串中仅出现小写字母
# 输入描述：
# 字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

# 输出描述：
# 删除字符串中出现次数最少的字符后的字符串。

# 示例1
# 输入：
# aabcddd

# 输出：
# aaddd