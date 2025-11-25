import pandas as pd

data=pd.read_excel("employee_100_details.xlsx")
print(data)
gp=data.groupby("Job Title").agg({"Department":"count"})
print(gp)
