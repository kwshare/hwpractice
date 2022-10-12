# HJ1 字符串最后一个单词的长度


"""
str1 = input()
arr1 = str1.split(" ")
arr1 = str1.split()
n = len(arr1) - 1
print(len(arr1[n]))

简单  通过率：32.50%  时间限制：1秒  空间限制：32M
知识点   字符串

描述:
计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。（注：字符串末尾不以空格为结尾）

输入描述：
输入一行，代表要计算的字符串，非空，长度小于5000。

输出描述：
输出一个整数，表示输入字符串最后一个单词的长度

示例1
输入：
hello nowcoder

输出：
8

说明：
最后一个单词为nowcoder，长度为8
"""

while True:
    try:
        input_str = input().split()
        str_length = len(input_str)
        last_str = len(input_str[str_length - 1])
        print(last_str)
    except:
        break
