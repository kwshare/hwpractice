# HJ74 参数解析




while True:
    try:
        str1=str(input())
        str1=str1.replace(' ','\n')
        e = ''
        flag = False
        for i in str1:
            if i == '"':  # 经过一次引号则拨动一次开关
                flag = not flag
            elif flag == True and i == '\n':
                e += ' '
            else:
                e += i
        b = e.count('\n') + 1
        print(b)
        print(e)
    except:
        break





'''
中等  通过率：35.29%  时间限制：1秒  空间限制：32M
知识点
字符串
模拟
warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。
描述
在命令行输入如下命令：

xcopy /s c:\\ d:\\e，

各个参数如下：

参数1：命令字xcopy

参数2：字符串/s

参数3：字符串c:\\

参数4: 字符串d:\\e

请编写一个参数解析程序，实现将命令行各个参数解析出来。


解析规则：

1.参数分隔符为空格
2.对于用""包含起来的参数，如果中间有空格，不能解析为多个参数。比如在命令行输入xcopy /s "C:\\program files" "d:\"时，参数仍然是4个，第3个参数应该是字符串C:\\program files，而不是C:\\program，注意输出参数时，需要将""去掉，引号不存在嵌套情况。
3.参数不定长

4.输入由用例保证，不会出现不符合要求的输入
数据范围：字符串长度：1\le s\le 1000\1≤s≤1000
进阶：时间复杂度：O(n)\O(n) ，空间复杂度：O(n)\O(n)
输入描述：
输入一行字符串，可以有空格

输出描述：
输出参数个数，分解后的参数，每个参数都独占一行

示例1
输入：
xcopy /s c:\\ d:\\e
复制
输出：
4
xcopy
/s
c:\\
d:\\e
'''