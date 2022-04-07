# HJ72 百钱买百鸡问题


while True:
    try:
        ppp = input()
        for a in range(21):  # a 最多买20只 公鸡
            for b in range(34):  # b 最多买33只 母鸡
                for c in range(101):  # c 最多买100只小鸡
                    if a + b + c == 100 and 5 * a + 3 * b + 1 * c / 3 == 100:
                        print(a, b, c)
    except:
        break

'''
简单  通过率：50.56%  时间限制：1秒  空间限制：32M
知识点
查找
warning 校招时部分企业笔试将禁止编程题跳出页面，为提前适应，练习时请使用在线自测，而非本地IDE。
描述
公元五世纪，我国古代数学家张丘建在《算经》一书中提出了“百鸡问题”：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
现要求你打印出所有花一百元买一百只鸡的方式。
输入描述：
输入任何一个整数，即可运行程序。

输出描述：
 输出有数行，每行三个整数，分别代表鸡翁，母鸡，鸡雏的数量

示例1
输入：
1
复制
输出：
0 25 75
4 18 78
8 11 81
12 4 84
'''