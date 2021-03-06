# HJ26 字符串排序


while True:
    try:
        s = input()
        a = ''
        for i in s:
            if i.isalpha():
                a += i
        b = sorted(a, key=str.upper)
        index = 0
        d = ''
        for i in range(len(s)):
            if s[i].isalpha():
                d += b[index]
                index += 1
            else:
                d += s[i]
        print(d)
    except:
        break




'''
中等  通过率：36.94%  时间限制：1秒  空间限制：32M
知识点
字符串
排序
warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。
描述
编写一个程序，将输入字符串中的字符按如下规则排序。

规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。

如，输入： Type 输出： epTy

规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。

如，输入： BabA 输出： aABb

规则 3 ：非英文字母的其它字符保持原来的位置。


如，输入： By?e 输出： Be?y

数据范围：输入的字符串长度满足 1 \le n \le 1000 \1≤n≤1000

输入描述：
输入字符串
输出描述：
输出字符串
示例1
输入：
A Famous Saying: Much Ado About Nothing (2012/8).
复制
输出：
A aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8).
'''