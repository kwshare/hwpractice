# HJ98 自动售货系统


class GoodSystem():
    # 商品名称
    goods_names = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']
    # 商品价格
    goods_price = [2, 3, 4, 5, 8, 6]
    # 每种商品的数量
    goods_nums = []
    # 币额
    money_flag = [1, 2, 5, 10]
    # 每种币值的张数
    money_nums = []
    # 投币余额
    balance = 0

    def __init__(self, param1, param2):
        """
        初始化商品数量和每种面额的张数
        """
        self.goods_nums = list(map(int, param1.split('-')))
        self.money_nums = list(map(int, param2.split('-')))
        print('S001:Initialization is successful')

    def put_money(self, money):
        # 投币
        if money not in [1, 2, 5, 10]:
            print('E002:Denomination error')
        elif money in [5, 10] and money > self.money_nums[0] + self.money_nums[1] * 2:
            print('E003:Change is not enough, pay fail')
        elif sum(self.goods_nums) == 0:
            print('E005:All the goods sold out')
        else:
            self.balance += money
            self.money_nums[self.money_flag.index(money)] += 1
            print('S002:Pay success,balance=%d' % self.balance)

    def buy_goods(self, name):
        # 购买商品
        if name not in self.goods_names:
            print('E006:Goods does not exist')
        elif self.goods_nums[self.goods_names.index(name)] == 0:
            print('E007:The goods sold out')
        elif self.balance < self.goods_price[self.goods_names.index(name)]:
            print('E008:Lack of balance')
        else:
            self.balance -= self.goods_price[self.goods_names.index(name)]
            self.goods_nums[self.goods_names.index(name)] -= 1
            print('S003:Buy success,balance=%d' % self.balance)

    def out_money(self):
        # 存钱盒总额
        total_money = self.money_nums[0] + self.money_nums[1] * 2 + self.money_nums[2] * 5 + self.money_nums[3] * 10
        # 每个币额退的数量
        out_count = [0, 0, 0, 0]
        if self.balance == 0:
            print('E009:Work failure')
        elif self.balance >= total_money:
            print('1 yuan coin number=%d' % self.money_nums[0])
            print('2 yuan coin number=%d' % self.money_nums[1])
            print('5 yuan coin number=%d' % self.money_nums[2])
            print('10 yuan coin number=%d' % self.money_nums[3])
        else:
            if self.balance >= self.money_nums[3] * 10:
                self.balance -= self.money_nums[3] * 10
                self.money_nums[3] = 0
                out_count[3] = self.money_nums[3]
            else:
                self.money_nums[3] -= self.balance // 10
                out_count[3] = self.balance // 10
                self.balance -= self.balance // 10 * 10
            if self.balance >= self.money_nums[2] * 5:
                self.balance -= self.money_nums[2] * 5
                self.money_nums[2] = 0
                out_count[2] = self.money_nums[2]
            else:
                self.money_nums[2] -= self.balance // 5
                out_count[2] = self.balance // 5
                self.balance -= self.balance // 5 * 5
            if self.balance >= self.money_nums[1] * 2:
                self.balance -= self.money_nums[1] * 2
                self.money_nums[1] = 0
                out_count[1] = self.money_nums[1]
            else:
                self.money_nums[1] -= self.balance // 2
                out_count[1] = self.balance // 2
                self.balance -= self.balance // 2 * 2
                self.money_nums[0] -= self.balance
            out_count[0] = self.balance
            self.balance = 0
            print('1 yuan coin number=%d' % out_count[0])
            print('2 yuan coin number=%d' % out_count[1])
            print('5 yuan coin number=%d' % out_count[2])
            print('10 yuan coin number=%d' % out_count[3])

    def query(self, command):
        # 查询功能
        order_list = command.split()
        if len(order_list) == 2 and order_list[1] == '0':
            goods_list = [[0 for i in range(3)] for j in range(6)]
            for i in range(3):
                goods_list[i][0] = self.goods_names[i]
                goods_list[i][1] = self.goods_price[i]
                goods_list[i][2] = self.goods_nums[i]
            goods_list.sort(key=lambda x: x[2])
            for i in range(3):
                print(' '.join(map(str, goods_list[i])))
        elif len(order_list) == 2 and order_list[1] == '1':
            print('1 yuan coin number=%d' % self.money_nums[0])
            print('2 yuan coin number=%d' % self.money_nums[1])
            print('5 yuan coin number=%d' % self.money_nums[2])
            print('10 yuan coin number=%d' % self.money_nums[3])
        else:
            print('E010:Parameter error')


