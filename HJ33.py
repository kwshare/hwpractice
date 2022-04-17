# HJ33 整数与IP地址间的转换


while True:
    try:
        ip = input()
        num = input()
    except:
        break
    else:
        # ip to num
        ip_list = ip.split('.')
        ip2num = str()
        for i in ip_list:
            a = bin(int(i,10))[2:]
            a = '0'*(8-len(a)) + a if len(a)<8 else a
            ip2num += a
        print(int(ip2num,2))
        # num to ip
        num2ip = []
        num2 = bin(int(num,10))[2:]
        num2 = '0'*(32-len(num2)) + num2 if len(num2)<32 else num2
        for i in range(4):
            b = num2[8*i:8*i+8]
            b = str(int(b,2))
            num2ip.append(b)
        print('.'.join(num2ip))






'''
中等  通过率：32.09%  时间限制：1秒  空间限制：32M
知识点
字符串
模拟
warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。
描述
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001

组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。

数据范围：保证输入的是合法的 IP 序列

输入描述：
输入
1 输入IP地址
2 输入10进制型的IP地址

输出描述：
输出
1 输出转换成10进制的IP地址
2 输出转换后的IP地址

示例1
输入：
10.0.3.193
167969729

输出：
167773121
10.3.3.193
'''