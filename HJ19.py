# HJ19 简单错误记录

# l = []
# ll = []
# while 1:
#     try:
#         s = input().split('\\')[-1]
#         data = s.split(' ')[0][-16:] + ' ' + s.split(' ')[1]
#         if data not in l:
#             l.append(data)
#             ll.append(1)
#         else:
#             ll[l.index(data)] += 1
#     except:
#         break
#
# for i in range(len(l[-8:])):
#     print(l[-8:][i], ll[-8:][i])





# import sys
# error_map = {}
# error_list = []
# for i in sys.stdin:
#     path, line_no = i.strip().split(' ')
#     filename = path.split('\\')[-1]
#     if len(filename) > 16:
#         filename = filename[-16:]
#     error_key = filename + ' ' + line_no
#     if error_key in error_map.keys():
#         error_map[error_key] = error_map[error_key] + 1
#     else:
#         error_list.append(error_key)
#         error_map[error_key] = 1
# for error_key in error_list[-8:]:
#     print(error_key, error_map.get(error_key))
#


lst=[]#用于数组记录
lst1=[]#最后上数字的数组
#先把[File,N]以一个单元的形式都加进lst，不考虑冲不冲股份， 把他看成一个整体，后面有count函数帮我们计算个数
while True:
    try:
        PATH,N=map(str,input().split(" "))
        File=PATH.split("\\")[-1]#必须用两个\测试出来的
        if len(File)>16:#解决大于16位，就取后16位的情况。
            File=File[-16:]
        lst.append([File,N])
    except:
        break
#print(lst)
#去除重复，帮助我们用作索引，这种方法还有个好处，那就是由于lst是顺序进入的，所以索引也是顺序的
lsttemp=[]
for [i,j] in lst:
    if [i,j] in lsttemp:
        continue
    else:
        lsttemp.append([i,j])

#通过索引再把对应数字加上，count函数就是该题的关键，也是不先做处理直接添加进lst的原因
for i,j in lsttemp:
    lst1.append([i,j,lst.count([i,j])])#加上对应数字

for [i,j,t] in lst1[-8:]:#输出倒数8个
    print(" ".join([i,j,str(t)]))#最后用join函数输出
# print(lst1)




# 较难  通过率：20.88%  时间限制：1秒  空间限制：32M
# 知识点   字符串   哈希

# 描述
# 开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。


# 处理：
# 1、 记录最多8条错误记录，循环记录，最后只用输出最后出现的八条错误记录。对相同的错误记录只记录一条，但是错误计数增加。最后一个斜杠后面的带后缀名的部分（保留最后16位）和行号完全匹配的记录才做算是“相同”的错误记录。
# 2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；
# 3、 输入的文件可能带路径，记录文件名称不能带路径。也就是说，哪怕不同路径下的文件，如果它们的名字的后16个字符相同，也被视为相同的错误记录
# 4、循环记录时，只以第一次出现的顺序为准，后面重复的不会更新它的出现时间，仍以第一次为准

# 数据范围：错误记录数量满足 1 \le n \le 100 \1≤n≤100  ，每条记录长度满足 1 <= len <= 100
# 输入描述：
# 每组只包含一个测试用例。一个测试用例包含一行或多行字符串。每行包括带路径文件名称，行号，以空格隔开。

# 输出描述：
# 将所有的记录统计并将结果输出，格式：文件名 代码行数 数目，一个空格隔开，如：

# 示例1
# 输入：
# D:\zwtymj\xccb\ljj\cqzlyaszjvlsjmkwoqijggmybr 645
# E:\je\rzuwnjvnuz 633
# C:\km\tgjwpb\gy\atl 637
# F:\weioj\hadd\connsh\rwyfvzsopsuiqjnr 647
# E:\ns\mfwj\wqkoki\eez 648
# D:\cfmwafhhgeyawnool 649
# E:\czt\opwip\osnll\c 637
# G:\nt\f 633
# F:\fop\ywzqaop 631
# F:\yay\jc\ywzqaop 631
# D:\zwtymj\xccb\ljj\cqzlyaszjvlsjmkwoqijggmybr 645

# 输出：
# rzuwnjvnuz 633 1
# atl 637 1
# rwyfvzsopsuiqjnr 647 1
# eez 648 1
# fmwafhhgeyawnool 649 1
# c 637 1
# f 633 1
# ywzqaop 631 2

# 说明：
# 由于D:\cfmwafhhgeyawnool 649的文件名长度超过了16个字符，达到了17，所以第一个字符'c'应该被忽略。
# 记录F:\fop\ywzqaop 631和F:\yay\jc\ywzqaop 631由于文件名和行号相同，因此被视为同一个错误记录，哪怕它们的路径是不同的。
# 由于循环记录时，只以第一次出现的顺序为准，后面重复的不会更新它的出现时间，仍以第一次为准，所以D:\zwtymj\xccb\ljj\cqzlyaszjvlsjmkwoqijggmybr 645不会被记录。