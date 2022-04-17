# HJ93 数组分组

# 深度优先递归
# 题目要求将数组分为两组，5和3的倍数不能在同一组内，非5或3的倍数随意放在任意一组，要求分配之后两组和相等
# 根据题意将数组中的5和3分别放到两组中，然后递归穷举所有非5或3的倍数的分组情况
def dfs(three, five, other):
    if not other:
        if sum(three) == sum(five):
            return True
        else:
            return False
    if dfs(three+other[:1], five, other[1:]):
        return True
    if dfs(three, five+other[:1], other[1:]):
        return True

while True:
    try:
        n, nums = int(input()), list(map(int, input().split()))
        three, five, other = [], [], []
        for num in nums:
            if num % 3 == 0:
                three.append(num)
            elif num % 5 == 0:
                five.append(num)
            else:
                other.append(num)
        if dfs(three, five, other):
            print ('true')
        else:
            print ('false')
    except:
        break


'''
较难  通过率：31.11%  时间限制：1秒  空间限制：32M
知识点
字符串
递归
warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。
描述
输入int型数组，询问该数组能否分成两组，使得两组中各元素加起来的和相等，并且，所有5的倍数必须在其中一个组中，所有3的倍数在另一个组中（不包括5的倍数），不是5的倍数也不是3的倍数能放在任意一组，可以将数组分为空数组，能满足以上条件，输出true；不满足时输出false。

数据范围：每个数组大小满足 1 \le n \le 50 \1≤n≤50  ，输入的数据大小满足 |val| \le 500 \∣val∣≤500
输入描述：
第一行是数据个数，第二行是输入的数据

输出描述：
返回true或者false

示例1
输入：
4
1 5 -5 1

输出：
true

说明：
第一组：5 -5 1
第二组：1
示例2
输入：
3
3 5 8

输出：
false

说明：
由于3和5不能放在同一组，所以不存在一种分法。
'''