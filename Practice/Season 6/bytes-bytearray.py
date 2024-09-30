# 1-------------------

# byt= bytes("salam","utf_8")
# hex_byt= byt.hex()
# print(hex_byt)

# 2-------------------

# رشته هگزادسیمال
# hex_str = "73616c616d"

# # تبدیل رشته هگزادسیمال به bytearray
# byte_array = bytearray.fromhex(hex_str)

# # چاپ bytearray
# print(byte_array)

# 3-------------------

# byt=bytearray("salam","utf-8")
# byt[0]=ord("k")
# print(byt)

# 4-------------------

# byt1=bytearray("salam","utf-8")
# byt2=bytearray(" neda","utf-8")
# print(byt1+byt2)

# 5-------------------

# # ایجاد یک bytearray
# byte_array = bytearray([10, 20, 30, 40, 50])
#
# # مقدار بایت مورد نظر برای جستجو
# byte_value = 20
#
# # بررسی وجود مقدار بایت در bytearray
# if byte_value in byte_array:
#     print(f"مقدار {byte_value} در bytearray وجود دارد.")
# else:
#     print(f"مقدار {byte_value} در bytearray وجود ندارد.")

# 6-------------------

# # ایجاد یک bytearray
# byte_array = bytearray(b'salam')
#
# # تبدیل bytearray به لیست از اعداد صحیح
# int_list = list(byte_array)
#
# # نمایش لیست از اعداد صحیح
# print(int_list)

# 7-------------------

# # ایجاد یک bytearray
# byte_array = bytearray([10, 20, 30, 40, 50])

# # مقدار بایت مورد نظر برای پیدا کردن ایندکس آن
# byte_value = 30

# # پیدا کردن ایندکس مقدار بایت در bytearray
# try:
#     index = byte_array.index(byte_value)
#     print(f"ایندکس مقدار {byte_value} در bytearray: {index}")
# except ValueError:
#     print(f"مقدار {byte_value} در bytearray وجود ندارد.")

