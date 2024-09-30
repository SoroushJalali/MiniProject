import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # do something before
        value = func(*args, **kwargs)
        # do something after
        return value

    wrapper_decorator()


# 1-------------------
# d = {"mergan": "0000", "link": "1234", "yasin": "4321"}
# black_list = {"mergan", 'link'}
#
#
# def ban(show_pass):
#     def inner(username, black_list):
#         if username in black_list:
#             print(f"{username} is in black list")
#         else:
#             show_pass(username)
#
#     return inner
#
#
# @ban
# def show_pass(username):
#     print(username, ":", d[username])
#
#
# def change_pass(username, new_pass):
#     d[username] = new_pass
#     print(f"new pass:{username}:{d[username]}")
#
#
# print(d)
# show_pass("yasin", black_list)
# change_pass("yasin", "1111")
# print(d)

# 2-------------------

from time import perf_counter


def time(math_):
    def inner(*x):
        math_(*x)

    return inner


@time
def math(a, b, c):
    print(a * b * c)

# math_(5,6,10)
