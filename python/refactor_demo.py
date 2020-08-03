# 重构：代码能够正确地运行，到可以做进一步改进。将代码划分为一系列完成具体工作的函数，这样的过程被称为重构。
import json
def greet_user():
    try:
        with open('files\\username3.json') as f_obj:
            username3 = json.load(f_obj)
    except FileNotFoundError:
        username3 = input('What is  your name?')
        with open('files\\username3.json', 'w') as f_obj:
            json.dump(username3, f_obj)
    else:
        print('Welcome back, ' + username3 + '!')

# greet_user()

# 上面的程序不止执行了一件事，不仅问候用户，还存储数据同时获取它，可将greet_user()进一步重构
def get_storedd_username():
    """如果存储了用户名，就获取它"""
    try:
        with open('files\\username4.json') as f_obj:
            username4 = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username4

def greet_user4():
    """问候用户，并指出其名字"""
    username4 = get_storedd_username()
    if username4:
        print('Welcome back, ' + username4 + '!')
    else:
        username4 = input('What is  your name?')
        with open('files\\username4.json', 'w') as f_obj:
            json.dump(username4, f_obj)

# greet_user4()

# greet_user4()还可以继续讲提示输入姓名与问候用户进行进一步提取
def get_stored_username5():
    """如果存储了用户名，就获取它"""
    try:
        with open('files\\username5.json') as f_obj:
            username5 = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username5

def get_new_username5():
    """提示用户输入用户名"""
    username5 = input('What is  your name?')
    with open('files\\username5.json', 'w') as f_obj:
        json.dump(username5, f_obj)
    return username5

def greet_username5():
    """问候用户，并指出其姓名"""
    username5 = get_storedd_username5()
    if username5:
        print('Welcome back, ' + username5 + '!')
    else:
        username5 = get_new_username5()

# greet_username5()