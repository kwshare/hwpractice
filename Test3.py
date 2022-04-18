# 计算疫情扩散的时间
# https://floating.blog.csdn.net/article/details/116904481


'''
在一个地图中(地图由n*n个区域组成），有部分区域被感染病菌。感染区域每天都会把周围（上下左右）的4个区域感染。
请根据给定的地图计算，多少天以后，全部区域都会被感染。

如果初始地图上所有区域全部都被感染，或者没有被感染区域，返回-1

输入描述:
一行N*N个数字（只包含0,1，不会有其他数字）表示一个地图，数字间用,分割，0表示未感染区域，1表示已经感染区域
每N个数字表示地图中一行，输入数据共表示N行N列的区域地图。
例如输入1,0,1,0,0,0,1,0,1，表示地图
1,0,1
0,0,0
1,0,1
输出描述:
一个整数，表示经过多少天以后，全部区域都被感染
示例1
输入
1,0,1,0,0,0,1,0,1
输出
2
说明
1天以后，地图中仅剩余中心点未被感染；2天以后，全部被感染。

示例2
输入
0,0,0,0
输出
-1
说明
无感染区域

示例3
输入
1,1,1,1,1,1,1,1,1
输出
-1
说明
全部都感染
备注:
1<=N<200

解法：该点是否会被感染，取决于该点的周围的四个点，是否有1 存在。

'''

def st(string):
    string_list = string.split(',')
    length = len(string_list)
    # 判断全为1或者全为0的情况
    if string_list.count('1') == length or string_list.count('0') == length:
        return -1
    slice = int(pow(length, 0.5))   # 开平方
    r = [string_list[i * slice:(i + 1) * slice] for i in range(slice)]
    rr = [string_list[i * slice:(i + 1) * slice] for i in range(slice)]

    def sp(r1, r2):
        for i in range(len(r1)):
            for j in range(len(r1)):
                if r1[i][j] == '1':
                    continue
                if i > 0:
                    if r2[i - 1][j] == '1':
                        r1[i][j] = '1'
                if j > 0:
                    if r2[i][j - 1] == '1':
                        r1[i][j] = '1'
                if 0 < j < len(r1) - 1:
                    if r2[i][j + 1] == '1':
                        r1[i][j] = '1'
                if 0 < i < len(r1) - 1:
                    if r2[i + 1][j] == '1':
                        r1[i][j] = '1'

    days = 0
    while True:
        sp(r, rr)
        days += 1
        if [j for i in r for j in i].count('1') == length:
            return days
        temp = r
        r = rr
        rr = temp


print(st(input()))