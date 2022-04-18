# HJ16 购物单

# n, m = map(int,input().split())
# primary, annex = {}, {}
# for i in range(1,m+1):
#     x, y, z = map(int, input().split())
#     if z==0:#主件
#         primary[i] = [x, y]
#     else:#附件
#         if z in annex:#第二个附件
#             annex[z].append([x, y])
#         else:#第一个附件
#             annex[z] = [[x,y]]
# m = len(primary)#主件个数转化为物品个数
# dp = [[0]*(n+1) for _ in range(m+1)]
# w, v= [[]], [[]]
# for key in primary:
#     w_temp, v_temp = [], []
#     w_temp.append(primary[key][0])#1、主件
#     v_temp.append(primary[key][0]*primary[key][1])
#     if key in annex:#存在主件
#         w_temp.append(w_temp[0]+annex[key][0][0])#2、主件+附件1
#         v_temp.append(v_temp[0]+annex[key][0][0]*annex[key][0][1])
#         if len(annex[key])>1:#存在两主件
#             w_temp.append(w_temp[0]+annex[key][1][0])#3、主件+附件2
#             v_temp.append(v_temp[0]+annex[key][1][0]*annex[key][1][1])
#             w_temp.append(w_temp[0]+annex[key][0][0]+annex[key][1][0])#3、主件+附件1+附件2
#             v_temp.append(v_temp[0]+annex[key][0][0]*annex[key][0][1]+annex[key][1][0]*annex[key][1][1])
#     w.append(w_temp)
#     v.append(v_temp)
# for i in range(1,m+1):
#     for j in range(10,n+1,10):#物品的价格是10的整数倍
#         max_i = dp[i-1][j]
#         for k in range(len(w[i])):
#             if j-w[i][k]>=0:
#                 max_i = max(max_i, dp[i-1][j-w[i][k]]+v[i][k])
#         dp[i][j] = max_i
# print(dp[m][n])




# while True:
#     try:
#         # 金额限制总价，物品数量
#         total,k = list(map(int,input().split(" ")))
#         ## 单价
#         W = {}
#         ## 单价* 重要程度=价值
#         V = {}
#         # 因为价格是10的倍数，为方便运算，价格/10
#         total = int(total/10)
#         # 主件个数
#         main_key = []
#         # 构造字典
#         for i in range(1,k+1):
#             W[i]=[0,0,0]
#             V[i]=[0,0,0]
#         for i in range(k):
#             # 单价，重要程度，类别
#             v,p,q = list(map(int,input().split(" ")))
#             if q == 0:
#                 W[i+1][0] = int(v/10)
#                 V[i+1][0] = int(v*p/10)
#                 main_key.append(i+1)
#             else:
#                 if W[q][1]==0:
#                     W[q][1] = int(v/10)
#                     V[q][1] = int(v*p/10)
#                 else:
#                     W[q][2] = int(v/10)
#                     V[q][2] = int(v*p/10)
#         W_lst = []
#         V_lst = []
#         for key in W.keys():
#             if key in main_key:
#                 W_lst.append(W[key])
#                 V_lst.append(V[key])
#         m = len(W_lst)
#         # 构造二维数
#         dp = [[0]*(total+1) for _ in range(m+1)]
#         for i in range(1,m+1):
#             w1 = W_lst[i-1][0]
#             w2 = W_lst[i-1][1]
#             w3 = W_lst[i-1][2]
#             v1 = V_lst[i-1][0]
#             v2 = V_lst[i-1][1]
#             v3 = V_lst[i-1][2]
#             for j in range(total+1):
#                 # 1. 不放入:
#                 dp[i][j] =dp[i-1][j]
#                 # 2. 放入一个主件
#                 if j-w1>=0:
#                     dp[i][j] = max(dp[i][j],dp[i-1][j-w1]+v1)
#                 # 3. 1个主件+附件1
#                 if j-w1-w2>=0:
#                     dp[i][j] = max(dp[i][j], dp[i-1][j-w2-w1]+v1+v2)
#                 # 4. 一个主件+附件2
#                 if j-w1-w3>=0:
#                     dp[i][j] =  max(dp[i][j], dp[i-1][j-w3-w1]+v1+v3)
#                 # 5. 一个主见+附件1+附件2
#                 if j-w1-w2-w3 >=0:
#                     dp[i][j] =  max(dp[i][j], dp[i-1][j-w3-w2-w1]+v1+v2+v3)
#         print(int(dp[m][total]*10))
#     except:
#         break



