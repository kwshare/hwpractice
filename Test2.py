# 火星符号计算
# https://blog.csdn.net/m0_60741207/article/details/121528948
'''
已知火星人使用的运算符号为#;$ 其与地球人的等价公式如下
x#y=2*x+3*y+4
x$y=3*x+y+2
x y是无符号整数 地球人公式按照c语言规则进行计算 火星人公式中$符优先级高于#相同的运算符按从左到右的顺序运算

输入描述： 火星人字符串表达式结尾不带回车换行 输入的字符串说明是 字符串为仅有无符号整数和操作符组成的计算表达式
1.用例保证字符串中操作数与操作符之间没有任何分隔符
2.用例保证操作数取值范围为32位无符号整数，
3.保证输入以及计算结果不会出现整型溢出
4.保证输入的字符串为合法的求值报文 例如: 123#4$5#76$78
5.保证不会出现非法的求值报文 例如: #4$5 这种缺少操作数 4$5# 这种缺少操作数 4#$5 这种缺少操作数 4 $5 有空格 3+4-5*6/7 有其他操作符 12345678987654321$54321 32位整数溢出

输出描述： 根据火星人字符串输出计算结果 结尾不带回车换行

案例1： 输入： 7#6$5#12 输出： 226 说明
示例7#6$5#12=7#(3*6+5+2)#12 =7#25#12 =(2*7+3*25+4)#12 =93#12 =2*93+3*12+4 =226
'''

# 定义x#y
def s(x, y):
    return 2 * x + 3 * y + 4

# 定义x$y
def d(x, y):
    return 3 * x + y + 2

# 查找x
def fx(m, index):
    for i in range(index - 1, 0, -1):
        if m[i] == "#" or m[i] == "$":
            return int(m[i + 1:index]), i + 1
    return int(m[:index]), 0

# 查找y
def fy(m, index):
    for i in range(index + 1, len(m)):
        if m[i] == "#" or m[i] == "$":
            return int(m[index + 1:i]), i - 1
    return int(m[index + 1:]), len(m)


r = input()

for i in r:
    if i == "$":
        x, x_index = fx(r, r.index(i))
        y, y_index = fy(r, r.index(i))
        r = r[:x_index] + str(d(x, y)) + r[y_index + 1:]

for i in r:
    if i == "#":
        x, x_index = fx(r, r.index(i))
        y, y_index = fy(r, r.index(i))
        r = r[:x_index] + str(s(x, y)) + r[y_index + 1:]

print(int(r))