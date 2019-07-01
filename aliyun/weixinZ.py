# coding: utf-8
from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
import json
logger = logging.getLogger(__name__)
bot = Bot()#获取二维码


#获取天气数据、返回值
def tqyp():
    url1="http://t.weather.sojson.com/api/weather/city/101280102"
    url2 = "http://t.weather.sojson.com/api/weather/city/101280601"
    url3="http://t.weather.sojson.com/api/weather/city/101280110"
    url4="http://t.weather.sojson.com/api/weather/city/101280109"

    re=requests.get(url1)  #番禺
    # print(re.json()["cityInfo"])forecast #0102番禺 0101广州市 深圳市0601  白云0110  天河0109
    tq0 = re.json()["cityInfo"]
    tq = re.json()["data"]["forecast"][0]
    tq1 = re.json()["data"]
    # print("当前城市:"+tq0["parent"],tq0["city"])
    gzpy = "您当前城市:" + tq0["parent"], tq0["city"], "今天" + tq["week"], "最" + tq["high"], "最" + tq["low"] \
        , "天气类型:" + tq["type"], tq["fx"], tq["fl"],"湿度:"+tq1["shidu"],"空气质量:"+ tq1["quality"],\
          "温馨提示：" + tq["notice"],"天气更新时间:" + tq0["updateTime"]

    re=requests.get(url2)   #深圳
    tq0 = re.json()["cityInfo"]
    tq = re.json()["data"]["forecast"][0]
    tq1 = re.json()["data"]
    szs = "您当前城市:" + tq0["parent"], tq0["city"], "今天" + tq["week"], "最" + tq["high"], "最" + tq["low"] \
        , "天气类型:" + tq["type"], tq["fx"], tq["fl"],"湿度:"+tq1["shidu"],"空气质量:"+ tq1["quality"],\
          "温馨提示：" + tq["notice"],"天气更新时间:" + tq0["updateTime"]

    re=requests.get(url3)   #广州白云区
    tq0 = re.json()["cityInfo"]
    tq = re.json()["data"]["forecast"][0]
    tq1 = re.json()["data"]
    gzby = "您工作地为:" + tq0["parent"], tq0["city"], "今天" + tq["week"], "最" + tq["high"], "最" + tq["low"] \
        , "天气类型:" + tq["type"], tq["fx"], tq["fl"],"湿度:"+tq1["shidu"],"空气质量:"+ tq1["quality"],\
          "温馨提示：" + tq["notice"],"天气更新时间:" + tq0["updateTime"]

    re=requests.get(url4)   #广州天河区
    tq0 = re.json()["cityInfo"]
    tq = re.json()["data"]["forecast"][0]
    tq1 = re.json()["data"]
    gzth = "您工作地为:" + tq0["parent"], tq0["city"], "今天" + tq["week"], "最" + tq["high"], "最" + tq["low"] \
        , "天气类型:" + tq["type"], tq["fx"], tq["fl"],"湿度:"+tq1["shidu"],"空气质量:"+ tq1["quality"],\
          "温馨提示：" + tq["notice"],"天气更新时间:" + tq0["updateTime"]

    return szs,gzpy,gzby,gzth
szs,gzpy,gzby,gzth=tqyp()

