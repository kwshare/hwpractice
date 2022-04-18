# HJ17 坐标移动


import sys
import re
x,y=0,0
cmd_list = sys.stdin.readline().strip().split(';')
fun={
    'A':lambda a,b,p:(a-p,b),
    'D':lambda a,b,p:(a+p,b),
    'W':lambda a,b,p:(a,b+p),
    'S':lambda a,b,p:(a,b-p)
}
for cmd in cmd_list:
    if re.search(r'^[A|S|W|D]\d\d?$', cmd) and len(cmd)<=3:
        x,y=fun[cmd[0]](x,y,int(cmd[1:]))
print(f'{x},{y}')

# s = input().split(';')
# x = y = 0
# for i in s:
#     if not i: continue
#     try:
#         if i[0] == 'A':
#             x -= int(i[1:])
#         if i[0] == 'D':
#             x += int(i[1:])
#         if i[0] == 'S':
#             y -= int(i[1:])
#         if i[0] == 'W':
#             y += int(i[1:])
#     except:
#         continue
# print('%d,%d' % (x, y))


# import sys
#
#
# def valid(s):
#     check1 = False
#     check2 = True
#     if not s:  # 判断是否为空
#         return check1
#     if s[0] in ["A", "S", "D", "W"]:  # 判断方向信息是否合法
#         check1 = True
#     for i in range(1, len(s)):  # 判断剩余位是否为数字
#         if ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
#             check2 = False
#
#     return check1 and check2
#
#
# for line in sys.stdin:
#     ops = line.split(';')
#
#     x = y = 0
#     for op in ops:
#         if not valid(op):  # 只有在合法情况下才可以对坐标x，y进行操作
#             continue
#         elif op[0] == 'A':
#             x -= int(op[1:])
#         elif op[0] == 'D':
#             x += int(op[1:])
#         elif op[0] == 'W':
#             y += int(op[1:])
#         elif op[0] == 'S':
#             y -= int(op[1:])
#
#     print("%d,%d" % (x, y))  # 输出最终的坐标结果

# 中等  通过率：24.79%  时间限制：1秒  空间限制：32M
# 知识点
# 字符串


# 描述
# 开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

# 输入：
# 合法坐标为A(或者D或者W或者S) + 数字（两位以内）
# 坐标之间以;分隔。
# 非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。
# 下面是一个简单的例子 如：
# A10;S20;W10;D30;X;A1A;B10A11;;A10;

# 处理过程：
# 起点（0,0）
# +   A10   =  （-10,0）
# +   S20   =  (-10,-20)
# +   W10  =  (-10,-10)
# +   D30  =  (20,-10)
# +   x    =  无效
# +   A1A   =  无效
# +   B10A11   =  无效
# +  一个空 不影响
# +   A10  =  (10,-10)
# 结果 （10， -10）

# 数据范围：每组输入的字符串长度满足 1 <=  n  <=  10000，坐标保证满足 -2^{31}  <=  x,y  <=  2^{31}-1 ，且数字部分仅含正数

# 输入描述：
# 一行字符串

# 输出描述：
# 最终坐标，以逗号分隔

# 示例1
# 输入：
# A10;S20;W10;D30;X;A1A;B10A11;;A10;

# 输出：
# 10,-10

# 示例2
# 输入：
# ABC;AKL;DA1;

# 输出：
# 0,0