# for循环用于针对集合中的每个元素的一个代码块，而while循环不断地运行，直到指定的条件不满足为止。

# 使用while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
    
# 让用户选择何时退出
message = ''
while message != 'quit':
    message = input('输入任意值继续，输入”quit“退出：')
    print('你输入的是：' + message)

"""
使用标志：在前面的实例中，我们让程序在满足指定条件时就执行特定的任务。但在更复杂的程序中，很多不同的事情都会导致程序停止运行。
例如，在游戏中，玩家的飞船毁了或者保护城市被摧毁，都会导致游戏结束。如果结束条件很多时，在while语句中检查所有这些条件，将会复杂又困难。
这时，我们定义一个变量用于判断游戏是否结束，这个变量就成为 标志，充当了程序的交通信号灯
"""
prompt = '\nTell me something, and i will repeat it back to you:'
prompt += "'\nEnter' 'quit' to end the program."
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

"""
使用break退出循环：
    要退出while循环，不再运行余下的代码，也不管条件测试的结果如何，可使用break语句。
    break用具控制程序流程，可使用它来控制哪些代码将执行，哪些代码不执行，从而按程序的要求执行你要的代码。
例如：让一个用户指出他去过哪些地方。在程序中，我们可以用用户数去“quit”后立即退出while循环。
"""
prompt = "\n请输入你去过哪些城市："
prompt += "\n（输入“quit”后退出程序）。"
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print('您去过的城市是：' + city)

# 在任何循环中都可以使用break语句，for循环也是如此

"""
在循环中使用continue：
    要返回到循环开头，并根据条件结果觉得是否继续执行循环，可使用continue语句。
    continue不会退出循环，当条件满足，它会跳过此次执行
例如：1~10如果是偶数便不打印
"""
nums = 0
while nums < 10:
    nums += 1
    if nums % 2 == 0:
        continue
    print(nums)     # 不需要else时，可省略

"""
使用while循环来处理列表和字典：for循环是一种遍历列表的有效方式，但在for循环中不应该修改列表，否则将导致Python难以跟踪其中的元素。要在遍历列表额同时对其进行修改，可使用while循环。通过将while循环同列表和字典结合起来使用，可收集、存储兵组织大量输入，提供以后查看和显示。
"""

# 在列表之间移动元素：假设有一个列表，包含新注册但未验证的用户，验证这些用户后，如何将他们移动到已验证列表
unconfirmation_users = ['白切鸡', '王富贵', '杨一叹']
confirmation_users = []
while unconfirmation_users:
    user = unconfirmation_users.pop()
    print('\n检测到未验证用户' + user + '，将其添加至已验证列表！')
    confirmation_users.append(user)
print('目前已验证用户：')
for confirmation_user in confirmation_users:
    print('\t' + confirmation_user)

# 删除包含特定值的左右元素：新建列表pets，while循环删除cat
pets = ['dog', 'cat', 'pig', 'cat', 'cat', 'dog']
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# 使用用户输入来填充字典
# 调查用户喜欢的动漫人物是什么，输入yes继续，输入no调查结束
favorite_role = {}
active = True
while active:
    name = input('请输入被调查者姓名：')
    role = input('请输入' + name + '喜欢的动漫人物：')
    favorite_role[name] = role
    
    active = input('调查是否继续？（no退出|任意值继续）')
    if active == 'no':
        active = False
for name, role in favorite_role.items():
    print(name + '最喜欢的动漫人物是' + role + '！')
    