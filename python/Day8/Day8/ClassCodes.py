class Employee:
    def __init__(self,empid,ename,salary):
        self.empid=empid
        self.ename=ename
        self.salary=salary

    def hello(self):
        print("Employee ID: ",self.empid)
        print("Employee Name: ",self.ename)
        print("Employee Salary: ",self.salary)

    def calculatetax(self):
        # taxrate=float(input("Enter tax rate in terms of percent: "))
        taxrate=25/100
        tax=self.salary*taxrate
        print("Tax on salary of Rs.",self.salary," is Rs.",tax)

class Developer(Employee):
    def __init__(self,empid,ename,salary):
        super().__init__(empid,ename,salary)

e=Employee(1,"Aman",99000)
d=Developer(2,"Arnav",95000)

c=[e,d]

for i in c:
    i.hello()
    i.calculatetax()
    print("\n")