#获取生活指数信息
def shzs():
    #广州生活指数
    ur1="http://d1.weather.com.cn/zs_index/101280101.html?_=1561449792583"
    # re=requests.get(ur1)

    headers = {'Accept':'*/*',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
               'Host': 'd1.weather.com.cn',
                'Referer':'http://www.weather.com.cn/life/',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3641.400 QQBrowser/10.4.3284.400',
               }
    r = requests.get(ur1,headers=headers,verify=False)
    r.encoding='utf-8'
    # print(r.text)
    # print(type(r.text))
    jd = json.loads(r.text.strip('var dataZS='))    #移除改var data=将其变为json数据
    # print(jd)
    zs=jd['zs']
    ssd=zs['co_name']+':'  #舒适度
    cy=zs['ct_name']+':'  #穿衣
    fs=zs['fs_name']+':'  #防晒
    gm=zs['gm_name']+':'  #感冒
    ls=zs['ls_name']+':'  #晾晒指数
    xq=zs['xq_name']+':'  #心情
    ys=zs['ys_name']+':'  #雨伞
    zs1=zs['zs_name']+':'  #中暑
    gzzs = jd['cn'], zs1, zs['zs_des_s'], fs, zs['fs_hint'], ls, zs['ls_des_s'], cy, zs['ct_hint'], \
           zs['ct_des_s'], gm, zs['gm_des_s'], ssd, zs['co_des_s'], ys, zs['ys_hint'], zs['ys_des_s']

    #深圳生活指数
    ur2='http://d1.weather.com.cn/zs_index/101280601.html?_=1561527678118'
    r2 = requests.get(ur2, headers=headers, verify=False)
    r2.encoding = 'utf-8'
    # print(r2.text)
    jd1 = json.loads(r2.text.strip('var dataZS='))
    # print(jd1)
    zs = jd1['zs']
    ssd = zs['co_name'] + ':'  # 舒适度
    cy = zs['ct_name'] + ':'  # 穿衣
    fs = zs['fs_name'] + ':'  # 防晒
    gm = zs['gm_name'] + ':'  # 感冒
    ls = zs['ls_name'] + ':'  # 晾晒指数
    xq = zs['xq_name'] + ':'  # 心情
    ys = zs['ys_name'] + ':'  # 雨伞
    zs1 = zs['zs_name'] + ':'  # 中暑
    szzs = jd1['cn'], zs1, zs['zs_des_s'], fs, zs['fs_hint'], ls, zs['ls_des_s'], cy, zs['ct_hint'], \
           zs['ct_des_s'], gm, zs['gm_des_s'], ssd, zs['co_des_s'], ys, zs['ys_hint'], zs['ys_des_s']

    return szzs, gzzs
szzs, gzzs = shzs()

#获取微信好友列表、选择好友、天气信息发送
def send_news():
    szs, gzpy, gzby, gzth = tqyp()
    szzs, gzzs = shzs()
    friends =bot.friends()#获取微信好友
    for i in friends:#循环好友
        # print(i.raw)
        e=i.raw
        e1=e['NickName']     #昵称
        e2=e['RemarkName']   #备注
        tq="天气信息:"
        # print('昵称:'+e1, '备注:'+e2, e['Signature'])
        if e2=="晓军":   #判断是否发送给谁
            aa = bot.friends().search(e2)[0]
            aa.send("天气预警信息推送，请注意查收:")
            aa.send(gzpy)  # 发送消息
            aa.send(gzby)
            aa.send(szs)
            aa.send(gzzs)
            # aa.send('晚安！')
            aa.send('以上信息均由微信自动推送！')
            print(aa)
        elif e2== "大兄弟":
            aa=bot.friends().search(e2)[0]#填入发送人名
            aa.send("天气预警信息推送，请注意查收:")
            aa.send(gzpy)#发送消息
            aa.send(gzth)
            aa.send(gzzs)
            aa.send('以上信息均由微信自动推送！')
            print(aa)
        # elif e2 == "李俊":
        #     aa = bot.friends().search(e2)[0]  # 填入发送人名
        #     aa.send("亲，天气预警信息推送，请注意查收:")
        #     aa.send(szs)  # 发送消息            aa.send(tq01)
        #     aa.send(szzs)
        #     # aa.send('爱你哟，么么哒！')
        #     aa.send('以上信息由怀军自动推送！')
        #     print(aa)
        # elif e2 == "某人":
        #     aa = bot.friends().search(e2)[0]  # 填入发送人名
        #     aa.send("亲，天气预警信息推送，请注意查收:")
        #     aa.send(szs)  # 发送消息            aa.send(tq01)
        #     aa.send(szzs)
        #     aa.send('爱你哟，么么哒！')
        #     # aa.send('以上信息均由微信自动推送！')
        #     print(aa)


        #每86400秒（1天），发送1次
            t = Timer(28800,send_news)
            t.start()
if __name__ == "__main__":
    send_news()