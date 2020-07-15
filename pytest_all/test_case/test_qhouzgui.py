# coding:utf-8
from public.get_data import *
import requests,pytest

url='http://wx4e4f7b3ce72d4d42.ttwx.quanhoo.com'
openId='38b108ec9d0dd33e50647a0988e95f58'
#pytest  mark  参数化
@pytest.mark.parametrize('value', qhouzgui())
def test_qhouzgui(value):
    a=value['apiname']
    print(a)
    c=value['apiurl']
    data={'openId':openId,value['key1']:value['value1'],value['key2']:value['value2']}
    j=value['check']
    re = requests.get(url + c, params=data)  # 如果表格直接传{a:b,c:d}参数，应该转换 params=eval({a:b,c:d})
    if re.status_code == 200:
        # print(type(relogin.json()))
        re = (re.json())
        assert j in str(re)

@pytest.mark.parametrize('value', qhouzgui())
def test_qhouzgui1(value):
    a=value['apiname']
    c=value['apiurl']
    data={'openId':openId,value['key1']:value['value1'],value['key2']:value['value2']}
    j=value['check']
    re = requests.get(url + c, params=data)  # 如果表格直接传{a:b,c:d}参数，应该转换 params=eval({a:b,c:d})
    if re.status_code == 200:
        # print(type(relogin.json()))
        re = (re.json())
        assert j in str(re)