# 在不超过 N 元（可以等于 N 元）的前提下，使物品的价格与重要度的乘积的总和最大
# 0-1背包问题变种，买归类为附件的物品，必须先买该附件所属的主件
# 也就是说，主件的个数才是总的物品的个数
# 考虑每个物品时要考虑每种可能出现的情况：
#     1、主件，2、主件+附件1，3、主件+附件2，4、主件+附件1+附件2
# 求解各种情况下的子问题,自底向上求解即可

line = str(input())
N = int(line.split(' ')[0])  # 总金额
m = int(line.split(' ')[1])  # 希望购买的个数
id2info = {}
other2info = {}
for i in range(m):
    line = str(input())
    id = i+1
    v = int(line.split(' ')[0])  # 价格（10的倍数）
    p = int(line.split(' ')[1])  # 重要度
    q = int(line.split(' ')[2])  # 主0附id件
    if q == 0:
        # 主键
        id2info[id] = [v,p]
    else:
        # q是主键id
        if q in other2info:
            # 第二个附件
            other2info[q].append([v,p])
        else:
            # 第一个附件
            other2info[q] = [[v,p]]

# 子问题：求dp（i，j），即最大价格为j*10，可选主件为x1,...xi（前i个）时的最大价值
i_num = len(id2info)
j_num = N // 10
w, v= [[]], [[]]  # 这里预留了一个空list
# print(other2info)
# 记录四种情况下的价格与价值
for key in id2info:
    w_temp, v_temp = [], []
    #1、主件
    w_temp.append(id2info[key][0])
    v_temp.append(id2info[key][0]*id2info[key][1])
    #存在附件
    if key in other2info:
        #2、主件+附件1
        w_temp.append(w_temp[0]+other2info[key][0][0])
        v_temp.append(v_temp[0]+other2info[key][0][0]*other2info[key][0][1])
        #存在两主件
        if len(other2info[key])>1:
            #3、主件+附件2
            w_temp.append(w_temp[0]+other2info[key][1][0])
            v_temp.append(v_temp[0]+other2info[key][1][0]*other2info[key][1][1])
            w_temp.append(w_temp[0]+other2info[key][0][0]+other2info[key][1][0])
            #4、主件+附件1+附件2
            v_temp.append(v_temp[0]+other2info[key][0][0]*other2info[key][0][1]+other2info[key][1][0]*other2info[key][1][1])
    w.append(w_temp)
    v.append(v_temp)
