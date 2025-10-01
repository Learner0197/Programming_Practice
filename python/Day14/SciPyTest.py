import pandas as pd
# data = {
# "empid": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
# "ename": ["John Smith", "Sarah Johnson", "Michael Brown", "Emily Davis", "David Wilson", "Lisa Anderson",
# "James Taylor", "Maria Garcia", "Robert Martinez", "Jennifer Lee", "William Rodriguez",
# "Elizabeth White", "Christopher Harris", "Jessica Clark", "Daniel Lewis", "Amanda Walker",
# "Matthew Hall", "Ashley Young", "Joshua King", "Stephanie Wright"],
# "salary": [65000, 72000, 58000, 81000, 69000, 75000, 62000, 78000, 70000, 64000, 85000, 59000, 91000,
# 67000, 73000, 66000, 88000, 61000, 76000, 68000],
# "deptid": [1, 2, 1, 3, 2, 3, 1, 2, 3, 1, 2, 4, 3, 1, 2, 4, 3, 1, 2, 4]
# }
#
# dept_data = {
# "deptid": [1, 2, 3, 4, 5],
# "dname": ["Engineering", "Sales", "Marketing", "HR", "Finance"],
# "location": ["San Francisco", "New York", "Los Angeles", "Chicago", "Boston"]
# }
#
#
# emp = pd.DataFrame(data)
# dep = pd.DataFrame(dept_data)
#
# emp.to_excel("emp.xlsx")
# dep.to_excel("dep.xlsx")

empl = pd.read_excel("emp.xlsx")
dept = pd.read_excel("dep.xlsx")

empl = empl.drop('Unnamed: 0', axis=1)
dept = dept.drop('Unnamed: 0', axis=1)


x = empl.merge(dept, how='left', on='deptid')
print(x)
y = x.groupby("deptid")
print(y.groups)
min = y["salary"].min()
max = y["salary"].max()
avg = y["salary"].mean()
print("Department wise minimum salary is:", min)
print("Department wise maximum salary is:", max)
print("Department wise average salary is:", avg)

z = x.groupby("location")
print(z.groups)
lmin = z["salary"].min()
lmax = z["salary"].max()
lavg = z["salary"].mean()
print("Location wise minimum salary is:", lmin)
print("Location wise maximum salary is:", lmax)
print("Location wise average salary is:", lavg)
