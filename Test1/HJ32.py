# HJ32 密码截取


str = input()
n = len(str)
list = []
for i in range(0,n-1):
    for j in range(1,n):
        if str[j] == str[i] and str[i+1:j] == str[j-1:i:-1]:
            list.append(len(str[i:j+1]))
print(max(list))





'''
中等  通过率：29.56%  时间限制：1秒  空间限制：32M
知识点
字符串
动态规划
warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。
描述
Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？

数据范围：字符串长度满足 1 \le n \le 2500 \1≤n≤2500
输入描述：
输入一个字符串（字符串的长度不超过2500）

输出描述：
返回有效密码串的最大长度

示例1
输入：
ABBA
复制
输出：
4

示例2
输入：
ABBBA

输出：
5

示例3
输入：
12HHHHA

输出：
4
'''