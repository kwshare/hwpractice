# HJ86 求最大连续bit数/



while True:
    try:
        num = int(input())
        tep = bin(num)[2:]
        print(bin(num))
        # print(tep)
        list1 = sorted(list(set(tep.split('0'))), key=lambda x: len(x), reverse=True)
        # list1 = sorted(list(set(tep.split('0'))), key=lambda x: len(x), reverse=True)
        # print(tep.split('0'))
        # print(set(tep.split('0')))
        # print(list(set(tep.split('0'))))
        # print(list1)
        print(len(list1[0]))
    except:
        break





'''
简单  通过率：45.81%  时间限制：1秒  空间限制：32M

知识点 位运算

warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。

描述
求一个int类型数字对应的二进制数字中1的最大连续数，例如3的二进制为00000011，最大连续2个1

数据范围：数据组数：1 <= t <= 5，1 <= n <= 500000

进阶：时间复杂度：O(logn) ，空间复杂度：O(1)

输入描述：
输入一个int类型数字

输出描述：
输出转成二进制之后连续1的个数

示例1
输入：
200

输出：
2

说明：
200的二进制表示是11001000，最多有2个连续的1。

'''