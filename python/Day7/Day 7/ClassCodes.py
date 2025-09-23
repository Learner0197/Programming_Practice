class Employee:
    def __init__(self,empid,ename,salary):
        self.empid=empid
        self.ename=ename
        self.salary=salary

    def hello(self):
        print("Employee ID: ",self.empid)
        print("Employee Name: ", self.ename)
        print("Employee Salary: ", self.salary)
        # print("Hello World from Employee")

e1=Employee(1,"Aman",99000)
e1.hello()
e2=Employee(2,"Arnav",95000)
e2.hello()

class Calculator:
    def add(self,n1,n2):
        print(n1+n2)
    def subtract(self,n1,n2):
        print(n1 -n2)
    def multiply(self,n1,n2):
        print(n1 * n2)
    def divide(self,n1,n2):
        print(n1//n2)

n=Calculator()
n.add(45,64)
n.subtract(145,35)
n.multiply(56754,436)
n.divide(5363,56)