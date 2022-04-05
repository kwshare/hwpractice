# HJ54 表达式求值


while True:
    try:
        print(int(eval(input())))
    except:
        break




'''
简单  通过率：56.15%  时间限制：1秒  空间限制：32M
知识点
字符串
基础数学
栈
warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。
描述
给定一个字符串描述的算术表达式，计算出结果值。

输入字符串长度不超过 100 ，合法的字符包括 ”+, -, *, /, (, )” ， ”0-9” 。

数据范围：运算过程中和最终结果均满足 |val| \le 2^{31}-1 \∣val∣≤2
31
 −1  ，即只进行整型运算，确保输入的表达式合法
输入描述：
输入算术表达式

输出描述：
计算出结果值

示例1
输入：
400+5

输出：
405
'''