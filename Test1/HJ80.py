# HJ80 整型数组合并


while True:
    try:
        first_num = int(input())
        first_list = list(map(int, input().split(" ")))
        second_num = int(input())
        second_list = list(map(int, input().split(" ")))

        total_list = first_list + second_list
        total_list = list(set(total_list))
        total_list.sort()
        res = ''.join(list(map(str, total_list)))
        print(res)
    except EOFError:
        break

'''
简单  通过率：34.34%  时间限制：1秒  空间限制：32M
知识点 排序  数组  哈希

warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。

描述
题目标题：
将两个整型数组按照升序合并，并且过滤掉重复数组元素。
输出时相邻两数之间没有空格。



输入描述：
输入说明，按下列顺序输入：
1 输入第一个数组的个数
2 输入第一个数组的数值
3 输入第二个数组的个数
4 输入第二个数组的数值

输出描述：
输出合并之后的数组

示例1
输入：
3
1 2 5
4
-1 0 3 2

输出：
-101235
'''