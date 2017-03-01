#！/usr/bin/python
#coding= utf-8

#################################
#           notyeat             #
#          小管家小溪             #
#################################
import calendar
import time,os
import urllib.request
import json
#color:
fontColor =  {'red':'\033[01;33m','black':'\033[0m','green':'\033[0;32m','yellow':'\033[0;33m','blue':'\033[0;34m'}
calendarColor   = fontColor['yellow']
weatherColor    = fontColor['green']
blackColor      = fontColor['black']
#想正确显示天气请更改本地的天气代码：http://www.360doc.com/content/14/0322/07/59625_362614659.shtml
weatherId = '101210501' #(这是绍兴的天气ID)
#clock:
clock = time.asctime(time.localtime()).split()
year = clock[4]
month = clock[1]
day = clock[2]
monthSwitch = {'Jan':1,'Feb':2,'Mar':3,'Apr':'4','May':5,'Jun':6,'Jul':7,'Aug':8,'Sept':9,'Oct':10,'Nov':11,'Dec':12}
month = monthSwitch[month]
#weather:
weatherUrl = 'http://weather.51wnl.com/weatherinfo/GetMoreWeather?cityCode='+weatherId+'&weatherType=0'
weatherHtml = urllib.request.urlopen(weatherUrl).read().decode('utf-8') #一定要decode utf-8
weatherJSON = json.JSONDecoder().decode(weatherHtml)
weatherInfo = weatherJSON['weatherinfo']

def caletool():     #输出日历
    cal = calendar.month(int(year),int(month))
    cal = cal[cal.index('\n'):]     #防止自动输出的年份影响下面字体颜色的输出
    mycale = cal[0:cal.index(day)] + calendarColor + cal[cal.index(day):cal.index(day) +len(day)] + blackColor +cal[cal.index(day) +len(day):]
    print(mycale)


def welcome():      #天气模块
    whoami =  os.popen('whoami', mode='r').read()
    print('Hello ! ' + whoami +'我是小管家小溪,今天是' + weatherInfo['date_y'])
    chinaDay = ['今天', '明天', '后天']
    for x in range(0, 3):
        i = str(x + 1)
        print(chinaDay[x] + '的天气是' +weatherColor+ weatherInfo['weather'+i] +blackColor+ ',温度是' +weatherColor+
              weatherInfo['temp'+i] +blackColor+ ',风向是' +weatherColor+ weatherInfo['wind'+i] +blackColor)
    caletool()

if __name__ == '__main__':
    welcome()
