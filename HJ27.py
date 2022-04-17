# HJ27 查找兄弟单词




while True:
    try:
        #读取输入数据，并且转换为列表
        data1 = input().split()
        #获取单词的个数
        n1 = data1[0]
        #按字典排序的第几个兄弟词
        n2 = data1[-1]
        #获取输入的n个单词
        data2 = data1[1:-2]
        #获取兄弟词
        data3 = data1[-2]

        #用于存储兄弟词的数量
        n3 = 0
        #用于存储兄弟词
        data4 = []

        for word in data2:
            if word == data3:
                continue
            elif sorted(word) == sorted(data3):
                n3 = n3 + 1
                data4.append(word)
        print(n3)
        #将兄弟词按照字典排序
        data5 = sorted(data4)
        print(data5[int(n2)-1])
    except:
        break




'''
中等  通过率：21.17%  时间限制：1秒  空间限制：32M
知识点
查找
warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。
描述
定义一个单词的“兄弟单词”为：交换该单词字母顺序（注：可以交换任意次），而不添加、删除、修改原有的字母就能生成的单词。
兄弟单词要求和原来的单词不同。例如： ab 和 ba 是兄弟单词。 ab 和 ab 则不是兄弟单词。
现在给定你 n 个单词，另外再给你一个单词 x ，让你寻找 x 的兄弟单词里，按字典序排列后的第 k 个单词是什么？
注意：字典中可能有重复单词。

数据范围：1 \le n \le 1000 \1≤n≤1000 ，输入的字符串长度满足 1 \le len(str) \le 10 \1≤len(str)≤10  ， 1 \le k < n \1≤k<n
输入描述：
输入只有一行。 先输入字典中单词的个数n，再输入n个单词作为字典单词。 然后输入一个单词x 最后后输入一个整数k
输出描述：
第一行输出查找到x的兄弟单词的个数m 第二行输出查找到的按照字典顺序排序后的第k个兄弟单词，没有符合第k个的话则不用输出。
示例1
输入：
3 abc bca cab abc 1
复制
输出：
2
bca
复制
示例2
输入：
6 cab ad abcd cba abc bca abc 1
复制
输出：
3
bca
复制
说明：
abc的兄弟单词有cab cba bca，所以输出3
经字典序排列后，变为bca cab cba，所以第1个字典序兄弟单词为bca
'''