import pymysql as p
import pandas as pd

con=p.connect(host="localhost",user="root",password="root",database="pgdai",autocommit=True)
cursor=con.cursor()

df=pd.read_sql("select * from payroll",con=con)
print(df)

con.commit()
con.close()