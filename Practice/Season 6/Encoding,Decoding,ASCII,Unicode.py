# 1-------------------

# # تعریف رشته
# input_string = "Hello, World!"
#
# # انکد کردن رشته به UTF-8 و تبدیل آن به نمایش هگزادسیمال
# hex_output = input_string.encode('utf-8').hex()
#
# # چاپ نتیجه
# print(hex_output)

# 2-------------------

# # تعریف بایت‌ها
# byte_data = b'My name is M\xc3\xb6bius'
#
# # دیکد کردن بایت‌ها با استفاده از UTF-8
# decoded_string = byte_data.decode('utf-8')
#
# # چاپ نتیجه
# print(decoded_string)

# 3-------------------

# # لیست کاراکترها
# characters = ['a', 'b', 'c', 'A', 'B', 'C', '1', '2', '3']
#
# # تبدیل کاراکترها به مقدار ASCII و ذخیره در لیست جدید
# ascii_values = [ord(char) for char in characters]
#
# # چاپ نتیجه
# print(ascii_values)

# 4-------------------

# # گرفتن جمله از کاربر
# sentence = input("لطفاً یک جمله وارد کنید: ")
#
# # محاسبه مجموع مقادیر ASCII تمام کاراکترهای جمله
# ascii_sum = sum(ord(char) for char in sentence)
#
# # چاپ نتیجه
# print("مجموع مقادیر ASCII جمله وارد شده:", ascii_sum)

# 5-------------------

# # لیست point code های Unicode
# unicode_points = [1024, 5678, 234, 987]
#
# # انکد کردن به UTF-16 و ذخیره بایت‌ها در یک لیست جدید
# encoded_bytes = [chr(code_point).encode('utf-16') for code_point in unicode_points]
#
# # چاپ نتیجه
# for i, byte_sequence in enumerate(encoded_bytes):
#     print(f"Point code {unicode_points[i]} in UTF-16 encoding: {byte_sequence}")

# 6-------------------

# # تعریف بایت‌ها
# byte_data = b'\xff\xfeM\x00y\x00 \x00N\x00a\x00m\x00e\x00'
#
# # دیکد کردن بایت‌ها با استفاده از UTF-16
# decoded_string = byte_data.decode('utf-16')
#
# # چاپ نتیجه
# print(decoded_string)

# 7-------------------

# def string_to_hex(s):
#     # انکد کردن رشته به UTF-8 و سپس تبدیل به هگزادسیمال
#     return s.encode('utf-8').hex()
#
# # تست کردن تابع
# input_string = "سلام"
# hex_output = string_to_hex(input_string)
# print(hex_output)
