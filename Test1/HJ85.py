# HJ85 最长回文子串


while True:
    try:
        s = input()
        res = []

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    res.append(j - i)
        if res != '':
            print(max(res))
    except:
        break




'''
简单  通过率：41.05%  时间限制：1秒  空间限制：32M

知识点  字符串 穷举

warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。

描述
给定一个仅包含小写字母的字符串，求它的最长回文子串的长度。
所谓回文串，指左右对称的字符串。
所谓子串，指一个字符串删掉其部分前缀和后缀（也可以不删）的字符串
数据范围：字符串长度 <= s <= 350

进阶：时间复杂度：O(n) ，空间复杂度：O(n)

输入描述：
输入一个仅包含小写字母的字符串

输出描述：
返回最长回文子串的长度

示例1
输入：
cdabbacc

输出：
4

说明：
abba为最长的回文子串
'''