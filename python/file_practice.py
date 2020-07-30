# 读取整个文件
with open('files\pi_digits') as file_object:    # open()返回的文件对象只在with代码中可用
    contents = file_object.read()
    print(contents)     # read()到达文件末尾时返回一个空行，可在print语句中使用rstrip()
    print(contents.rstrip())
"""
    要以任何方式使用文件，都得先打开文件。函数open()接受一个参数：要打开文件的名称，并返回一个表示文件的对象。关键字with在不再需要访问文件时将其
关闭。
"""

# 逐行读取
filename = 'files\pi_digits'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 创建一个包含文件内容的列表
with open(filename) as file_object:
    lines = file_object.readlines()     # 方法readlines()读取文件每一行，存储在列表中

print(type(lines))
print(lines)

for line in lines:
    print(line.rstrip())

# 写入文件：只能写入字符串，数值数据需先转换类型
filename = 'files\programming'

with open(filename, 'w') as file_object:    # r（读取模式）、（写入模式）、a（附加模式）、r+（读取和写入），省略参数默认只读。使用w会清楚之前的文件内容
    file_object.write('I love programming')

# 写入多行
with open('files\programming2', 'w') as file_object:    # r（读取模式）、（写入模式）、a（附加模式）、r+（读取和写入），省略参数默认只读。使用w会清楚之前的文件内容
    file_object.write('I love programming.\n')  # 不会自动换行
    file_object.write('I love programming.\n')

# 添加文件到附件：添加内容而不覆盖原有内容
with open('files\programming2', 'a') as file_object:    # r（读取模式）、（写入模式）、a（附加模式）、r+（读取和写入），省略参数默认只读。使用w会清楚之前的文件内容
    file_object.write('I love programming.\n')  # 不会自动换行
    file_object.write('I love programming.\n')
