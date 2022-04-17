# HJ107 求解立方根

import sys

def cube():
    num = float(sys.stdin.readline().strip())
    if num == 0:
        return 0
    if num > 0:
        sig = 1
    else:
        sig = -1
    num = abs(num)

    if num > 1:
        start = 0
        end = num
    else:
        start = num
        end = 1
    mid = (end + start) / 2
    while abs(mid ** 3 - num) > 0.001:
        if mid ** 3 > num:
            end = mid
        else:
            start = mid
        mid = (end + start) / 2
    print(round(sig * mid, 1))

cube()


# 中等  通过率：28.46%  时间限制：1秒  空间限制：32M
# 知识点 基础数学 二分

# warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。

# 描述
# 计算一个浮点数的立方根，不使用库函数。
# 保留一位小数。

# 数据范围：|val| <= 20

# 输入描述：
# 待求解参数，为double类型（一个实数）

# 输出描述：
# 输出参数的立方根。保留一位小数。

# 示例1
# 输入：
# 216

# 输出：
# 6.0

# 示例2
# 输入：
# 2.7

# 输出：
# 1.4