'''
出现次数全排序筛选，不对
'''
import pandas as pd

# 读数据
data = pd.read_excel("lottery_data.xlsx")
df = data[['开奖日期', '前区', '后区']]

# 策略1
# df = df.head(20)

# 策略2
df = df.head(1000)

df['新前区'] = df['前区'].str.split(' ')
df['新后区'] = df['后区'].str.split(' ')
numbers = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
           '18', '19',
           '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37',
           '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73',
           '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91',
           '92', '93', '94', '95', '96', '97', '98', '99']
bef_cnt = {numb: 0 for numb in numbers}

for i in range(df.shape[0]):
    for numb in df.at[i, '新前区']:
        bef_cnt[numb] = bef_cnt[numb] + 1

bef_cnt = sorted(bef_cnt.items(), key=lambda x: x[1], reverse=True)
for t in bef_cnt:
    print(t[0], t[1])
