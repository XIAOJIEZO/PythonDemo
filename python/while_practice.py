# for循环用于针对集合中的每个元素的一个代码块，而while循环不断地运行，直到指定的条件不满足为止。

# 使用while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
    
# 让用户选择何时退出
message = ''
while message == 'quit':
    message = input('输入任意值继续，输入"quit退出"')
    print('你输入的是' + message)
    