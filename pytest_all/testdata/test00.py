# coding:utf-8
import pytest

'''
assert x == a  # 是否相等
assert x != a  # 是否不相等
assert x is a  # 是否是同一内存地址
assert x in a  # a 是否包含 x
assert x not in a  # a 是否不包含 x
assert x > a  # 是否大于 a
assert x < a  # 是否小于 a
assert isinstance(x, dict)  # x 是否是 dict 类型

'''
# 类和方法
print('类和方法,执行顺序')
def setup_module():
    print("setup_module：整个.py模块只执行一次")
    print("比如：所有用例开始前只打开一次浏览器")

def teardown_module():
    print("teardown_module：整个.py模块只执行一次")
    print("比如：所有用例结束只最后关闭浏览器")

def setup_function():
    print("setup_function：每个用例开始前都会执行")

def teardown_function():
    print("teardown_function：每个用例结束前都会执行")

def test_one():
    print("正在执行----test_one")
    x = "this"
    assert 'h' in x

def test_two():
    print("正在执行----test_two")
    x = "hello"
    assert hasattr(x, 'check')

class TestCase():

    def setup_class(self):
        print("setup_class：所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之前")

    def test_three(self):
        print("正在执行----test_three")
        x = "this"
        assert 'h' in x

    def test_four(self):
        print("正在执行----test_four")
        x = "hello"
        assert hasattr(x, 'check')

if __name__ == "__main__":
    pytest.main(["-s","-q", "test00.py"])