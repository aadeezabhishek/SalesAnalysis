import os
import pandas as pd
import matplotlib.pyplot as plt
# #
# # df = pd.read_csv(r'C:\Users\user\Desktop\tutorial\SalesAnalysis\Sales_April_2019.csv')
# #
# # files = [file for file in os.listdir(r'C:\Users\user\Desktop\tutorial\SalesAnalysis')]
# # all_months_data = pd.DataFrame()
# # for file in files:
# #     df = pd.read_csv(r'C:\Users\user\Desktop\tutorial\SalesAnalysis/' + file)
# #     all_months_data = pd.concat([all_months_data,df])
# #
# # all_months_data.to_csv("all_data.csv", index=False)
#
#
#
all_data = pd.read_csv(r'C:\Users\user\Desktop\tutorial\SalesAnalysis\all_data.csv')
# print(all_data.head())
# nan_df = all_data[all_data.isna().any(axis=1)]
# print(nan_df.head())
all_data = all_data.dropna(how="all")
all_data = all_data[all_data['Order Date'].str[0:2] != "Or"]
pd.set_option('display.max_columns', 9)

all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')

all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])

all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']

cols = list(all_data.columns.values)
print(cols)
all_data = all_data[cols[0:4] + [cols[-1]] + cols[4:7]]

# result = all_data.groupby('Month').sum()
#
# def get_city(address):
#     return address.split(',')[1]
# def get_state(address):
#     return address.split(',')[2].split(' ')[1]
#
# all_data['City'] = all_data['Purchase Address'].apply(lambda x: get_city(x) + '(' + get_state(x) + ')')
# result1 = all_data.groupby('City').sum()['Sales']


all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])
all_data['Hour'] = all_data['Order Date'].dt.hour
all_data['Minute'] = all_data['Order Date'].dt.minute
hours = [hour for hour, df in all_data.groupby('Hour')]


result3  = all_data.groupby(['Hour']).count()
# print(result3)
plt.plot(hours, result3)
plt.xticks(hours)
plt.xlabel('Hour')
plt.ylabel('Likelihood of users to buy product')
plt.grid()
plt.show()



# months = range(1,13)
# plt.bar(months,result['Sales'])
# plt.xlabel('Months')
# plt.ylabel('Sales in Millions')
# plt.title("Sales Analysis of 2019")
#
# cities = [city for city, df in all_data.groupby('City')]
#
# plt.bar(cities, result1)
# plt.xticks(cities,rotation='vertical', size= 8)
# plt.xlabel('Cities')
# plt.ylabel('Sales in USD($)')
# plt.title("Sales Analysis by cities-2019")
#
# plt.show()

# # print(result)
# # print(all_data.head())
#
# # print(all_data[['Product','Order Date', 'Order ID']])
# # all_data['month'] = all_data['Order Date'].str[0:2]
# # print(all_data.head())