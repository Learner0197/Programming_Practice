from pickletools import markobject

from matplotlib import pyplot as plt
import pandas as pd

# plt.plot(["abc", "mno", "xyz", "pqr"],[99000, 45000, 25000, 78000], marker='x',linestyle= "dashdot", color='red')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.xlabel("Emp Name")
# plt.ylabel("Salary")
# plt.show()
#
# emp = pd.read_excel('emp.xlsx')
# dep = pd.read_excel('dep.xlsx')
#
# emp.drop("Unnamed: 0", axis=1, inplace=True)
# print(emp.head())
# dep.drop("Unnamed: 0", axis=1, inplace=True)
# print(dep.head())
#
# x= emp.merge(dep, how='left', on='deptid')
# print(x)
#
# salary_by_dept = x.groupby('deptid')['salary'].mean().reset_index()
# salary_by_dept.columns = ['deptid','mean_salary']
#
# salary_by_loc = x.groupby('location')['salary'].mean().reset_index()
# salary_by_loc.columns = ['location','mean_salary']
#
# # plt.hist(did, bins=100)
# # plt.show()
#
# # plt.bar(did, sal)
# # plt.show()
#
# plt.subplot(1, 2, 1)
# plt.plot(salary_by_dept['deptid'], salary_by_dept['mean_salary'], marker="x", color='violet', alpha=0.7)
# plt.xticks(salary_by_dept['deptid'], salary_by_dept['deptid'])
# plt.xlabel('Department ID')
# plt.ylabel('Salary')
# plt.title('Salary vs Department ID')
# plt.grid(True)
#
# plt.subplot(1, 2, 2)
# plt.plot(x["empid"], x["salary"], marker="x", color='blue', alpha=0.7)
# plt.xlabel('EMP id')
# plt.ylabel('Salary')
# plt.title('Salary vs EmpID')
# plt.grid(True)
# plt.show()

movie = pd.read_csv('movies.csv')
# writer_scores = movie.groupby('writer')['score'].mean().reset_index()
# writer_scores_limited = writer_scores.head(500)
#
# plt.scatter(range(len(writer_scores_limited)), writer_scores_limited['score'],
#             marker="x", color='green', alpha=0.7, s=100)
# plt.xticks(range(len(writer_scores_limited)), writer_scores_limited['writer'],
#            rotation=45, ha='right')
# plt.xlabel('Writer')
# plt.ylabel('Mean Score')
# plt.title('Mean Score by Writer (Top 30)')
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# gross_by_budget = movie['gross']/movie['budget']
# df = gross_by_budget.to_frame()
# df.columns = ['grossbudgetratio']
# df = df.head(50)
# gross_budget = movie['name']
# name_limited = gross_budget.head(50)
# plt.bar(name_limited,df['grossbudgetratio'],width=0.6,edgecolor='blue',linewidth=3,color='red')
# # plt.plot(gross_budget_limited, df,
# #             marker="x", color='green', alpha=0.7)
# # plt.xticks(gross_budget_limited, gross_budget_limited,
# #            rotation=45, ha='right')
# plt.xlabel('Name')
# plt.ylabel('Budget')
# plt.title('Name vs Budget')
# plt.grid(True)
# plt.tight_layout()
# plt.show()

corona = pd.read_csv('merged_output.csv')
corona.drop('Suspected',axis=1,inplace=True)
Cases_by_country = corona.groupby('Country/Region')['Confirmed'].sum().reset_index()
Deaths_by_country = corona.groupby('Country/Region')['Death'].sum().reset_index()
new1 = Cases_by_country.drop(15)
new2 = Deaths_by_country.drop(15)
# country_total.columns = ['Country', 'Confirmed']
# print(new)
# print(country_total.max())
# distinct = country.distinct()
plt.figure(figsize=(14, 6))
plt.subplot(1,2,1)
plt.bar(new1['Country/Region'], sorted(new1['Confirmed']))
plt.xticks(new1['Country/Region'], new1['Country/Region'], rotation=45, ha='right')
plt.title('Confirmed Cases by Country')

plt.subplot(1,2,2)
plt.bar(new2['Country/Region'], sorted(new2['Death']))
plt.xticks(new2['Country/Region'], new2['Country/Region'], rotation=45, ha='right')
plt.title('Deaths by Country')
plt.tight_layout()
plt.show()