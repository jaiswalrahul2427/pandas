import pandas as pd

data=pd.read_excel("Detail.xlsx")
print(data)

data["Bonus"]=(data["Salary"]/100)*20
print(data)
