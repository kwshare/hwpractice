# HJ90 合法IP


while True:
    try:
        string = input().split('.')
        count = 0
        if len(string) != 4:
            print('NO')
            continue
        for i in string:
            if not i.isdigit():
                print("NO")
                continue
            elif int(i) > 255 or (i.startswith('0') and len(i) > 1):
                print('NO')
                continue
            else:
                count += 1
        if count == 4:
            print("YES")
    except:
        break


'''
中等  通过率：30.93%  时间限制：1秒  空间限制：32M
知识点 字符串 链表  队列  栈  安全工程师  小米   2021

warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。

描述
IPV4地址可以用一个32位无符号整数来表示，一般用点分方式来显示，点将IP地址分成4个部分，每个部分为8位，表示成一个无符号整数（因此正号不需要出现），如10.137.17.1，是我们非常熟悉的IP地址，一个IP地址串中没有空格出现（因为要表示成一个32数字）。

现在需要你用程序来判断IP是否合法。

数据范围：数据组数：1\le t\le 18\1≤t≤18
进阶：时间复杂度：O(n)\O(n) ，空间复杂度：O(n)\O(n)

输入描述：
输入一个ip地址，保证不包含空格

输出描述：
返回判断的结果YES or NO

示例1
输入：
255.255.255.1000

输出：
NO
'''