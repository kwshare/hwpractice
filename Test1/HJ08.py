# HJ8 合并表记录

# n = int(input())
# dic = {}
#
# for i in range(n):
#     line = input().split()
#     key = int(line[0])
#     value = int(line[1])
#     dic[key] = dic.get(key, 0) + value
#
# for i in sorted(dic):
#     print(i, dic[i])


# 简单  通过率：35.03%  时间限制：1秒  空间限制：32M
# 知识点 哈希

# 描述
# 数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出。

# 提示:
# 0 <= index <= 11111111
# 1 <= value <= 100000

# 输入描述：
# 先输入键值对的个数n（1 <= n <= 500）
# 接下来n行每行输入成对的index和value值，以空格隔开

# 输出描述：
# 输出合并后的键值对（多行）

# 示例1
# 输入：
# 4
# 0 1
# 0 2
# 1 2
# 3 4

# 输出：
# 0 3
# 1 2
# 3 4

n = int(input())
d ={}

for i in range(n):
    line = input().split()
    key = int(line[0])
    value = int(line[1])
    d[key] = d.get(key, 0) + value

for i in sorted(d):
    print(i, d[i])
