from itertools import count


class Employee:
    count=0
    def __init__(self, empid, ename, basicsal):
        self.empid=empid
        self.ename=ename
        self.basicsal=basicsal
        Employee.count += 1

    @staticmethod
    def getcount():
        return Employee.count

    def __repr__(self):
        return "Employee ID:"+str(self.empid)+" Employee Name:"+str(self.ename)+" Basic Salary Rs.: "+str(self.basicsal)

    def __eq__(self, other):
        return self.empid==other.empid

    def __lt__(self, other):
        return self.basicsal<other.basicsal

    def __gt__(self, other):
        return self.basicsal>other.basicsal

    @staticmethod
    def thisisstatic():
        return Employee.count




    # def dispDetails(self):
    #     print("Employee ID:",self.empid)
    #     print("Employee Name:", self.ename)
    #     print("Basic Salary Rs.:", self.basicsal)

a1=Employee(1,"abc",50000)
a2=Employee(2,"def",75000)
a3=Employee(3,"ghi",65000)
l=[a1,a2,a3]

print(l)
print(Employee.getcount())
print(a1<a3)
print(a2>a3)
print(Employee.thisisstatic())

# for i in l:
#     i.dispDetails()


