import akshare as ak
import datetime
import pandas as pd
from utils_fund import *

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

# select_fund_by_name("天弘永利债券")
#        基金代码 拼音缩写   基金简称      基金类型      拼音全称
# 2101   002794  THYLZQE  天弘永利债券E  债券型-混合债  TIANHONGYONGLIZHAIQUANE
# 7690   009610  THYLZQC  天弘永利债券C  债券型-混合债  TIANHONGYONGLIZHAIQUANC
# 13853  420002  THYLZQA  天弘永利债券A  债券型-混合债  TIANHONGYONGLIZHAIQUANA
# 13859  420102  THYLZQB  天弘永利债券B  债券型-混合债  TIANHONGYONGLIZHAIQUANB

# 基金基本信息 & 指定时段收益
fund_num = ['002794', '009610', '420002', '420102']
date_info = {'date1': {'dt_start': '2021-07-28', 'dt_end': '2022-01-28', 'dt_info': '近半年'},
             'date2': {'dt_start': '2021-10-28', 'dt_end': '2022-01-28', 'dt_info': '近三月'},
             'date3': {'dt_start': '2021-08-01', 'dt_end': '2021-10-12', 'dt_info': '创业板回调1'},
             'date4': {'dt_start': '2021-12-14', 'dt_end': '2022-01-28', 'dt_info': '创业板回调2 + 沪深回调'}}

for date in date_info.keys():
    print_info(date_info[date]['dt_info'])
    for fund in fund_num:
        fund_info = get_fund_info(fund)
        get_fund_total_return(fund, fund_info, date_info[date]['dt_start'], date_info[date]['dt_end'])

'''
天弘永利债券
基金: 天弘永利债券E, 2021-07-28 至 2022-01-28, 累计收益率: 7.67
基金: 天弘永利债券C, 2021-07-28 至 2022-01-28, 累计收益率: 7.52
基金: 天弘永利债券A, 2021-07-28 至 2022-01-28, 累计收益率: 7.46
基金: 天弘永利债券B, 2021-07-28 至 2022-01-28, 累计收益率: 7.68

基金: 天弘永利债券E, 2021-10-28 至 2022-01-28, 累计收益率: 2.51
基金: 天弘永利债券C, 2021-10-28 至 2022-01-28, 累计收益率: 2.43
基金: 天弘永利债券A, 2021-10-28 至 2022-01-28, 累计收益率: 2.40
基金: 天弘永利债券B, 2021-10-28 至 2022-01-28, 累计收益率: 2.51

基金: 天弘永利债券E, 2021-08-01 至 2021-09-29, 累计收益率: 3.17
基金: 天弘永利债券C, 2021-08-01 至 2021-09-29, 累计收益率: 3.12
基金: 天弘永利债券A, 2021-08-01 至 2021-09-29, 累计收益率: 3.10
基金: 天弘永利债券B, 2021-08-01 至 2021-09-29, 累计收益率: 3.17
'''
