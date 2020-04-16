# -*- coding:utf-8 -*-
import werobot, requests, pymysql
import re
from bs4 import BeautifulSoup

robot = werobot.WeRoBot(token='yanhuaijun')


# 全部回复
# @robot.handler
# def echo(message):
#    return 'Hello World!'

# 你发什么我回复什么
# @robot.text
# def echo(message):
#   return message.content

# 连接数据库
def my_db(msg):
    conn = pymysql.Connect(
        host='47.106.143.70',  ##mysql服务器地址
        port=3306,  ##mysql服务器端口号
        user='666',  ##用户名
        passwd='123456',  ##密码  J5p";~OVazNl%y)?
        db='666',  ##数据库名
        charset='utf8',  ##连接编码
    )
    sq1 = 'SELECT * FROM cityid WHERE city_name LIKE "%s"' % ('%' + msg + '%')
    # cursor = con.cursor()  # 获取游标
    # sql = 'select * from my_user where username="%s";' % username
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(sq1)
    uer = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return uer


# 通过数据库返回的城市编码查询天气信息
def tqyb(uer):
    url1 = "http://t.weather.sojson.com/api/weather/city/" + uer['city_code']
    re = requests.get(url1)
    tq0 = re.json()["cityInfo"]
    tq = re.json()["data"]["forecast"][0]
    tq1 = re.json()["data"]
    # print("当前城市:"+tq0["parent"],tq0["city"])
    tq00 = "当前城市:" + tq0["parent"], tq0["city"], "今天" + tq["week"], "最" + tq["high"], "最" + tq["low"] \
        , "天气类型:" + tq["type"], tq["fx"], tq["fl"], "温馨提示：" + tq["notice"] \
        , "湿度:" + tq1["shidu"], "空气质量:" + tq1["quality"], "感冒指数:" + tq1["ganmao"], "天气更新时间:" + tq0["updateTime"]
    # print(tq00)
    return str(tq00)


# 百科函数
def baike(baikename):
    url = 'http://www.baike.com/wiki/' + baikename
    rebaike = requests.get(url)
    print(rebaike)
    soup1 = BeautifulSoup(rebaike.text, features='html.parser')
    s1 = soup1.find_all(attrs={'id': 'originalsummarycontent'})
    # print(s1[0]['value'])
    baikere = s1[0]['value']
    return baikere


@robot.subscribe
def subscribe(message):
    return "终于等到你，还好我没放弃！"


@robot.image
def img(message):
    # print(type(message))
    # print(type(message.img))
    # return message.img
    return "别闹，还是发文字吧!"


@robot.voice
def voice(message):
    return "有什么心里话，可以微我。"


@robot.video
def video(message):
    return "抱歉我看不懂视频！可以给我主人发哦"


@robot.link
def link(message):
    return "抱歉我打不开链接，你可以告诉我里面的故事啊！"


@robot.unknown
def unknown(message):
    return "可以好好说话吗？"


# 匹配什么发什么
@robot.text
def echo(message):
    # try:
    # 提取消息
    msg1 = message.content
    print(msg1)
    msg = msg1[0:2]
    uer = my_db(msg)
    # print(tq00)
    # return tq00
    if 'tq'in msg1 or '区号'in msg1 or '编码' in msg1:
        # 如果数据库返回城市信息，就获取城市天气信息并且返回
        if uer:
            tq00 = tqyb(uer)
            if '区号' in msg1:
                if uer['area_code'] == 'NULL':
                    return '客官别急，数据正在补齐中....请谅解'
                else:
                    qh = msg + '的区号为:' + uer['area_code']
                    return qh
            elif '编码' in msg1:
                if uer['area_code'] == 'NULL':
                    return '客官别急，数据正在补齐中....请谅解'
                else:
                    bm = msg + '邮政编码为:' + uer['post_code']
                    return bm
            else:
                print(uer['city_code'])
                return tq00
        else:
            try:
                baikename = msg1
                baikere = baike(baikename)
                return baikere
            except:
                return '噢，淘气，请换一个姿势！\n天气查询输入：广州tq\n区号查询输入：广州区号\n邮政编码查询输入：广州编码'
    # 解析消息
    elif re.compile(".*?你好.*?").match(msg1) or \
            re.compile(".*?嗨.*?").match(msg1) or \
            re.compile(".*?哈喽.*?").match(msg1) or \
            re.compile(".*?hello.*?").match(msg1) or \
            re.compile(".*?hi.*?").match(msg1) or \
            re.compile(".*?who are you.*?").match(msg1) or \
            re.compile(".*?你是谁.*?").match(msg1) or \
            re.compile(".*?你的名字.*?").match(msg1) or \
            re.compile(".*?什么名字.*?").match(msg1):
        return "哟~客官你终于来了！\n我是江湖百晓生!\n有什么能帮您的吗？\n我可以为你提供天气查询哦！\n例如输入：深圳tq"
    elif re.compile(".*?怀军.*?").match(msg1):
        return '来者何人，竟敢直呼我的大名！'
    elif re.compile(".*?厉害.*?").match(msg1):
        return '承让承让 (๑•̀ㅂ•́)ﻭ✧'
    elif re.compile(".*?想你.*?").match(msg1):
        return '我也想你'
    elif re.compile(".*?miss you.*?").match(msg1):
        return 'I miss you,too'
    elif re.compile(".*?爱你.*?").match(msg1):
        return '害羞，你爱我什么？'
    elif re.compile(".*?我爱你.*?").match(msg1):
        return '我也爱你'
    elif re.compile(".*?love you.*?").match(msg1):
        return 'I love you,too'
    elif re.compile(".*?美女.*?").match(msg1):
        return '我是男生哦♂'
    elif re.compile(".*?帅哥.*?").match(msg1):
        return '谢谢夸奖 (๑•̀ㅂ•́)ﻭ✧'
    elif re.compile(".*?傻逼.*?").match(msg1):
        return '说你自己吗？'
    elif re.compile(".*?下班.*?").match(msg1):
        return '下班了是不是很开心呀'
    else:
        try:
            baikename = msg1
            baikere = baike(baikename)
            return baikere
        except:
            return '噢，淘气' \
                   '，请换一个姿势！\n天气查询输入：广州tq\n区号查询输入：广州区号\n邮政编码查询输入：广州编码'


# except Exception as e:
# print (e)

@robot.key_click("abort")
def abort():
    return "I'm a robot"


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80

robot.run()
