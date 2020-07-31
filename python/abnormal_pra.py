# 异常：Python发生错误时，会创建一个异常对象。异常是使用try-except代码块处理的
try:
    print(5/0)
except ZeroDivisionError:
    print('you  can\'t divide by zero!')
    
# 处理FileNotFoundError异常：最常见的问题是文件找不到
filename = '123.txt' 
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    message = filename + ' file does not exist'
    print(message)
    
# 分析文本
filename = 'snowman.txt'
try:
    with open('files\\' + filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    message = filename + ' file does not exist'
    print(message)
else:       # 依赖于try代码块成功执行的代码都应放到else代码块中
    # 计算大致包含多少个单词
    words = contents.split()    # 方法split()，生成一个列表，以空格为分隔符拆分多个部分（包括符号），存储在列表
    num_words = len(words)
    print(filename + '单词数' + str(num_words))
    
# 处理多个文件
def count_words(filenames):
    for filename in filenames:
        try:
            with open('files\\' + filename) as file_object:
                contents = file_object.read()
                
        except FileNotFoundError:
            message = filename + ' file does not exist'
            print(message)
            
        else:     
            words = contents.split()    
            num_words = len(words)
            print('文件' + filename + '单词数' + str(num_words))

filenames = ['snowman.txt', 'pi_digits', '123.txt']
count_words(filenames)

# 失败时一声不吭
try:
    print(5/0)
except ZeroDivisionError:
    pass
    
"""
练习
1、加法计算器，让用户犯错后能够继续输入
2、创建两个文件，cats.txt、dogs.txt。读取文件，打印内容
3、计算一个文件某个单词出现的次数
"""
# 1
nums = input('Please enter the number to sum,use spaces to separate numbers.\n')
num_list = nums.split()
sum = 0
for num in num_list:
    try:
        num = int(num)
    except ValueError:
        print('Please enter int type!')
        break
    else:
        sum += num
        
if sum ==0:
    pass
else:
    print(sum)
    
# 2
filename = input('Enter the name of the file you want to read:')
try:
    with open('files\\' + filename) as cats_object:
        for cat in cats_object:
            print(cat.rstrip())
except FileNotFoundError:
    message = filename + ' file does not exist'
    print(message)
    
# 3
try:
    with open('files\snowman.txt') as snowman_obj:
        snowman = snowman_obj
        count = snowman.lower().count('he')
                
except FileNotFoundError:
    message = filename + ' file does not exist'
    print(message)