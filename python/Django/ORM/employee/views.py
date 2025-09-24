from django.shortcuts import render
from django.contrib import messages
from .models import Employee 

def insert(request):
    if request.method == "POST":
        empid = request.POST.get('empid')
        ename = request.POST.get('ename')
        salary = request.POST.get('salary')
        age = request.POST.get('age')

        emp = Employee(empid = empid, ename = ename, salary = salary, age = age)
        emp.save()
        messages.success(request, 'Employee added')

    return render(request, "insert.html")

def display(request):
    emp = Employee.objects.all()
    return render(request, "delete.html", {"emp":emp})

def update(request):
    employee=None
    if request.method == 'POST':
        if 'search' in request.POST:
            empid = request.POST.get('empid')

    employee = Employee.objects.get(empid=empid)
    empid = request.POST.get('empid')
    ename = request.POST.get('ename')
    salary = request.POST.get('salary')
    age = request.POST.get('age')
    employee = Employee.objects.get(empid=empid)
    employee.ename = ename
    employee.salary = salary
    employee.age = age
    employee.save()
    return render(request, 'employee/update.html', {'employee': employee})

def delete(request):
        request.method="POST"
        empid=request.POST.get(empid=empid)
        employee = Employee.objects.get(empid=empid)
        employee_name = employee.ename
        employee.delete()
        return render(request,'employee/delete.html')
# Create your views here.