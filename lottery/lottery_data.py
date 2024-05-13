# ！user/bin/env python
# _*_ coding:utf-8 _*_
# _*_ author:taojinwnen _*_
import collections
import json
import pandas as pd
import requests
import time
from lxml import etree

starttime = time.time()
# User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
# 本次爬取使用的网站为中国体彩网：https://www.lottery.gov.cn/kj/kjlb.html?dlt
# 多次查看后，所需的开奖数据储存在json文件中，以下为页数和前100的url
# https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=30&isVerify=1&pageNo=71
# url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=100&isVerify=1&pageNo=1&termLimits=100'
# 'lotteryDrawNum': '21011', 'lotteryDrawResult': '06 09 11 14 21 01 03',
# 'lotteryDrawStatus': 20, 'lotteryDrawTime': '2021-01-25'
columns = ['开奖日期', '期号', '前区', '后区']
# data = {'开奖日期': '', '期号': '', '前区': '', '后区': ''}
data = collections.OrderedDict()  # 定义为有序字典
dates = []
ids = []
front = []  # 前区
behind = []  # 后区
for pageNos in range(1, 71):
    url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=30&isVerify=1&pageNo={}'.format(
        pageNos)
    # 发送请求（获取json文件）
    response = requests.get(url, headers=header)
    content = response.content.decode('utf-8')
    # 使用lxml的etree解析html文件
    html = etree.HTML(content)
    js = json.loads(content)  # json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。
    numbers = js.get('value')  # 获取js内储存所需要数据的字典
    lists = numbers.get('list')  # 获取字典内的列表，但list内部还有30个字典储存着每一期的开奖数据（第一页开奖数据）
    for shujudict in lists:
        date = shujudict.get('lotteryDrawTime')
        dates.append(date)
        id = shujudict.get('lotteryDrawNum')
        ids.append(id)
        shuju = shujudict.get('lotteryDrawResult')
        number = shuju.split(' ')
        # qianqu = number[:5] #转为列表显示效果较差，有[]、'、,三种符号
        # houqu = number[-2:]
        qianqu = shuju[:14]
        houqu = shuju[-5:]
        front.append(qianqu)
        behind.append(houqu)
    data['开奖日期'] = dates
    data['期号'] = ids
    data['前区'] = front
    data['后区'] = behind
df = pd.DataFrame(data, columns=columns)
df.to_excel('lottery_data.xlsx')
endtime = time.time()
time = endtime - starttime
print("耗时：", time, "秒")
# contents = html.xpath("//div[@class='g-history']/table[@class='m-historyTab']/tr/td/text()")
