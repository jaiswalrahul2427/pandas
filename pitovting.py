import pandas as pd

dic={"Keys":["k1","k2","k1",'k2'],
     "Names":["John","Ben","David","Peter"],
     "Houses":["red","blue","green","red"]}

df=pd.DataFrame(dic)
print(df)
print(df.pivot(index="Keys",columns="Names",values="Houses"))