# HJ73 计算日期到天数转换




import datetime
while True:
    try:
        date = input().split()  # 将输入从空格分开 转换成列表
        year, month, day = int(date[0]), int(date[1]), int(date[2])
        date = datetime.datetime(year, month, day)
        which_day = date.strftime('%j').lstrip('0')
        print(which_day)
    except:
        break




'''
简单  通过率：42.59%  时间限制：1秒  空间限制：32M
知识点
字符串
思维
warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。
描述
根据输入的日期，计算是这一年的第几天。
保证年份为4位数且日期合法。
进阶：时间复杂度：O(n)\O(n) ，空间复杂度：O(1)\O(1)
输入描述：
输入一行，每行空格分割，分别是年，月，日

输出描述：
输出是这一年的第几天
示例1
输入：
2012 12 31
复制
输出：
366
复制
示例2
输入：
1982 3 4
复制
输出：
63
'''