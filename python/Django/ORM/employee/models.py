from django.db import models

# Create your models here.
class Employee(models.Model):
    empid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=50)
    salary=models.IntegerField(default=0)
    age=models.IntegerField(default=0)

    def __str__(self):
        return "EMPID:" +str(self.empid)+ ", EMPNAME:" +str(self.ename)+ ", Salary:" +str(self.salary)
