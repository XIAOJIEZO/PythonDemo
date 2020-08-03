# 喜欢的数字，编写一个程序，提示用户输入她喜欢的数字，并使用json.dump()，将这个数字存储到文件中。再编写一个程序，从文件中读取这个值
import json

def get_stored_number():
    """从文件读取数字"""
    try:
        with open('files\\favorite_number.json') as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number

def get_favorite_number():
    """从用户获取数字"""
    number = input('Please enter your favorite number:')
    with open('files\\favorite_number.json', 'w') as f_obj:
        json.dump(number, f_obj)
        print('Saved the number!')
    return number

def display_favorite_number():
    usernum = get_stored_number()
    if usernum:
        print('I know your favorite number! Its ' + str(usernum))
    else:
        get_favorite_number()

# display_favorite_number()