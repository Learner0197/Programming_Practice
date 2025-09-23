def replacedatainfile(source, destination, filename):
    f=open(filename,'r')
    content = f.read()
    updated_content = content.replace(source, destination)
    f.close()

    g=open(filename,'w')
    g.write(updated_content)
    g.close()

replacedatainfile("World", "Earth", "withoutblank.txt")

def csvtotable(filename):
    f = open(filename, 'r')
    content = f.readlines()
    for i in content:
        i = i.split(",")
        i = "\t".join(i)
        print(i)
    f.close()

csvtotable("customers.csv")

class Employee:
    count=0
    def __init__(self, empid, ename, basicsal):
        self.empid=empid
        self.ename=ename
        self.basicsal=basicsal

    def __repr__(self):
        return "Employee ID: "+self.empid+"Employee Name: "+self.ename+"Salary Rs.: "+self.basicsal

a1=Employee(1,"abc",50000)
a2=Employee(2,"def",75000)
a3=Employee(3,"ghi",65000)
l=[a1,a2,a3]

f=open("Employees.txt", "w")
c=f.writelines(str(l))
f.close()
