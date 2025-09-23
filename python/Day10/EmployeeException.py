from logging import basicConfig

from Day10.userdefinedexceptions import TravelException, MedicalAllowanceException


class Employee:
    def __init__(self, empid, ename, basicSalary, medicalAllowance):
        self.empid = empid
        self.ename = ename
        self.basicSalary = basicSalary
        self.pf = 0.12 * basicSalary
        self.pt = 200
        self.hra = 0.5 * basicSalary
        self.medicalAllowance = medicalAllowance

        if self.medicalAllowance < 2000:
            raise MedicalAllowanceException

    def grossSal(self):
        gross = self.basicSalary + self.hra + self.medicalAllowance
        return gross

    def netSal(self):
        net = self.grossSal() - self.pf - self.pt
        return net

    def showDetails(self):
        print("EMPID:", self.empid)
        print("EMPName:", self.ename)
        print("Basic Salary:", self.basicSalary)
        print("Medical Allowance:", self.medicalAllowance)
        print("Gross Salary:", self.grossSal())
        print("Net Salary:", self.netSal())

    def __repr__(self):
        dets= "Employee ID: "+str(self.empid)+" Employee Name: "+str(self.ename)+" Basic Salary Rs.: "+str(self.basicSalary)
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

    # def Managernet(self):
    #     net = self.Managergross() - self.pf - self.pt
    #     return net
    #
    # def ManagerDet(self):
    #     return self.empid, self.ename, self.basicSalary, self.pf, self.pt, self.hra, self.medicalAllowance, self.managerAllowance, self.foodAllowance, self.otherAllowance


class MarketingExecutive(Employee):
    def __init__(self, empid, ename, basicSalary, medicalAllowance, travelKM=0):
        super().__init__(empid, ename, basicSalary, medicalAllowance)
        self.travelKM = travelKM
        self.phoneAllowance = 1000
        self.travelAllowance = 5 * travelKM

        if self.travelKM <= 0:
            raise TravelException

    def grossSal(self):
        gross = super().grossSal() + self.phoneAllowance + self.travelAllowance
        return gross

    # def MarkexNet(self):
    #     net = self.MarkExGross() - self.pf - self.pt
    #     return net
    #
    # def MarkExDet(self):
    #     return self.empid, self.ename, self.basicSalary, self.pf, self.pt, self.hra, self.medicalAllowance, self.travelKM, self.travelAllowance, self.phoneAllowance


e = Employee(1, "Arnav", 80000, 1000)
m = Manager(2, "Aman", 85000, 20000)
me = MarketingExecutive(3, "Atharva", 90000, 20000)

l = [e, m, me]
print(e.grossSal())
print(e.netSal())
print(e.showDetails())

print(m.showDetails())

print(me.showDetails())

print(l)