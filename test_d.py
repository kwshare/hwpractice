# while True:
#     try:
#         m = input()
#         a = input().split(" ")
#         b = input().split(" ")
#         for i in range(m):
#             c=0
#             d=0
#             for i in a:
#                 c += i
#             for i in b:
#                 d += i
#         print(c)
#         print(d)
#     except:
#         break


# num = [(1,2.5), (1.5, 3.2), (1.3, 4.0), (2.2, 1.8)]
# y,z = max(num, key=lambda x:x[0])
# z1 = sorted(num, key=lambda x:x[0])
# z2 = sorted(num, key=lambda x:x[1])
# print(y, z)
# print(z1)
# print(z2)

print( "round(80.23456, 2) : ", round(80.23456, 2))
print( "round(100.000056, 5) : ", round(100.000056, 5))
print( "round(100.000056, 3) : ", round(100.000056, 3))
print( "round(-100.000056, 3) : ", round(-100.000056, 3))
print( "round(-100.000056, 5) : ", round(-100.000056, 5))