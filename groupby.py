import pandas as pd

data=pd.read_excel("employee_100_details.xlsx")
gp=data.groupby("Job Title").agg({"Department":"count"})
print(gp)