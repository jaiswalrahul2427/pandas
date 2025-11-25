import pandas as pd

data1 = {
    "Emp ID": ["E01", "E02", "E03", "E04", "E05", "E06"],
    "Name": ["Ram", "Shyam", "Rahul", "Vishhal", "Ravi", "Aman"],
    "Age": [34, 35, 25, 80, 60, 55]
}

# NOTE: Salary list has only 5 values → missing 1 value
data2 = {
    "Emp ID": ["E07", "E08", "E09", "E010", "E011", "E012"],
    "Salary": [45000, 50000, 60000, 45000, 32000,None]   # Missing salary for E06
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merge with LEFT join (keeps all rows from df1)
print(pd.concat([df1,df2]))
