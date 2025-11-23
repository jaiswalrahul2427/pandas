import pandas as pd

data={ "name":["John","Peter","Lisa"],
      "Age":[25,28,31],
      "Salary":[30000,45000,25000]
      }
df=pd.DataFrame(data)
print(df)