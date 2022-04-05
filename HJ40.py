# HJ40 统计字符



while True:
    try:
        s=input()
        l=[0,0,0]
        for i in s:
            l[0]+=int(i.isalpha())
            l[1]+=int(i==' ')
            l[2]+=int(i.isnumeric())
        print(l[0])
        print(l[1])
        print(l[2])
        print(len(s)-l[0]-l[1]-l[2])
    except:
        break






'''

简单  通过率：44.71%  时间限制：1秒  空间限制：32M
知识点
字符串
哈希
warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。
描述
输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。

数据范围：输入的字符串长度满足 1 \le n \le 1000 \1≤n≤1000

输入描述：
输入一行字符串，可以有空格

输出描述：
统计其中英文字符，空格字符，数字字符，其他字符的个数

示例1
输入：
1qazxsw23 edcvfr45tgbn hy67uj m,ki89ol.\\/;p0-=\\][
复制
输出：
26
3
10
12
'''