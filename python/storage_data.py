# 存储数据
import json

numbers = [1, 3, 4, 8, 9]
filename = 'numbers.json'       # 通常使用文件扩展名.json来指出文件存储的数据为json格式
with open('files\\' + filename, 'w') as f_obj:
    json.dump(numbers, f_obj)       # json.dump()接收两个参数：要存储的数据以及可用于存储数据的文件对象。

# 使用使用Jason.load()将列表读取到内存中
with open('files\\' + filename) as f_obj:
    j_numbers = json.load(f_obj)    # json.load()加在存储在文件中的信息
print(j_numbers)

# 保存和读取用户生成的数据：对于用户生成的数据，使用json保存他们大有裨益，因为不以某种方式进行存储，等程序停止运行时用户的信息将丢失。
# 例子，用户首次登陆程序时被提示输入用户名，再次运行程序时就记住他了
username = input('What is  your name?')
with open('files\\username.json', 'w') as f_obj:
    json.dump(username, f_obj)

with open('files\\username.json') as f_obj:
    username = json.load(f_obj)
    print('Welcome back, ' + username + '!')

# 优化，将其合并为一个程序
try:
    with open('files\\username2.json') as f_obj:
        username2 = json.load(f_obj)
except FileNotFoundError:
    username2 = input('What is  your name?')
    with open('files\\username2.json', 'w') as f_obj:
        json.dump(username2, f_obj)
else:
    print('Welcome back, ' + username2 + '!')