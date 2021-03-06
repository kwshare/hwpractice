# HJ71 字符串通配符



import re
while True:
    try:
        s1 = input().lower()
        s2 = input().lower()
        s1 = s1.replace('.', '\.').replace('?', '[0-9a-z]').replace('*','#')
        s1 = re.sub('#+','[0-9a-z]*',s1)
        if bool(re.fullmatch(s1, s2)):
            print('true')
        else:
            print('false')
    except:
        break







'''
中等  通过率：29.48%  时间限制：1秒  空间限制：32M
知识点
字符串
warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。
描述
问题描述：在计算机中，通配符一种特殊语法，广泛应用于文件搜索、数据库、正则表达式等领域。现要求各位实现字符串通配符的算法。
要求：
实现如下2个通配符：
*：匹配0个或以上的字符（注：能被*和?匹配的字符仅由英文字母和数字0到9组成，下同）
？：匹配1个字符

注意：匹配时不区分大小写。

输入：
通配符表达式；
一组字符串。
输出：

返回不区分大小写的匹配结果，匹配成功输出true，匹配失败输出false
数据范围：字符串长度：1\le s\le 100\1≤s≤100
进阶：时间复杂度：O(n^2)\O(n
2
 ) ，空间复杂度：O(n)\O(n)
输入描述：
先输入一个带有通配符的字符串，再输入一个需要匹配的字符串

输出描述：
返回不区分大小写的匹配结果，匹配成功输出true，匹配失败输出false

示例1
输入：
te?t*.*
txt12.xls
复制
输出：
false
复制
示例2
输入：
z
zz
复制
输出：
false
复制
示例3
输入：
pq
pppq
复制
输出：
false
复制
示例4
输入：
**Z
0QZz
复制
输出：
true
复制
示例5
输入：
?*Bc*?
abcd
复制
输出：
true
复制
示例6
输入：
h*?*a
h#a
复制
输出：
false
复制
说明：
根据题目描述可知能被*和?匹配的字符仅由英文字母和数字0到9组成，所以?不能匹配#，故输出false
示例7
输入：
p*p*qp**pq*p**p***ppq
pppppppqppqqppqppppqqqppqppqpqqqppqpqpppqpppqpqqqpqqp
复制
输出：
false
'''