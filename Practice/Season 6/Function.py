# توابع
# 1-------------------

# def count_(s):
#     print(len(s))
#
#
# s = input("enter your str:")
# count_(s)

# 2-------------------

# def max_min(x, l1):
#     if x.lower() == "max":
#         print(f"max:{max(l1)}")
#     elif x.lower() == "min":
#         print(f"min:{min(l1)}")
#     else:
#         print("error")
#
#
# l1 = []
# for i in range(1, 11):
#     l1.append(int(input(f"enter number{i}:")))
# x = input("max or min:")
# max_min(x, l1)

# 3-------------------

# def sum_(line):
#     sum1 = 0
#     for i in range(1, line + 1):
#         sum1 += i
#     print(f"sum is {sum1}")
#
#
# line = int(input("how many line do you wants?"))
# sum_(line)

# 4-------------------

# def odd_even():
#     num = int(input("enter number:"))
#     for i in range(2, num):
#         if num % i == 0:
#             print("its even")
#             break
#     else:
#         print("its odd")
#
#
# odd_even()

# 5-------------------

# def real_price():
#     price = int(input("enter a price:"))
#     discount = int(input("enter a discount:"))
#     print(f"real price is {price - (price * (discount / 100))}")
#
#
# real_price()

# 6-------------------

# def char(c):
#     if 48 <= ord(c) <= 58:
#         print("its a number")
#     elif 65 <= ord(c) <= 90:
#         print("its a Uppercase letters")
#     elif 97 <= ord(c) <= 122:
#         print("its a Lowercase letters")
#     else:
#         print("its another symbol")
# 
#
# c = input("enter char:")
# char(c)
