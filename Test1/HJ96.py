# HJ96 表示数字

while True:
    try:
        s = input()
        s_o = ''
        char_pre = ''
        for i in s:  # 遍历字符串
            if i.isdigit():  # 遇到数字，判断其前面是否非数字，是则表示数字的开始，先插入‘*’
                if char_pre.isdigit() != True:
                    s_o += '*'
            else:  # 非数字情况，判断其前是否为数字，是则表示数字结束，插入‘*’
                if char_pre.isdigit():
                    s_o += '*'
            s_o += i  # 把当前字符带出来
            char_pre = i  # 当前字符更新到 前字符
        if i.isdigit():  # 结束的时候，判断是否数字结束，如果是的话，插入‘*’
            s_o += '*'
        print(s_o)
    except:
        break



# 正则表达式
# import re
# while True:
#     try:
#         print(re.sub('(\d+)', '*\g<1>*', input()))
#     except:
#         break



'''
简单  通过率：33.77%  时间限制：1秒  空间限制：32M

知识点 字符串 模拟

warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。

描述
将一个字符中所有的整数前后加上符号“*”，其他字符保持不变。连续的数字视为一个整数。


数据范围：字符串长度满足 1≤ n ≤100

输入描述：
输入一个字符串

输出描述：
字符中所有出现的数字前后加上符号“*”，其他字符保持不变

示例1
输入：
Jkdi234klowe90a3

输出：
Jkdi*234*klowe*90*a*3*
'''