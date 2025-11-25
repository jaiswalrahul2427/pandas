import pandas as pd

data1={"Emp ID":["E01","E02","E03","E04","E05","E06"],
      "Name":["Ram","Shyam","Rahul","Vishhal","Ravi","Aman"],
      "Age":[34,35,25,80,60,55]}

data2={"Emp ID":["E01","E02","E03","E04","E05","E06",],
         "Salary":[45000,50000,60000,30000,45000,32000]  }

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

print(df1)
print(df2)

print(pd.merge(df1,df2,on="Emp ID"))