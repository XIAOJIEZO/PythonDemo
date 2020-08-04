# 被测试的函数
"""
def get_formatted_name(fist_name, last_name):
    full_name = fist_name + ' ' + last_name
    return full_name
"""

"""
def get_formatted_name(fist_name, middle, last_name):
    full_name = fist_name + ' ' + middle + ' ' + last_name
    return full_name
"""
def get_formatted_name(fist_name, last_name, middle = ''):
    if middle:
        full_name = fist_name + ' ' + middle + '_' + last_name
    else:
        full_name = fist_name + ' ' + last_name
    return full_name.title()