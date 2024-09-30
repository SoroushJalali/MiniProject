# ژنراتور
# 1-------------------

# def enu_gen(secuence,start=0):
#     i = 0
#     while i < len(secuence):
#         yield (start, secuence[i])
#         start+=1
#         i += 1
#
#
# l = enu_gen(["salam", "mergan", "yasin"],0)
# print(list(l))

# 2-------------------

# def fib_gen(limit):
#     a, b = 0, 1
#     i = 1
#     while i <= limit:
#         a, b = b, a + b
#         i += 1
#         yield a
#
#
# fib = fib_gen(20)
# for i in fib:
#     print(i, end="\t")


# 3-------------------

# def sum_gen(li):
#     s = 0
#     for i in li:
#         s += i
#         yield s
#
#
# sg = sum_gen([1, 2, 3, 4, 5, 6])
# for i in sg:
#     print(i)

# 4-------------------

# def rev_gen(s):
#     l = len(s)
#     for i in range(l - 1, -1, -1):
#         yield s[i]
#
#
# rev = rev_gen("hifd")
# for ch in rev:
#     print(ch)

# 5-------------------
# def my_gen(input_="e"):
#     start = 0
#     if input_.lower() == "o":
#         start = 1
#     while True:
#         yield start
#         start += 2
#
#
# s = my_gen("o")
# for _ in range(20):
#     print(next(s))

# 6-------------------
# def num_gen():
#     c = 1
#     while True:
#         s = ""
#         for i in range(1, c + 1):
#             s += f"{c}\t"
#         yield s
#         c += 1
#
#
# num_ = num_gen()
# for _ in range(12):
#     print(next(num_))