if __name__ == '__main__':

    while True:

        try:
            command_list = input().split(';')[:-1]
            for command in command_list:
                if command[0] == 'r':
                    goods_system = GoodSystem(command.split()[1], command.split()[2])
                elif command[0] == 'p':
                    goods_system.put_money(int(command.split()[1]))
                elif command[0] == 'b':
                    goods_system.buy_goods(command.split()[1])
                elif command[0] == 'q':
                    goods_system.query(command.split()[0])
                elif command[0] == 'c':
                    goods_system.out_money()

        except:
            break

# 困难  通过率：27.31%  时间限制：1秒  空间限制：32M
# 知识点 字符串 模拟

# 描述
# 1 总体说明
# 考生需要模拟实现一个简单的自动售货系统，实现投币、购买商品、退币、查询库存商品及存钱盒信息的功能。
# 系统初始化时自动售货机中商品为6种商品,商品的单价参见1.1规格说明，存钱盒内放置1元、2元、5元、10元钱币，商品数量和钱币张数通过初始化命令设置，参见2.1 系统初始化。
# 1.1规格说明
# 1. 商品:每种商品包含商品名称、单价、数量三种属性，其中商品名不重复。考生不能修改商品名称和单价，初始化命令设置商品数量。这些信息在考试框架中进行定义，考生在实现功能代码时可直接使用。


# 商品名称 单价 数量
# A1	    2	X
# A2	    3	X
# A3	    4	X
# A4	    5	X
# A5	    8	X
# A6	    6	X

# 2. 存钱盒信息：钱币面额、张数两种属性。初始化命令设置各种面额钱币张数。这些信息在考试框架中进行定义，考生在实现功能代码时可直接使用。
# 钱币面额 张数
# 10元    X
# 5元     X
# 2元     X
# 1元	  X

# 3. 退币原则 ：
# 1) 根据系统存钱盒内钱币的 信息 ，按钱币总张数最少的原则进行退币。
# 2) 如果因零钱不足导致不能退币，则尽最大可能退币，以减少用户损失。
# 例如：假设存钱盒内只有4张2元，无其它面额钱币。如果需要退币7元，系统因零钱不足无法退币，则继续尝试退币6元，最终系统成功退币3张2元,用户损失1元钱币。
# 4. 投币操作说明：每次投币成功，投入的钱币面额累加到投币余额；同时，本次投入的钱币放入存钱盒中，存钱盒相应面额钱币增加。
# 5. 投币余额：指当前自动售货机中用户剩余的可购买商品的钱币总额；例如：投入2元面额的钱币，投币余额增加2元；购买一件价格2元的商品，投币余额减少2元；
# 6. 退币操作说明：退币操作需要遵守 退币原则 ；退币成功后，投币余额清零，同时扣除存钱盒相应的金额。
# 7. 购买商品操作说明：一次仅允许购买一件商品；购买商品成功后，自动售货机中对应商品数量减1，投币余额扣除本次购买商品的价格。
# 2 操作说明
# 命令字与第一个参数间使用一个空格分隔，多条命令采用分号隔开。考试系统会对输入命令格式进行处理，考生不需要关注输入命令格式的合法性，只需要实现命令处理函数。
# 2.1 系统初始化
# 命令格式：
# r A1 数量 -A2 数量 -A3 数量 -A4 数量 -A5 数量 -A6 数量 1 元张数 -2 元张数 -5 元张数 -10 元张数
# 参数名称    参数说明       类型  取值范围
# A1数量     商品A1数量      整数   [0,30]
# A2数量     商品A2数量      整数   [0,30]
# A3数量     商品A3数量      整数   [0,30]
# A4数量     商品A4数量      整数   [0,30]
# A5数量     商品A5数量      整数   [0,30]
# A6数量     商品A6数量      整数   [0,30]
# 1元张数    面额1元钱币张数  整数   [0,30]
# 2元张数    面额2元钱币张数  整数   [0,30]
# 5元张数    面额5元钱币张数  整数   [0,30]
# 10元张数   面额10元钱币张数 整数   [0,30]
# 商品和各种面额钱币取值范围只是作为初始化命令的限制，其它场景下不限制取值范围；考试框架已经实现取值范围的检查，考生不需要关注。
# 功能说明：设置自动售货机中商品数量和存钱盒各种面额的钱币张数；
# 约束说明：系统在任意阶段均可执行r初始化系统；考生不需要关注参数的合法性，不需要关注增加或缺少参数的场景；
# 输出说明：输出操作成功提示（执行完r命令后系统会自动输出操作结果，考生不需要再次调用输出函数），例：

