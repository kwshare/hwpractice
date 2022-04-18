# HJ18 识别有效的IP地址和掩码并进行分类统计

ipClass2num = {
    'A':0,
    'B':0,
    'C':0,
    'D':0,
    'E':0,
    'ERROR':0,
    'PRIVATE':0,
}
# 私有IP地址和A,B,C,D,E类地址是不冲突的，也就是说需要同时+1
def check_ip(ip:str):
    ip_bit = ip.split('.')
    if len(ip_bit) != 4 or '' in ip_bit:  #ip 的长度为4 且每一位不为空
        return False
    for i in ip_bit:
        if int(i)<0 or int(i) >255:   #检查Ip每一个10位的值范围为0~255
            return False
    return True
def check_mask(mask:str):
    if not check_ip(mask):
        return False
    if mask == '255.255.255.255' or mask == '0.0.0.0':
        return False
    mask_list = mask.split('.')
    if len(mask_list) != 4:
        return False
    mask_bit = []
    for i in mask_list:#小数点隔开的每一数字段
        i = bin(int(i))#每一数字段转换为每一段的二进制数字段
        i = i[2:] #从每一段的二进制数字段的第三个数开始，因为前面有两个ob
        mask_bit.append(i.zfill(8)) #.zfill:返回指定长度的字符串，原字符串右对齐，前面填充0
    whole_mask = ''.join(mask_bit)
#     print(whole_mask)
    whole0_find = whole_mask.find("0")#查0从哪里开始
    whole1_rfind = whole_mask.rfind("1")#查1在哪里结束
    if whole1_rfind+1 == whole0_find:#两者位置差1位为正确
        return True
    else:
        return False
def check_private_ip(ip:str):
    # 三类私网
    ip_list = ip.split('.')
    if ip_list[0] == '10': return True
    if ip_list[0] == '172' and 16<=int(ip_list[1])<=31: return True
    if ip_list[0] == '192' and ip_list[1] == '168': return True
    return False
while True:
    try:
        s = input()
        ip = s.split('~')[0]
        mask = s.split('~')[1]
        if check_ip(ip):
            first = int(ip.split('.')[0])
            if first==127 or first==0:
                # 若不这样写，当类似于【0.*.*.*】和【127.*.*.*】的IP地址的子网掩码错误时，会额外计数
                continue
            if check_mask(mask):
                if check_private_ip(ip):
                    ipClass2num['PRIVATE'] += 1
                if 0<first<127:
                    ipClass2num['A'] += 1
                elif 127<first<=191:
                    ipClass2num['B'] += 1
                elif 192<=first<=223:
                    ipClass2num['C'] += 1
                elif 224<=first<=239:
                    ipClass2num['D'] += 1
                elif 240<=first<=255:
                    ipClass2num['E'] += 1
            else:
                ipClass2num['ERROR'] += 1
        else:
            ipClass2num['ERROR'] += 1
    except:
        break
for v in ipClass2num.values():
    print(v,end=(' '))






# import sys
#
# res = [0, 0, 0, 0, 0, 0, 0]
#
#
# def puip(ip):
#     if 1 <= ip[0] <= 126:  # A类地址判断条件
#         res[0] += 1
#     elif 128 <= ip[0] <= 191:  # B类地址判断条件
#         res[1] += 1
#     elif 192 <= ip[0] <= 223:  # C类地址判断条件
#         res[2] += 1
#     elif 224 <= ip[0] <= 239:  # D类地址判断条件
#         res[3] += 1
#     elif 240 <= ip[0] <= 255:  # E类地址判断条件
#         res[4] += 1
#     return
#
#
# def prip(ip):  # 私有IP地址判断条件
#     if (ip[0] == 10) or (ip[0] == 172 and 16 <= ip[1] <= 32) or (ip[0] == 192 and ip[1] == 168):
#         res[6] += 1
#     return
#
#
# def ym(msk):  # 判断掩码合法性
#     val = (msk[0] << 24) + (msk[1] << 16) + (msk[2] << 8) + msk[3]  # 转换成32位
#     if val == 0:  # 排除全0的情况
#         return False
#     if (val + 1) == (1 << 32):  # 排除全1的情况
#         return False
#     flag = 0
#     while (val):
#         digit = val & 1  # 逐位判断
#         if digit == 1:
#             flag = 1
#         if flag == 1 and digit == 0:  # flag=1表示已经不允许再出现0
#             return False
#         val >>= 1
#     return True
#
#
# def judge(line):
#     ip, msk = line.strip().split('~')
#     ips = [int(x) for x in filter(None, ip.split('.'))]  # 获得表示IP的列表，理论上应该包含四个元素
#     msks = [int(x) for x in filter(None, msk.split('.'))]  # 获得表示掩码的列表，理论上应该包含四个元素
#     if ips[0] == 0 or ips[0] == 127:  # 排除非法IP不计数
#         return
#     if len(ips) < 4 or len(msks) < 4:  # 判断错误掩码或错误IP
#         res[5] += 1
#         return
#     if ym(msks) == True:  # 通过掩码判断的可以进行IP判断
#         puip(ips)
#         prip(ips)
#     else:
#         res[5] += 1
#     return
#
#
# for line in sys.stdin:
#     judge(line)
# # judge("192.168.0.2~255.255.255.0")
#
# res = [str(x) for x in res]
# print(" ".join(res))




# 较难  通过率：20.37%  时间限制：1秒  空间限制：32M
# 知识点 字符串 查找


# 描述
# 请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。

# 所有的IP地址划分为 A,B,C,D,E五类
# A类地址从1.0.0.0到126.255.255.255;
# B类地址从128.0.0.0到191.255.255.255;
# C类地址从192.0.0.0到223.255.255.255;
# D类地址从224.0.0.0到239.255.255.255；
# E类地址从240.0.0.0到255.255.255.255

# 私网IP范围是：
# 从10.0.0.0到10.255.255.255
# 从172.16.0.0到172.31.255.255
# 从192.168.0.0到192.168.255.255


# 子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
# （注意二进制下全是1或者全是0均为非法子网掩码）

# 注意：
# 1. 类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时请忽略
# 2. 私有IP地址和A,B,C,D,E类地址是不冲突的

# 输入描述：
# 多行字符串。每行一个IP地址和掩码，用~隔开。
# 请参考帖子https://www.nowcoder.com/discuss/276处理循环输入的问题。

# 输出描述：
# 统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。

# 示例1
# 输入：
# 10.70.44.68~255.254.255.0
# 1.0.0.1~255.0.0.0
# 192.168.0.2~255.255.255.0
# 19..0.~255.255.255.0

# 输出：
# 1 0 1 0 0 2 1

# 说明：
# 10.70.44.68~255.254.255.0的子网掩码非法，19..0.~255.255.255.0的IP地址非法，所以错误IP地址或错误掩码的计数为2；
# 1.0.0.1~255.0.0.0是无误的A类地址；
# 192.168.0.2~255.255.255.0是无误的C类地址且是私有IP；
# 所以最终的结果为1 0 1 0 0 2 1


# 示例2
# 输入：
# 0.201.56.50~255.255.111.255
# 127.201.56.50~255.255.111.255

# 输出：
# 0 0 0 0 0 0 0

# 说明：
# 类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时请忽略