# 1-------------------


# import operations_math as om
# while True:
#     x=input("choose:\n\t1)sum\n\t2)mines\n\t3)multiply\n\t4)divide\n\t0)exit")
#     if x=="0":
#         print("bye")
#         break
#     elif x=="1":
#         num1, num2 = input("enter num1 ane num2:").split(" ")
#         print(om.sum_(int(num1),int(num2)))
#     elif x=="2":
#         num1, num2 = input("enter num1 ane num2:").split(" ")
#         print(om.mines_(int(num1),int(num2)))
#     elif x=="3":
#         num1, num2 = input("enter num1 ane num2:").split(" ")
#         print(om.multiply(int(num1),int(num2)))
#     elif x=="4":
#         num1, num2 = input("enter num1 ane num2:").split(" ")
#         print(om.divide(int(num1),int(num2)))

# 2-------------------

# from shapes import *
# from shapes.circle import s_circle, p_circle
# from shapes.rectangle import s_rectangle, p_rectangle
#
# while True:
#     a = input("choose:\n\t1)circle\n\t2)rectangle\n\t0)exit")
#     if a == "0":
#         print("bye")
#         break
#     elif a == "1":
#         b = input("S or P:")
#         if b.lower() == "s":
#
#             r = int(input("r:"))
#             print(s_circle(r))
#         else:
#             r = int(input("r:"))
#             print(p_circle(r))
#
#     elif a == "2":
#         b = input("S or P:")
#         if b.lower() == "s":
#             x = int(input("x:"))
#             y = int(input("y:"))
#             print(s_rectangle(x, y))
#         else:
#             x = int(input("x:"))
#             y = int(input("y:"))
#             print(p_rectangle(x, y))

# 3-------------------

# from data_analysis.statistics import *
#
# # گرفتن ورودی به عنوان یک رشته
# input_string = input("لطفا لیستی از اعداد را با فاصله وارد کنید: ")
#
# # تبدیل رشته به لیستی از اعداد
# numbers = list(map(int, input_string.split()))
# while True:
#     a = input("choose:\n\t1)ave\n\t2)median\n\t3)standard_deviation\n\t0)exit")
#     if a == "0":
#         print("bye")
#         break
#     elif a == "1":
#         print("ave:", ave(numbers))
#
#     elif a == "2":
#         print("median:", median(numbers))
#
#     elif a=="3":
#         print("standard_deviation:", standard_deviation(numbers))

# dit = {"name":"asas"}
# print(dit["name"])


