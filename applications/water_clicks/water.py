# /usr/bin/env python
# coding: utf-8

__author__ = 'David Zong'

import urllib
import urllib2
import time
import random
import string
import socket


def random_sleep_time(digits_length):
    digits_char = string.digits
    need_sleep_time = ''
    for i in range(digits_length):
        need_sleep_time += random.choice(digits_char)
    return int(need_sleep_time)+20


def random_deviceId(num, bit_length):
    deviceId_list = []
    for i in xrange(num):
        str = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        length = len(chars) - 1
        for i in range(bit_length):
            str += chars[random.randint(0, length)]
        deviceId_list.append(str)
    return deviceId_list


def random_phone(num):
    phone_list = []
    for i in xrange(num):
        phone = '136'
        chars = '0123456789'
        length = len(chars) - 1
        for i in range(8):
            phone += chars[random.randint(0, length)]
        phone_list.append(phone)
    return phone_list


def random_name(num, name_length):
    name_list = []
    for i in xrange(num):
        str = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        length = len(chars) - 1
        for i in range(name_length):
            str += chars[random.randint(0, length)]
        name_list.append(str)
    return name_list


headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
           'Content-Type': 'application/x-www-form-urlencoded',
           'Host': 'www.shanghaiwater.gov.cn',
           'Origin': 'http://www.shanghaiwater.gov.cn',
           'Proxy-Connection': 'keep-alive',
           'Referer': 'http://www.shanghaiwater.gov.cn/gb/sswj/n327/index.html',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
           'X-Requested-With': 'XMLHttpRequest'}


url = 'http://www.shanghaiwater.gov.cn/toupiao/api/Vote/'
bit_length = len('1eceu26db2e9de9s6912f29dr2ef0bbc')
name_length = 10
num = 800
deviceId_list = random_deviceId(num, bit_length)
phone_list = random_phone(num)
name_list = random_name(num, name_length)
# print(deviceId_list)
for i in xrange(num):
    text = {'DeviceId': deviceId_list[i],
            'PhoneNumber': phone_list[i],
            'UserName': name_list[i],
            'Works': 4243}
    data_urlencode = urllib.urlencode(text).encode(encoding='utf-8')
    req = urllib2.Request(url=url, data=data_urlencode, headers=headers)
    try:
        response = urllib2.urlopen(req, timeout=300)
        data = response.read().decode('utf-8')
        print(data)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        next_people_time = random_sleep_time(1)
        print('wait', next_people_time, 'next\n')
        time.sleep(next_people_time)
    except socket.error:
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        print('wait too long\n')
        continue

