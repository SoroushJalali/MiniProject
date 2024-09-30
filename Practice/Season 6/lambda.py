# لامبدا
# 1-------------------

# num = int(input("enter your number:"))
# li = [i for i in range(1, num + 1)]
# x = filter(lambda j: j % 2 == 0, li)
# y = filter(lambda j: j % 2 != 0, li)
# print("len even:", len(list(x)), "\nlen odd:", len(list(y)))

# 2-------------------

# li = [("mahan", 14), ("soroush", 16), ("mergan", 5)]
# li.sort(key=lambda x: x[1], reverse=True)
# print(li)

# 3-------------------

# li = [{"name":"apple","color": "red", "weight": 50},
#       {"name":"banana","color": "yellow", "weight": 20},
#       {"name":"coconat","color": "brown", "weight": 12}
#       ]
# li1 = sorted(li, key=lambda x: x['color'])
# print(li1)

# 4-------------------

# num = int(input("enter your number:"))
# li = [i for i in range(1, num + 1)]
# even = list(filter(lambda x: x % 2 == 0, li))
# odd = list(filter(lambda x: x % 2 != 0, li))
# print(f"even:{even}\nodd:{odd}")

# 5-------------------

# num = int(input("enter your number:"))
# li = [i for i in range(1, num + 1)]
# cube = list(map(lambda x: x ** 3, li))
# squaer = list(map(lambda x: x ** 2, li))
# print(f"cube:{cube}\nsquaer:{squaer}")

# 6-------------------

# s =(input("enter str:"))
# start_with = lambda x: True if x.startswith("s") else False
# print(start_with(s))

# 7-------------------

# s = (input("enter str:"))
# is_num = lambda x: x.replace(".", "", 1).isdigit()
# print(is_num(s))
