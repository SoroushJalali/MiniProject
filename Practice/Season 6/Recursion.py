# تابع بازگشتی
# 1-------------------

# def sum_list(li):
#     c = len(li) - 1
#     if c == 0:
#         return li[0]
#     n = li[c]
#     del li[c]
#     c -= 1
#     return sum_list(li) + n
#
#
# print(sum_list([1, 2, 2, 3, 4, 5]))

# 2-------------------

# def power_num(num, power):
#     if power == 0:
#         return 1
#     return power_num(num, power - 1) * num
#
#
# print(power_num(5, 3))

# 3-------------------

# def reverse_string(s):
#     # شرط توقف: اگر رشته خالی باشد، رشته خالی برگردانده می‌شود
#     if len(s) == 0:
#         return s
#     # بازگشت: آخرین کاراکتر را به جلو می‌آورد و تابع را بر روی بقیه رشته فراخوانی می‌کند
#     return s[-1] + reverse_string(s[:-1])
#
# # مثال استفاده
# input_string = "سلام"
# print(reverse_string(input_string))

# 4-------------------

# def count_occurrences(lst, element):
#     # شرط توقف: اگر لیست خالی باشد، صفر برگردانده می‌شود
#     if len(lst) == 0:
#         return 0
#     # اگر عنصر اول لیست با عنصر مورد نظر برابر باشد، 1 اضافه می‌شود و تابع بر روی بقیه لیست فراخوانی می‌شود
#     if lst[0] == element:
#         return 1 + count_occurrences(lst[1:], element)
#     else:
#         # در غیر این صورت، تابع بر روی بقیه لیست بدون اضافه کردن 1 فراخوانی می‌شود
#         return count_occurrences(lst[1:], element)
#
# # مثال استفاده
# lst = [1, 2, 3, 4, 2, 2, 2]
# element = 2
# count = count_occurrences(lst, element)
# print(count)  # خروجی: 3

# 5-------------------

# def is_palindrome(s):
#     # شرط توقف: اگر رشته کمتر از 2 کاراکتر داشته باشد، پالین‌دروم است
#     if len(s) < 2:
#         return True
#     # بررسی اینکه اولین و آخرین کاراکتر یکسان هستند یا خیر
#     if s[0] == s[-1]:
#         # اگر یکسان بودند، تابع را بر روی رشته بدون اولین و آخرین کاراکتر فراخوانی می‌کنیم
#         return is_palindrome(s[1:-1])
#     else:
#         # اگر اولین و آخرین کاراکتر یکسان نبودند، رشته پالین‌دروم نیست
#         return False
#
# # مثال استفاده
# input_string = "radar"
# result = is_palindrome(input_string)
# print(result)  # خروجی: True
#
# input_string = "hello"
# result = is_palindrome(input_string)
# print(result)  # خروجی: False


# =========================
# def palindrome(s):
#     n = len(s) - 1
#     if n % 2 == 0:
#         if s[0:n // 2] == s[-1:n // 2:-1]:
#             return "yes"
#         else:
#             return "no"
#     else:
#         if s[0:(n // 2) + 1] == s[-1:n // 2:-1]:
#             return "yes"
#         else:
#             return "no"
#
#
# print(palindrome("sdass"))

# 6-------------------

# def sum_func(num):
#     c = 0
#     if num // 10 == 0:
#         c = num % 10 + c
#         return c
#     c = num % 10 + c
#     return sum_func(num // 10) + c
#
#
# print(sum_func(12))

