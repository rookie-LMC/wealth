import pandas as pd

# 读数据
data = pd.read_excel("lottery_data.xlsx")
df = data[['开奖日期', '前区', '后区']]

# 策略1
df = df.head(20)

# 策略2
# df = df.head(50)

# 裁剪数据
df[['新前区1', '新前区2', '新前区3', '新前区4', '新前区5']] = df['前区'].str.split(' ', expand=True)
df[['新后区1', '新后区2']] = df['后区'].str.split(' ', expand=True)
total_num = df.shape[0]
print("根据最近{0}期筛选最优号码".format(total_num))

numbers = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
           '18', '19',
           '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37',
           '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73',
           '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91',
           '92', '93', '94', '95', '96', '97', '98', '99']
number_part = ['新前区1', '新前区2', '新前区3', '新前区4', '新前区5', '新后区1', '新后区2']

for part in number_part:
    best_num = ''
    best_cnt = 0
    for numb in numbers:
        df_part = df[df[part] == numb]
        select_cnt = df_part.shape[0]
        if select_cnt > best_cnt:
            best_cnt = select_cnt
            best_num = numb
    print("pos: {0}, best_num: {1}, best_cnt: {2}".format(part, best_num, best_cnt))
