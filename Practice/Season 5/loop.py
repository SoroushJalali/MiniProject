# تکرار
# 1-------------------

# num1 = int(input("enter num 1:"))
# num2 = int(input("enter num 2:"))
# l1 = [num1, num2]
# for i in range(min(l1), max(l2) + 1):
#     print(i)

# 2-------------------

# num1 = int(input("enter num 1:"))
# num2 = int(input("enter num 2:"))
# min_ = min(num1, num2)
# for i in range(1, min_ + 1):
#     if num1 % i == 0 and num2 % i == 0:
#         print(i, end="\t")

# 3-------------------

# num1 = int(input("enter num 1:"))
# num2 = int(input("enter num 2:"))
# min_ = min(num1, num2)
# for i in range(min_,0,-1):
#     if num1 % i == 0 and num2 % i == 0:
#         print(i)
#         break

# 4-------------------

# num1 = int(input("enter num 1:"))
# num2 = int(input("enter num 2:"))
# min_ = min(num2, num1)
# max_ = max(num2, num1)
# for i in range(1, min_ + 1):
#     if (max_ * i) % min_ == 0:
#         print(max_ * i)
#         break

# 5-------------------

# i = 0
# num = int(input("enter num:"))
# while True:
#     num = num // 10
#     i += 1
#     if num == 0:
#         break
# print(i)

# 6-------------------

# line = int(input("how many line do you have?"))
# for i in range(1, line + 1):
#     print(" " * (line - i), i * "*")

# 7-------------------

# import random
#
# l1 = list(range(1, 11))
# l1_copy = l1.copy()
# while True:
#     if len(l1_copy)==0:
#         break
#     random_number = random.choice(l1_copy)
#     check = input(f"your number is {random_number}? ")
#     if "yes" == check.lower():
#         print("afrin")
#         break
#     l1_copy.remove(random_number)

