import pandas as pd
data=pd.read_csv("D:/My Download/customers-100.csv")
print(data.head(10))
print(data["Website"].duplicated().sum())
