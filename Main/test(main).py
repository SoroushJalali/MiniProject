import datetime
import copy
import random


# x = "soroush"
# print(len(x))
# b = "123456"
# print(b[::-1])

# l=["sa","sddf","45","lk"]
# print("*".join(l))
# s="  soroush jalali+++"
# print(s.strip())


# x=3.21212121
# print(round(x,2))

#
# a = input("a:")
# x = {a: "1234"}
# print(x)
# print("a is {a}".format(a=x[a]))

# l = [9]
# s = "reza"
# l = list(s)
# l[0] = "b"
# l="".join(l)
# print(type(l))
# print(l)

# x = None
# print(type(x))

# x = int(input("x:"))
# i = 1
# l = []
# while i <= x:
#     if x % i == 0:
#         print(i)
#         l.append(i)
#     i += 1
# del l[-1]
# if sum(l) == x:
#     print("kamel")
# else:
#     "kamel nist"


# i = 1
# a = 0
# b = 1
# while i <= 20:
#     print(a)
#     a, b = b, a + b
#     i += 1

# l =[1,2,3,]
# l1 = ["a","s","x"]
# print(list(zip(l,l1)))
# l=[2,1,3]
# print(random.choices(l))


# def func(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
#
# x = 3
# func(1, 2, c=x)

# def outer_function():
#     def inner_function():
#         return "Hello from inner function!"
#
#     return inner_function
#
#
# my_func = outer_function()
# print(my_func())  # Output: Hello from inner function!
# def a():
#     pass
#
#     def a1():
#         print("salam")
#
#     a1()
# print(a())

# from functools import reduce

# x=int(input("x:"))
# l1=[i for  i in range(1,x+1)]
# print(reduce(lambda a,y:a*y,l1))

# import random
#
# # گزینه‌های بازی
# options = ["سنگ", "کاغذ", "قیچی"]
#
# # دریافت ورودی از کاربر
# user_choice = input("یکی از گزینه‌های 'سنگ'، 'کاغذ' یا 'قیچی' را انتخاب کنید: ").strip()
#
# # انتخاب کامپیوتر
# computer_choice = random.choice(options)
#
# print(f"انتخاب شما: {user_choice}")
# print(f"انتخاب کامپیوتر: {computer_choice}")
#
# # تعیین برنده
# if user_choice == computer_choice:
#     print("مساوی شد!")
# elif (user_choice == "سنگ" and computer_choice == "قیچی") or \
#      (user_choice == "کاغذ" and computer_choice == "سنگ") or \
#      (user_choice == "قیچی" and computer_choice == "کاغذ"):
#     print("شما برنده شدید!")
# else:
#     print("کامپیوتر برنده شد!")

# def dec(f):
#     def inner(x,y):
#
#     return inner
#
#
# def func(x,y):
#     print(x/y)
#
# new_func=dec(func)

# func(5,3)

# def greet(*name,**names):  # *args
#     # for name in names:
#     print(f"Hello, {name}!")
#
# greet("soroush",name="ali")
# # ارسال تعداد زیادی آرگومان


# def dec(func,y):
#     if y==0:
#         print("warning")
#     else:
#         func
#
# def func (x,y):
#     print(x/y)
#
# dec(func(1,0))

# def dec(func):
#     def inner(a, b):
#         if b == 0:
#             print("warning")
#         else:
#             func(a, b)
#
#     return inner
#
#
# def func(x, y):
#     print(x / y)
#
#
# fun1 = dec(func)
# fun1(1, 5)


# def gen(x):
#     yield x**2
#     print("ssss")
#
# print(gen(5))

# import random
#
# print(help(random))








