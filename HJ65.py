# HJ65 查找两个字符串a,b中的最长公共子串




while True:
    try:
        a, b = input(), input() # a保存短，b保存长
        if len(a) > len(b):
            a, b = b, a
        res = ''
        for i in range(0, len(a)):
            for j in range(i+1, len(a)):
                if a[i:j+1] in b and j+1-i > len(res):
                    res = a[i:j+1]
        print(res)
    except:
        break






'''
中等  通过率：36.15%  时间限制：1秒  空间限制：32M
知识点
字符串
warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。
描述
查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
注：子串的定义：将一个字符串删去前缀和后缀（也可以不删）形成的字符串。请和“子序列”的概念分开！

数据范围：字符串长度1\le length \le300 \1≤length≤300
进阶：时间复杂度：O(n^3)\O(n
3
 ) ，空间复杂度：O(n)\O(n)
输入描述：
输入两个字符串

输出描述：
返回重复出现的字符
示例1
输入：
abcdefghijklmnop
abcsafjklmnopqrstuvw
复制
输出：
jklmnop
'''