# coding: utf-8 ##泉后掌柜销售素材与培训接口从表格获取URL参数
import requests,json,time
from bs4 import BeautifulSoup
import xlrd
def qhouzgui():
    workbook = xlrd.open_workbook('../testdata/jiekou.xlsx')  #表格路径
    table = workbook.sheets()[0]   #第一个表[0]
    zguilist=[]
    for jj in range(1,table.nrows):
        a = table.cell(jj, 0).value  ##接口名称
        b = table.cell(jj, 1).value  ##域名
        c = table.cell(jj, 2).value  ## 接口地址
        d = table.cell(jj, 3).value  ##接口参数
        e = table.cell(jj, 4).value
        f = table.cell(jj, 5).value
        g = table.cell(jj, 6).value
        h = table.cell(jj, 7).value
        i = table.cell(jj, 8).value
        j = table.cell(jj, 9).value
        #可以返回单个值，也可以返回数组
        data={'apiname':a,'apiurl':c,'key':d,'value':e,'key1':f,'value1':g,'key2':h,'value2':i,'check':j}
        zguilist.append(data)
    return zguilist

# zguilist=qhouzgui()
# print(zguilist[0])