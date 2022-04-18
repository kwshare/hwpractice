# HJ67 24点游戏算法


def helper(arr,item):#先写一个利用递归+枚举解决算24的程序
    if item<1:
        return False
    if  len(arr)==1:#递归终点，当数组arr只剩一个数的时候，判断是否等于item
        return arr[0]==item
    else:#如果arr不是只剩一个数，就调用函数本身（直到只剩一个为止返回真假）
        for i in range(len(arr)):
            m=arr[0:i]+arr[i+1:]
            n=arr[i]
            if helper(m,item+n) or helper(m, item-n) or helper(m, item*n) or helper(m, item/n):
                return True
        return False

while True:
    try:
        if helper(list(map(int,input().split())), 24):
            print('true')
        else:
            print('false')
    except:
        break







'''
中等  通过率：36.95%  时间限制：1秒  空间限制：32M
知识点
dfs
搜索
warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。
描述
给出4个1-10的数字，通过加减乘除运算，得到数字为24就算胜利,除法指实数除法运算,运算符仅允许出现在两个数字之间,本题对数字选取顺序无要求，但每个数字仅允许使用一次，且需考虑括号运算
此题允许数字重复，如3 3 4 4为合法输入，此输入一共有两个3，但是每个数字只允许使用一次，则运算过程中两个3都被选取并进行对应的计算操作。
输入描述：
读入4个[1,10]的整数，数字允许重复，测试用例保证无异常数字。

输出描述：
对于每组案例，输出一行表示能否得到24点，能输出true，不能输出false

示例1
输入：
7 2 1 10
复制
输出：
true
'''