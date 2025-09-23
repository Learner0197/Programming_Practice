import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

print(client.list_database_names())

db=client['cdac']
emp=db['employee']

print(list(emp.find()))

#db.employee.insert_one({'_id':8,'emmpid':8,'ename':'bvd','salary':80000,'Email':'ghg@ymail.com'})
# db.employee.delete_one({'emmpid':8})
# db.employee.insert_one({'_id':8,'empid':8,'ename':'bvd','salary':80000,'Email':'ghg@ymail.com'})

# db.employee.update_one({'empid':8},{'$set':{'salary':72000}})
# print(list(emp.find()))

data = {"_id":10, "empid":10, "salary":55000}
db.employee.insert_one(data)
print(list(emp.find()))