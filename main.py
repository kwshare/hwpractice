import os



def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")

        print("---  OK  ---")

    else:
        print("---  There is this folder!  ---")



def txt(name):  # 定义函数名
    # 获取文件路径
    b = os.getcwd() + "\\"
    print(os.getcwd())
    # print(os.getcwd()[:-4])

    # if not os.path.exists(b):  # 判断当前路径是否存在，没有则创建new文件夹
    #     os.makedirs(b)
    # 文件名称
    xxoo = b + "HJ" + name + '.py'  # 在当前py文件所在路径下的new文件中创建txt
    print(xxoo)
    # 直接打开一个文件，如果文件不存在则创建文件
    file = open(xxoo, mode='w')

    # file.write("text")  # 写入内容信息

    file.close()
    print('ok')


txt('test')  # 创建名称为test的txt文件

if __name__ == '__main__':
    path = "E:\\workspace\\hwpractice\\"
    mkdir(path)  # 调用函数
    for i in range(108, 150):
        txt(str(i))



