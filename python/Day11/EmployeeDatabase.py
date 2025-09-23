import pymysql as p
con=p.connect(host='localhost',user='root',password='root',database='pgdai', autocommit=True)
cursor = con.cursor()

# cursor.execute('create table employee(empid int, ename varchar(200), salary int)')

class Employee:
    def __init__(self, empid, ename, salary):
        self.empid=empid
        self.ename=ename
        self.salary=salary

class databaseConnection:
    def __init__(self):
        pass

    @staticmethod
    def insert(employee):
        cursor.execute("insert into employee values(%s, %s, %s)", (employee.empid, employee.ename, employee.salary))
        return True
    @staticmethod
    def update(newsal,eid):
        cursor.execute("update employee set salary = %s where empid = %s", (newsal, eid))
        return True
    @staticmethod
    def delete(eid):
        cursor.execute("delete from employee where empid = %s", eid)
        return True
    @staticmethod
    def display():
        cursor.execute("select * from employee")
        data = cursor.fetchall()
        print(data)
        return True


a1=Employee(1,"abc",50000)
a2=Employee(2,"xyz",65000)
a3=Employee(3,"mno",60000)
a4=Employee(4,"pqr",55000)
a5=Employee(5,"qwe",97000)

databaseConnection.delete(1)
databaseConnection.insert(a1)
databaseConnection.insert(a2)
databaseConnection.insert(a3)
databaseConnection.insert(a4)
databaseConnection.insert(a5)
databaseConnection.display()
databaseConnection.update(45000, 4)
databaseConnection.update(70000, 2)
databaseConnection.delete(2)

