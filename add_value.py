import pandas as pd
data=pd.read_excel("Detail.xlsx")
print(data)
data["Full Name"]=data["First Name"].str.capitalize()+" "+data["Last Name"].str.capitalize()
print(data)