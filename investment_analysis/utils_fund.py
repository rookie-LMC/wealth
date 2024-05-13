import akshare as ak
import datetime
import pandas as pd


def print_info(s):
    print('*' * 10 + ' ' + s + ' ' + '*' * 10)


def select_fund_by_name(name):
    fund_info_df = ak.fund_em_fund_name()
    print(fund_info_df.loc[fund_info_df['基金简称'].str.contains(name)])


def get_fund_info(fund_num):
    """
    基金基本信息
    """
    fund_info_df = ak.fund_em_fund_name()
    fund_target = fund_info_df.loc[fund_info_df['基金代码'] == fund_num]

    fund_info = {}
    fund_name = fund_target.iloc[0].at['基金简称']
    fund_type = fund_target.iloc[0].at['基金类型']
    fund_info['基金简称'] = fund_name
    fund_info['基金类型'] = fund_type
    return fund_info


def get_fund_total_return(fund_num, fund_info, dt_start, dt_end):
    """
    基金收益率
    """
    total_return_df = ak.fund_em_open_fund_info(fund=fund_num, indicator="累计收益率走势")
    print("基金收益率数据: {begin} ~ {end}".format(begin=total_return_df.iloc[0].at["净值日期"],
                                            end=total_return_df.iloc[total_return_df.shape[0] - 1].at["净值日期"]))
    total_return = total_return_df.loc[
        (total_return_df['净值日期'] >= pd.to_datetime(dt_start)) &
        (total_return_df['净值日期'] <= pd.to_datetime(dt_end))]
    total_return_list = total_return['累计收益率'].tolist()

    print("基金: {fund}, {dt_start} 至 {dt_end}, 累计收益率: {val}".format(fund=fund_info['基金简称'],
                                                                   dt_start=dt_start, dt_end=dt_end,
                                                                   val=str(
                                                                       total_return_list[-1] - total_return_list[0])))
