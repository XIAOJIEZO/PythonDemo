"""
    python的标准库模块unittest提供了代码测试工具。单元测试用于核实函数的某个方面没有问题；测试用例是一组单元测试，
这些单元测试一起核实函数在各种情形下的行为都符合要求。
"""
import unittest
from name_functon import get_formatted_name

class NamesTsetCase(unittest.TestCase):
    """测试name_function.py"""

    def setUp(self):
        """创建测试数据"""
        self.firstname = 'tony'
        self.lastname = 'stark'
        self.middle = 'f'

    def test_first_last_name(self):     # 方法名test开始的都会被运行
        """测试是否能够处理Tony Stark这样的姓名"""
        formatted_name = get_formatted_name(self.firstname, self.lastname)
        self.assertEqual(formatted_name, 'Tony Stark')

    def test_first_middle_last_name(self):
        """测试是否能够处理Wide F Wellson这样的姓名"""
        formatted_name = get_formatted_name(self.firstname, self.lastname, self.middle)
        self.assertEqual(formatted_name, 'Tony F Stark')

# unittest.main()不加括号,运行测试
unittest.main