# HJ28 素数伴侣


def get_primenum(s):
    if s < 4:
        return True
    # 通过从2到它的平方根之间没有可除尽的数来判断这个数是否为素数。原理：一个数与另一个数能除尽则也能除尽这个数的2倍数。若直接判断从2到这个数之间的数则会耗费大量的时间来计算导致超时。
    for i in range(2, int(s ** 0.5) + 1):
        if s % i == 0:
            return False
    return True


def find_even(evens, previous_select, final_select, odd):
    for i, even in enumerate(evens):
        if get_primenum(even + odd) and previous_select[i] == 0:
            previous_select[i] = 1
            # 判断第i位偶数是否被匹配或者它的匹配奇数是否有其他选择，如果有其他选择，则当前的奇数匹配第i位偶数
            if final_select[i] == 0 or find_even(evens, previous_select, final_select, final_select[i]):
                final_select[i] = odd
                return True
    return False


while True:
    try:
        N = int(input())
        list0 = list(map(int, input().split(' ')))
        count0 = 0
        evens, odds = [], []
        for list1 in list0:
            if list1 % 2 == 0:
                evens.append(list1)
            else:
                odds.append(list1)
        final_select = [0] * len(evens)
        for odd in odds:
            previous_select = [0] * len(evens)
            if find_even(evens, previous_select, final_select, odd):
                count0 += 1
        print(count0)
    except:
        break

'''
困难  通过率：25.52%  时间限制：1秒  空间限制：32M

知识点 查找  排序

warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。

描述
题目描述
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。现在密码学会请你设计一个程序，从已有的 N （ N 为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选方案多种多样，例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，而将2和5、6和13编组将得到两组“素数伴侣”，能组成“素数伴侣”最多的方案称为“最佳方案”，当然密码学会希望你寻找出“最佳方案”。

输入:
有一个正偶数 n ，表示待挑选的自然数的个数。后面给出 n 个具体的数字。

输出:
输出一个整数 K ，表示你求得的“最佳方案”组成“素数伴侣”的对数。


数据范围： 1≤n≤100  ，输入的数据大小满足 2≤val≤30000
输入描述：
输入说明
1 输入一个正偶数 n
2 输入 n 个整数

输出描述：
求得的“最佳方案”组成“素数伴侣”的对数。

示例1
输入：
4
2 5 6 13

输出：
2

示例2
输入：
2
3 6

输出：
0

示例3
输入：
2
3 6

输出：
0
'''
