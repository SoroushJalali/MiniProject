# 1-------------------

# import json
#
#
# def data(j_data):
#     p_data = json.loads(j_data)
#     return p_data
#
#
# json_data = '{"name": "Ali", "age": 25, "city": "Tehran","b":true}'
# print(data(json_data))

# 2-------------------

# import json
#
#
# def data(j_data):
#     p_data = json.loads(j_data)
#     key = input("your key:")
#
#     return p_data[key]
#
#
# json_data = '{"name": "Ali", "age": 25, "city": "Tehran","b":true}'
# print(data(json_data))

# 3-------------------

# import json
#
#
# def data(j_data):
#     p_data = json.loads(j_data)
#     key = input("your key:")
#     value = input("your value:")
#     p_data[key] = value
#     j_update = json.dumps(p_data)
#     return j_update
#
#
# json_data = '{"name": "Ali", "age": 25, "city": "Tehran","b":true}'
# print(data(json_data))

# 4-------------------

# chat GPT
# import json
# from collections import Counter
#
#
# def count_unique_values(json_string):
#     # تبدیل رشته JSON به لیست از دیکشنری‌ها
#     data = json.loads(json_string)
#
#
#     # جمع‌آوری مقادیر مرتبط با کلید 'color'
#     colors = [item["color"] for item in data]
#
#     # شمارش تعداد هر مقدار منحصر به فرد
#     color_counts = dict(Counter(colors))
#     return color_counts
#
#
# # مثال ورودی
# json_string = '[{"color": "red"}, {"color": "blue"}, {"color": "red"}, {"color": "green"}]'
#
# # فراخوانی تابع و چاپ نتیجه
# result = count_unique_values(json_string)
# print(result)

# --------------------------------------

# code ma
# import json
#
#
# def data(j_data):
#     p_data = json.loads(j_data)
#     li = []
#     for i in p_data:
#         li.append(i["color"])
#     key = set(li)
#     key = list(key)
#     dic = {}
#     for i in key:
#         dic[i] = li.count(i)
#
#     return dic
#
#
# json_data = '[{"color": "red"}, {"color": "blue"}, {"color": "red"}, {"color": "green"}]'
#
# print(data(json_data))

# 5-------------------

# import json
#
#
# def merge_json(json_str1, json_str2):
#     # تبدیل رشته‌های JSON به دیکشنری‌های پایتون
#     dict1 = json.loads(json_str1)
#     dict2 = json.loads(json_str2)
#
#     # ادغام دیکشنری‌ها
#     merged_dict = dict1 | dict2
#
#     # تبدیل دیکشنری ادغام شده به رشته JSON
#     return json.dumps(merged_dict, indent=4)
#
#
# # مثال استفاده
# json1 = '{"name": "Ali", "age": 25}'
# json2 = '{"city": "Tehran", "country": "Iran"}'
#
# merged_json = merge_json(json1, json2)
# print(merged_json)

# 6-------------------

# import json
# import csv
#
#
# def json_to_csv(json_string, csv_file_path):
#     # تبدیل رشته JSON به یک شیء پایتون
#     data = json.loads(json_string)
#
#     # بررسی اینکه داده‌ها در فرمت یک لیست از دیکشنری‌ها باشند
#     if isinstance(data, list):
#         # باز کردن فایل CSV برای نوشتن
#         with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
#             # دریافت کلید‌های دیکشنری به عنوان نام ستون‌های CSV
#             fieldnames = data[0].keys()
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
#
#             # نوشتن هدر‌های CSV
#             writer.writeheader()
#
#             # نوشتن داده‌های JSON در CSV
#             for row in data:
#                 writer.writerow(row)
#     else:
#         print("فرمت JSON باید یک لیست از دیکشنری‌ها باشد.")
#
#
# # نمونه استفاده از تابع
# json_string = '''
# [
#     {"name": "John", "age": 30, "city": "New York"},
#     {"name": "Anna", "age": 25, "city": "London"},
#     {"name": "Mike", "age": 35, "city": "Chicago"}
# ]
# '''
#
# csv_file_path = "output.csv"
# json_to_csv(json_string, csv_file_path)

# 7-------------------

# import csv
#
#
# def json_to_csv(python_string, csv_file_path):
#     # بررسی اینکه داده‌ها در فرمت یک لیست از دیکشنری‌ها باشند
#     if isinstance(python_string, list):
#         # باز کردن فایل CSV برای نوشتن
#         with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
#             # دریافت کلید‌های دیکشنری به عنوان نام ستون‌های CSV
#             fieldnames = python_string[0].keys()
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
#
#             # نوشتن هدر‌های CSV
#             writer.writeheader()
#
#             # نوشتن داده‌های JSON در CSV
#             for row in python_string:
#                 writer.writerow(row)
#     else:
#         print("فرمت JSON باید یک لیست از دیکشنری‌ها باشد.")
#
#
# # نمونه استفاده از تابع
# python_string = \
#     [
#         {"name": "John", "age": 30, "city": "New York"},
#         {"name": "Anna", "age": 25, "city": "London"},
#         {"name": "Mike", "age": 35, "city": "Chicago"}
#     ]
#
# csv_file_path = "output1.csv"
# json_to_csv(python_string, csv_file_path)

# 8-------------------
import csv

def sum_column(file_path, column_name):
    total = 0
    try:
        with open(file_path, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                try:
                    value = float(row[column_name])  # تبدیل به عدد (اعشاری برای پشتیبانی از مقادیر اعشاری)
                    total += value
                except ValueError:
                    print(f"Skipping non-numeric value: {row[column_name]}")
                    continue
        print(f"Total sum of column '{column_name}': {total}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except KeyError:
        print(f"Column '{column_name}' not found in CSV file.")

# مثال استفاده
file_path = "output2.csv"
column_name = input("Enter the column name: ")
sum_column(file_path, column_name)

