# HJ2 计算某字符出现次数

"""
string_1 = input()
string_1 = string_1.upper()
list_1 = list(string_1)
check = input()
check = check.upper()
num = 0
for word in list_1:
    if word == check:
        num = num + 1

print(num)


简单  通过率：30.44%  时间限制：1秒  空间限制：32M
知识点 字符串 哈希

描述
写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，然后输出输入字符串中该字符的出现次数。（不区分大小写字母）
数据范围： 1 <= n <= 1000
输入描述：
第一行输入一个由字母和数字以及空格组成的字符串，第二行输入一个字符。
输出描述：
输出输入字符串中含有该字符的个数。（不区分大小写字母）

示例1
输入：
ABCabc
A

输出：
2
"""


while True:
    try:
        input_str = input()
        input_cha = input()
        upper_str = input_str.upper()
        upper_cha = input_cha.upper()
        char_count = 0
        for i in upper_str:
            if i == upper_cha:
                char_count += 1
        print(char_count)
    except:
        break