# 命令	                    输出	                            含义
# r 6-5-4-3-2-1 4-3-2-1;	S001:Initialization is successful	初始化成功

# 2.2 投币
# 命令格式：p 钱币面额
# 功能说明：
# （1） 如果投入非1元、2元、5元、10元的钱币面额（钱币面额不考虑负数、字符等非正整数的情况），输出“E002:Denomination error”；
# （2） 如果存钱盒中1元和2元面额钱币总额小于本次投入的钱币面额，输出“E003:Change is not enough, pay fail”，但投入1元和2元面额钱币不受此限制。
# （3） 如果自动售货机中商品全部销售完毕，投币失败。输出“E005:All the goods sold out”；
# （4） 如果投币成功，输出“S002:Pay success,balance=X”；
# 约束说明：
# （1） 系统在任意阶段都可以投币；
# （2） 一次投币只能投一张钱币；
# （3） 同等条件下，错误码的优先级：E002 > E003 > E005；
# 输出说明：如果投币成功，输出“S002:Pay success,balance=X”。
# 例：
# 命令    输出
# p 10;  S002:Pay success,balance=10

# 2.3 购买商品
# 命令格式：b 商品名称
# 功能说明：
# （1） 如果购买的商品不在商品列表中，输出“E006:Goods does not exist”；
# （2） 如果所购买的商品的数量为0，输出“E007:The goods sold out”；
# （3） 如果投币余额小于待购买商品价格，输出“E008:Lack of balance”；
# （4） 如果购买成功，输出“S003:Buy success,balance=X”；
# 约束说明：
# （1） 一次购买操作仅能购买一件商品，可以多次购买；
# （2） 同等条件下，错误码的优先级：E006 > E007 > E008；
# 输出说明：
# 如果购买成功，输出“S003:Buy success,balance=X”。
# 例:
# 命令      输出
# b A1;   S003:Buy success,balance=8

# 2.4 退币
# 命令格式：c
# 功能说明：
# （1） 如果投币余额等于0的情况下，输出“E009:Work failure”；
# （2） 如果投币余额大于0的情况下，按照 退币原则 进行“找零”，输出退币信息；
# 约束说明：
# （1） 系统在任意阶段都可以退币；
# （2） 退币方式必须按照 退币原则 进行退币；
# 输出说明：如果退币成功，按照 退币原则 输出退币信息。
# 例，退5元钱币:
'''
命令              输出
c;              1 yuan coin number=0
                2 yuan coin number=0
                5 yuan coin number=1
                10 yuan coin number=0

2.5 查询
命令格式：q 查询类别
功能说明：
（1） 查询自动售货机中商品信息，包含商品名称、单价、数量。 根据商品数量从大到小进行排序；商品数量相同时，按照商品名称的先后顺序进行排序 。
例如：A1的商品名称先于A2的商品名称，A2的商品名称先于A3的商品名称。
（2） 查询存钱盒信息，包含各种面额钱币的张数；
（3） 查询类别如下表所示:
查询类别     查询内容
0           查询商品信息
1	        查询存钱盒信息
如果“查询类别”参数错误，输出“E010:Parameter error”。“查询类别”参数错误时，不进行下面的处理；

输出说明：
“查询类别”为0时，输出自动售货机中所有商品信息（商品名称单价数量）例：
命令             输出
q 0;            A1 2 6
                A2 3 5
                A3 4 4
                A4 5 3
                A5 8 2
                A6 6 0
“查询类别”为1时，输出存钱盒信息（各种面额钱币的张数），格式固定。例：
命令          输出
q 1;        1 yuan coin number=4
            2 yuan coin number=3
            5 yuan coin number=2
            10 yuan coin number=1

输入描述：
依照说明中的命令码格式输入命令。

输出描述：
输出执行结果

示例1
输入：
r 22-18-21-21-7-20 3-23-10-6;c;q0;p 1;b A6;c;b A5;b A1;c;q1;p 5;


输出：
S001:Initialization is successful
E009:Work failure
E010:Parameter error
S002:Pay success,balance=1
E008:Lack of balance
1 yuan coin number=1
2 yuan coin number=0
5 yuan coin number=0
10 yuan coin number=0
E008:Lack of balance
E008:Lack of balance
E009:Work failure
E010:Parameter error
S002:Pay success,balance=5
'''