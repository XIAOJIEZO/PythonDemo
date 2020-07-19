# 函数，函数是带名字的代码块用于完成具体的工作
# 定义一个函数
def display_hello(name):    #
    """显示简单的问候语"""
    print('hello,' + name)

display_hello('Jack')

# 形参和实参：在前面的例子中，name是一个形参（函数完成其工作所需要的信息）；在代码display_hello('Jack')中，值“Jack”是一个实参

"""
练习：
1、编写一个display_message()函数，打印一个句子。指出你在本章学的是什么
2、编写一个favorite_book()函数，其中包含一个名为title的形参，打印一条信息，指出你喜欢的书籍
"""
# 1
def display_message():      # 可以不传参
    print('本章学习函数')

display_message()

# 2
def favorite_book(book_name):
    print('我最喜欢的书籍是《' + book_name + '》')

favorite_book('海地两万里')

# 传递参数：位置实参（位置实参的顺序很重要）
def favorite_comic(name, comic_name):
    print(name + '最喜欢的动漫是“' + comic_name + '”')

favorite_comic('Logen', 'Naruto')

# 使用函数while循环
active = True
while active:
    name = input('请输入人名：')
    comic_name = input('请输入' + name + '喜欢的动漫：')
    favorite_comic(name, comic_name)

    active = input('输入“quit”退出')
    if active == 'quit':
        active = False

# 关键字实参：关键之实参是传递给函数的名称-值对。直接在实参中将名称和值关联起来（不需要按顺序）
favorite_comic(comic_name = '狐妖', name = 'peter')   # 务必准确指定函数定义中的形参名

# 默认值：可给每个形参指定默认值
def favorite_fruits(name, fruit_name = '苹果'):
    """显示最喜欢的额水果"""
    print(name + '最喜欢的水果是' + fruit_name)

favorite_fruits('冯宝宝')
favorite_fruits('张楚岚', '香蕉')    # 实参可覆盖形参的默认值

# 返回值：函数并非直接显示输出，相反，它可以处理一些数据，并返回一个或一组值
def get_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name

full_name = get_name('tony', 'stark')   # 将返回值复制给full_name
print(full_name)

# 让实参变为可选的：有时候，需要让实参变成可选的
# 比如有的人的姓名有中间名，有的人没有，就需要让中间名变成可选的
def get_names(first_name, last_name, middle_name = ''):
    if middle_name:     # 非空字符串解读为True
        full_name = first_name + ' ' + middle_name + '' +last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

full_name = get_names('tony', 'stark')
print(full_name)

full_name = ('wade', 'wellson', 'f')    # 为什么输出的是元组
print(full_name)

# 返回字典：函数可返回任何类型的值，包含列表字典等
def build_persion(first_name, last_name):
    persion = {'first': first_name, 'last': last_name}
    return persion

persion = build_persion('冯', '宝宝')
print(persion)

"""
练习
1、编写函数，创建一个描述音乐专辑的字典。包含歌手名字、专辑名，返回一个包含这两项信息的字典
    添加一个可选形参，存储专辑包含的歌曲数
    使用while循环，让用户来输入这些信息
"""
def make_album(singer, album, num = ''):
    if num:
        singer = {'singer': singer, 'album': album, 'num': num}
    else:
        singer = {'singer': singer, 'album': album}
    return singer

def get_singer():   # 定义get_singer()函数调用make_album()函数
    act = True
    while act:
        singer = input('请输入歌手姓名：')
        album = input('请输入专辑：')
        num = input('请输入歌曲数量（若无相关信息请输入n）：')
        if num == 'n':
            singer_info = make_album(singer, album)
        else:
            singer_info = make_album(singer, album, num)
        print(singer_info)

        act = input('输入“quit”退出')
        if act == 'quit':
            act = False

get_singer()    # 调用get_singer() 函数