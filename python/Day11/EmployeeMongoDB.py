import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

print(client.list_database_names())

db=client['cdac']
emp=db['employee2']

class Employee:
    def __init__(self, empid, ename, salary):
        self.empid=empid
        self.ename=ename
        self.salary=salary

    def to_dict(self):
        return {
            "empid": self.empid,
            "ename": self.ename,
            "salary": self.salary
        }

class databaseConnection:
    def __init__(self):
        pass

    @staticmethod
    def insert(employee):
        employee_dict = employee.to_dict()
        emp.insert_one(employee_dict)

    @staticmethod
    def update(empid,newsal):
        filter_query = {"empid": empid}
        update_query = {"$set": {"salary": newsal}}
        emp.update_one(filter_query, update_query)

    @staticmethod
    def delete(empid):
        emp.delete_one({"empid": empid})
    @staticmethod
    def display():
        print(list(emp.find()))


a1=Employee(1,"abc",50000)
a2=Employee(2,"xyz",65000)
a3=Employee(3,"mno",60000)
a4=Employee(4,"pqr",55000)
a5=Employee(5,"qwe",97000)


# databaseConnection.insert(a1)
# databaseConnection.insert(a2)
# databaseConnection.insert(a3)
# databaseConnection.insert(a4)
# databaseConnection.insert(a5)
databaseConnection.display()

databaseConnection.update(3,78000)
databaseConnection.delete(5)
databaseConnection.display()