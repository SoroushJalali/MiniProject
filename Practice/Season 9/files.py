# 1-------------------

# with open("output.txt", "a") as f:
#     while True:
#         s = input("s:")
#         if s == "exit":
#             break
#         f.write(s)
#         f.write("\n")

# 2-------------------

# # برنامه برای خواندن فایل و حذف فاصله‌های اضافی بین کلمات
# def read_and_process_file(file_name):
#     try:
#         with open(file_name, 'r', encoding='utf-8') as file:
#             for line in file:
#                 # حذف فاصله‌های اضافی بین کلمات و چاپ خط
#                 processed_line = ' '.join(line.split())
#                 print(processed_line)
#     except FileNotFoundError:
#         print(f"فایل '{file_name}' یافت نشد.")
#
#
# # فراخوانی تابع برای فایل 'data.txt'
# read_and_process_file('data.txt')

# 3-------------------

# import re
#
# with open("sample.txt", "r") as f:
#     word = input("word:")
#     matches = re.findall(rf"\b{word}\b", f.read(), re.IGNORECASE)
#     print(f"تعداد تکرار '{word}':", len(matches))

# 4-------------------

# with open("source.txt", "r") as f1, open("destination.txt", "w") as f2:
#     f2.write(f1.read())

# 5-------------------

# برنامه برای دریافت چندین خط متن از کاربر و اضافه کردن به فایل 'notes.txt'
# def append_to_file(file_name):
#     with open(file_name, 'a', encoding='utf-8') as file:  # باز کردن فایل به صورت append
#         while True:
#             user_input = input("لطفاً یک خط متن وارد کنید (برای خروج یک خط خالی وارد کنید): ")
#             if user_input == "":  # اگر ورودی خط خالی باشد، حلقه متوقف می‌شود
#                 print("خروج از برنامه.")
#                 break
#             file.write(user_input + "\n")  # اضافه کردن متن وارد شده به فایل
#
#
# # فراخوانی تابع برای فایل 'notes.txt'
# append_to_file('notes.txt')

# 6-------------------

# sum_ = 0
# n = 0
# with open("numbers.txt", "r") as f:
#     for i in f.readlines():
#         i = int(i)
#         sum_ += i
#         n += 1
#     print(sum_ / n)

# 7-------------------

# with open("document.txt", "r") as f1, open("document_updated.txt", "w") as f2:
#     word = input("word:")
#     replace_ = input("replace to:")
#     s = f1.read()
#     print(s)
#     if word in s:
#         print(word)
#         s = s.replace(word, replace_)
#         print(f2.write(s))

# 8-------------------

# import os
#
# file_path = 'txt.delete_to_file'
#
# # بررسی وجود فایل
# if os.path.exists(file_path):
#     os.remove(file_path)
#     print(f"فایل '{file_path}' با موفقیت حذف شد.")
# else:
#     print(f"فایل '{file_path}' وجود ندارد.")
