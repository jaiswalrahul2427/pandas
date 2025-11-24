import pandas as pd

data={"Months":["January","Febraury","March","April"]}
a=pd.DataFrame(data)

def extract(value):
    return value[0:3]
a["short_Months"]=a["Months"].map(extract)
print(a)