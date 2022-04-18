# HJ30 字符串合并处理





import re

# 构造函数加密字符，如果是[0-9A-Fa-f]则按规则返回加密值，否则返回原始值
def encrypt(x):
    if re.search(r'[0-9A-Fa-f]', x):
        return hex(int(bin(int(x, 16))[2:].rjust(4, '0')[::-1], 2))[2:].upper()
        """
        1. int(x, 16) - 将字符x转成16进制
        2. bin(int(x, 16))[2:].rjust(4,'0')[::-1] - 继续将十六进制转成二进制，并去除二进制开头"0b"，如果二进制长度小于4，则在前面补0至四位,然后再倒序。
        比如bin(int('7', 16))输出0b111,[2:]去除0b后为111，rjust(4,'0')左侧补0则变为0111，[::-1]倒序后变为二进制的1110
        3. hex(int(i,2)[2:].upper() - 其中i表示注释2的内容。这一步是将上一步获取的二进制转成十六进制，并去除开头的"0x",最后再将其转成大写。
        """
    else:
        return x

while True:
    try:
        a = list(input().replace(" ", "")) # 去除输入中的空格，并将输入的字符处理成列表
        a[::2] = sorted(a[::2])  # 奇数位置从小到大排序
        a[1::2] = sorted(a[1::2])  # 偶数位置从小到大排序
        res = ""
        for i in a:
            res += encrypt(i) # 调用加密函数，遍历输出结果
        print(res)
    except:
        break






'''
较难  通过率：26.52%  时间限制：1秒  空间限制：32M
知识点
字符串
排序
warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。
描述
按照指定规则对输入的字符串进行处理。

详细描述：

第一步：将输入的两个字符串str1和str2进行前后合并。如给定字符串 "dec" 和字符串 "fab" ， 合并后生成的字符串为 "decfab"

第二步：对合并后的字符串进行排序，要求为：下标为奇数的字符和下标为偶数的字符分别从小到大排序。这里的下标的意思是字符在字符串中的位置。注意排序后在新串中仍需要保持原来的奇偶性。例如刚刚得到的字符串“decfab”，分别对下标为偶数的字符'd'、'c'、'a'和下标为奇数的字符'e'、'f'、'b'进行排序（生成 'a'、'c'、'd' 和 'b' 、'e' 、'f'），再依次分别放回原串中的偶数位和奇数位，新字符串变为“abcedf”

第三步：对排序后的字符串中的'0'~'9'、'A'~'F'和'a'~'f'字符，需要进行转换操作。
转换规则如下：
对以上需要进行转换的字符所代表的十六进制用二进制表示并倒序，然后再转换成对应的十六进制大写字符（注：字符 a~f 的十六进制对应十进制的10~15，大写同理）。
如字符 '4'，其二进制为 0100 ，则翻转后为 0010 ，也就是 2 。转换后的字符为 '2'。
如字符 ‘7’，其二进制为 0111 ，则翻转后为 1110 ，对应的十进制是14，转换为十六进制的大写字母为 'E'。
如字符 'C'，代表的十进制是 12 ，其二进制为 1100 ，则翻转后为 0011，也就是3。转换后的字符是 '3'。
根据这个转换规则，由第二步生成的字符串 “abcedf” 转换后会生成字符串 "5D37BF"。


数据范围：输入的字符串长度满足 1 \le n \le 100 \1≤n≤100

输入描述：
样例输入两个字符串，用空格隔开。

输出描述：
输出转化后的结果。

示例1
输入：
dec fab
复制
输出：
5D37BF
复制
示例2
输入：
ab CD
复制
输出：
3B5D
复制
说明：
合并后为abCD，按奇数位和偶数位排序后是CDab（请注意要按ascii码进行排序，所以C在a前面，D在b前面），转换后为3B5D
示例3
输入：
123 15
复制
输出：
88C4A
'''