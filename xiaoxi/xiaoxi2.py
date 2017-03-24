#!/usr/bin/python3
#coding= utf-8

#################################
#           notyeat             #
#          小管家小溪 V2.1        #
#################################
import calendar
import time,os
import urllib.request
import json
import getpass
import datetime
#secret modle
passwd = '1/2sb'


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

whoami =  os.popen('whoami', mode='r').read()
Dividing_line = '-----------------------------------------------'
def caletool():     #输出日历
    cal = calendar.month(int(year),int(month))
    cal = cal[cal.index('\n'):]     #防止自动输出的年份影响下面字体颜色的输出
    mycale = cal[0:cal.index(day)] + calendarColor + cal[cal.index(day):cal.index(day) +len(day)] + blackColor +cal[cal.index(day) +len(day):]
    print(mycale)


def welcome():      #天气模块
    chinaDay = ['今天', '明天', '后天']
    for x in range(0, 5):
        i = str(x + 1)
        if x < 3:
            toDay = chinaDay[x]
        else:
            toDay = str((int(day) + x)) + '号'
        print(toDay + '的天气是' +weatherColor+ weatherInfo['weather'+i] +blackColor+ ',温度是' +weatherColor+
              weatherInfo['temp'+i] +blackColor+ ',风向是' +weatherColor+ weatherInfo['wind'+i] +blackColor)
#    safe()
def safe():
    userId = whoami.strip('\n')
    filename = '/var/log/xiaoxi.log'
    toDay =str(year)+'年' + str(month)+'月' + str((int(day))) + '号' + clock[3]
    log = toDay + ',以ID:'+userId+'登陆这台电脑\n'
    if os.path.exists(filename):
        f = open(filename,'a')
        f.write(log)
        f.close()
    else:
        f = open(filename,'w')
        f.write(log)
        f.close()
    secret = getpass.getpass('')
    if secret == passwd :
        f = open(filename)
        for x in f.readlines():
            x = x.strip('\n')
            print(x)
        f.close()

def Character_painting():
    character = {
        'sun': '''
                 *                     . :
                        \     |   /
                 .          ____            .
                     ---   /    \   ---     .
                  .       | ~  ~ |        .
                     ---   \__O_/   ---
                ...       /       \
                              |
        ''',
        'rain': '''
                ,‘’‘╭⌒╮⌒╮.’,‘’‘,,',.'',,','',.
                 ╱◥██◣''o',‘’‘,,',.''.'',,',.
                ｜田｜田田│ '',,',.',‘’‘,,',.''
                ╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬
        ''',
        'night': '''

                 ::∴★∵**☆．∴★∵**☆．
                  █████    ．☆．∵★∵∴☆．
                  █田█田█．*☆．∴★∵．
                  █田█田█    ．★∵∴☆．★∵∴．
                  █田█田█．★∵∴☆．★..**．
                  █田█田█  ．★★∵∴☆．★*☆．
                  █████．
                ◢██□██◣．~~~~~*^_^*
        ''',
        'cloud': '''

                ::.--.-.::
                :( (    ):::::  东边日出西边雨
                (_,  \ ) ,_)::  道是无晴却有情       |
                :::-'--`--:::::::: ~~|     ,       \ _ /
                ::::::::::::::::::: ,|`-._/|   -==  (_)  ==-
                ::::::::^^::::::::.' |   /||\      /   \
                ::::::^^::::::::.'   | ./ ||`\       |
                :::::::::::::::/ `-. |/._ ||  \
                ::::::::::::::|      ||   ||   \
                 ~~=~_~^~ =~ \~~~~~~~'~~~~'~~~~/~~`` ~=~^~
                ~^^~~-=~^~ ^ `--------------'~^~=~^~_~^=~^~


        ''',
        'thunder': '''
                ╭⌒╮打雷啦━┅~ ¤　 ╭⌒╮ ╭⌒╮
                ╭⌒╭⌒╮╭⌒╮～╭⌒╮︶︶,　︶︶
                ,︶︶︶︶,""︶~~ ,""~︶︶　 ,""
        ''',
        'snow': '''

                    /     \ _
                    ~x   .-~_)_
                      ~x".-~   ~-.
                  _   ( /         \   _
                  ||   T  o  o     Y  ||
                ==:l   l   <       !  I;==
                   \\   \  .__/   /  //
                    \\ ,r"-,___.-'r.//
                     }^ \.( )   _.'//.
                    /    }~Xi--~  //  \
                   Y    Y I\ \    "    Y
        ''',
        'Christmas': '''
                        圣诞节快乐哟！
                      *             ,
                                  _/^\_
                                 <     >
                *                 /.-.\         *
                         *        `/&\`                   *
                                 ,@.*;@,
                                /_o.I %_\    *
                   *           (`'--:o(_@;
                              /`;--.,__ `')             *
                            ;@`o % O,*`'`&\
                       *    (`'--)_@ ;o %'()\      *
                            /`;--._`'--._O'@;
                           /&*,()~o`;-.,_ `""`)
                *          /`,@ ;+& () o*;-';\
                          (`""--.,_0o*`;-'&()\
                          /-.,_    ``''-...-'`)  *
                     *   /@%;o`:;'--,._   _.]'\
                         ;*,&();@%&^;~`"'`o;@();         *
                        /()Emily & ().o@Robin%OCF\
                        `"="==""==,,,.,="=="==="`
                     __.----.(\-''#####---...___...-----._
                   '`         \)_`"""""`
                           .--' ')
                         o(  )_-\
                           `"""` `
        '''
    }
    todayWeather = weatherInfo['weather1']
    now = datetime.datetime.now()
    if weatherInfo['date_y'].find('12月25') > 0:
        print(character['Christmas'])
    elif int(now.strftime('%H')) > 19:
        print('\n很晚咯老公早点睡')
        print(character['night'])
    elif todayWeather.find('雨') > 0:
        print('\n老公今天下雨记得带雨伞喔~')
        print(character['rain'])
    elif todayWeather.find('晴') > 0:
        print('\n今天天气好好哦，小溪好开心 ^_^')
        print(character['sun'])
    elif todayWeather.find('雪') > 0:
        print('\n老公今天要带小溪去玩雪吗')
        print(character['snow'])
    elif todayWeather.find('雷') > 0:
        print('\n打雷了，小溪好怕')
        print(character['thunder'])

if __name__ == '__main__':
    print('Hello , ' + whoami  + '我是小管家小溪,今天是' + weatherInfo['date_y'])
    Character_painting()
    caletool()
    welcome()
