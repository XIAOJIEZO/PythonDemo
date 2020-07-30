# 1、提示用户输入姓名，将名字写入到文件guests.txt文件中。
name = input('请输入姓名：')

with open('files\guests.txt', 'w') as file_object:
    file_object.write(name)


# 2、用户循环输入姓名，打印问候语，并将访问记录添加到文件guest_book.txt。


action = True
while action:
    name = input('请输入姓名：')
    with open('files\guests_book.txt', 'a') as file_object:
        file_object.write(name + '\n')
    print('hello,' + name + '!')

    action = input('输入quit退出：')
    if action == 'quit':
        break

