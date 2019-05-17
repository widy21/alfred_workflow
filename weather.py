#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'hua.xiao'

# -*- coding:utf-8 -*-
import json,sys
from datetime import datetime
from workflow import Workflow, web

reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')

#这个是和风天气的API key,替换成你自己的就行
API_KEY = '你的API_KEY'

#返回某日是星期几
def the_day(num):
    week = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
    return week[num]

def main(wf):
    url = 'https://free-api.heweather.com/x3/weather?cityid=CN101010100&key=' + API_KEY
    #这里用了deanishe 的框架里面的web模块来请求页面,web模块类似requests库
    r = web.get(url=url)
    r.raise_for_status()
    resp = r.text
    data = json.loads(resp)

    d = data['HeWeather data service 3.0'][0]
    city = d['basic']['city']

    #获取一周内的数据
    for n in range(0,7):
        day = d['daily_forecast'][n]
    #把API获取的天气、温度、风力等信息拼接成 alfred条目的标题、副标题
        title = city + '\t' + the_day(datetime.weekday(datetime.strptime(day['date'],'%Y-%m-%d')))+ '\t' +day['cond']['txt_d']
        subtitle = '白天 {weather_day}|' \
                   '夜间 {weather_night} |' \
                   ' {tmp_low}~{tmp_high}摄氏度|' \
                   ' {wind_dir} {wind_sc}'.format(
            weather_day = day['cond']['txt_d'],
            weather_night = day['cond']['txt_n'],
            tmp_high = day['tmp']['max'],
            tmp_low = day['tmp']['min'],
            wind_sc = day['wind']['sc'],
            wind_dir = day['wind']['dir']
        )
    #向alfred添加条目,传标题、副标题、图片路径(图片直接用的和风天气提供的天气图,每个图片的命名对应天气状态码)
        wf.add_item(title=title,subtitle=subtitle,icon='images/{code}.png'.format(code = day['cond']['code_d']))

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))