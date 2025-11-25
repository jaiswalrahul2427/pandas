import pandas as pd

dic={
     "Names":["John","Ben","David","Peter"],
     "Houses":["red","blue","green","red"],
     "Grade":["3rd","8th","9th","8th"]}

df=pd.DataFrame(dic)
print(df)
print(pd.melt(df,id_vars=["Names"],value_vars=["Houses"]))

print(pd.melt(df,id_vars=["Names"],value_vars=["Houses","Grade"],var_name="Houses&Grade",value_name="Values"))