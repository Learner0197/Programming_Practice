import pymysql as p
con=p.connect(host='localhost',user='root',password='root',database='pgdai', autocommit=True)
cursor = con.cursor()

#cursor.execute('create table employeepayroll(empid int, ename varchar(200), salary int, position varchar(25))')

class Employee:
    def __init__(self, empid, ename, basicSalary, medicalAllowance):
        self.empid = empid
        self.ename = ename
        self.basicSalary = basicSalary
        self.pf = 0.12 * basicSalary
        self.pt = 200
        self.hra = 0.5 * basicSalary
        self.medicalAllowance = medicalAllowance

    def grossSal(self):
        gross = self.basicSalary + self.hra + self.medicalAllowance
        return gross

    def netSal(self):
        net = self.grossSal() - self.pf - self.pt
        return net

    def getPosition(self):
        return "Employee"

    def showDetails(self):
        print("EMPID:", self.empid)
        print("EMPName:", self.ename)
        print("Basic Salary:", self.basicSalary)
        print("Medical Allowance:", self.medicalAllowance)
        print("Gross Salary:", self.grossSal())
        print("Net Salary:", self.netSal())
        print("Position:", self.getPosition())

    def __repr__(self):
        dets = "Employee ID: " + str(self.empid) + " Employee Name: " + str(self.ename) + " Basic Salary Rs.: " + str(self.basicSalary)
        return dets

class Manager(Employee):
    def __init__(self, empid, ename, basicSalary, medicalAllowance):
        super().__init__(empid, ename, basicSalary, medicalAllowance)
        self.managerAllowance = 0.08 * basicSalary
        self.foodAllowance = 0.1 * basicSalary
        self.otherAllowance = 0.03 * basicSalary

    def grossSal(self):
        gross = super().grossSal() + self.managerAllowance + self.foodAllowance + self.otherAllowance
        return gross

    def getPosition(self):
        return "Manager"

class MarketingExecutive(Employee):
    def __init__(self, empid, ename, basicSalary, medicalAllowance, travelKM):
        super().__init__(empid, ename, basicSalary, medicalAllowance)
        self.travelKM = travelKM
        self.phoneAllowance = 1000
        self.travelAllowance = 5 * travelKM

    def grossSal(self):
        gross = super().grossSal() + self.phoneAllowance + self.travelAllowance
        return gross

    def getPosition(self):
        return "MarketingExecutive"

class DatabaseConnection:
    def __init__(self):
        pass

    @staticmethod
    def insert(employee):
        cursor.execute("insert into employee values(%s, %s, %s, %s)",
                     (employee.empid, employee.ename, employee.basicSalary, employee.getPosition()))
        return True

    @staticmethod
    def update(newsal, eid):
        cursor.execute("update employee set salary = %s where empid = %s", (newsal, eid))
        return True

    @staticmethod
    def delete(eid):
        cursor.execute("delete from employee where empid = %s", (eid,))
        return True

    @staticmethod
    def display():
        cursor.execute("select * from employee")
        data = cursor.fetchall()
        print(data)
        return True

    @staticmethod
    def search(eid):
        cursor.execute("select * from employee where empid = %s", (eid,))
        data = cursor.fetchone()
        print(data)
        return data

# Create employee objects
e = Manager(1, "Arnav", 80000, 10000)
m = Manager(2, "Aman", 85000, 20000)
me = MarketingExecutive(3, "Atharva", 90000, 20000, 50)


DatabaseConnection.insert(e)
DatabaseConnection.insert(m)
DatabaseConnection.insert(me)
DatabaseConnection.display()
DatabaseConnection.search(2)
DatabaseConnection.update(95000, 1)
DatabaseConnection.display()
DatabaseConnection.delete(3)
DatabaseConnection.display()

