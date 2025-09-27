import pandas as pd

e = pd.read_excel('example.xls',sheet_name=0)
e2 = pd.read_excel('example.xls',sheet_name=1)
# print(e)
# print(e2)
# print(e.describe())
# print(e2.describe())
#print(e.info()) prints metadata of dataframe
# print(e.head(5)) prints first 5 rows from start
# print(e.tail(5)) prints last 5 rows
# print(e["NAME"]) prints column with title "NAME"
# print(e.iloc[1])

# print(e["SALARY"]>60000)
# print(e[e["SALARY"]>60000])

# print(e[["NAME","SALARY"]])
#
# print(e["SALARY"]>50000)
# emp_50k=e[e["SALARY"]>50000]
# emp_50k.to_csv("emp_50k.csv")
# print(emp_50k.describe())
#
print(pd.read_csv("emp_50k.csv",index_col="EMPID"))

print(e.count())
print(e.sum())

