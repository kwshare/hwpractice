# HJ91 走方格的方案数

# 题意符合排列组合问题，从左上到右下需要向右移动m次和向下移动n次（或向右n次和向下m次）
# 移动总步数为T=m+n，则可能的移动情况为C(T,m)或者C(T,n)
def factorial(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

while True:
    try:
        m,n = list(map(int,input().split()))
        print(m, n)
        # calculate C_m+n_m
        s = factorial(m+n)/(factorial(m)*factorial(n))
        # print(s)
        print (str(int(s)))
    except:
        break




'''
简单  通过率：47.58%  时间限制：1秒  空间限制：32M

知识点     动态规划    基础数学

warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。

描述
请计算n*m的棋盘格子（n为横向的格子数，m为竖向的格子数）从棋盘左上角出发沿着边缘线从左上角走到右下角，总共有多少种走法，要求不能走回头路，即：只能往右和往下走，不能往左和往上走。

注：沿棋盘格之间的边缘线行走

数据范围： 1 <= n,m <= 8


输入描述：
输入两个正整数n和m，用空格隔开。(1≤n,m≤8)

输出描述：
输出一行结果

示例1
输入：
2 2

输出：
6
'''