import requests
# from bs4 import BeautifulSoup
#
y=1
for i in range(0,50):
    url = "http://www.gd121.cn/api/yj.json"
    re1 = requests.get(url)
    re1.encoding='utf-8'
    # print(re1)
    re=re1.json()[i]
    # print(re)
    # print(re["PUBLISHDATE"], re["Title"], re["SENDER_CNNAME"], re["CONTACTCODE"])
    if y == 1:
    #CONTACTCODE 地区编码  440100 广州市  440300 深圳市
        if  "4401"  in re["CONTACTCODE"]:
            print(re["PUBLISHDATE"],re["Title"],re["SENDER_CNNAME"],re["CONTACTCODE"])
            # gzyj=re["PUBLISHDATE"],re["Title"],re["SENDER_CNNAME"],re["CONTACTCODE"]


        elif "4403"  in re["CONTACTCODE"]:
            print(re["PUBLISHDATE"],re["Title"],re["SENDER_CNNAME"],re["CONTACTCODE"])

    else:
        print(re["PUBLISHDATE"], re["Title"], re["SENDER_CNNAME"], re["CONTACTCODE"])
#
# #天气预警 返回函数
# def tqyjhs():
#     gzsli=[]
#     szsli=[]
#     url = "http://gd121.cn/api/yj.json"
#     re1 = requests.get(url)
#     for i in range(0, 60):
#         re = re1.json()[i]
#         if "4401" in re["CONTACTCODE"]:
#             # print(re["PUBLISHDATE"], re["Title"], re["SENDER_CNNAME"], re["CONTACTCODE"])
#             gzyj = re["PUBLISHDATE"], re["Title"], re["SENDER_CNNAME"], re["CONTACTCODE"]
#             # print(gzyj)
#             gzsli.append(gzyj)
#
#
#         elif "4403" in re["CONTACTCODE"]:
#             # print(re["PUBLISHDATE"], re["Title"], re["SENDER_CNNAME"], re["CONTACTCODE"])
#             szyj=re["PUBLISHDATE"], re["Title"], re["SENDER_CNNAME"], re["CONTACTCODE"]
#             szsli.append(szyj)
#
#     return gzsli,szsli
#
# def tqyb():
#     url1="http://t.weather.sojson.com/api/weather/city/101280101"
#     url2 = "http://t.weather.sojson.com/api/weather/city/101280601"
#
#     re=requests.get(url1)
#     # print(re.json()["cityInfo"])forecast #0102番禺 0101广州市 深圳市0601 白云0110  天河0109
#     # print(re.json()["cityInfo"])
#     # print(re.json()["data"]["forecast"][0])
#
#     tq0=re.json()["cityInfo"]
#     tq=re.json()["data"]["forecast"][0]
#     tq1=re.json()["data"]
#     # print("当前城市:"+tq0["parent"],tq0["city"])
#     tq00="当前城市:"+tq0["parent"],tq0["city"],"今天"+tq["week"],"最"+tq["high"],"最"+tq["low"]\
#         ,"天气类型:"+tq["type"],tq["fx"],tq["fl"],"温馨提示："+tq["notice"]\
#         ,"湿度:"+tq1["shidu"],"空气质量:"+tq1["quality"],"感冒指数:"+tq1["ganmao"],"天气更新时间:"+tq0["updateTime"]
#     print(tq00)
#
#
#
# #获取天气数据、返回值
# def tqyp():
#     url1="http://t.weather.sojson.com/api/weather/city/101280102"
#     url2 = "http://t.weather.sojson.com/api/weather/city/101280601"
#     url3="http://t.weather.sojson.com/api/weather/city/101280110"
#     url4="http://t.weather.sojson.com/api/weather/city/101280109"
#
#     re=requests.get(url1)  #番禺
#     # print(re.json()["cityInfo"])forecast #0102番禺 0101广州市 深圳市0601  白云0110  天河0109
#     # print(re.json()["cityInfo"])
#     # print(re.json()["data"]["forecast"][0])
#
#     tq0 = re.json()["cityInfo"]
#     tq = re.json()["data"]["forecast"][0]
#     tq1 = re.json()["data"]
#     # print("当前城市:"+tq0["parent"],tq0["city"])
#     gzpy = "您当前城市:" + tq0["parent"], tq0["city"], "今天" + tq["week"], "最" + tq["high"], "最" + tq["low"] \
#         , "天气类型:" + tq["type"], tq["fx"], tq["fl"],"湿度:"+tq1["shidu"],"空气质量:"+ tq1["quality"],\
#           "温馨提示：" + tq["notice"],"天气更新时间:" + tq0["updateTime"]
#
#     # tq0=re.json()["cityInfo"]
#     # # print("当前城市:"+tq0["parent"],tq0["city"])
#     # tq00="当前城市:"+tq0["parent"],tq0["city"],"今天"+tq["week"],"最"+tq["high"],"最"+tq["low"]\
#     #     ,"天气类型:"+tq["type"],tq["fx"],tq["fl"],"温馨提示："+tq["notice"]\
#     #     ,"湿度:"+tq1["shidu"],"空气质量:"+tq1["quality"],"感冒指数:"+tq1["ganmao"]
#     #
#     # tq=re.json()["data"]["forecast"][0]
#     # # print("今天"+tq["week"],"最"+tq["high"],"最"+tq["low"],"天气类型:"+tq["type"],tq["fx"],tq["fl"],"温馨提示："+tq["notice"])
#     # tq01="今天"+tq["week"],"最"+tq["high"],"最"+tq["low"],"天气类型:"+tq["type"],tq["fx"],tq["fl"],"温馨提示："+tq["notice"]
#     #
#     # tq1=re.json()["data"]
#     # # print("湿度:"+tq1["shidu"],"空气质量:"+tq1["quality"],"感冒指数:"+tq1["ganmao"])
#     # tq02="湿度:"+tq1["shidu"],"空气质量:"+tq1["quality"],"感冒指数:"+tq1["ganmao"]
#
#     re=requests.get(url2)   #深圳
#     tq0 = re.json()["cityInfo"]
#     tq = re.json()["data"]["forecast"][0]
#     tq1 = re.json()["data"]
#     szs = "您当前城市:" + tq0["parent"], tq0["city"], "今天" + tq["week"], "最" + tq["high"], "最" + tq["low"] \
#         , "天气类型:" + tq["type"], tq["fx"], tq["fl"],"湿度:"+tq1["shidu"],"空气质量:"+ tq1["quality"],\
#           "温馨提示：" + tq["notice"],"天气更新时间:" + tq0["updateTime"]
#
#     re=requests.get(url3)   #广州白云区
#     tq0 = re.json()["cityInfo"]
#     tq = re.json()["data"]["forecast"][0]
#     tq1 = re.json()["data"]
#     gzby = "您工作地为:" + tq0["parent"], tq0["city"], "今天" + tq["week"], "最" + tq["high"], "最" + tq["low"] \
#         , "天气类型:" + tq["type"], tq["fx"], tq["fl"],"湿度:"+tq1["shidu"],"空气质量:"+ tq1["quality"],\
#           "温馨提示：" + tq["notice"],"天气更新时间:" + tq0["updateTime"]
#
#     re=requests.get(url4)   #广州天河区
#     tq0 = re.json()["cityInfo"]
#     tq = re.json()["data"]["forecast"][0]
#     tq1 = re.json()["data"]
#     gzth = "您工作地为:" + tq0["parent"], tq0["city"], "今天" + tq["week"], "最" + tq["high"], "最" + tq["low"] \
#         , "天气类型:" + tq["type"], tq["fx"], tq["fl"],"湿度:"+tq1["shidu"],"空气质量:"+ tq1["quality"],\
#           "温馨提示：" + tq["notice"],"天气更新时间:" + tq0["updateTime"]
#
#
#
#     return szs,gzpy,gzby,gzth
# szs,gzpy,gzby,gzth=tqyp()
#
# print(szs)
# print(gzpy)
# print(gzby)
# print(gzth)
#
#
#
# #预警信息广州
# def gzyj():
#     url = "http://gd121.cn/api/yj.json"
#     re1 = requests.get(url)
#     # print(re1.json()[0])
#     gzlis=[]
#     for i in range(0,60):
#         re = re1.json()[i]
#         # print(re1.json()[0])
#         # CONTACTCODE 地区编码  440100 广州市  440300 深圳市  re["CONTACTCODE"]打印气象局名称
#         if "4401" in re["CONTACTCODE"]:
#             gz=(re["PUBLISHDATE"], re["Title"], re["SENDER_CNNAME"])
#             gzlis.append(gz)
#     return gzlis
# #预警信息深圳
# def szyj():
#     url = "http://gd121.cn/api/yj.json"
#     re1 = requests.get(url)
#     # print(re1.json()[0])
#     szlis=[]
#     for i in range(0,60):
#         re = re1.json()[i]
#         # print(re1.json()[0])
#         # CONTACTCODE 地区编码  440100 广州市  440300 深圳市
#         if "4403" in re["CONTACTCODE"]:
#             sz=(re["PUBLISHDATE"], re["Title"], re["SENDER_CNNAME"])
#             print(sz)
#             szlis.append(sz)
#     return szlis
# gzlis=gzyj()
# szlis=szyj()
# # print(gzlis)
# # print(szlis)
#
#
#
#
# # r= requests.get("http://gd121.cn/yj/yj_search.shtml")
# # print(r.encoding)
# # print(r.apparent_encoding)
# # r.encoding=r.apparent_encoding
# # # print(r.text)
#
# # soup = BeautifulSoup(r.text,features='html.parser')
# #
# # aa = soup.find(class_='ListTitle')
# # print(aa)
# #
# # a = soup.find(target="_blank")
# # print(a)
# #
# #
# # aa1=soup.find_all("a")
# # print(aa1)
# # for i in aa1:
# #     print(i)