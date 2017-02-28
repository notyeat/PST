#！/usr/bin/python
#coding= utf-8

# ToDo: 小管家小溪
import calendar
import time,os
import urllib.request
import json
#color:
red = '\033[01;33m'  # {green:'\033[0;32m',yellow:'\033[0;33m',blue:'\033[0;34m'}
green = '\033[0;32m'
black = '\033[0m'
#想正确显示天气请更改本地的天气代码：http://www.360doc.com/content/14/0322/07/59625_362614659.shtml
weatherId = '101210501' #(这是绍兴的天气ID)
#clock:
clock = time.asctime(time.localtime())
clocklist = clock.split()
year = clocklist[4]
month = clocklist[1]
day = clocklist[2]
switch = {'Jan':1,'Feb':2,'Mar':3,'Apr':'4','May':5,'Jun':6,'Jul':7,'Aug':8,'Sept':9,'Oct':10,'Nov':11,'Dec':12}
month = switch[month]
#weather:
weatherUrl = 'http://weather.51wnl.com/weatherinfo/GetMoreWeather?cityCode='+weatherId+'&weatherType=0'
weatherHtml = urllib.request.urlopen(weatherUrl).read().decode('utf-8') #一定要decode utf-8
weatherJSON = json.JSONDecoder().decode(weatherHtml)
weatherInfo = weatherJSON['weatherinfo']

def caletool():
    cal = calendar.month(int(year),int(month))
    mycale = cal[0:cal.index(day)] + red + cal[cal.index(day):cal.index(day) +len(day)] + black +cal[cal.index(day) +len(day):]
    mycale = mycale[mycale.index('\n'):]
    print(mycale)
def welcome():
    whoami =  os.popen('whoami', mode='r').read()
    print('Hello ! ' + whoami +'我是小管家小溪,今天是' + weatherInfo['date_y'])
    print('今天的天气是' + green + weatherInfo['weather1'] + black + ',温度是' +green+ weatherInfo['temp1'] +black+ ',风向是' +green+ weatherInfo['wind1'] +black)
    print('明天的天气是' + green + weatherInfo['weather2'] + black + ',温度是' +green+ weatherInfo['temp2'] +black+ ',风向是' +green+ weatherInfo['wind2'] +black)
    print('后天的天气是' + green + weatherInfo['weather3'] + black + ',温度是' +green+ weatherInfo['temp3'] +black+ ',风向是' +green+ weatherInfo['wind3'] +black)
    caletool()
welcome()



