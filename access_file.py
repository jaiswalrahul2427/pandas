import pandas as pd

# data= pd.read_csv("D:/My Download/customers-100.csv")
# print(data)

data=pd.read_excel("C:/Users/91945/OneDrive/Documents/AI classes.xlsx")
holiday_data=pd.read_excel("holiday_dates.xlsx")
print(data)
print(holiday_data)
print("For the first 5 datas:\n",holiday_data.head())
print("__Print about data datatypr and memory storage:__")
print(data.info())
print(holiday_data.describe())