# dp = [[0]*(j_num+1)]*(i_num+1)  # 会引发浅拷贝的问题，i_num+1个列表的内存会指向同一块
# 因此无论修改哪个[0]*(j_num+1)]，其余的i_num个也会跟着改变
dp = [[0]*(j_num+1) for _ in range(i_num+1)]
# dp[i][j] = max(物品不放入背包，主件，主件+附件1，主件+附件2，主件+附件1+附件2)
for i in range(1, i_num+1):
    for j in range(1, j_num+1):
        pre_max = dp[i-1][j]
        for x in range(len(w[i])):
            if j*10 - w[i][x] >= 0:
                pre_max = max(pre_max, dp[i-1][(j*10 - w[i][x])//10]+v[i][x])
        dp[i][j] = pre_max
print(dp[i_num][j_num])



# from collections import defaultdict
#
# # 处理输入
# n, m = map(int, input().split())
# n //= 10  # 价格总为 10 的倍数，优化空间复杂度
# prices = defaultdict(lambda: [0, 0, 0])  # 主从物品的价格
# values = defaultdict(lambda: [0, 0, 0])  # 主从物品的价值
#
# for i in range(m):      # i 代表第 i + 1 个物品
#     v, p, q = map(int, input().split())
#     v //= 10            # 价格总为 10 的倍数，优化空间复杂度
#     if q == 0:          # 追加主物品
#         prices[i + 1][0] = v
#         values[i + 1][0] = v * p
#     elif prices[q][1]:  # 追加从物品
#         prices[q][2] = v
#         values[q][2] = v * p
#     else:
#         prices[q][1] = v
#         values[q][1] = v * p
#
# # 处理输出
# dp = [0] * (n + 1)  # 初始化 dp 数组
#
# for i, v in prices.items():
#     for j in range(n, v[0] - 1, -1):
#         p1, p2, p3 = v
#         v1, v2, v3 = values[i]
#         # 处理主从组合的四种情况
#         dp[j] = max(dp[j], dp[j - p1] + v1)
#         dp[j] = max(dp[j], dp[j - p1 - p2] + v1 + v2) if j >= p1 + p2 else dp[j]
#         dp[j] = max(dp[j], dp[j - p1 - p3] + v1 + v3) if j >= p1 + p3 else dp[j]
#         dp[j] = max(dp[j], dp[j - p1 - p2 - p3] + v1 + v2 + v3) if j >= p1 + p2 + p3 else dp[j]
#
# print(dp[n] * 10)



# 中等 通过率：21.21 % 时间限制：1秒空间限制：32M
# 知识点
# 动态规划

# 描述
# 王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的，下表就是一些主件与附件的例子：

# 主件    附件
# 电脑    打印机，扫描仪
# 书柜    图书
# 书桌    台灯，文具
# 工作椅   无

# 如果要买归类为附件的物品，必须先买该附件所属的主件，且每件物品只能购买一次。
# 每个主件可以有0个、 1个或2个附件。附件不再有从属于自己的附件。
# 王强查到了每件物品的价格（都是10元的整数倍），而他只有N元的预算。除此之外，他给每件物品规定了一个重要度，用整数1 ~ 5表示。他希望在花费不超过N元的前提下，使自己的满意度达到最大。
# 满意度是指所购买的每件物品的价格与重要度的乘积的总和，假设设第ii件物品的价格为v[i]，重要度为w[i]，共选中了k件物品，编号依次为j_1, j_2, ..., j_k,则满意度为：v[j_1] * w[j_1] + v[j_2] * w[j_2] + … +v[j_k] * w[j_k]（其中 * 为乘号）
# 请你帮助王强计算可获得的最大的满意度。

# 输入描述：
# 输入的第1行，为两个正整数N，m，用一个空格隔开：

# （其中 N （ N < 32000 ）表示总钱数， m （m < 60 ）为可购买的物品的个数。）

# 从第2行到第m + 1行，第j行给出了编号为j - 1的物品的基本数据，每行有3个非负整数v p q
# （其中v表示该物品的价格（ v < 10000 ）， p表示该物品的重要度（ 1 ~ 5 ）， q表示该物品是主件还是附件。如果 q = 0 ，表示该物品为主件，如果 q > 0 ，表示该物品为附件， q 是所属主件的编号）


# 输出描述：
# 输出一个正整数，为张强可以获得的最大的满意度。

# 示例1
# 输入：
# 1000  5
# 800   2   0
# 400   5   1
# 300   5   1
# 400   3   0
# 500   2   0

# 输出：
# 2200

# 示例2
# 输入：
# 50    5
# 20    3   5
# 20    3   5
# 10    3   0
# 10    2   0
# 10    1   0

# 输出：
# 130

# 说明：
# 由第1行可知总钱数N为50以及希望购买的物品个数m为5；
# 第2和第3行的q为5，说明它们都是编号为5的物品的附件；
# 第4 ~6行的q都为0，说明它们都是主件，它们的编号依次为3~5；
# 所以物品的价格与重要度乘积的总和的最大值为10 * 1 + 20 * 3 + 20 * 3 = 130