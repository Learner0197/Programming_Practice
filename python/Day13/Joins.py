import pandas as pd
emp = pd.read_excel('employee_data.xlsx')
surv = pd.read_excel('employee_engagement_survey_data.xlsx')
print(emp.info())
print(surv.info())
print(emp.head())
print(surv.head())

x = emp.merge(surv, how='left', on='EmpID')
print(x)