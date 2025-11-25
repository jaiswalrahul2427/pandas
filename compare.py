import pandas as pd

dic={"fruits":["mango","apples","banana","papaya"],
     "price":[100,150,50,35],
     "Quantity":[15,10,10,3]}

df1=pd.DataFrame(dic)
print(df1)

df2=df1.copy()
df2.loc[0,"price"]=120
df2.loc[1,"price"]=80
print(df2)

print(f"\n{df1.compare(df2)}")
# keep_shape is bydefault=false
print(f"\n{df1.compare(df2,keep_shape=True)}")